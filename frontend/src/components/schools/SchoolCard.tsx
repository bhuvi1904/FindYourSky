import React from 'react';
import { Link } from 'react-router-dom';
import { ExternalLink, MapPin, Plane, CheckCircle2, AlertTriangle, Shield, Check } from 'lucide-react';
import { SchoolSummary } from '../../types';

interface SchoolCardProps {
  school: SchoolSummary;
  isSelectedForCompare?: boolean;
  onToggleCompare?: (schoolId: string) => void;
}

export const SchoolCard: React.FC<SchoolCardProps> = ({
  school,
  isSelectedForCompare = false,
  onToggleCompare,
}) => {
  const getCategoryColor = (category: string) => {
    switch (category) {
      case 'Category A+':
        return 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30';
      case 'Category A':
        return 'bg-sky-500/10 text-sky-400 border-sky-500/30';
      case 'Category B+':
        return 'bg-blue-500/10 text-blue-400 border-blue-500/30';
      case 'Category B':
        return 'bg-amber-500/10 text-amber-400 border-amber-500/30';
      case 'Category C':
        return 'bg-orange-500/10 text-orange-400 border-orange-500/30';
      default:
        return 'bg-slate-500/10 text-slate-400 border-slate-500/30';
    }
  };

  return (
    <div className={`aviation-card relative flex flex-col justify-between ${
      isSelectedForCompare ? 'ring-2 ring-sky-400 border-sky-400/50' : ''
    }`}>
      <div>
        {/* Header row */}
        <div className="flex items-start justify-between gap-3 mb-3">
          <div>
            <div className="flex items-center space-x-2">
              <span className={`text-[11px] font-bold px-2 py-0.5 rounded-full border ${getCategoryColor(school.latest_ranking_category)}`}>
                DGCA {school.latest_ranking_category}
              </span>
              <span className="text-[10px] text-slate-400 font-mono">
                {school.ownership_type.replace('_', ' ').toUpperCase()}
              </span>
            </div>
            <h3 className="font-bold text-lg text-white mt-1.5 leading-snug">
              <Link to={`/schools/${school.school_id}`} className="hover:text-sky-400 transition-colors">
                {school.name}
              </Link>
            </h3>
          </div>

          {onToggleCompare && (
            <button
              onClick={() => onToggleCompare(school.school_id)}
              className={`text-xs px-2.5 py-1 rounded-md font-medium flex items-center space-x-1 border transition-all ${
                isSelectedForCompare
                  ? 'bg-sky-500 text-slate-950 border-sky-400 font-bold'
                  : 'bg-slate-800/80 text-slate-300 border-slate-700 hover:border-slate-600'
              }`}
            >
              {isSelectedForCompare ? <Check className="w-3.5 h-3.5" /> : null}
              <span>{isSelectedForCompare ? 'Selected' : 'Compare'}</span>
            </button>
          )}
        </div>

        {/* Location & DGCA info */}
        <div className="flex items-center space-x-4 text-xs text-slate-400 mb-4 font-mono">
          <div className="flex items-center space-x-1">
            <MapPin className="w-3.5 h-3.5 text-sky-400/70" />
            <span>{school.primary_city || 'India'}, {school.primary_state}</span>
          </div>
          <div className="flex items-center space-x-1">
            <Shield className="w-3.5 h-3.5 text-emerald-400/70" />
            <span>{school.dgca_approval_no}</span>
          </div>
        </div>

        {/* Key Operational Grid */}
        <div className="grid grid-cols-2 gap-2 p-3 rounded-lg bg-slate-950/60 border border-slate-800/70 text-xs mb-4">
          <div>
            <span className="text-slate-400 block text-[10px] font-mono">ACTIVE FLEET</span>
            <span className="font-semibold text-white">
              {school.total_fleet_count} Aircraft
              {school.multi_engine_count > 0 && (
                <span className="text-sky-400 text-[11px] block font-mono">({school.multi_engine_count} Multi-Engine)</span>
              )}
            </span>
          </div>
          <div>
            <span className="text-slate-400 block text-[10px] font-mono">INDICATIVE FEE</span>
            {school.indicative_fee_inr ? (
              <span className="font-semibold text-emerald-400">
                ₹{(school.indicative_fee_inr / 100000).toFixed(1)} Lakhs
                {school.is_fee_verified ? (
                  <span className="text-[10px] text-slate-400 block font-normal">Verified quote</span>
                ) : (
                  <span className="text-[10px] text-amber-400 block font-normal">Estimated</span>
                )}
              </span>
            ) : (
              <span className="text-slate-400 italic">Not published</span>
            )}
          </div>
        </div>

        {/* Tags */}
        <div className="flex flex-wrap gap-1.5 mb-4 text-[11px]">
          {school.glass_cockpit_available && (
            <span className="px-2 py-0.5 rounded bg-sky-500/10 text-sky-300 border border-sky-500/20">
              Garmin Glass Cockpit
            </span>
          )}
          {school.night_flying_available && (
            <span className="px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">
              Night Operations
            </span>
          )}
          {school.latest_dgca_score && (
            <span className="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-mono">
              Audit: {school.latest_dgca_score.toFixed(1)}/100
            </span>
          )}
        </div>
      </div>

      {/* Footer link row */}
      <div className="flex items-center justify-between border-t border-slate-800/70 pt-3 mt-2 text-xs">
        <Link
          to={`/schools/${school.school_id}`}
          className="text-sky-400 hover:text-sky-300 font-medium inline-flex items-center space-x-1"
        >
          <span>Full School Profile</span>
          <span>→</span>
        </Link>

        {school.website_url && (
          <a
            href={school.website_url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-slate-400 hover:text-white inline-flex items-center space-x-1"
            title="Official School Website"
          >
            <span>Official Web</span>
            <ExternalLink className="w-3 h-3" />
          </a>
        )}
      </div>
    </div>
  );
};
