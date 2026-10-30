import React from 'react';
import { BookOpen, ShieldCheck, BarChart3, Layers, Compass, AlertTriangle, CheckCircle2 } from 'lucide-react';
import { Link } from 'react-router-dom';

export const MethodologyPage: React.FC = () => {
  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10">
      {/* Header */}
      <div>
        <div className="flex items-center space-x-2 text-xs font-mono text-sky-400 font-semibold mb-2">
          <BookOpen className="w-4 h-4" />
          <span>ACADEMIC & STATISTICAL METHODOLOGY</span>
        </div>
        <h1 className="text-3xl font-black text-white tracking-tight">
          System Architecture & Statistical Formulation
        </h1>
        <p className="text-xs sm:text-sm text-slate-400 mt-2 leading-relaxed">
          Technical reference detailing mathematical formulation, sampling adequacy criteria, cross-validation protocols, and academic boundaries of the FindYourSky recommendation engine.
        </p>
      </div>

      {/* 1. Multi-Stage Pipeline */}
      <section className="aviation-card space-y-4">
        <h2 className="text-lg font-bold text-white flex items-center space-x-2">
          <span className="w-6 h-6 rounded-md bg-sky-500/20 text-sky-400 font-mono text-xs flex items-center justify-center font-bold">1</span>
          <span>Multi-Stage Recommendation Architecture</span>
        </h2>
        <p className="text-xs text-slate-300 leading-relaxed">
          The engine operates sequentially to prevent unviable institutions from biasing statistical normalization:
        </p>
        <div className="space-y-3 text-xs font-mono">
          <div className="p-3 rounded-lg bg-slate-950/70 border border-slate-800">
            <span className="text-sky-400 font-bold block">STAGE 1: Regulatory & Hard Eligibility Filtering</span>
            <span className="text-slate-400 text-[11px] block mt-0.5 font-sans">
              Filters schools on active DGCA CAR approval, budget cut-offs (with user-selected strictness 0%, 10%, or 25%), multi-engine requirements, and geographic relocation constraints.
            </span>
          </div>
          <div className="p-3 rounded-lg bg-slate-950/70 border border-slate-800">
            <span className="text-emerald-400 font-bold block">STAGE 2: Multi-Criteria Preference Scoring</span>
            <span className="text-slate-400 text-[11px] block mt-0.5 font-sans">
              Calculates normalized sub-scores (0-100) across Affordability, DGCA Ranking, Fleet Size, Location Proximity, and Airfield Infrastructure, normalized with user preference weights.
            </span>
          </div>
          <div className="p-3 rounded-lg bg-slate-950/70 border border-slate-800">
            <span className="text-purple-400 font-bold block">STAGE 3: Statistical Triad Integration</span>
            <span className="text-slate-400 text-[11px] block mt-0.5 font-sans">
              Blends preference scores with Logistic Regression predicted suitability probabilities, EFA latent factor dimensions, or K-Means cluster profile similarities.
            </span>
          </div>
          <div className="p-3 rounded-lg bg-slate-950/70 border border-slate-800">
            <span className="text-amber-400 font-bold block">STAGE 4: Qualitative Explanation & Sensitivity Simulation</span>
            <span className="text-slate-400 text-[11px] block mt-0.5 font-sans">
              Generates discrete advantages, trade-offs, and missingness warnings, accompanied by a dynamic +/- 20% sensitivity analysis.
            </span>
          </div>
        </div>
      </section>

      {/* 2. Model 1: Logistic Regression */}
      <section className="aviation-card space-y-4">
        <h2 className="text-lg font-bold text-white flex items-center space-x-2">
          <BarChart3 className="w-5 h-5 text-sky-400" />
          <span>Model 1: Binary Logistic Regression</span>
        </h2>
        <p className="text-xs text-slate-300 leading-relaxed">
          Supervised inference predicting the conditional log-odds of a flight school meeting premier DGCA Tier-1 benchmarks:
        </p>
        <div className="p-4 rounded-xl bg-slate-950/80 border border-slate-800 text-xs font-mono text-center text-sky-300">
          ln( P / (1 - P) ) = \u03b2\u2080 + \u03b2\u2081(Fee) + \u03b2\u2082(Fleet) + \u03b2\u2083(MultiEngine) + \u03b2\u2084(DGCAScore) + \u03b2\u2085(SafetyAudit) + ...
        </div>
        <p className="text-xs text-slate-400 leading-relaxed">
          Odds ratios are computed as OR_j = exp(\u03b2_j), reflecting multiplicative shifts in the likelihood of premier classification per one standard deviation increase in predictor X_j. All metrics are cross-validated using Stratified K-Fold splits.
        </p>
      </section>

      {/* 3. Model 2: Factor Analysis */}
      <section className="aviation-card space-y-4">
        <h2 className="text-lg font-bold text-white flex items-center space-x-2">
          <Layers className="w-5 h-5 text-emerald-400" />
          <span>Model 2: Exploratory Factor Analysis (EFA)</span>
        </h2>
        <p className="text-xs text-slate-300 leading-relaxed">
          Unsupervised dimensionality reduction resolving multi-collinearity across operational indicators. Sampling adequacy is verified mathematically:
        </p>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs font-mono">
          <div className="p-3 rounded-lg bg-slate-950/70 border border-slate-800">
            <span className="text-emerald-400 font-bold block mb-1">Kaiser-Meyer-Olkin (KMO)</span>
            <span>KMO = \u2211\u2211 r\u00b2 / (\u2211\u2211 r\u00b2 + \u2211\u2211 a\u00b2)</span>
            <span className="text-[10px] text-slate-400 block mt-1 font-sans">
              Evaluates whether partial correlations among variables are sufficiently small.
            </span>
          </div>
          <div className="p-3 rounded-lg bg-slate-950/70 border border-slate-800">
            <span className="text-sky-400 font-bold block mb-1">Bartlett's Sphericity Test</span>
            <span>\u03c7\u00b2 = - (N - 1 - (2p+5)/6) \u2022 ln |R|</span>
            <span className="text-[10px] text-slate-400 block mt-1 font-sans">
              Tests hypothesis that correlation matrix R is an identity matrix (df = p(p-1)/2).
            </span>
          </div>
        </div>
        <p className="text-xs text-slate-400 leading-relaxed">
          Factors are orthogonally rotated via the Varimax criterion to maximize the variance of squared loadings, achieving an interpretable simple structure across Institutional Scale, Fleet Modernity, and Affordability.
        </p>
      </section>

      {/* 4. Model 3: K-Means Clustering */}
      <section className="aviation-card space-y-4">
        <h2 className="text-lg font-bold text-white flex items-center space-x-2">
          <Compass className="w-5 h-5 text-purple-400" />
          <span>Model 3: K-Means Cluster Profiling</span>
        </h2>
        <p className="text-xs text-slate-300 leading-relaxed">
          Partitions institutions into K distinct clusters minimizing within-cluster variance (WCSS):
        </p>
        <div className="p-4 rounded-xl bg-slate-950/80 border border-slate-800 text-xs font-mono text-center text-purple-300">
          {"Inertia = \u2211 (within-cluster sum of squares) across K clusters"}
        </div>
        <p className="text-xs text-slate-400 leading-relaxed">
          Optimal cluster count K is determined through silhouette analysis across candidate values (K \u2208 [2..5]). Coordinates are projected onto a 2D plane via Principal Component Analysis (PCA) for intuitive spatial visualization.
        </p>
      </section>

      {/* Known Limitations */}
      <section className="aviation-card p-6 border-l-4 border-l-amber-400 space-y-3">
        <h3 className="font-bold text-white text-base flex items-center space-x-2">
          <AlertTriangle className="w-5 h-5 text-amber-400" />
          <span>Known Data Limitations & Academic Boundaries</span>
        </h3>
        <ul className="space-y-2 text-xs text-slate-300 leading-relaxed list-disc list-inside">
          <li>
            <strong>Sample Size Boundary:</strong> Complete national directory of all 41 DGCA-approved Flying Training Organisations across India, incorporating the latest Phase 2 performance rankings (MoCA / PIB PRID 2255276).
          </li>
          <li>
            <strong>Fee Component Discrepancies:</strong> While flight training hours are verified, student boarding and exam charges vary based on individual accommodation choices.
          </li>
          <li>
            <strong>No Admission Guarantee:</strong> Match scores represent analytical suitability and do not constitute admission guarantees, airline employment endorsements, or regulatory certification.
          </li>
        </ul>
      </section>
    </div>
  );
};
