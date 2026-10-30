import React, { useState, useEffect } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { Scale, CheckCircle2, AlertTriangle, ArrowLeft, Shield, ExternalLink, X, Plus } from 'lucide-react';
import { compareSchools, fetchSchools } from '../api/client';
import { SchoolComparisonResponse, SchoolSummary } from '../types';

export const ComparePage: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [comparison, setComparison] = useState<SchoolComparisonResponse | null>(null);
  const [allSchools, setAllSchools] = useState<SchoolSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Read IDs from URL or default
  const idsParam = searchParams.get('ids');
  const currentIds = idsParam ? idsParam.split(',').filter(Boolean) : ['FTO_IGRUA_001', 'FTO_NFTI_002', 'FTO_CAA_003'];

  useEffect(() => {
    fetchSchools().then(setAllSchools).catch(() => {});
  }, []);

  const loadComparison = async (ids: string[]) => {
    if (ids.length < 2) {
      setError('Please select at least 2 schools to compare.');
      setLoading(false);
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const data = await compareSchools(ids);
      setComparison(data);
    } catch (err: any) {
      setError(err.message || 'Failed to compare selected flying schools.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadComparison(currentIds);
  }, [idsParam]);

  const handleRemoveSchool = (schoolId: string) => {
    const updated = currentIds.filter((id) => id !== schoolId);
    if (updated.length >= 2) {
      setSearchParams({ ids: updated.join(',') });
    } else {
      alert('You must have at least 2 schools to compare.');
    }
  };

  const handleAddSchool = (schoolId: string) => {
    if (currentIds.includes(schoolId)) return;
    if (currentIds.length >= 5) {
      alert('You can compare a maximum of 5 flying schools simultaneously.');
      return;
    }
    const updated = [...currentIds, schoolId];
    setSearchParams({ ids: updated.join(',') });
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div>
        <div className="flex items-center space-x-2 text-xs font-mono text-sky-400 font-semibold mb-2">
          <Scale className="w-4 h-4" />
          <span>SIDE-BY-SIDE EVALUATION</span>
        </div>
        <h1 className="text-3xl font-black text-white tracking-tight">
          Flying Training Organisations Comparison
        </h1>
        <p className="text-xs sm:text-sm text-slate-400 mt-2 max-w-2xl leading-relaxed">
          Evaluate key operational differences across verified DGCA audit scores, fee structures, multi-engine aircraft capacity, and runway infrastructure.
        </p>
      </div>

      {/* School Selector Bar */}
      <div className="aviation-card p-4 flex flex-wrap items-center justify-between gap-4">
        <div className="flex flex-wrap items-center gap-2">
          <span className="text-xs text-slate-400 font-mono">COMPARING ({currentIds.length}/5):</span>
          {comparison?.schools.map((s) => (
            <span
              key={s.school_id}
              className="inline-flex items-center space-x-1 px-3 py-1 rounded-full bg-slate-800 border border-slate-700 text-xs font-mono text-slate-200"
            >
              <span>{s.short_name || s.name}</span>
              <button
                onClick={() => handleRemoveSchool(s.school_id)}
                className="text-slate-400 hover:text-rose-400 p-0.5"
              >
                <X className="w-3 h-3" />
              </button>
            </span>
          ))}
        </div>

        {currentIds.length < 5 && (
          <div className="w-full sm:w-auto">
            <select
              onChange={(e) => {
                if (e.target.value) {
                  handleAddSchool(e.target.value);
                  e.target.value = '';
                }
              }}
              defaultValue=""
              className="bg-slate-950/80 border border-slate-800 rounded-lg px-3 py-1.5 text-xs text-slate-300 focus:outline-none focus:border-sky-500 font-mono"
            >
              <option value="" disabled>+ Add School to Compare...</option>
              {allSchools
                .filter((s) => !currentIds.includes(s.school_id))
                .map((s) => (
                  <option key={s.school_id} value={s.school_id}>
                    {s.name} ({s.latest_ranking_category})
                  </option>
                ))}
            </select>
          </div>
        )}
      </div>

      {/* Loading state */}
      {loading ? (
        <div className="py-20 text-center">
          <div className="w-12 h-12 border-4 border-sky-400 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-xs font-mono text-slate-400">Loading multi-school comparison matrix...</p>
        </div>
      ) : error ? (
        <div className="aviation-card p-8 text-center text-rose-400">
          <AlertTriangle className="w-10 h-10 mx-auto mb-2" />
          <p>{error}</p>
        </div>
      ) : comparison ? (
        <div className="space-y-8">
          {/* Main Comparison Table */}
          <div className="aviation-card overflow-hidden p-0">
            <div className="overflow-x-auto">
              <table className="w-full text-xs text-left">
                {/* School Headers */}
                <thead className="bg-slate-950 font-mono border-b border-slate-800">
                  <tr>
                    <th className="py-4 px-6 w-1/4 text-slate-400 uppercase tracking-wider text-[11px]">
                      METRIC CATEGORY
                    </th>
                    {comparison.schools.map((s) => (
                      <th key={s.school_id} className="py-4 px-6 w-1/4 align-top">
                        <div className="space-y-1">
                          <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-sky-500/10 text-sky-400 border border-sky-500/30">
                            {s.dgca_ranking_category}
                          </span>
                          <h4 className="font-bold text-white text-sm mt-1">
                            <Link to={`/schools/${s.school_id}`} className="hover:text-sky-400">
                              {s.short_name || s.name}
                            </Link>
                          </h4>
                          <span className="text-[11px] text-slate-400 block font-normal font-sans">
                            {s.primary_city}, {s.primary_state}
                          </span>
                        </div>
                      </th>
                    ))}
                  </tr>
                </thead>

                {/* Table Metric Rows */}
                <tbody className="divide-y divide-slate-800/60 font-mono">
                  {comparison.comparison_table.map((row, idx) => (
                    <tr key={idx} className="hover:bg-slate-800/30">
                      <td className="py-3.5 px-6 font-bold text-slate-300">
                        <div className="flex items-center space-x-2">
                          <span className="text-[10px] uppercase text-sky-400/80 px-1.5 py-0.5 rounded bg-sky-500/5">
                            {row.category}
                          </span>
                          <span>{row.metric_label}</span>
                        </div>
                      </td>
                      {comparison.schools.map((s) => {
                        const val = row.values[s.school_id];
                        const isVerified = row.data_verified[s.school_id];

                        return (
                          <td key={s.school_id} className="py-3.5 px-6">
                            <div className="space-y-0.5">
                              <span className="font-bold text-white text-xs">{val || 'Not Verified'}</span>
                              {!isVerified && (
                                <span className="text-[10px] text-amber-400 block font-sans italic">
                                  Subject to verification
                                </span>
                              )}
                            </div>
                          </td>
                        );
                      })}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {/* Trade-off Matrix Cards */}
          <div>
            <h3 className="font-bold text-white text-lg mb-4 flex items-center space-x-2">
              <AlertTriangle className="w-5 h-5 text-amber-400" />
              <span>Comparative Trade-Off Matrix</span>
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {comparison.schools.map((s) => (
                <div key={s.school_id} className="aviation-card space-y-3">
                  <h4 className="font-bold text-white text-sm pb-2 border-b border-slate-800">
                    {s.short_name || s.name}
                  </h4>
                  <ul className="space-y-1.5 text-xs text-slate-300">
                    {s.tradeoffs.map((t, i) => (
                      <li key={i} className="flex items-start space-x-1.5">
                        <span className="text-amber-400">•</span>
                        <span>{t}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          </div>
        </div>
      ) : null}
    </div>
  );
};
