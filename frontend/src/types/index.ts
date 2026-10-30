export interface SchoolBase {
  id?: number;
  base_id: string;
  is_primary: boolean;
  airport_name: string;
  icao_code?: string;
  city: string;
  state: string;
  region: string;
  runway_length_meters?: number;
  runway_surface?: string;
  night_flying_available: boolean;
  atc_type?: string;
  latitude?: number;
  longitude?: number;
}

export interface AircraftFleet {
  id?: number;
  aircraft_model: string;
  manufacturer?: string;
  engine_type: string;
  avionics_type?: string;
  count: number;
  operational_count: number;
  fuel_type?: string;
}

export interface SchoolFee {
  id?: number;
  course_name: string;
  currency: string;
  tuition_flying_inr: number;
  ground_school_inr: number;
  simulator_inr: number;
  hostel_mess_annual_inr: number;
  tax_gst_inr: number;
  total_estimated_inr: number;
  is_fee_inclusive_hostel: boolean;
  is_fee_verified: boolean;
  fee_effective_date?: string;
  source_url?: string;
  inclusions: string[];
  exclusions: string[];
  notes?: string;
}

export interface DGCARanking {
  id?: number;
  ranking_period: string;
  ranking_category: string;
  overall_score?: number;
  national_rank?: number;
  annual_hours_logged?: number;
  safety_audit_score?: number;
  cfi_cadre_strength?: number;
  source_id?: string;
  effective_date?: string;
  notes?: string;
}

export interface SchoolProgramme {
  id?: number;
  programme_name: string;
  licence_type: string;
  duration_months: number;
  description?: string;
}

export interface SchoolSummary {
  id: number;
  school_id: string;
  name: string;
  short_name?: string;
  slug: string;
  website_url: string;
  ownership_type: string;
  dgca_approval_no: string;
  operational_status: string;
  latest_ranking_category: string;
  latest_dgca_score?: number;
  primary_city?: string;
  primary_state?: string;
  primary_region?: string;
  total_fleet_count: number;
  multi_engine_count: number;
  glass_cockpit_available: boolean;
  night_flying_available: boolean;
  indicative_fee_inr?: number;
  is_fee_verified: boolean;
  confidence_score: number;
  completeness_score: number;
  is_synthetic: boolean;
}

export interface SchoolDetail extends SchoolSummary {
  approval_validity?: string;
  established_year?: number;
  last_verified_date?: string;
  bases: SchoolBase[];
  fleet: AircraftFleet[];
  fees: SchoolFee[];
  rankings: DGCARanking[];
  programmes: SchoolProgramme[];
}

export interface PreferenceWeights {
  cost: number;
  ranking: number;
  fleet: number;
  location: number;
  infrastructure: number;
}

export interface QuestionnaireInput {
  career_objective: string;
  max_budget_inr: number;
  budget_includes_hostel: boolean;
  financing_required: boolean;
  budget_flexibility: string;
  preferred_regions: string[];
  preferred_states: string[];
  willing_to_relocate: boolean;
  min_dgca_category: string;
  require_multi_engine: boolean;
  require_hostel: boolean;
  require_glass_cockpit: boolean;
  require_night_flying: boolean;
  allow_missing_fee: boolean;
  allow_unverified: boolean;
  preset_name: string;
  weights: PreferenceWeights;
}

export interface SchoolMatchResult {
  school_id: string;
  name: string;
  short_name?: string;
  slug: string;
  website_url: string;
  primary_city: string;
  primary_state: string;
  primary_region: string;
  rank: number;
  overall_match_score: number;
  regulatory_eligibility: string;
  cost_score: number;
  ranking_score: number;
  fleet_score: number;
  location_score: number;
  infrastructure_score: number;
  statistical_boost: number;
  indicative_fee_inr?: number;
  is_fee_verified: boolean;
  fee_inclusions: string[];
  fee_exclusions: string[];
  budget_gap_inr: number;
  dgca_ranking_category: string;
  dgca_overall_score?: number;
  total_fleet_count: number;
  multi_engine_count: number;
  aircraft_models: string[];
  night_flying_available: boolean;
  atc_environment?: string;
  match_reasons: string[];
  tradeoffs: string[];
  missing_information: string[];
  dgca_approval_no: string;
  approval_validity?: string;
  last_verified_date?: string;
  confidence_score: number;
  completeness_score: number;
  dgca_document_url?: string;
  is_synthetic: boolean;
}

export interface RecommendationResponse {
  run_id: string;
  analytical_mode: string;
  total_evaluated: number;
  eligible_count: number;
  schools: SchoolMatchResult[];
  methodology_summary: string;
  weights_applied: Record<string, number>;
  sensitivity_analysis?: Record<string, Array<{
    short_name: string;
    base_score: number;
    simulated_score: number;
    score_delta: number;
  }>>;
}

export interface ComparisonMetricRow {
  metric_label: string;
  category: string;
  values: Record<string, string | null>;
  highlight_best_id?: string;
  data_verified: Record<string, boolean>;
}

export interface SchoolComparisonResponse {
  schools: SchoolMatchResult[];
  comparison_table: ComparisonMetricRow[];
  tradeoff_matrix: Record<string, string[]>;
}

export interface LogisticRegressionSummary {
  is_available: boolean;
  status_message: string;
  sample_size: number;
  positive_count: number;
  negative_count: number;
  features: string[];
  coefficients: Record<string, number>;
  odds_ratios: Record<string, number>;
  intercept: number;
  accuracy?: number;
  precision?: number;
  recall?: number;
  f1_score?: number;
  roc_auc?: number;
  brier_score?: number;
  confusion_matrix?: number[][];
  roc_curve_points?: Array<{ fpr: number; tpr: number }>;
  school_probabilities?: Array<{
    school_id: string;
    name: string;
    suitability_probability: number;
    actual_tier_label: number;
  }>;
  is_synthetic_demonstration: boolean;
  validation_method: string;
  training_timestamp?: string;
}

export interface FactorAnalysisSummary {
  is_available: boolean;
  status_message: string;
  sample_size: number;
  feature_count: number;
  features: string[];
  kmo_overall?: number;
  kmo_per_variable?: Record<string, number>;
  bartlett_chi_square?: number;
  bartlett_p_value?: number;
  num_factors_selected: number;
  eigenvalues: number[];
  cumulative_variance: number[];
  factor_loadings: Record<string, number[]>;
  communalities: Record<string, number>;
  factor_labels: string[];
  school_factor_scores: Array<{
    school_id: string;
    name: string;
    short_name: string;
    ranking_category: string;
    factor_scores: Record<string, number>;
  }>;
}

export interface ClusteringSummary {
  is_available: boolean;
  status_message: string;
  optimal_k: number;
  candidate_k_values: number[];
  inertias: number[];
  silhouette_scores: number[];
  cluster_profiles: Array<{
    cluster_id: number;
    cluster_name: string;
    description: string;
    size: number;
    percentage: number;
    mean_tuition_fee_lakhs: number;
    mean_fleet_size: number;
    mean_multi_engine_count: number;
    mean_dgca_score: number;
    mean_annual_hours_k: number;
    night_flying_available_pct: number;
  }>;
  pca_2d_points: Array<{
    school_id: string;
    name: string;
    short_name: string;
    cluster_id: number;
    cluster_name: string;
    pca_x: number;
    pca_y: number;
    ranking_category: string;
    fee_lakhs: number;
    fleet_size: number;
  }>;
  stability_score: number;
}

export interface AnalyticsOverviewResponse {
  total_schools: number;
  verified_schools_count: number;
  active_models_count: number;
  logistic_regression_ready: boolean;
  factor_analysis_ready: boolean;
  clustering_ready: boolean;
  data_completeness_average: number;
}

export interface DataQualityDashboard {
  total_schools: number;
  verified_approval_pct: number;
  verified_website_pct: number;
  verified_ranking_pct: number;
  published_fee_pct: number;
  missingness_by_field: Record<string, number>;
  stale_records_count: number;
  source_coverage_count: number;
  last_refresh_date: string;
  completeness_distribution: Record<string, number>;
}

export interface RecommendationQualityReport {
  benchmark_dataset: string;
  total_queries_evaluated: number;
  ndcg_at_3: number;
  ndcg_at_5: number;
  precision_at_3: number;
  precision_at_5: number;
  recall_at_5: number;
  mrr: number;
  baseline_ndcg_at_5: number;
  relevance_methodology: string;
}

export interface DataSource {
  id?: number;
  source_id: string;
  name: string;
  url: string;
  source_type: string;
  publisher?: string;
  description?: string;
  verification_status: string;
  retrieval_date?: string;
}
