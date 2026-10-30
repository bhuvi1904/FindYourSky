import pytest

def test_api_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "models" in data
    assert data["models"]["logistic_regression"] == "ready"

def test_list_schools(client):
    response = client.get("/api/schools")
    assert response.status_code == 200
    schools = response.json()
    assert len(schools) >= 15
    first = schools[0]
    assert "name" in first
    assert "website_url" in first
    assert "dgca_approval_no" in first
    assert "latest_ranking_category" in first

def test_filter_schools_by_region(client):
    response = client.get("/api/schools?region=North")
    assert response.status_code == 200
    schools = response.json()
    assert len(schools) > 0
    for s in schools:
        assert s["primary_region"] == "North"

def test_get_school_detail(client):
    response = client.get("/api/schools/FTO_IGRUA_001")
    assert response.status_code == 200
    data = response.json()
    assert data["school_id"] == "FTO_IGRUA_001"
    assert "Indira Gandhi" in data["name"]
    assert len(data["bases"]) > 0
    assert len(data["fleet"]) > 0
    assert len(data["fees"]) > 0
    assert len(data["rankings"]) > 0

def test_get_school_sources(client):
    response = client.get("/api/schools/FTO_IGRUA_001/sources")
    assert response.status_code == 200
    sources = response.json()
    assert len(sources) > 0
    assert sources[0]["field_name"] == "dgca_approval_no"

def test_get_sources_registry(client):
    response = client.get("/api/sources")
    assert response.status_code == 200
    sources = response.json()
    assert len(sources) >= 5
    source_ids = [s["source_id"] for s in sources]
    assert "SRC_DGCA_PORTAL" in source_ids
    assert "SRC_PIB_FTO_2026" in source_ids

def test_get_rankings(client):
    response = client.get("/api/rankings?period=2025-2026")
    assert response.status_code == 200
    rankings = response.json()
    assert len(rankings) > 0
    assert rankings[0]["national_rank"] == 1
    assert "ranking_category" in rankings[0]

def test_validate_questionnaire(client):
    payload = {
        "max_budget_inr": 4500000.0,
        "preset_name": "balanced",
        "weights": {
            "cost": 0.30,
            "ranking": 0.30,
            "fleet": 0.20,
            "location": 0.10,
            "infrastructure": 0.10
        }
    }
    response = client.post("/api/questionnaire/validate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["is_valid"] is True
    assert "normalized_weights" in data
    assert abs(sum(data["normalized_weights"].values()) - 1.0) < 0.001

def test_recommendations_hybrid(client):
    payload = {
        "max_budget_inr": 5000000.0,
        "career_objective": "CPL_ME_IR",
        "preset_name": "balanced",
        "weights": {
            "cost": 0.25,
            "ranking": 0.25,
            "fleet": 0.20,
            "location": 0.15,
            "infrastructure": 0.15
        }
    }
    response = client.post("/api/recommendations?mode=hybrid", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["analytical_mode"] == "hybrid"
    assert data["eligible_count"] > 0
    schools = data["schools"]
    assert len(schools) > 0
    # Check top school structure
    top = schools[0]
    assert top["rank"] == 1
    assert top["overall_match_score"] >= schools[-1]["overall_match_score"]
    assert len(top["match_reasons"]) > 0
    assert len(top["tradeoffs"]) > 0
    assert "sensitivity_analysis" in data

def test_recommendations_modes(client):
    payload = {
        "max_budget_inr": 5500000.0,
        "weights": {"cost": 0.2, "ranking": 0.4, "fleet": 0.2, "location": 0.1, "infrastructure": 0.1}
    }
    for mode in ["hybrid", "logistic_regression", "factor_analysis", "clustering"]:
        resp = client.post(f"/api/recommendations?mode={mode}", json=payload)
        assert resp.status_code == 200
        d = resp.json()
        assert d["analytical_mode"] == mode
        assert len(d["schools"]) > 0

def test_compare_schools(client):
    payload = {
        "school_ids": ["FTO_IGRUA_001", "FTO_NFTI_002", "FTO_CAA_003"]
    }
    response = client.post("/api/recommendations/compare", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert len(data["schools"]) == 3
    assert len(data["comparison_table"]) >= 5
    assert "tradeoff_matrix" in data

def test_analytics_logistic_regression(client):
    response = client.get("/api/analytics/logistic-regression")
    assert response.status_code == 200
    data = response.json()
    assert data["is_available"] is True
    assert "coefficients" in data
    assert "odds_ratios" in data
    assert "roc_curve_points" in data
    assert data["accuracy"] is not None
    assert data["sample_size"] >= 15

def test_analytics_factor_analysis(client):
    response = client.get("/api/analytics/factor-analysis?factors=3")
    assert response.status_code == 200
    data = response.json()
    assert data["is_available"] is True
    assert "kmo_overall" in data
    assert "bartlett_chi_square" in data
    assert len(data["eigenvalues"]) > 0
    assert len(data["factor_labels"]) == data["num_factors_selected"]
    assert len(data["school_factor_scores"]) > 0

def test_analytics_clustering(client):
    response = client.get("/api/analytics/clustering")
    assert response.status_code == 200
    data = response.json()
    assert data["is_available"] is True
    assert data["optimal_k"] >= 2
    assert len(data["cluster_profiles"]) == data["optimal_k"]
    assert len(data["pca_2d_points"]) > 0
    assert "stability_score" in data

def test_evaluation_latest(client):
    response = client.get("/api/evaluation/latest")
    assert response.status_code == 200
    data = response.json()
    assert "logistic_regression" in data
    assert "factor_analysis" in data
    assert "clustering" in data
    assert "recommendation_quality" in data
    assert "data_quality" in data
    assert data["recommendation_quality"]["ndcg_at_5"] > 0

def test_data_quality_dashboard(client):
    response = client.get("/api/data-quality")
    assert response.status_code == 200
    data = response.json()
    assert data["total_schools"] >= 15
    assert data["verified_approval_pct"] >= 90.0
    assert "missingness_by_field" in data

def test_submit_feedback(client):
    payload = {
        "rating": 5,
        "was_helpful": True,
        "comments": "Excellent transparency in criterion breakdown."
    }
    response = client.post("/api/feedback", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
