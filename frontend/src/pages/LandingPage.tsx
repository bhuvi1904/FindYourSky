import React from 'react';
import { Link } from 'react-router-dom';
import { Plane, Compass, Award, BarChart3, ShieldCheck, ArrowRight, CheckCircle2, ChevronRight, Layers, FileCheck } from 'lucide-react';

export const LandingPage: React.FC = () => {
  return (
    <div className="space-y-20">
      {/* Hero Section */}
      <section className="relative pt-12 pb-20 overflow-hidden radar-sweep">
        <div className="max-w-5xl mx-auto text-center px-4 sm:px-6 relative z-10">
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-sky-500/10 border border-sky-400/30 text-sky-400 text-xs font-semibold mb-6">
            <span className="w-2 h-2 rounded-full bg-sky-400 animate-pulse" />
            <span>DGCA CAR SECTION 7 SERIES D COMPLIANT</span>
          </div>

          <h1 className="text-4xl sm:text-6xl font-black text-white tracking-tight leading-tight sm:leading-none">
            Find Your Optimal <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 via-cyan-300 to-blue-500">
              Indian Flying School
            </span>
          </h1>

          <p className="mt-6 text-base sm:text-lg text-slate-300 max-w-2xl mx-auto leading-relaxed">
            Data-driven decision support system evaluating DGCA-approved Flying Training Organisations across verified fees, aircraft fleet, official rankings, and multi-criteria student preferences.
          </p>

          <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link
              to="/questionnaire"
              className="w-full sm:w-auto px-8 py-3.5 rounded-xl bg-sky-400 hover:bg-sky-300 text-slate-950 font-bold text-sm shadow-lg shadow-sky-500/25 flex items-center justify-center space-x-2 transition-all transform hover:-translate-y-0.5"
            >
              <span>Start Personalised Match</span>
              <ArrowRight className="w-4 h-4" />
            </Link>

            <Link
              to="/schools"
              className="w-full sm:w-auto px-8 py-3.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 border border-slate-700 font-semibold text-sm flex items-center justify-center space-x-2 transition-all"
            >
              <span>Explore All 41 DGCA FTOs</span>
            </Link>
          </div>

          {/* Quick Stats Grid */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-16 text-left">
            <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800/80">
              <span className="text-2xl font-black text-white font-mono block">41</span>
              <span className="text-xs text-slate-400">DGCA Approved FTOs</span>
            </div>
            <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800/80">
              <span className="text-2xl font-black text-emerald-400 font-mono block">100%</span>
              <span className="text-xs text-slate-400">Verified DGCA Records</span>
            </div>
            <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800/80">
              <span className="text-2xl font-black text-sky-400 font-mono block">3</span>
              <span className="text-xs text-slate-400">Statistical Models</span>
            </div>
            <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800/80">
              <span className="text-2xl font-black text-purple-400 font-mono block">5-Way</span>
              <span className="text-xs text-slate-400">School Comparison</span>
            </div>
          </div>
        </div>
      </section>

      {/* Analytical Triad Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-3xl mx-auto mb-12">
          <span className="text-xs font-mono uppercase tracking-wider text-sky-400 font-bold">Scientific Foundation</span>
          <h2 className="text-2xl sm:text-3xl font-black text-white mt-2">
            Three Rigorous Statistical Approaches
          </h2>
          <p className="text-sm text-slate-400 mt-3 leading-relaxed">
            Unlike commercial listing sites that promote paid sponsorships, FindYourSky applies genuine Python scientific modeling to rank schools objectively.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Card 1: Logistic Regression */}
          <div className="aviation-card flex flex-col justify-between">
            <div>
              <div className="w-10 h-10 rounded-lg bg-sky-500/10 border border-sky-400/30 flex items-center justify-center text-sky-400 mb-4">
                <BarChart3 className="w-5 h-5" />
              </div>
              <h3 className="font-bold text-lg text-white mb-2">1. Logistic Regression</h3>
              <p className="text-xs text-slate-400 leading-relaxed mb-4">
                Computes odds ratios and predictive probabilities of top-tier institutional success using standardized predictors with cross-validated calibration.
              </p>
            </div>
            <Link
              to="/analytics/logistic-regression"
              className="text-xs font-semibold text-sky-400 hover:text-sky-300 flex items-center space-x-1 pt-3 border-t border-slate-800"
            >
              <span>Inspect Coefficients & ROC Curve</span>
              <ChevronRight className="w-3.5 h-3.5" />
            </Link>
          </div>

          {/* Card 2: Factor Analysis */}
          <div className="aviation-card flex flex-col justify-between">
            <div>
              <div className="w-10 h-10 rounded-lg bg-emerald-500/10 border border-emerald-400/30 flex items-center justify-center text-emerald-400 mb-4">
                <Layers className="w-5 h-5" />
              </div>
              <h3 className="font-bold text-lg text-white mb-2">2. Factor Analysis (EFA)</h3>
              <p className="text-xs text-slate-400 leading-relaxed mb-4">
                Discovers underlying latent dimensions (Institutional Scale, Fleet Modernity, Affordability) via Varimax rotation, Scree plot eigenvalues, and KMO test.
              </p>
            </div>
            <Link
              to="/analytics/factor-analysis"
              className="text-xs font-semibold text-emerald-400 hover:text-emerald-300 flex items-center space-x-1 pt-3 border-t border-slate-800"
            >
              <span>View Scree Plot & Loadings</span>
              <ChevronRight className="w-3.5 h-3.5" />
            </Link>
          </div>

          {/* Card 3: Clustering */}
          <div className="aviation-card flex flex-col justify-between">
            <div>
              <div className="w-10 h-10 rounded-lg bg-purple-500/10 border border-purple-400/30 flex items-center justify-center text-purple-400 mb-4">
                <Compass className="w-5 h-5" />
              </div>
              <h3 className="font-bold text-lg text-white mb-2">3. K-Means Clustering</h3>
              <p className="text-xs text-slate-400 leading-relaxed mb-4">
                Partitions Indian flying schools into objective operational archetypes evaluated via Silhouette scores, inertia elbow analysis, and 2D PCA projection.
              </p>
            </div>
            <Link
              to="/analytics/clustering"
              className="text-xs font-semibold text-purple-400 hover:text-purple-300 flex items-center space-x-1 pt-3 border-t border-slate-800"
            >
              <span>Explore 2D PCA Clusters</span>
              <ChevronRight className="w-3.5 h-3.5" />
            </Link>
          </div>
        </div>
      </section>

      {/* Decision Integrity & Data Provenance */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="rounded-2xl p-8 sm:p-10 bg-gradient-to-r from-slate-900 via-slate-900 to-sky-950 border border-slate-800 shadow-2xl">
          <div className="max-w-3xl">
            <span className="text-xs font-mono uppercase tracking-wider text-sky-400 font-bold">Academic Transparency</span>
            <h2 className="text-2xl sm:text-3xl font-black text-white mt-2">
              Honest Disclosures & Provenance Verification
            </h2>
            <p className="text-sm text-slate-300 mt-3 leading-relaxed">
              We separate regulatory facts from statistical predictions and user preference weights. If fee data or airfield night lighting is unverified for an institution, we state it explicitly rather than pretending missing data is zero.
            </p>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-6">
              <div className="flex items-start space-x-2 text-xs text-slate-300">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0 mt-0.5" />
                <span>Field-level provenance linking each approval to official DGCA notices</span>
              </div>
              <div className="flex items-start space-x-2 text-xs text-slate-300">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0 mt-0.5" />
                <span>Clear distinction between CPL flight hours, ground school, and hostel fees</span>
              </div>
              <div className="flex items-start space-x-2 text-xs text-slate-300">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0 mt-0.5" />
                <span>Multi-engine fleet verification (DA42, Seneca, Vulcanair P68C, Tecnam)</span>
              </div>
              <div className="flex items-start space-x-2 text-xs text-slate-300">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0 mt-0.5" />
                <span>Direct clickable official links to DGCA portals and school websites</span>
              </div>
            </div>

            <div className="mt-8 flex items-center space-x-4">
              <Link
                to="/sources"
                className="px-5 py-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white text-xs font-semibold flex items-center space-x-1.5 transition-colors"
              >
                <FileCheck className="w-4 h-4 text-sky-400" />
                <span>View DGCA Document Register</span>
              </Link>
              <Link
                to="/about/methodology"
                className="text-xs font-semibold text-sky-400 hover:text-sky-300 flex items-center space-x-1"
              >
                <span>Read Full Methodology</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};
