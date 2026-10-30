import {
  SchoolSummary, SchoolDetail, QuestionnaireInput,
  RecommendationResponse, SchoolComparisonResponse,
  LogisticRegressionSummary, FactorAnalysisSummary,
  ClusteringSummary, AnalyticsOverviewResponse,
  DataQualityDashboard, DataSource
} from '../types';

const API_BASE = '/api';

export async function fetchSchools(params?: {
  region?: string;
  state?: string;
  ranking_category?: string;
  has_multi_engine?: boolean;
  max_budget?: number;
  search?: string;
}): Promise<SchoolSummary[]> {
  const query = new URLSearchParams();
  if (params?.region) query.append('region', params.region);
  if (params?.state) query.append('state', params.state);
  if (params?.ranking_category) query.append('ranking_category', params.ranking_category);
  if (params?.has_multi_engine !== undefined) query.append('has_multi_engine', String(params.has_multi_engine));
  if (params?.max_budget) query.append('max_budget', String(params.max_budget));
  if (params?.search) query.append('search', params.search);

  const res = await fetch(`${API_BASE}/schools?${query.toString()}`);
  if (!res.ok) throw new Error('Failed to fetch flying schools directory.');
  return res.json();
}

export async function fetchSchoolDetail(id: string): Promise<SchoolDetail> {
  const res = await fetch(`${API_BASE}/schools/${id}`);
  if (!res.ok) throw new Error(`Failed to fetch school details for '${id}'.`);
  return res.json();
}

export async function validateQuestionnaire(input: QuestionnaireInput) {
  const res = await fetch(`${API_BASE}/questionnaire/validate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(input),
  });
  if (!res.ok) throw new Error('Failed to validate questionnaire.');
  return res.json();
}

export async function getRecommendations(
  input: QuestionnaireInput,
  mode: string = 'hybrid'
): Promise<RecommendationResponse> {
  const res = await fetch(`${API_BASE}/recommendations?mode=${mode}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(input),
  });
  if (!res.ok) throw new Error('Failed to generate recommendations.');
  return res.json();
}

export async function compareSchools(
  schoolIds: string[],
  questionnaire?: QuestionnaireInput
): Promise<SchoolComparisonResponse> {
  const res = await fetch(`${API_BASE}/recommendations/compare`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ school_ids: schoolIds, questionnaire }),
  });
  if (!res.ok) throw new Error('Failed to compare selected flying schools.');
  return res.json();
}

export async function fetchAnalyticsOverview(): Promise<AnalyticsOverviewResponse> {
  const res = await fetch(`${API_BASE}/analytics/overview`);
  if (!res.ok) throw new Error('Failed to load analytics overview.');
  return res.json();
}

export async function fetchLogisticRegression(syntheticDemo: boolean = false): Promise<LogisticRegressionSummary> {
  const res = await fetch(`${API_BASE}/analytics/logistic-regression?synthetic_demo=${syntheticDemo}`);
  if (!res.ok) throw new Error('Failed to load logistic regression model diagnostics.');
  return res.json();
}

export async function fetchFactorAnalysis(factors: number = 3): Promise<FactorAnalysisSummary> {
  const res = await fetch(`${API_BASE}/analytics/factor-analysis?factors=${factors}`);
  if (!res.ok) throw new Error('Failed to load factor analysis model.');
  return res.json();
}

export async function fetchClustering(k?: number): Promise<ClusteringSummary> {
  const url = k ? `${API_BASE}/analytics/clustering?k=${k}` : `${API_BASE}/analytics/clustering`;
  const res = await fetch(url);
  if (!res.ok) throw new Error('Failed to load clustering model.');
  return res.json();
}

export async function fetchLatestEvaluation(): Promise<any> {
  const res = await fetch(`${API_BASE}/evaluation/latest`);
  if (!res.ok) throw new Error('Failed to load model evaluation reports.');
  return res.json();
}

export async function fetchSources(): Promise<DataSource[]> {
  const res = await fetch(`${API_BASE}/sources`);
  if (!res.ok) throw new Error('Failed to load authoritative data sources.');
  return res.json();
}

export async function submitFeedback(data: {
  rating: number;
  was_helpful: boolean;
  comments?: string;
  school_id?: string;
}) {
  const res = await fetch(`${API_BASE}/feedback`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return res.json();
}
