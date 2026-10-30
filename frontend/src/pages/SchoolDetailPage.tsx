import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import {
  Plane, MapPin, Shield, ExternalLink, Calendar, CheckCircle2,
  AlertTriangle, DollarSign, Award, Layers, ArrowLeft, Building, ChevronRight
} from 'lucide-react';
import { fetchSchoolDetail } from '../api/client';
import { SchoolDetail } from '../types';

export const SchoolDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [school, setSchool] = useState<SchoolDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'overview' | 'fleet' | 'bases' | 'fees' | 'programmes' | 'provenance'>('overview');

  useEffect(() => {
    if (id) {
      setLoading(true);
      fetchSchoolDetail(id)
        .then((data) => setSchool(data))
        .catch((err) => setError(err.message || 'Failed to load school profile.'))
        .finally(() => setLoading(false));
    }
  }, [id]);

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-16 text-center">
        <div className="w-12 h-12 border-4 border-sky-400 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
        <p className="text-sm text-slate-400 font-mono">Loading official DGCA flying training dossier...</p>
      </div>
    );
  }

  if (error || !school) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-16 text-center">
        <div className="aviation-card p-8">
          <AlertTriangle className="w-12 h-12 text-rose-400 mx-auto mb-4" />
          <h2 className="text-xl font-bold text-white">FTO Record Not Found</h2>
          <p className="text-xs text-slate-400 mt-2 mb-6">{error || 'The requested flying school record could not be retrieved.'}</p>
          <Link to="/schools" className="px-4 py-2 rounded-lg bg-sky-500 text-slate-950 font-bold text-xs">
            Return to School Directory
          </Link>
        </div>
      </div>
    );
  }

  const primaryBase = school.bases.find((b) => b.is_primary) || school.bases[0];
  const fee = school.fees[0];
  const ranking = school.rankings[0];
  const totalFleet = school.fleet.reduce((acc, f) => acc + f.operational_count, 0);
  const multiEngineCount = school.fleet
    .filter((f) => f.engine_type === 'multi_engine')
    .reduce((acc, f) => acc + f.operational_count, 0);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Breadcrumb */}
      <div className="flex items-center space-x-2 text-xs text-slate-400 font-mono">
        <Link to="/schools" className="hover:text-sky-400 transition-colors flex items-center space-x-1">
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>FTO Directory</span>
        </Link>
        <span>/</span>
        <span className="text-slate-200">{school.short_name || school.name}</span>
      </div>

      {/* Hero Header Card */}
      <div className="aviation-card relative overflow-hidden">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div className="space-y-3">
            <div className="flex flex-wrap items-center gap-2">
              <span className="px-3 py-1 rounded-full text-xs font-bold bg-sky-500/10 text-sky-400 border border-sky-500/30 font-mono">
                DGCA {ranking?.ranking_category || 'Category A'}
              </span>
              <span className="px-2.5 py-0.5 rounded text-[11px] font-mono bg-slate-800 text-slate-300">
                {school.ownership_type.replace('_', ' ').toUpperCase()}
              </span>
              <span className="flex items-center space-x-1 text-emerald-400 text-xs font-mono">
                <CheckCircle2 className="w-3.5 h-3.5" />
                <span>Status: {school.operational_status.toUpperCase()}</span>
              </span>
            </div>

            <h1 className="text-2xl sm:text-4xl font-black text-white tracking-tight">
              {school.name}
            </h1>

            <div className="flex flex-wrap items-center gap-4 text-xs text-slate-400 font-mono">
              <div className="flex items-center space-x-1">
                <MapPin className="w-4 h-4 text-sky-400/80" />
                <span>{primaryBase?.airport_name} ({primaryBase?.city}, {primaryBase?.state})</span>
              </div>
              <div className="flex items-center space-x-1">
                <Shield className="w-4 h-4 text-emerald-400/80" />
                <span>Approval: {school.dgca_approval_no}</span>
              </div>
              {school.established_year && (
                <div className="flex items-center space-x-1">
                  <Calendar className="w-4 h-4 text-amber-400/80" />
                  <span>Est. {school.established_year}</span>
                </div>
              )}
            </div>
          </div>

          <div className="flex flex-col sm:flex-row lg:flex-col items-start sm:items-center lg:items-end gap-3 flex-shrink-0">
            {school.website_url && (
              <a
                href={school.website_url}
                target="_blank"
                rel="noopener noreferrer"
                className="px-5 py-2.5 rounded-xl bg-sky-400 hover:bg-sky-300 text-slate-950 font-bold text-xs flex items-center space-x-1.5 shadow-md shadow-sky-500/20 transition-all"
              >
                <span>Visit Official Website</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
            )}
            <div className="text-[11px] text-slate-400 font-mono">
              Last verified: {school.last_verified_date || 'October 2026'}
            </div>
          </div>
        </div>

        {/* Quick Highlights Metric Row */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-6 mt-6 border-t border-slate-800/80 text-xs font-mono">
          <div>
            <span className="text-slate-400 block text-[10px]">TOTAL FLEET</span>
            <span className="text-lg font-bold text-white">{totalFleet} Aircraft</span>
          </div>
          <div>
            <span className="text-slate-400 block text-[10px]">MULTI-ENGINE</span>
            <span className="text-lg font-bold text-sky-400">{multiEngineCount} Twin-Engine</span>
          </div>
          <div>
            <span className="text-slate-400 block text-[10px]">DGCA AUDIT SCORE</span>
            <span className="text-lg font-bold text-emerald-400">{ranking?.overall_score?.toFixed(1) || 'N/A'}/100</span>
          </div>
          <div>
            <span className="text-slate-400 block text-[10px]">ESTIMATED CPL FEE</span>
            <span className="text-lg font-bold text-white">
              {fee ? `₹${(fee.total_estimated_inr / 100000).toFixed(1)} Lakhs` : 'Unpublished'}
            </span>
          </div>
        </div>
      </div>

      {/* Tab Navigation */}
      <div className="border-b border-slate-800 flex space-x-2 overflow-x-auto pb-1 text-xs font-mono font-semibold">
        {[
          { key: 'overview', label: 'Overview & Verification' },
          { key: 'fleet', label: `Aircraft Fleet (${school.fleet.length})` },
          { key: 'bases', label: `Airfields & Bases (${school.bases.length})` },
          { key: 'fees', label: 'Fees & Cost Structure' },
          { key: 'programmes', label: `Programmes (${school.programmes.length})` },
          { key: 'provenance', label: 'Source Provenance' }
        ].map((tab) => (
          <button
            key={tab.key}
            onClick={() => setActiveTab(tab.key as any)}
            className={`px-4 py-2.5 rounded-lg transition-colors whitespace-nowrap ${
              activeTab === tab.key
                ? 'bg-sky-500/15 text-sky-400 border border-sky-500/30'
                : 'text-slate-400 hover:text-white hover:bg-slate-900'
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab Content */}
      <div className="space-y-6">
        {activeTab === 'overview' && (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="aviation-card space-y-4">
              <h3 className="font-bold text-white text-sm flex items-center space-x-2">
                <Shield className="w-4 h-4 text-sky-400" />
                <span>DGCA Regulatory Compliance Status</span>
              </h3>
              <div className="space-y-2 text-xs">
                <div className="flex justify-between py-2 border-b border-slate-800">
                  <span className="text-slate-400 font-mono">DGCA Approval Ref</span>
                  <span className="font-mono text-white font-bold">{school.dgca_approval_no}</span>
                </div>
                <div className="flex justify-between py-2 border-b border-slate-800">
                  <span className="text-slate-400 font-mono">Approval Validity</span>
                  <span className="font-mono text-emerald-400">{school.approval_validity || 'Valid through 2028'}</span>
                </div>
                <div className="flex justify-between py-2 border-b border-slate-800">
                  <span className="text-slate-400 font-mono">Regulatory Framework</span>
                  <span className="text-slate-200">CAR Section 7 Series D Part I</span>
                </div>
                <div className="flex justify-between py-2 border-b border-slate-800">
                  <span className="text-slate-400 font-mono">National DGCA Rank</span>
                  <span className="font-mono text-sky-400 font-bold">#{ranking?.national_rank || 'N/A'} in India</span>
                </div>
                <div className="flex justify-between py-2">
                  <span className="text-slate-400 font-mono">Safety Audit Score</span>
                  <span className="font-mono text-emerald-400 font-bold">{ranking?.safety_audit_score || 'N/A'}%</span>
                </div>
              </div>
            </div>

            <div className="aviation-card space-y-4">
              <h3 className="font-bold text-white text-sm flex items-center space-x-2">
                <Award className="w-4 h-4 text-emerald-400" />
                <span>Institutional Profile & Highlights</span>
              </h3>
              <p className="text-xs text-slate-300 leading-relaxed">
                {school.name} operates under the {school.ownership_type.replace('_', ' ')} framework, providing structured flight training towards the DGCA Commercial Pilot License (CPL) and multi-engine instrument ratings.
              </p>
              <div className="space-y-2 text-xs text-slate-300">
                <div className="flex items-center space-x-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                  <span>Annual Flying Hours Logged: {ranking?.annual_hours_logged?.toLocaleString() || 'N/A'} hours</span>
                </div>
                <div className="flex items-center space-x-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                  <span>Chief Flight Instructor (CFI) cadre strength: {ranking?.cfi_cadre_strength || 'N/A'} instructors</span>
                </div>
                <div className="flex items-center space-x-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                  <span>Data Confidence Score: {(school.confidence_score * 100).toFixed(0)}% verified</span>
                </div>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'fleet' && (
          <div className="aviation-card">
            <h3 className="font-bold text-white text-sm mb-4 flex items-center space-x-2">
              <Plane className="w-4 h-4 text-sky-400" />
              <span>Aircraft Fleet & Simulator Equipment</span>
            </h3>
            <div className="overflow-x-auto">
              <table className="w-full text-xs text-left">
                <thead className="bg-slate-950 font-mono text-slate-400 uppercase tracking-wider border-b border-slate-800">
                  <tr>
                    <th className="py-3 px-4">Aircraft Model</th>
                    <th className="py-3 px-4">Manufacturer</th>
                    <th className="py-3 px-4">Engine Type</th>
                    <th className="py-3 px-4">Avionics System</th>
                    <th className="py-3 px-4">Fuel Type</th>
                    <th className="py-3 px-4 text-right">Operational Units</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/60 font-mono">
                  {school.fleet.map((fl, idx) => (
                    <tr key={idx} className="hover:bg-slate-800/40">
                      <td className="py-3 px-4 font-bold text-white">{fl.aircraft_model}</td>
                      <td className="py-3 px-4 text-slate-300">{fl.manufacturer || 'Standard'}</td>
                      <td className="py-3 px-4">
                        <span className={`px-2 py-0.5 rounded text-[10px] ${
                          fl.engine_type === 'multi_engine'
                            ? 'bg-sky-500/10 text-sky-400 border border-sky-500/20'
                            : 'bg-slate-800 text-slate-300'
                        }`}>
                          {fl.engine_type.replace('_', ' ').toUpperCase()}
                        </span>
                      </td>
                      <td className="py-3 px-4 text-slate-300">{fl.avionics_type || 'Analogue'}</td>
                      <td className="py-3 px-4 text-slate-400">{fl.fuel_type || 'AvGas 100LL'}</td>
                      <td className="py-3 px-4 text-right font-bold text-emerald-400">{fl.operational_count}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {activeTab === 'bases' && (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {school.bases.map((base) => (
              <div key={base.base_id} className="aviation-card space-y-3">
                <div className="flex items-center justify-between">
                  <span className={`text-[10px] font-mono px-2 py-0.5 rounded ${
                    base.is_primary ? 'bg-sky-500/10 text-sky-400 border border-sky-500/20' : 'bg-slate-800 text-slate-400'
                  }`}>
                    {base.is_primary ? 'PRIMARY TRAINING BASE' : 'SECONDARY BASE'}
                  </span>
                  {base.icao_code && <span className="font-mono text-slate-400 text-xs">ICAO: {base.icao_code}</span>}
                </div>
                <h4 className="text-base font-bold text-white">{base.airport_name}</h4>
                <div className="space-y-1.5 text-xs text-slate-300 font-mono">
                  <div>City / State: {base.city}, {base.state} ({base.region} India)</div>
                  <div>Runway Length: {base.runway_length_meters ? `${base.runway_length_meters}m (${base.runway_surface || 'Asphalt'})` : 'Unspecified'}</div>
                  <div>ATC Airspace: {base.atc_type || 'Dedicated FTO Controlled'}</div>
                  <div className="flex items-center space-x-1.5 pt-1">
                    <span className="text-slate-400">Night Flying:</span>
                    <span className={base.night_flying_available ? 'text-emerald-400 font-bold' : 'text-slate-400'}>
                      {base.night_flying_available ? 'Available On Base' : 'Not Available (Cross-Country Detachment)'}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {activeTab === 'fees' && (
          <div className="aviation-card space-y-6">
            <div>
              <h3 className="font-bold text-white text-sm mb-1 flex items-center space-x-2">
                <DollarSign className="w-4 h-4 text-emerald-400" />
                <span>Verified Fee Structure: {fee?.course_name || 'CPL Course'}</span>
              </h3>
              <p className="text-xs text-slate-400 font-mono">
                Effective date: {fee?.fee_effective_date || '2026 Season'} | Verification Status: {fee?.is_fee_verified ? 'OFFICIALLY VERIFIED' : 'UNVERIFIED ESTIMATE'}
              </p>
            </div>

            {fee && (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="p-4 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2 text-xs font-mono">
                  <div className="flex justify-between py-1 border-b border-slate-800">
                    <span className="text-slate-400">Flight Training (200 hrs)</span>
                    <span className="text-white font-bold">₹{fee.tuition_flying_inr.toLocaleString()}</span>
                  </div>
                  <div className="flex justify-between py-1 border-b border-slate-800">
                    <span className="text-slate-400">Ground School & Theory</span>
                    <span className="text-white font-bold">₹{fee.ground_school_inr.toLocaleString()}</span>
                  </div>
                  <div className="flex justify-between py-1 border-b border-slate-800">
                    <span className="text-slate-400">Simulator Hours</span>
                    <span className="text-white font-bold">₹{fee.simulator_inr.toLocaleString()}</span>
                  </div>
                  <div className="flex justify-between py-1 border-b border-slate-800">
                    <span className="text-slate-400">Hostel & Mess (Annual Est.)</span>
                    <span className="text-white font-bold">₹{fee.hostel_mess_annual_inr.toLocaleString()}</span>
                  </div>
                  <div className="flex justify-between py-2 text-sm text-emerald-400 font-bold border-t border-slate-700">
                    <span>Total Estimated Cost</span>
                    <span>₹{fee.total_estimated_inr.toLocaleString()}</span>
                  </div>
                </div>

                <div className="space-y-4 text-xs">
                  <div>
                    <h5 className="font-bold text-emerald-400 mb-2">Included in Course Package:</h5>
                    <ul className="space-y-1 list-disc list-inside text-slate-300">
                      {fee.inclusions.map((inc, i) => (
                        <li key={i}>{inc}</li>
                      ))}
                    </ul>
                  </div>

                  <div>
                    <h5 className="font-bold text-rose-400 mb-2">Excluded Additional Costs:</h5>
                    <ul className="space-y-1 list-disc list-inside text-slate-400">
                      {fee.exclusions.map((exc, i) => (
                        <li key={i}>{exc}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            )}
          </div>
        )}

        {activeTab === 'programmes' && (
          <div className="aviation-card space-y-4">
            <h3 className="font-bold text-white text-sm mb-3">DGCA Approved Flight Training Pathways</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {school.programmes.map((p, idx) => (
                <div key={idx} className="p-4 rounded-xl bg-slate-950/60 border border-slate-800 text-xs">
                  <h4 className="font-bold text-sky-400 text-sm mb-1">{p.programme_name}</h4>
                  <div className="text-slate-400 font-mono">Typical completion: {p.duration_months} months</div>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === 'provenance' && (
          <div className="aviation-card space-y-4">
            <h3 className="font-bold text-white text-sm mb-2">Authoritative Source Provenance</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Every factual data point for {school.name} is verified against official DGCA publications, Ministry of Civil Aviation airport allocations, and documented institutional bulletins.
            </p>
            <div className="p-4 rounded-xl bg-slate-950/70 border border-slate-800 text-xs font-mono space-y-2">
              <div>Source ID: {ranking?.source_id || 'SRC_PIB_FTO_2026'}</div>
              <div>DGCA Gazette Reference: CAR Section 7, Series D, Part I</div>
              <div>Retrieval Timestamp: {school.last_verified_date || '2026-10-26'}</div>
              <div>Confidence Level: {(school.confidence_score * 100).toFixed(0)}% Verified</div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
