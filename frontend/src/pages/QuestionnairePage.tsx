import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Compass, ArrowRight, ArrowLeft, Wallet, Plane, MapPin,
  Sliders, ShieldCheck, AlertCircle, Info, Sparkles
} from 'lucide-react';
import { StepIndicator } from '../components/questionnaire/StepIndicator';
import { PresetSelector, PRESETS } from '../components/questionnaire/PresetSelector';
import { QuestionnaireInput, PreferenceWeights } from '../types';
import { validateQuestionnaire } from '../api/client';

export const QuestionnairePage: React.FC = () => {
  const navigate = useNavigate();
  const [currentStep, setCurrentStep] = useState(0);
  const [validating, setValidating] = useState(false);
  const [warnings, setWarnings] = useState<string[]>([]);

  // Form State
  const [formData, setFormData] = useState<QuestionnaireInput>({
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
    weights: {
      cost: 0.25,
      ranking: 0.25,
      fleet: 0.20,
      location: 0.15,
      infrastructure: 0.15,
    },
  });

  const steps = [
    'Career Pathway',
    'Budget & Finance',
    'Fleet & Location',
    'Preference Weights',
  ];

  const handlePresetChange = (name: string, weights: PreferenceWeights) => {
    setFormData((prev) => ({
      ...prev,
      preset_name: name,
      weights,
    }));
  };

  const handleWeightSlider = (key: keyof PreferenceWeights, val: number) => {
    setFormData((prev) => ({
      ...prev,
      preset_name: 'custom',
      weights: {
        ...prev.weights,
        [key]: val,
      },
    }));
  };

  const handleNext = async () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1);
    } else {
      // Validate and submit
      setValidating(true);
      try {
        const valRes = await validateQuestionnaire(formData);
        if (valRes.warnings && valRes.warnings.length > 0) {
          setWarnings(valRes.warnings);
        }
        // Save to sessionStorage and navigate
        sessionStorage.setItem('findyoursky_questionnaire', JSON.stringify(formData));
        navigate('/recommendations');
      } catch (err: any) {
        setWarnings([err.message || 'Validation error']);
      } finally {
        setValidating(false);
      }
    }
  };

  const handleBack = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="text-center mb-6">
        <div className="inline-flex items-center space-x-2 text-xs font-mono text-sky-400 font-semibold mb-2">
          <Compass className="w-4 h-4" />
          <span>MULTI-CRITERIA DECISION SUPPORT</span>
        </div>
        <h1 className="text-2xl sm:text-3xl font-black text-white tracking-tight">
          Flying Training Organisation Questionnaire
        </h1>
        <p className="text-xs sm:text-sm text-slate-400 mt-2 max-w-xl mx-auto">
          Complete your training preferences to filter eligible academies and generate an analytically ranked recommendation shortlist.
        </p>
      </div>

      {/* Progress Indicator */}
      <StepIndicator
        steps={steps}
        currentStep={currentStep}
        onStepClick={(s) => setCurrentStep(s)}
      />

      {/* Step Container Card */}
      <div className="aviation-card p-6 sm:p-8">
        {/* Step 1: Career Pathway */}
        {currentStep === 0 && (
          <div className="space-y-6">
            <div>
              <h3 className="font-bold text-white text-lg flex items-center space-x-2">
                <Plane className="w-5 h-5 text-sky-400" />
                <span>1. Primary Flight Training Objective</span>
              </h3>
              <p className="text-xs text-slate-400 mt-1">
                Select your intended pilot licensing syllabus and desired credential pathway.
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {[
                {
                  id: 'CPL_ME_IR',
                  title: 'CPL with Multi-Engine & Instrument Rating',
                  desc: 'Standard commercial airline preparation pathway (185h SE + 15h ME + IR). Recommended for airline cadet applicants.',
                },
                {
                  id: 'CPL',
                  title: 'Commercial Pilot License (Single Engine Only)',
                  desc: '200 hours flight training on single-engine trainers (Cessna 172 / Tecnam). Multi-engine endorsement deferred.',
                },
                {
                  id: 'CADET_PREP',
                  title: 'Airline Cadet Program Pathway',
                  desc: 'Priority given to FTOs with direct airline cadet affiliations (IndiGo, Air India) and CAE/Garmin flight syllabus.',
                },
                {
                  id: 'INSTRUCTOR',
                  title: 'Flight Instructor Rating (AFIR / FIR)',
                  desc: 'Hours building and instructional certification pathway for aspiring commercial flight instructors.',
                },
              ].map((opt) => (
                <div
                  key={opt.id}
                  onClick={() => setFormData({ ...formData, career_objective: opt.id })}
                  className={`p-4 rounded-xl border cursor-pointer transition-all ${
                    formData.career_objective === opt.id
                      ? 'bg-sky-500/15 border-sky-400 ring-2 ring-sky-500/20 shadow-md'
                      : 'bg-slate-950/60 border-slate-800 hover:border-slate-700'
                  }`}
                >
                  <h4 className="font-bold text-sm text-white mb-1">{opt.title}</h4>
                  <p className="text-xs text-slate-400 leading-relaxed">{opt.desc}</p>
                </div>
              ))}
            </div>

            {/* Minimum DGCA Ranking Filter */}
            <div className="pt-4 border-t border-slate-800/80">
              <label className="block text-xs font-mono text-slate-300 font-semibold mb-2">
                MINIMUM REQUIRED DGCA RANKING CATEGORY
              </label>
              <select
                value={formData.min_dgca_category}
                onChange={(e) => setFormData({ ...formData, min_dgca_category: e.target.value })}
                className="w-full bg-slate-950/80 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-sky-500"
              >
                <option value="Any">Any Category (Category A through C, Exempt)</option>
                <option value="Category A">Category A Only (Top National Tier - Avyanna)</option>
                <option value="Category B">Category B and above (Premier Academies & Flying Clubs)</option>
                <option value="Category C">Category C and above (All Operational FTOs)</option>
              </select>
              <p className="text-[11px] text-slate-400 mt-1.5 font-mono">
                Categories reflect official DGCA ranking audits assessing safety records, CFI cadre strength, and annual flight hours.
              </p>
            </div>
          </div>
        )}

        {/* Step 2: Budget & Finance */}
        {currentStep === 1 && (
          <div className="space-y-6">
            <div>
              <h3 className="font-bold text-white text-lg flex items-center space-x-2">
                <Wallet className="w-5 h-5 text-emerald-400" />
                <span>2. Budget Allocation & Financial Flexibility</span>
              </h3>
              <p className="text-xs text-slate-400 mt-1">
                Set your maximum target financial envelope for commercial pilot flight training in India.
              </p>
            </div>

            {/* Budget Slider */}
            <div className="p-6 rounded-xl bg-slate-950/70 border border-slate-800 space-y-4">
              <div className="flex items-center justify-between">
                <span className="text-xs font-mono text-slate-400">MAXIMUM TARGET BUDGET (INR)</span>
                <span className="text-2xl font-black font-mono text-emerald-400">
                  ₹{(formData.max_budget_inr / 100000).toFixed(0)} Lakhs
                </span>
              </div>
              <input
                type="range"
                min={3000000}
                max={7500000}
                step={250000}
                value={formData.max_budget_inr}
                onChange={(e) => setFormData({ ...formData, max_budget_inr: Number(e.target.value) })}
                className="w-full accent-sky-400 h-2 bg-slate-800 rounded-lg cursor-pointer"
              />
              <div className="flex justify-between text-[11px] text-slate-400 font-mono">
                <span>₹30 Lakhs (Subsidized Club)</span>
                <span>₹50 Lakhs (National Avg)</span>
                <span>₹75 Lakhs (Premier Cadet)</span>
              </div>
            </div>

            {/* Financial Toggles */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <label className="flex items-start space-x-3 p-4 rounded-xl border border-slate-800 bg-slate-950/40 cursor-pointer">
                <input
                  type="checkbox"
                  checked={formData.budget_includes_hostel}
                  onChange={(e) => setFormData({ ...formData, budget_includes_hostel: e.target.checked })}
                  className="w-4 h-4 rounded mt-0.5 bg-slate-900 border-slate-700 text-sky-500"
                />
                <div>
                  <span className="text-xs font-bold text-white block">Budget Includes Accommodation</span>
                  <span className="text-[11px] text-slate-400 block mt-0.5">
                    Account for annual boarding & mess costs (typically ₹1.8L - ₹2.8L) within the budget ceiling.
                  </span>
                </div>
              </label>

              <label className="flex items-start space-x-3 p-4 rounded-xl border border-slate-800 bg-slate-950/40 cursor-pointer">
                <input
                  type="checkbox"
                  checked={formData.financing_required}
                  onChange={(e) => setFormData({ ...formData, financing_required: e.target.checked })}
                  className="w-4 h-4 rounded mt-0.5 bg-slate-900 border-slate-700 text-sky-500"
                />
                <div>
                  <span className="text-xs font-bold text-white block">Education Loan / Financing Required</span>
                  <span className="text-[11px] text-slate-400 block mt-0.5">
                    Highlight schools with established nationalized bank tie-ups (SBI, Canara, PNB pilot loan schemes).
                  </span>
                </div>
              </label>
            </div>

            {/* Budget Flexibility */}
            <div>
              <label className="block text-xs font-mono text-slate-300 font-semibold mb-2">
                BUDGET STRICTNESS TOLERANCE
              </label>
              <div className="grid grid-cols-3 gap-3 text-xs">
                {[
                  { id: 'strict', label: 'Strict (0%)', desc: 'Hard cut-off at budget' },
                  { id: 'moderate', label: 'Moderate (+10%)', desc: 'Permit slight budget stretch' },
                  { id: 'high', label: 'High (+25%)', desc: 'Open to premium options' },
                ].map((flex) => (
                  <div
                    key={flex.id}
                    onClick={() => setFormData({ ...formData, budget_flexibility: flex.id })}
                    className={`p-3 rounded-lg border text-center cursor-pointer transition-all ${
                      formData.budget_flexibility === flex.id
                        ? 'bg-sky-500/20 border-sky-400 text-sky-300 font-bold'
                        : 'bg-slate-950 border-slate-800 text-slate-400 hover:border-slate-700'
                    }`}
                  >
                    <div>{flex.label}</div>
                    <span className="text-[10px] text-slate-400 font-normal block mt-1">{flex.desc}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Step 3: Fleet & Location */}
        {currentStep === 2 && (
          <div className="space-y-6">
            <div>
              <h3 className="font-bold text-white text-lg flex items-center space-x-2">
                <MapPin className="w-5 h-5 text-indigo-400" />
                <span>3. Geographic & Operational Constraints</span>
              </h3>
              <p className="text-xs text-slate-400 mt-1">
                Configure relocation willingness and specialized training equipment requirements.
              </p>
            </div>

            {/* Relocation & Region */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-mono text-slate-300 font-semibold mb-2">
                  PREFERRED TRAINING ZONE
                </label>
                <select
                  value={formData.preferred_regions[0] || 'Anywhere'}
                  onChange={(e) => setFormData({ ...formData, preferred_regions: [e.target.value] })}
                  className="w-full bg-slate-950/80 border border-slate-800 rounded-lg px-4 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-sky-500"
                >
                  <option value="Anywhere">Anywhere in India (Recommended)</option>
                  <option value="North">North India (UP, Haryana, Punjab, Rajasthan)</option>
                  <option value="South">South India (Karnataka, Telangana, AP)</option>
                  <option value="West">West India (Maharashtra, Gujarat)</option>
                  <option value="Central">Central India (Madhya Pradesh)</option>
                  <option value="East">East India (Assam, Jharkhand)</option>
                </select>
              </div>

              <div className="flex items-center">
                <label className="flex items-start space-x-3 p-4 rounded-xl border border-slate-800 bg-slate-950/40 cursor-pointer w-full">
                  <input
                    type="checkbox"
                    checked={formData.willing_to_relocate}
                    onChange={(e) => setFormData({ ...formData, willing_to_relocate: e.target.checked })}
                    className="w-4 h-4 rounded mt-0.5 bg-slate-900 border-slate-700 text-sky-500"
                  />
                  <div>
                    <span className="text-xs font-bold text-white block">Willing to Relocate Anywhere in India</span>
                    <span className="text-[11px] text-slate-400 block mt-0.5">
                      Recommended. Opens up top-ranked central government and joint-venture academies.
                    </span>
                  </div>
                </label>
              </div>
            </div>

            {/* Mandatory Technical Checkboxes */}
            <div className="pt-4 border-t border-slate-800/80">
              <span className="text-xs font-mono text-slate-300 font-semibold block mb-3">
                MANDATORY OPERATIONAL REQUIREMENTS
              </span>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <label className="flex items-center space-x-2.5 p-3 rounded-lg border border-slate-800 bg-slate-950/60 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={formData.require_multi_engine}
                    onChange={(e) => setFormData({ ...formData, require_multi_engine: e.target.checked })}
                    className="w-4 h-4 rounded bg-slate-900 border-slate-700 text-sky-500"
                  />
                  <span className="text-slate-300 font-medium">Require In-House Multi-Engine Fleet (DA42 / Seneca)</span>
                </label>

                <label className="flex items-center space-x-2.5 p-3 rounded-lg border border-slate-800 bg-slate-950/60 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={formData.require_glass_cockpit}
                    onChange={(e) => setFormData({ ...formData, require_glass_cockpit: e.target.checked })}
                    className="w-4 h-4 rounded bg-slate-900 border-slate-700 text-sky-500"
                  />
                  <span className="text-slate-300 font-medium">Garmin Glass Cockpit Avionics (G1000 / G3X)</span>
                </label>

                <label className="flex items-center space-x-2.5 p-3 rounded-lg border border-slate-800 bg-slate-950/60 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={formData.require_night_flying}
                    onChange={(e) => setFormData({ ...formData, require_night_flying: e.target.checked })}
                    className="w-4 h-4 rounded bg-slate-900 border-slate-700 text-sky-500"
                  />
                  <span className="text-slate-300 font-medium">Night Flying Runway Lighting on Base</span>
                </label>

                <label className="flex items-center space-x-2.5 p-3 rounded-lg border border-slate-800 bg-slate-950/60 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={formData.require_hostel}
                    onChange={(e) => setFormData({ ...formData, require_hostel: e.target.checked })}
                    className="w-4 h-4 rounded bg-slate-900 border-slate-700 text-sky-500"
                  />
                  <span className="text-slate-300 font-medium">On-Campus Student Hostel & Mess Facility</span>
                </label>
              </div>
            </div>
          </div>
        )}

        {/* Step 4: Preference Weights */}
        {currentStep === 3 && (
          <div className="space-y-6">
            <div>
              <h3 className="font-bold text-white text-lg flex items-center space-x-2">
                <Sliders className="w-5 h-5 text-sky-400" />
                <span>4. Multi-Criteria Preference Weighting</span>
              </h3>
              <p className="text-xs text-slate-400 mt-1">
                Choose a balanced preset or customize how much relative weight to assign to each measurable criterion.
              </p>
            </div>

            {/* Presets */}
            <PresetSelector
              currentPreset={formData.preset_name}
              onSelectPreset={handlePresetChange}
            />

            {/* Custom Sliders */}
            <div className="p-6 rounded-xl bg-slate-950/70 border border-slate-800 space-y-4">
              <h4 className="text-xs font-mono font-bold text-slate-300 uppercase">
                Active Criterion Weights (Normalized in Recommendation Engine)
              </h4>

              <div className="space-y-3">
                {[
                  { key: 'cost', label: 'Affordability & Cost Efficiency', color: 'accent-emerald-400' },
                  { key: 'ranking', label: 'DGCA Ranking & Safety Audits', color: 'accent-sky-400' },
                  { key: 'fleet', label: 'Fleet Scale & Multi-Engine Capacity', color: 'accent-blue-400' },
                  { key: 'location', label: 'Geographic Location Convenience', color: 'accent-indigo-400' },
                  { key: 'infrastructure', label: 'Runway, ATC & Campus Infrastructure', color: 'accent-cyan-400' },
                ].map((it) => {
                  const val = formData.weights[it.key as keyof PreferenceWeights];
                  return (
                    <div key={it.key} className="space-y-1">
                      <div className="flex justify-between text-xs font-mono">
                        <span className="text-slate-300">{it.label}</span>
                        <span className="text-sky-400 font-bold">{(val * 100).toFixed(0)}%</span>
                      </div>
                      <input
                        type="range"
                        min={0}
                        max={1}
                        step={0.05}
                        value={val}
                        onChange={(e) => handleWeightSlider(it.key as keyof PreferenceWeights, Number(e.target.value))}
                        className={`w-full ${it.color} h-1.5 bg-slate-800 rounded cursor-pointer`}
                      />
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Warnings list if any */}
            {warnings.length > 0 && (
              <div className="p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs space-y-1">
                <div className="font-bold flex items-center space-x-1 mb-1">
                  <AlertCircle className="w-4 h-4 text-amber-400" />
                  <span>Validation Notices</span>
                </div>
                {warnings.map((w, idx) => (
                  <p key={idx}>• {w}</p>
                ))}
              </div>
            )}
          </div>
        )}

        {/* Wizard Footer Buttons */}
        <div className="flex items-center justify-between pt-6 mt-6 border-t border-slate-800">
          <button
            onClick={handleBack}
            disabled={currentStep === 0}
            className={`px-5 py-2.5 rounded-lg text-xs font-semibold flex items-center space-x-1.5 transition-colors ${
              currentStep === 0
                ? 'opacity-30 cursor-not-allowed text-slate-500'
                : 'bg-slate-800 hover:bg-slate-700 text-slate-200'
            }`}
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Back</span>
          </button>

          <button
            onClick={handleNext}
            disabled={validating}
            className="px-6 py-2.5 rounded-lg bg-sky-400 hover:bg-sky-300 text-slate-950 font-bold text-xs shadow-md shadow-sky-500/20 flex items-center space-x-2 transition-all transform hover:-translate-y-0.5"
          >
            {validating ? (
              <span>Validating constraints...</span>
            ) : currentStep === steps.length - 1 ? (
              <>
                <Sparkles className="w-4 h-4" />
                <span>Generate Recommendations</span>
              </>
            ) : (
              <>
                <span>Next Step</span>
                <ArrowRight className="w-4 h-4" />
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};
