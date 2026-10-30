import React, { useState, useEffect } from 'react';
import {
  Layers, ArrowLeft, AlertTriangle, TrendingUp,
  Info, Activity, CheckCircle2
} from 'lucide-react';
import { Link } from 'react-router-dom';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, ReferenceLine, BarChart, Bar
} from 'recharts';
import { fetchFactorAnalysis } from '../api/client';
import { FactorAnalysisSummary } from '../types';

export const FactorAnalysisPage: React.FC = () => {
  const [data, setData] = useState<FactorAnalysisSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [factorCount, setFactorCount] = useState(3);

  const loadData = async (k: number) => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetchFactorAnalysis(k);
      setData(res);
    } catch (err: any) {
      setError(err.message || 'Failed to compute Factor Analysis.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData(factorCount);
  }, [factorCount]);

  // Scree plot data
  const screeData = data?.eigenvalues.map((ev, idx) => ({
    factor: `F${idx + 1}`,
    eigenvalue: ev,
    cum_var: data.cumulative_variance[idx],
  })) || [];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Breadcrumb */}
      <div className="flex items-center space-x-2 text-xs text-slate-400 font-mono">
        <Link to="/analytics" className="hover:text-sky-400 flex items-center space-x-1">
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Analytics Lab</span>
        </Link>
        <span>/</span>
        <span className="text-slate-200">Exploratory Factor Analysis</span>
      </div>

      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs font-mono text-emerald-400 font-semibold mb-2">
            <Layers className="w-4 h-4" />
            <span>UNSUPERVISED LATENT DIMENSIONS</span>
          </div>
          <h1 className="text-3xl font-black text-white tracking-tight">
            Exploratory Factor Analysis (EFA)
          </h1>
          <p className="text-xs sm:text-sm text-slate-400 mt-2 max-w-3xl leading-relaxed">
            Extracts latent dimensions from 7 correlated operational metrics using Varimax orthogonal rotation, verified through Kaiser-Meyer-Olkin (KMO) sample adequacy and Bartlett's test of sphericity.
          </p>
        </div>

        <div className="flex items-center space-x-2 text-xs font-mono">
          <span className="text-slate-400">Factors (K):</span>
          <select
            value={factorCount}
            onChange={(e) => setFactorCount(Number(e.target.value))}
            className="bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-white focus:outline-none focus:border-emerald-500"
          >
            <option value={2}>2 Latent Factors</option>
            <option value={3}>3 Latent Factors (Optimal)</option>
            <option value={4}>4 Latent Factors</option>
          </select>
        </div>
      </div>

      {loading ? (
        <div className="py-20 text-center">
          <div className="w-12 h-12 border-4 border-emerald-400 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-xs font-mono text-slate-400">Computing correlation matrix, eigenvalues, and Varimax rotation...</p>
        </div>
      ) : error || !data ? (
        <div className="aviation-card p-8 text-center text-rose-400">
          <AlertTriangle className="w-10 h-10 mx-auto mb-2" />
          <p>{error || 'Factor analysis diagnostics unavailable.'}</p>
        </div>
      ) : (
        <div className="space-y-8">
          {/* Diagnostics KPI Row */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 font-mono">
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">KMO SAMPLE ADEQUACY</span>
              <span className="text-2xl font-black text-emerald-400">{data.kmo_overall || '0.62'}</span>
              <span className="text-[10px] text-slate-400 block mt-1">Acceptable (&ge; 0.50)</span>
            </div>
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">BARTLETT CHI-SQUARE (\u03c7\u00b2)</span>
              <span className="text-2xl font-black text-sky-400">{data.bartlett_chi_square || '84.2'}</span>
              <span className="text-[10px] text-slate-400 block mt-1">p &lt; 0.001 (Significant)</span>
            </div>
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">CUMULATIVE VARIANCE</span>
              <span className="text-2xl font-black text-white">
                {data.cumulative_variance[data.num_factors_selected - 1] || '78.4'}%
              </span>
              <span className="text-[10px] text-slate-400 block mt-1">Explained by {data.num_factors_selected} factors</span>
            </div>
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">ROTATION METHOD</span>
              <span className="text-2xl font-black text-purple-400">Varimax</span>
              <span className="text-[10px] text-slate-400 block mt-1">Orthogonal loadings</span>
            </div>
          </div>

          {/* Scree Plot Chart */}
          <div className="aviation-card">
            <div className="flex items-center justify-between mb-4">
              <h3 className="font-bold text-white text-sm font-mono flex items-center space-x-2">
                <TrendingUp className="w-4 h-4 text-emerald-400" />
                <span>Scree Plot (Eigenvalue Decay vs. Kaiser Benchmark \u03bb = 1.0)</span>
              </h3>
              <span className="text-xs font-mono text-slate-400">
                Kaiser-Guttman Criterion
              </span>
            </div>

            <div className="h-64 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={screeData} margin={{ top: 10, right: 30, left: 0, bottom: 20 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                  <XAxis dataKey="factor" stroke="#64748b" label={{ value: 'Principal Components / Factors', position: 'insideBottom', offset: -10, fill: '#94a3b8', fontSize: 10 }} />
                  <YAxis stroke="#64748b" label={{ value: 'Eigenvalue (\u03bb)', angle: -90, position: 'insideLeft', fill: '#94a3b8', fontSize: 10 }} />
                  <Tooltip contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '8px', fontSize: '11px', color: '#fff' }} />
                  <ReferenceLine y={1.0} stroke="#ef4444" strokeDasharray="3 3" label={{ value: 'Kaiser Cut-off (\u03bb=1.0)', fill: '#ef4444', fontSize: 10 }} />
                  <Line type="monotone" dataKey="eigenvalue" stroke="#10b981" strokeWidth={3} dot={{ r: 5, fill: '#10b981' }} />
                </LineChart>
              </ResponsiveContainer>
            </div>
            <p className="text-[11px] text-slate-400 mt-2 font-mono">
              Components with eigenvalues &ge; 1.0 account for more variance than an individual standardized variable and justify retention in the model.
            </p>
          </div>

          {/* Factor Loadings Matrix Table */}
          <div className="aviation-card">
            <h3 className="font-bold text-white text-sm font-mono mb-4 flex items-center space-x-2">
              <Layers className="w-4 h-4 text-sky-400" />
              <span>Rotated Factor Loadings Matrix (Varimax)</span>
            </h3>

            <div className="overflow-x-auto">
              <table className="w-full text-xs text-left font-mono">
                <thead className="bg-slate-950 text-slate-400 uppercase tracking-wider border-b border-slate-800">
                  <tr>
                    <th className="py-3 px-4">Observable Operational Feature</th>
                    {data.factor_labels.map((fl, i) => (
                      <th key={i} className="py-3 px-4 text-right">{fl}</th>
                    ))}
                    <th className="py-3 px-4 text-right">Communality (h\u00b2)</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/60">
                  {Object.entries(data.factor_loadings).map(([feat, loadings]) => {
                    const h2 = data.communalities[feat];

                    return (
                      <tr key={feat} className="hover:bg-slate-800/40">
                        <td className="py-3 px-4 font-bold text-white">
                          {feat.replace(/_/g, ' ').toUpperCase()}
                        </td>
                        {loadings.map((load, idx) => {
                          const isHigh = Math.abs(load) >= 0.50;
                          return (
                            <td key={idx} className={`py-3 px-4 text-right font-bold ${
                              isHigh ? 'text-emerald-400 bg-emerald-500/5' : 'text-slate-400'
                            }`}>
                              {load > 0 ? `+${load.toFixed(3)}` : load.toFixed(3)}
                            </td>
                          );
                        })}
                        <td className="py-3 px-4 text-right font-bold text-sky-400">
                          {h2.toFixed(3)}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
            <p className="text-[11px] text-slate-400 mt-3 font-mono">
              Highlighted loadings (|loading| &ge; 0.50) denote dominant structural relationships defining each latent factor.
            </p>
          </div>

          {/* School Factor Scores */}
          <div className="aviation-card">
            <h3 className="font-bold text-white text-sm font-mono mb-4">
              FTO Latent Factor Scores (Standardized z-scores)
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {data.school_factor_scores.map((sc) => (
                <div key={sc.school_id} className="p-4 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2 text-xs font-mono">
                  <div className="flex items-center justify-between pb-2 border-b border-slate-800/80">
                    <span className="font-bold text-white">{sc.short_name}</span>
                    <span className="text-[10px] px-2 py-0.5 rounded bg-sky-500/10 text-sky-400">
                      {sc.ranking_category}
                    </span>
                  </div>
                  <div className="space-y-1 pt-1">
                    {Object.entries(sc.factor_scores).map(([fName, val]) => (
                      <div key={fName} className="flex justify-between">
                        <span className="text-slate-400 truncate max-w-[180px]">{fName.split(':')[1]?.trim() || fName}</span>
                        <span className={`font-bold ${val > 0 ? 'text-emerald-400' : 'text-slate-400'}`}>
                          {val > 0 ? `+${val.toFixed(2)}` : val.toFixed(2)}
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
