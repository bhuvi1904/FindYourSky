import React, { useState, useEffect } from 'react';
import {
  Compass, ArrowLeft, AlertTriangle, TrendingUp,
  Activity, Info, Layers, CheckCircle2, MapPin
} from 'lucide-react';
import { Link } from 'react-router-dom';
import {
  ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, LineChart, Line, BarChart, Bar, Cell
} from 'recharts';
import { fetchClustering } from '../api/client';
import { ClusteringSummary } from '../types';

const CLUSTER_COLORS = ['#38bdf8', '#10b981', '#f59e0b', '#a855f7', '#ec4899'];

export const ClusteringPage: React.FC = () => {
  const [data, setData] = useState<ClusteringSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedK, setSelectedK] = useState<number | undefined>(undefined);

  const loadData = async (k?: number) => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetchClustering(k);
      setData(res);
    } catch (err: any) {
      setError(err.message || 'Failed to compute K-Means clustering.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData(selectedK);
  }, [selectedK]);

  // Chart data for Elbow & Silhouette
  const diagnosticData = data?.candidate_k_values.map((kVal, idx) => ({
    k: `K = ${kVal}`,
    inertia: data.inertias[idx],
    silhouette: data.silhouette_scores[idx],
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
        <span className="text-slate-200">K-Means Clustering</span>
      </div>

      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center space-x-2 text-xs font-mono text-purple-400 font-semibold mb-2">
            <Compass className="w-4 h-4" />
            <span>UNSUPERVISED PATTERN RECOGNITION</span>
          </div>
          <h1 className="text-3xl font-black text-white tracking-tight">
            K-Means Operational Cluster Profiling
          </h1>
          <p className="text-xs sm:text-sm text-slate-400 mt-2 max-w-3xl leading-relaxed">
            Partitions Indian flying training organisations into distinct operational archetypes through inertia elbow analysis, silhouette optimization, and 2-dimensional Principal Component projection.
          </p>
        </div>

        <div className="flex items-center space-x-2 text-xs font-mono">
          <span className="text-slate-400">Cluster Count (K):</span>
          <select
            value={selectedK || data?.optimal_k || 3}
            onChange={(e) => setSelectedK(Number(e.target.value))}
            className="bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-white focus:outline-none focus:border-purple-500"
          >
            <option value={2}>K = 2 Clusters</option>
            <option value={3}>K = 3 (Diagnostic Optimal)</option>
            <option value={4}>K = 4 Clusters</option>
            <option value={5}>K = 5 Clusters</option>
          </select>
        </div>
      </div>

      {loading ? (
        <div className="py-20 text-center">
          <div className="w-12 h-12 border-4 border-purple-400 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-xs font-mono text-slate-400">Iterating K-means clustering across random seeds & computing PCA projection...</p>
        </div>
      ) : error || !data ? (
        <div className="aviation-card p-8 text-center text-rose-400">
          <AlertTriangle className="w-10 h-10 mx-auto mb-2" />
          <p>{error || 'Clustering diagnostics unavailable.'}</p>
        </div>
      ) : (
        <div className="space-y-8">
          {/* Key Metrics */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 font-mono">
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">OPTIMAL CLUSTERS (K)</span>
              <span className="text-2xl font-black text-purple-400">{data.optimal_k} Clusters</span>
              <span className="text-[10px] text-slate-400 block mt-1">Silhouette maximized</span>
            </div>
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">PEAK SILHOUETTE SCORE</span>
              <span className="text-2xl font-black text-emerald-400">
                {Math.max(...data.silhouette_scores).toFixed(3)}
              </span>
              <span className="text-[10px] text-slate-400 block mt-1">Well-separated clusters</span>
            </div>
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">SEED STABILITY INDEX</span>
              <span className="text-2xl font-black text-sky-400">{data.stability_score.toFixed(3)}</span>
              <span className="text-[10px] text-slate-400 block mt-1">Adjusted Rand Index (ARI)</span>
            </div>
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">INPUT ATTRIBUTES</span>
              <span className="text-2xl font-black text-white">8 Dimensions</span>
              <span className="text-[10px] text-slate-400 block mt-1">Standardized z-scores</span>
            </div>
          </div>

          {/* Diagnostic Charts: Inertia Elbow & Silhouette */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Inertia Elbow Curve */}
            <div className="aviation-card">
              <div className="flex items-center justify-between mb-4">
                <h3 className="font-bold text-white text-sm font-mono flex items-center space-x-2">
                  <TrendingUp className="w-4 h-4 text-sky-400" />
                  <span>Inertia Elbow Curve (Within-Cluster Sum of Squares)</span>
                </h3>
              </div>
              <div className="h-60 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={diagnosticData} margin={{ top: 10, right: 20, left: 0, bottom: 20 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                    <XAxis dataKey="k" stroke="#64748b" label={{ value: 'Cluster Count Candidate (K)', position: 'insideBottom', offset: -10, fill: '#94a3b8', fontSize: 10 }} />
                    <YAxis stroke="#64748b" label={{ value: 'Inertia (WCSS)', angle: -90, position: 'insideLeft', fill: '#94a3b8', fontSize: 10 }} />
                    <Tooltip contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '8px', fontSize: '11px', color: '#fff' }} />
                    <Line type="monotone" dataKey="inertia" stroke="#38bdf8" strokeWidth={3} dot={{ r: 5, fill: '#38bdf8' }} />
                  </LineChart>
                </ResponsiveContainer>
              </div>
              <p className="text-[11px] text-slate-400 mt-2 font-mono">
                The "elbow point" reflects diminishing returns in variance reduction when adding extra clusters.
              </p>
            </div>

            {/* Silhouette Scores */}
            <div className="aviation-card">
              <div className="flex items-center justify-between mb-4">
                <h3 className="font-bold text-white text-sm font-mono flex items-center space-x-2">
                  <Activity className="w-4 h-4 text-emerald-400" />
                  <span>Silhouette Coefficient by Cluster Count</span>
                </h3>
              </div>
              <div className="h-60 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={diagnosticData} margin={{ top: 10, right: 20, left: 0, bottom: 20 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                    <XAxis dataKey="k" stroke="#64748b" label={{ value: 'Cluster Count Candidate (K)', position: 'insideBottom', offset: -10, fill: '#94a3b8', fontSize: 10 }} />
                    <YAxis stroke="#64748b" domain={[0, 0.6]} label={{ value: 'Silhouette Score (-1 to +1)', angle: -90, position: 'insideLeft', fill: '#94a3b8', fontSize: 10 }} />
                    <Tooltip contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '8px', fontSize: '11px', color: '#fff' }} />
                    <Bar dataKey="silhouette" fill="#10b981" radius={[4, 4, 0, 0]}>
                      {diagnosticData.map((entry, index) => (
                        <Cell
                          key={`cell-${index}`}
                          fill={entry.k === `K = ${data.optimal_k}` ? '#10b981' : '#334155'}
                        />
                      ))}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
              </div>
              <p className="text-[11px] text-slate-400 mt-2 font-mono">
                Higher silhouette indicates stronger intra-cluster cohesion and clearer inter-cluster separation.
              </p>
            </div>
          </div>

          {/* 2D PCA Cluster Projection */}
          <div className="aviation-card">
            <div className="flex items-center justify-between mb-4">
              <div>
                <h3 className="font-bold text-white text-sm font-mono flex items-center space-x-2">
                  <Compass className="w-4 h-4 text-purple-400" />
                  <span>2D Principal Component Projection (PCA Mapping)</span>
                </h3>
                <p className="text-xs text-slate-400 mt-1 font-mono">
                  Each dot represents one of the 41 DGCA flying training organisations projected onto principal components PC1 & PC2.
                </p>
              </div>
            </div>

            <div className="h-80 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <ScatterChart margin={{ top: 20, right: 20, bottom: 20, left: 20 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                  <XAxis
                    type="number"
                    dataKey="pca_x"
                    name="Principal Component 1"
                    stroke="#64748b"
                    label={{ value: 'PC1 (Fleet Scale & Operational Capacity)', position: 'insideBottom', offset: -10, fill: '#94a3b8', fontSize: 10 }}
                  />
                  <YAxis
                    type="number"
                    dataKey="pca_y"
                    name="Principal Component 2"
                    stroke="#64748b"
                    label={{ value: 'PC2 (Tuition & Infrastructure)', angle: -90, position: 'insideLeft', fill: '#94a3b8', fontSize: 10 }}
                  />
                  <Tooltip
                    cursor={{ strokeDasharray: '3 3' }}
                    content={({ active, payload }) => {
                      if (active && payload && payload.length) {
                        const pt = payload[0].payload;
                        return (
                          <div className="p-3 rounded-lg bg-slate-900 border border-slate-700 text-xs font-mono text-white shadow-xl">
                            <div className="font-bold text-sky-400">{pt.name}</div>
                            <div className="text-slate-400 mt-1">{pt.cluster_name}</div>
                            <div className="text-emerald-400">Fee: ₹{pt.fee_lakhs} Lakhs | Fleet: {pt.fleet_size} Aircraft</div>
                            <div className="text-purple-400">{pt.ranking_category}</div>
                          </div>
                        );
                      }
                      return null;
                    }}
                  />
                  {data.cluster_profiles.map((cp, cIdx) => {
                    const clusterPoints = data.pca_2d_points.filter((p) => p.cluster_id === cp.cluster_id);
                    return (
                      <Scatter
                        key={cp.cluster_id}
                        name={cp.cluster_name}
                        data={clusterPoints}
                        fill={CLUSTER_COLORS[cIdx % CLUSTER_COLORS.length]}
                      />
                    );
                  })}
                </ScatterChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Cluster Archetype Centroids */}
          <div>
            <h3 className="font-bold text-white text-base mb-4 font-mono">
              Computed Cluster Centroids & Operational Profiles
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {data.cluster_profiles.map((cp, idx) => (
                <div
                  key={cp.cluster_id}
                  className="aviation-card border-t-4 space-y-4"
                  style={{ borderTopColor: CLUSTER_COLORS[idx % CLUSTER_COLORS.length] }}
                >
                  <div>
                    <span className="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider block">
                      ARCHETYPE {cp.cluster_id + 1} ({cp.size} FTOs • {cp.percentage}%)
                    </span>
                    <h4 className="font-bold text-white text-base mt-1">
                      {cp.cluster_name.split(':')[1]?.trim() || cp.cluster_name}
                    </h4>
                  </div>

                  <p className="text-xs text-slate-300 leading-relaxed">
                    {cp.description}
                  </p>

                  <div className="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2 text-xs font-mono">
                    <div className="flex justify-between py-1 border-b border-slate-800">
                      <span className="text-slate-400">Mean Total Fee</span>
                      <span className="font-bold text-emerald-400">₹{cp.mean_tuition_fee_lakhs.toFixed(1)} Lakhs</span>
                    </div>
                    <div className="flex justify-between py-1 border-b border-slate-800">
                      <span className="text-slate-400">Mean Fleet Size</span>
                      <span className="font-bold text-white">{cp.mean_fleet_size.toFixed(1)} Aircraft</span>
                    </div>
                    <div className="flex justify-between py-1 border-b border-slate-800">
                      <span className="text-slate-400">Multi-Engine Assets</span>
                      <span className="font-bold text-sky-400">{cp.mean_multi_engine_count.toFixed(1)} Twin-Engine</span>
                    </div>
                    <div className="flex justify-between py-1 border-b border-slate-800">
                      <span className="text-slate-400">DGCA Audit Score</span>
                      <span className="font-bold text-purple-400">{cp.mean_dgca_score.toFixed(1)}/100</span>
                    </div>
                    <div className="flex justify-between py-1">
                      <span className="text-slate-400">Night Flying Active</span>
                      <span className="font-bold text-slate-200">{cp.night_flying_available_pct.toFixed(0)}%</span>
                    </div>
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
