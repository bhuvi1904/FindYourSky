# Intelligent Flying School Recommendation System (FindYourSky)

A full-stack, production-grade statistical decision support and recommendation system designed to evaluate Directorate General of Civil Aviation (DGCA) approved Flying Training Organisations (FTOs) in India for aspiring commercial pilots.

Built with an academic focus on **Business Analytics, Machine Learning, and Statistical Modeling**, the platform provides transparent multi-criteria decision analysis (MCDA), quantitative factor reduction, clustering archetype analysis, and predictive logistic classification.

---

## ✈️ System Architecture & Technology Stack

```
                              ┌──────────────────────────────────────────────┐
                              │       React 18 + TypeScript + Vite           │
                              │  Tailwind CSS • Recharts • Lucide Icons      │
                              │    React Router (14 Routes) • Zod Validation │
                              └──────────────────────┬───────────────────────┘
                                                     │ REST API / JSON
                                                     ▼
                              ┌──────────────────────────────────────────────┐
                              │             FastAPI (Python 3.12)            │
                              │    Pydantic V2 • SQLAlchemy 2.0 • Alembic    │
                              └──────┬───────────────────────────────┬───────┘
                                     │                               │
                ┌────────────────────┴────────────────┐              │
                ▼                                     ▼              ▼
┌──────────────────────────────┐   ┌──────────────────────────────┐  │
│   Statistical Modeling Engine│   │ Recommendation Engine (MCDA) │  │
│ • Logistic Regression (Sklearn)│   │ • Hard Regulatory Filtering  │  │
│ • Factor Analysis (EFA+Varimax)│  │ • Normalized Weight Scoring  │  │
│ • K-Means (Inertia, Silhouette)│ │ • +/- 20% Sensitivity Sim    │  │
└──────────────────────────────┘   └──────────────────────────────┘  │
                                                                     ▼
                                                   ┌──────────────────────────────┐
                                                   │ Relational Database Engine   │
                                                   │ • SQLite (Dev Fallback)      │
                                                   │ • PostgreSQL 16 (Production) │
                                                   │ • 15 Normalized Tables       │
                                                   └──────────────────────────────┘
```

- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS, Lucide icons, Recharts, React Router v6, React Hook Form, Zod.
- **Backend**: Python 3.12, FastAPI, SQLAlchemy 2.0, Pydantic, scikit-learn, SciPy, pandas, NumPy, statsmodels, pytest.
- **Database**: SQLite (default local development) and PostgreSQL (production Docker deployment) with 15 relational tables.
- **Source Registry**: Verified DGCA, Ministry of Civil Aviation (MoCA), and Press Information Bureau (PIB) official documents.

---

## 🚀 Quick Start & Reproduction

### Prerequisites
- Python 3.12+
- Node.js 18+ and npm
- (Optional) Docker and Docker Compose

### Option A: Local Native Setup (Windows / macOS / Linux)

#### 1. Backend Setup & Test Execution
```bash
# Navigate to backend directory
cd backend

# Create virtual environment (Windows)
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Initialize database schema and seed all 41 verified DGCA FTOs
python -m app.db.init_db

# Run automated test suite (17 comprehensive test cases)
pytest -o pythonpath=. -v

# Launch FastAPI development server (http://127.0.0.1:8000)
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

#### 2. Frontend Setup
```bash
# In a new terminal, navigate to frontend directory
cd frontend

# Install npm packages
npm install

# Run TypeScript check and production build
npm run build

# Start Vite development server (http://localhost:5173)
npm run dev
```

#### 3. Automated One-Click Runners (PowerShell)
From the project root:
- **Run all tests & builds**: `powershell -ExecutionPolicy Bypass -File .\scripts\run_tests.ps1`
- **Re-seed database**: `powershell -ExecutionPolicy Bypass -File .\scripts\seed_database.ps1`
- **Launch full stack**: `powershell -ExecutionPolicy Bypass -File .\scripts\run_local.ps1`

---

### Option B: Docker Compose Deployment

```bash
# Build and start PostgreSQL, Backend API, and Frontend SPA
docker-compose up --build
```
- Frontend: `http://localhost`
- Backend API Docs (Swagger): `http://localhost:8000/docs`
- Backend ReDoc: `http://localhost:8000/redoc`

---

## 📊 Analytical Modes & Statistical Models

The system implements four distinct analytical engines accessible through both dedicated REST APIs and interactive dashboards:

| Engine / Mode | Key Algorithms & Methods | Key Outputs & Visualizations |
|---|---|---|
| **1. Hybrid Analytical Engine** (Default) | Hard regulatory constraints, user-weighted Multi-Criteria Decision Analysis (MCDA), statistical boost integration. | Ranked shortlist, match tier, itemized score breakdown, qualitative match reasons, trade-offs, and **$\pm 20\%$ sensitivity analysis**. |
| **2. Binary Logistic Regression** | Scikit-learn Pipeline, Stratified K-Fold CV ($k=3$), $z$-score feature scaling, Sigmoid probability mapping. | Coefficients, Odds Ratios ($\exp(\beta)$), ROC Curve points, AUC-ROC ($0.80+$), Confusion Matrix, Brier calibration score. |
| **3. Exploratory Factor Analysis** | Kaiser-Meyer-Olkin (KMO) measure, Bartlett's test of sphericity, Scree plot eigenvalues, Varimax orthogonal rotation. | KMO sample adequacy ($0.72$), Bartlett $\chi^2$ ($p < 0.001$), 3 latent factor dimensions, communalities, factor loadings matrix. |
| **4. K-Means Clustering** | Candidate sweep $K \in [2, 5]$, within-cluster sum of squares (Inertia), Silhouette coefficient, PCA 2D coordinates. | Inertia elbow curve, Silhouette curve, centroid archetype profiling (e.g. *Premier Academy* vs *Regional Cost-Effective*), 2D PCA cluster scatter. |

---

## 🗺️ Complete Frontend Route Inventory (14 Routes)

| Route Path | Page Title | Primary Functionality |
|---|---|---|
| `/` | Landing Portal | Hero section, statistical pipeline summary, quick workflow entry points. |
| `/schools` | FTO Directory | Filterable grid of all 41 DGCA-approved Indian FTOs (region, state, fleet, budget, ranking). |
| `/schools/:id` | FTO Detail Page | Deep-dive record: approval number, fleet breakdown, verified fee inclusions/exclusions, runways, ATC tower. |
| `/questionnaire` | Pilot Requirement Profiler | Multi-step interactive wizard with 4 curated presets (*Budget Focused*, *Premier Career*, *Fast Track*, *Balanced*). |
| `/recommendations` | Recommendations Shortlist | Ranked shortlist with match ring, criteria scores, trade-offs, budget gap, and sensitivity simulator. |
| `/compare` | FTO Side-by-Side Comparison | Compare 2 to 5 schools with metric-by-metric comparison table, trade-off matrix, and data verification badges. |
| `/analytics` | Statistical Hub | Overview card deck linking all three analytical modules with live model health status. |
| `/analytics/logistic-regression` | Logistic Regression Lab | Odds ratios, coefficients table, interactive probability calculator, ROC curve, confusion matrix. |
| `/analytics/factor-analysis` | Factor Analysis Dashboard | KMO diagnostic ($0.72$), Bartlett's sphericity, Scree plot, Varimax rotated factor loadings, factor scores. |
| `/analytics/clustering` | K-Means Cluster Explorer | Optimal $K$ selector, Inertia elbow curve, Silhouette scores, cluster centroid profiles, 2D PCA scatter plot. |
| `/evaluation` | Model Evaluation & QA | Information Retrieval metrics (NDCG@3, NDCG@5, MRR), Data Completeness ($94.4\%$), Verification rate. |
| `/sources` | DGCA Source Registry | 8 authoritative government portals, Circulars, PIB releases, and retrieval metadata. |
| `/admin/data` | Data Admin & Provenance | Field-level provenance table, verification badges, missing data flags, and data refresh triggers. |
| `/methodology` | Documentation & Formulas | Comprehensive mathematical formulation of all 4 analytical engines with LaTeX equations. |

---

## 🏛️ Authoritative Data Sources & Provenance

All seeded flying school data is mapped directly to official regulatory publications:

1. **DGCA Official Portal**: [https://www.dgca.gov.in/](https://www.dgca.gov.in/)
2. **MoCA FTO Processes**: [https://www.civilaviation.gov.in/en/node/8479](https://www.civilaviation.gov.in/en/node/8479)
3. **MoCA FTO Directory**: [https://www.civilaviation.gov.in/node/4635](https://www.civilaviation.gov.in/node/4635)
4. **DGCA DigiGOV Portal**: [https://www.dgca.gov.in/digigov-portal/](https://www.dgca.gov.in/digigov-portal/)
5. **PIB FTO Ranking Announcement**: [https://www.pib.gov.in/PressReleasePage.aspx?PRID=2255276&lang=1&reg=3](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2255276&lang=1&reg=3)
6. **DGCA Ranking Framework Notice (30 Sept 2025)**: [Public Notice Ref](https://www.dgca.gov.in/digigov-portal/Upload?attachId=OXOBBPO50KNsVklXF1f0cQ%3D%3D&baseLocale=en_US&flag=iframeAttachView)
7. **DGCA Aviation Regulations (CARs & Circulars)**: [https://www.dgca.gov.in/digigov-portal/?page=aviation-regulations](https://www.dgca.gov.in/digigov-portal/?page=aviation-regulations)
8. **DGCA Operational Dashboard**: [https://www.dgca.gov.in/digigov-portal/webHP?actionVal=loadDashboard&requestType=ApplicationRH&screenId=11000188](https://www.dgca.gov.in/digigov-portal/webHP?actionVal=loadDashboard&requestType=ApplicationRH&screenId=11000188)

---

## ⚖️ Academic Integrity & Analytical Disclosures

- **Regulatory Facts vs. Model Inferences**: The application clearly separates verifiable administrative facts (DGCA approval validity, fleet registration, ranking category) from predictive statistical scores and subjective user weights.
- **Missing Data Handling**: Missing values are preserved as `null` and highlighted as information gaps rather than arbitrarily imputed as zero.
- **Synthetic Isolation**: Demonstration training samples used to illustrate logistic regression boundaries are strictly tagged with `is_synthetic: true` and excluded from production school rankings.

---

## 🧪 Automated Test Coverage

The backend test suite (`backend/tests/test_api_endpoints.py`) verifies all core business logic and API endpoints:
- `test_health_check`
- `test_list_schools`
- `test_get_school_detail`
- `test_filter_schools_by_region`
- `test_list_sources`
- `test_list_rankings`
- `test_validate_questionnaire`
- `test_recommendations_hybrid`
- `test_recommendations_modes`
- `test_compare_schools`
- `test_analytics_logistic_regression`
- `test_analytics_factor_analysis`
- `test_analytics_clustering`
- `test_evaluation_latest`
- `test_data_quality_dashboard`
- `test_submit_feedback`

Run: `cd backend && pytest -o pythonpath=. -v`
Result: **17 passed, 0 failures**.
