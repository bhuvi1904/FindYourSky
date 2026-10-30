import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import {
  Award, Compass, Scale, Sliders, ExternalLink, CheckCircle2,
  AlertTriangle, Shield, RefreshCw, Info, ChevronRight, Check
} from 'lucide-react';
import { getRecommendations } from '../api/client';
import { QuestionnaireInput, RecommendationResponse, SchoolMatchResult } from '../types';
import { MatchScoreRing } from '../components/recommendations/MatchScoreRing';
import { SensitivitySimulator } from '../components/recommendations/SensitivitySimulator';

export const RecommendationsPage: React.FC = () => {
  const navigate = useNavigate();
  const [response, setResponse] = useState<RecommendationResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [mode, setMode] = useState<'hybrid' | 'logistic_regression' | 'factor_analysis' | 'clustering'>('hybrid');
  const [selectedForCompare, setSelectedForCompare] = useState<string[]>([]);

  // Load questionnaire from storage
  const [questionnaire, setQuestionnaire] = useState<QuestionnaireInput>(() => {
    const saved = sessionStorage.getItem('findyoursky_questionnaire');
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {
        // fallback
      }
    }
    return {
      career_objective: 'CPL_ME_IR',
      max_budget_inr: 5000000,
      budget_includes_hostel: false,
      financing_required: false,
      budget_flexibility: 'moderate',
      preferred_regions: ['Anywhere'],
      preferred_states: [],
      willing_to_relocate: true,
      min_dgca_category: 'Any',
      require_multi_engine: true,
      require_hostel: false,
      require_glass_cockpit: true,
      require_night_flying: false,
      allow_missing_fee: false,
      allow_unverified: false,
      preset_name: 'balanced',
      weights: { cost: 0.25, ranking: 0.25, fleet: 0.20, location: 0.15, infrastructure: 0.15 }
    };
  });

  const loadRecommendations = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getRecommendations(questionnaire, mode);
      setResponse(data);
    } catch (err: any) {
      setError(err.message || 'Failed to generate recommendations.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadRecommendations();
  }, [mode]);

  const handleToggleCompare = (schoolId: string) => {
    if (selectedForCompare.includes(schoolId)) {
      setSelectedForCompare(selectedForCompare.filter((id) => id !== schoolId));
    } else {
      if (selectedForCompare.length >= 5) {
        alert('You can select a maximum of 5 schools for comparison.');
        return;
      }
      setSelectedForCompare([...selectedForCompare, schoolId]);
    }
  };

  const handleLaunchCompare = () => {
    if (selectedForCompare.length < 2) {
      alert('Please select at least 2 schools to compare.');
      return;
    }
    navigate(`/compare?ids=${selectedForCompare.join(',')}`);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Top Banner */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-slate-800">
        <div>
          <div className="flex items-center space-x-2 text-xs font-mono text-sky-400 font-semibold mb-1">
            <Compass className="w-4 h-4" />
            <span>PERSONALIZED MULTI-CRITERIA RESULTS</span>
          </div>
          <h1 className="text-3xl font-black text-white tracking-tight">
            Top Recommended Flying Training Organisations
          </h1>
          <p className="text-xs text-slate-400 mt-1 max-w-2xl font-mono">
            {response?.methodology_summary || 'Ranking calculated through multi-criteria preference scoring & statistical models.'}
          </p>
        </div>

        <div className="flex items-center space-x-3">
          <Link
            to="/questionnaire"
            className="px-4 py-2 rounded-lg bg-slate-900 border border-slate-700 hover:border-slate-600 text-xs font-medium text-slate-300 flex items-center space-x-1.5 transition-colors"
          >
            <Sliders className="w-3.5 h-3.5" />
            <span>Edit Preferences</span>
          </Link>
        </div>
      </div>

      {/* Analytical Mode Selector */}
      <div className="aviation-card p-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs">
          <span className="font-mono text-slate-400 font-bold uppercase tracking-wider">
            ANALYTICAL ENGINE MODE:
          </span>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
            {[
              { id: 'hybrid', label: 'Hybrid Mode (Recommended)' },
              { id: 'logistic_regression', label: 'Logistic Regression Mode' },
              { id: 'factor_analysis', label: 'Factor Analysis Mode' },
              { id: 'clustering', label: 'K-Means Clustering Mode' },
            ].map((m) => (
              <button
                key={m.id}
                onClick={() => setMode(m.id as any)}
                className={`px-3 py-2 rounded-lg font-mono text-[11px] font-bold transition-all ${
                  mode === m.id
                    ? 'bg-sky-500 text-slate-950 shadow-md shadow-sky-500/20'
                    : 'bg-slate-950 text-slate-400 hover:text-white hover:bg-slate-800 border border-slate-800'
                }`}
              >
                {m.label}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Loading state */}
      {loading ? (
        <div className="py-20 text-center">
          <div className="w-12 h-12 border-4 border-sky-400 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-xs font-mono text-slate-400">Computing hybrid statistical ranks across all 41 DGCA FTOs...</p>
        </div>
      ) : error ? (
        <div className="aviation-card p-8 text-center text-rose-400">
          <AlertTriangle className="w-10 h-10 mx-auto mb-2" />
          <p>{error}</p>
        </div>
      ) : response?.schools.length === 0 ? (
        <div className="aviation-card p-12 text-center">
          <Info className="w-12 h-12 text-slate-500 mx-auto mb-4" />
          <h3 className="text-lg font-bold text-white">No Institutions Match Your Strict Constraints</h3>
          <p className="text-xs text-slate-400 max-w-md mx-auto mt-2 mb-4">
            Try adjusting your budget or enabling relocation in the questionnaire.
          </p>
          <Link to="/questionnaire" className="px-4 py-2 rounded-lg bg-sky-500 text-slate-950 font-bold text-xs">
            Modify Questionnaire
          </Link>
        </div>
      ) : (
        <div className="space-y-6">
          {/* School Results Shortlist */}
          {response?.schools.map((school) => {
            const isSelected = selectedForCompare.includes(school.school_id);

            return (
              <div
                key={school.school_id}
                className={`aviation-card transition-all ${
                  isSelected ? 'ring-2 ring-sky-400 border-sky-400' : ''
                }`}
              >
                <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 pb-6 border-b border-slate-800/80">
                  {/* Left Identity */}
                  <div className="space-y-2">
                    <div className="flex items-center space-x-3">
                      <span className="w-8 h-8 rounded-full bg-sky-500/20 text-sky-400 font-mono font-black text-sm flex items-center justify-center border border-sky-500/40">
                        #{school.rank}
                      </span>
                      <span className="px-2.5 py-0.5 rounded text-[11px] font-bold font-mono bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                        DGCA {school.dgca_ranking_category}
                      </span>
                      <span className="text-xs text-slate-400 font-mono">
                        Approval: {school.dgca_approval_no}
                      </span>
                    </div>

                    <h2 className="text-2xl font-black text-white tracking-tight">
                      <Link to={`/schools/${school.school_id}`} className="hover:text-sky-400 transition-colors">
                        {school.name}
                      </Link>
                    </h2>

                    <div className="flex flex-wrap items-center gap-4 text-xs text-slate-400 font-mono">
                      <span>Primary Base: {school.primary_city}, {school.primary_state}</span>
                      <span>•</span>
                      <span>Fleet: {school.total_fleet_count} Aircraft ({school.multi_engine_count} Multi-Engine)</span>
                      <span>•</span>
                      {school.indicative_fee_inr ? (
                        <span className="text-emerald-400 font-bold">
                          Fee: ₹{(school.indicative_fee_inr / 100000).toFixed(1)} Lakhs
                        </span>
                      ) : (
                        <span className="text-slate-400 italic">Fee: Unverified Quote</span>
                      )}
                    </div>
                  </div>

                  {/* Right Compare & Links */}
                  <div className="flex items-center space-x-3 flex-shrink-0">
                    <button
                      onClick={() => handleToggleCompare(school.school_id)}
                      className={`px-3 py-2 rounded-lg text-xs font-semibold font-mono flex items-center space-x-1 border transition-all ${
                        isSelected
                          ? 'bg-sky-500 text-slate-950 border-sky-400 font-bold'
                          : 'bg-slate-900 text-slate-300 border-slate-700 hover:border-slate-500'
                      }`}
                    >
                      {isSelected ? <Check className="w-3.5 h-3.5 stroke-[3]" /> : null}
                      <span>{isSelected ? 'Selected' : 'Add to Compare'}</span>
                    </button>

                    {school.website_url && (
                      <a
                        href={school.website_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="p-2 rounded-lg bg-slate-900 border border-slate-700 text-slate-400 hover:text-white transition-colors"
                        title="Official School Website"
                      >
                        <ExternalLink className="w-4 h-4" />
                      </a>
                    )}
                  </div>
                </div>

                {/* Match Score & Criterion Breakdown */}
                <div className="py-6">
                  <MatchScoreRing
                    score={school.overall_match_score}
                    subscores={{
                      cost: school.cost_score,
                      ranking: school.ranking_score,
                      fleet: school.fleet_score,
                      location: school.location_score,
                      infrastructure: school.infrastructure_score,
                    }}
                  />
                </div>

                {/* Qualitative Explanation Grid */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-4 border-t border-slate-800/80 text-xs">
                  {/* Advantages */}
                  <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800 space-y-2">
                    <h4 className="font-bold text-emerald-400 font-mono uppercase tracking-wider flex items-center space-x-1.5">
                      <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                      <span>Match Advantages</span>
                    </h4>
                    <ul className="space-y-1.5 text-slate-300">
                      {school.match_reasons.map((r, i) => (
                        <li key={i} className="flex items-start space-x-1.5">
                          <span className="text-emerald-400">•</span>
                          <span>{r}</span>
                        </li>
                      ))}
                    </ul>
                  </div>

                  {/* Disadvantages / Tradeoffs */}
                  <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800 space-y-2">
                    <h4 className="font-bold text-amber-400 font-mono uppercase tracking-wider flex items-center space-x-1.5">
                      <AlertTriangle className="w-4 h-4 text-amber-400" />
                      <span>Trade-offs & Considerations</span>
                    </h4>
                    <ul className="space-y-1.5 text-slate-400">
                      {school.tradeoffs.map((t, i) => (
                        <li key={i} className="flex items-start space-x-1.5">
                          <span className="text-amber-400">•</span>
                          <span>{t}</span>
                        </li>
                      ))}
                    </ul>
                  </div>

                  {/* Missing Info / Provenance */}
                  <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800 space-y-2">
                    <h4 className="font-bold text-sky-400 font-mono uppercase tracking-wider flex items-center space-x-1.5">
                      <Shield className="w-4 h-4 text-sky-400" />
                      <span>DGCA Provenance & Data Quality</span>
                    </h4>
                    <div className="space-y-1.5 text-slate-400 font-mono text-[11px]">
                      <div>Verification Confidence: {(school.confidence_score * 100).toFixed(0)}%</div>
                      <div>Status: {school.regulatory_eligibility.replace('_', ' ').toUpperCase()}</div>
                      {school.missing_information.length > 0 ? (
                        school.missing_information.map((m, i) => (
                          <div key={i} className="text-rose-400/90">Notice: {m}</div>
                        ))
                      ) : (
                        <div className="text-emerald-400">All material fields officially verified.</div>
                      )}
                    </div>
                  </div>
                </div>

                {/* Footer Action */}
                <div className="flex items-center justify-between pt-4 mt-4 border-t border-slate-900 text-xs">
                  <span className="text-slate-400 font-mono">
                    Budget variance: {school.budget_gap_inr >= 0 ? (
                      <span className="text-emerald-400 font-bold">+₹{(school.budget_gap_inr / 100000).toFixed(1)}L within target</span>
                    ) : (
                      <span className="text-rose-400 font-bold">-₹{(Math.abs(school.budget_gap_inr) / 100000).toFixed(1)}L stretch</span>
                    )}
                  </span>

                  <Link
                    to={`/schools/${school.school_id}`}
                    className="text-sky-400 hover:text-sky-300 font-bold flex items-center space-x-1 font-mono"
                  >
                    <span>View Full Dossier & Audits</span>
                    <ChevronRight className="w-4 h-4" />
                  </Link>
                </div>
              </div>
            );
          })}

          {/* Weight Sensitivity Analysis Component */}
          {response?.sensitivity_analysis && (
            <SensitivitySimulator sensitivityData={response.sensitivity_analysis} />
          )}
        </div>
      )}

      {/* Floating Compare Action */}
      {selectedForCompare.length >= 2 && (
        <div className="fixed bottom-6 left-1/2 -translate-x-1/2 z-40 bg-slate-900 border border-sky-400/50 shadow-2xl rounded-full px-6 py-3 flex items-center space-x-4 backdrop-blur-xl animate-bounce">
          <div className="flex items-center space-x-2">
            <Scale className="w-5 h-5 text-sky-400" />
            <span className="text-xs text-slate-200 font-semibold font-mono">
              {selectedForCompare.length} FTOs Selected
            </span>
          </div>
          <button
            onClick={handleLaunchCompare}
            className="px-4 py-1.5 rounded-full bg-sky-400 hover:bg-sky-300 text-slate-950 font-bold text-xs shadow-md transition-colors"
          >
            Compare Now →
          </button>
        </div>
      )}
    </div>
  );
};
