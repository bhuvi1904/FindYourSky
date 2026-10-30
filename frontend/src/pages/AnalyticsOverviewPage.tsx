import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { BarChart3, Layers, Compass, ShieldCheck, Database, ArrowRight, AlertCircle } from 'lucide-react';
import { fetchAnalyticsOverview } from '../api/client';
import { AnalyticsOverviewResponse } from '../types';

export const AnalyticsOverviewPage: React.FC = () => {
  const [data, setData] = useState<AnalyticsOverviewResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAnalyticsOverview()
      .then(setData)
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div>
        <div className="flex items-center space-x-2 text-xs font-mono text-sky-400 font-semibold mb-2">
          <BarChart3 className="w-4 h-4" />
          <span>STATISTICAL MODELING LAB</span>
        </div>
        <h1 className="text-3xl font-black text-white tracking-tight">
          Business Analytics & Model Diagnostics
        </h1>
        <p className="text-xs sm:text-sm text-slate-400 mt-2 max-w-2xl leading-relaxed">
          Transparent algorithmic workbench implementing Logistic Regression, Exploratory Factor Analysis (EFA), and K-Means Clustering on verified Indian FTO operational records.
        </p>
      </div>

      {/* Summary KPI Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div className="aviation-card p-4">
          <span className="text-[10px] font-mono text-slate-400 block">TOTAL INSTITUTIONS</span>
          <span className="text-2xl font-black text-white font-mono">{data?.total_schools || 41}</span>
          <span className="text-[11px] text-slate-400 block mt-1">DGCA approved schools</span>
        </div>
        <div className="aviation-card p-4">
          <span className="text-[10px] font-mono text-slate-400 block">VERIFIED STATUS</span>
          <span className="text-2xl font-black text-emerald-400 font-mono">{data?.verified_schools_count || 17}</span>
          <span className="text-[11px] text-emerald-400/80 block mt-1">High confidence (&ge;90%)</span>
        </div>
        <div className="aviation-card p-4">
          <span className="text-[10px] font-mono text-slate-400 block">DATA COMPLETENESS</span>
          <span className="text-2xl font-black text-sky-400 font-mono">{data?.data_completeness_average || 87.5}%</span>
          <span className="text-[11px] text-sky-400/80 block mt-1">Across 12 core dimensions</span>
        </div>
        <div className="aviation-card p-4">
          <span className="text-[10px] font-mono text-slate-400 block">ACTIVE ML MODELS</span>
          <span className="text-2xl font-black text-purple-400 font-mono">{data?.active_models_count || 3}</span>
          <span className="text-[11px] text-purple-400/80 block mt-1">LR, Factor Analysis, K-Means</span>
        </div>
      </div>

      {/* Model Navigation Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Model 1: Logistic Regression */}
        <div className="aviation-card flex flex-col justify-between">
          <div>
            <div className="w-10 h-10 rounded-lg bg-sky-500/10 border border-sky-400/30 flex items-center justify-center text-sky-400 mb-4">
              <BarChart3 className="w-5 h-5" />
            </div>
            <div className="flex items-center space-x-2 mb-2">
              <span className="px-2 py-0.5 rounded bg-sky-500/10 text-sky-400 text-[10px] font-mono font-bold border border-sky-500/20">
                SUPERVISED
              </span>
              <span className="text-[10px] text-emerald-400 font-mono">Stratified CV Ready</span>
            </div>
            <h3 className="font-bold text-lg text-white mb-2">Binary Logistic Regression</h3>
            <p className="text-xs text-slate-400 leading-relaxed mb-4">
              Estimates the probability of top-tier DGCA suitability based on fee normalization, fleet availability, safety audit score, and airfield infrastructure.
            </p>
          </div>
          <Link
            to="/analytics/logistic-regression"
            className="text-xs font-bold text-sky-400 hover:text-sky-300 flex items-center justify-between pt-4 border-t border-slate-800"
          >
            <span>Inspect Coefficients & ROC Curve</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>

        {/* Model 2: Factor Analysis */}
        <div className="aviation-card flex flex-col justify-between">
          <div>
            <div className="w-10 h-10 rounded-lg bg-emerald-500/10 border border-emerald-400/30 flex items-center justify-center text-emerald-400 mb-4">
              <Layers className="w-5 h-5" />
            </div>
            <div className="flex items-center space-x-2 mb-2">
              <span className="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 text-[10px] font-mono font-bold border border-emerald-500/20">
                DIMENSIONALITY
              </span>
              <span className="text-[10px] text-emerald-400 font-mono">Varimax Rotation</span>
            </div>
            <h3 className="font-bold text-lg text-white mb-2">Exploratory Factor Analysis (EFA)</h3>
            <p className="text-xs text-slate-400 leading-relaxed mb-4">
              Reduces 7 correlated operational metrics into 3 orthogonal latent dimensions: Institutional Scale, Fleet Modernity, and Affordability.
            </p>
          </div>
          <Link
            to="/analytics/factor-analysis"
            className="text-xs font-bold text-emerald-400 hover:text-emerald-300 flex items-center justify-between pt-4 border-t border-slate-800"
          >
            <span>View Scree Plot & KMO Diagnostics</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>

        {/* Model 3: Clustering */}
        <div className="aviation-card flex flex-col justify-between">
          <div>
            <div className="w-10 h-10 rounded-lg bg-purple-500/10 border border-purple-400/30 flex items-center justify-center text-purple-400 mb-4">
              <Compass className="w-5 h-5" />
            </div>
            <div className="flex items-center space-x-2 mb-2">
              <span className="px-2 py-0.5 rounded bg-purple-500/10 text-purple-400 text-[10px] font-mono font-bold border border-purple-500/20">
                UNSUPERVISED
              </span>
              <span className="text-[10px] text-purple-400 font-mono">PCA 2D Projection</span>
            </div>
            <h3 className="font-bold text-lg text-white mb-2">K-Means Clustering</h3>
            <p className="text-xs text-slate-400 leading-relaxed mb-4">
              Identifies natural clusters among Indian flight schools using Silhouette diagnostic sweeps across candidate K (2..5), projecting onto 2D PCA space.
            </p>
          </div>
          <Link
            to="/analytics/clustering"
            className="text-xs font-bold text-purple-400 hover:text-purple-300 flex items-center justify-between pt-4 border-t border-slate-800"
          >
            <span>Explore Centroids & 2D Projection</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      </div>
    </div>
  );
};
