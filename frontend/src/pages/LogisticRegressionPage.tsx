import React, { useState, useEffect } from 'react';
import {
  BarChart3, ShieldCheck, AlertTriangle, ArrowLeft,
  Activity, Info, CheckCircle2, TrendingUp
} from 'lucide-react';
import { Link } from 'react-router-dom';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, ReferenceLine
} from 'recharts';
import { fetchLogisticRegression } from '../api/client';
import { LogisticRegressionSummary } from '../types';

export const LogisticRegressionPage: React.FC = () => {
  const [data, setData] = useState<LogisticRegressionSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchLogisticRegression()
      .then(setData)
      .catch((err) => setError(err.message || 'Failed to load model diagnostics.'))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Breadcrumb */}
      <div className="flex items-center space-x-2 text-xs text-slate-400 font-mono">
        <Link to="/analytics" className="hover:text-sky-400 flex items-center space-x-1">
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Analytics Lab</span>
        </Link>
        <span>/</span>
        <span className="text-slate-200">Logistic Regression</span>
      </div>

      {/* Header */}
      <div>
        <div className="flex items-center space-x-2 text-xs font-mono text-sky-400 font-semibold mb-2">
          <BarChart3 className="w-4 h-4" />
          <span>SUPERVISED CLASSIFICATION & INFERENCE</span>
        </div>
        <h1 className="text-3xl font-black text-white tracking-tight">
          Binary Logistic Regression Diagnostics
        </h1>
        <p className="text-xs sm:text-sm text-slate-400 mt-2 max-w-3xl leading-relaxed">
          Standardized scikit-learn Pipeline modeling the probability of an Indian FTO attaining premier DGCA Tier-1 status based on fleet scale, multi-engine capacity, normalized tuition fees, and safety audits.
        </p>
      </div>

      {loading ? (
        <div className="py-20 text-center">
          <div className="w-12 h-12 border-4 border-sky-400 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-xs font-mono text-slate-400">Fitting logistic regression pipeline & cross-validating...</p>
        </div>
      ) : error || !data ? (
        <div className="aviation-card p-8 text-center text-rose-400">
          <AlertTriangle className="w-10 h-10 mx-auto mb-2" />
          <p>{error || 'Model diagnostics unavailable.'}</p>
        </div>
      ) : (
        <div className="space-y-8">
          {/* Top KPI Metrics Row */}
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4 font-mono">
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">ROC-AUC</span>
              <span className="text-2xl font-black text-emerald-400">{data.roc_auc?.toFixed(3) || 'N/A'}</span>
              <span className="text-[10px] text-slate-400 block mt-1">Cross-validated</span>
            </div>
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">ACCURACY</span>
              <span className="text-2xl font-black text-sky-400">{data.accuracy ? `${(data.accuracy * 100).toFixed(1)}%` : 'N/A'}</span>
              <span className="text-[10px] text-slate-400 block mt-1">OOF Prediction</span>
            </div>
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">PRECISION</span>
              <span className="text-2xl font-black text-white">{data.precision?.toFixed(3) || 'N/A'}</span>
              <span className="text-[10px] text-slate-400 block mt-1">Positive class</span>
            </div>
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">RECALL</span>
              <span className="text-2xl font-black text-white">{data.recall?.toFixed(3) || 'N/A'}</span>
              <span className="text-[10px] text-slate-400 block mt-1">True positive rate</span>
            </div>
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">F1 SCORE</span>
              <span className="text-2xl font-black text-purple-400">{data.f1_score?.toFixed(3) || 'N/A'}</span>
              <span className="text-[10px] text-slate-400 block mt-1">Harmonic mean</span>
            </div>
            <div className="aviation-card p-4">
              <span className="text-[10px] text-slate-400 block">BRIER SCORE</span>
              <span className="text-2xl font-black text-amber-400">{data.brier_score?.toFixed(4) || 'N/A'}</span>
              <span className="text-[10px] text-slate-400 block mt-1">Calibration loss</span>
            </div>
          </div>

          {/* Model Specification & Validation Info */}
          <div className="aviation-card p-5 bg-slate-950/80 border border-slate-800 text-xs font-mono">
            <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
              <div>
                <span className="text-slate-400 block text-[10px]">TOTAL OBSERVATIONS (N)</span>
                <span className="text-white font-bold text-sm">{data.sample_size} Institutions</span>
              </div>
              <div>
                <span className="text-slate-400 block text-[10px]">CLASS DISTRIBUTION</span>
                <span className="text-white font-bold text-sm">{data.positive_count} Positives / {data.negative_count} Negatives</span>
              </div>
              <div>
                <span className="text-slate-400 block text-[10px]">VALIDATION SCHEME</span>
                <span className="text-emerald-400 font-bold text-sm">{data.validation_method}</span>
              </div>
              <div>
                <span className="text-slate-400 block text-[10px]">INTERCEPT (\u03b2\u2080)</span>
                <span className="text-sky-400 font-bold text-sm">{data.intercept.toFixed(4)}</span>
              </div>
            </div>
          </div>

          {/* Chart & Confusion Matrix Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* ROC Curve Chart */}
            <div className="aviation-card">
              <div className="flex items-center justify-between mb-4">
                <h3 className="font-bold text-white text-sm font-mono flex items-center space-x-2">
                  <TrendingUp className="w-4 h-4 text-emerald-400" />
                  <span>Receiver Operating Characteristic (ROC Curve)</span>
                </h3>
                <span className="text-xs font-mono text-emerald-400 font-bold">
                  AUC = {data.roc_auc?.toFixed(3)}
                </span>
              </div>

              <div className="h-64 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={data.roc_curve_points || []} margin={{ top: 10, right: 20, left: 0, bottom: 20 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                    <XAxis
                      dataKey="fpr"
                      type="number"
                      domain={[0, 1]}
                      stroke="#64748b"
                      label={{ value: 'False Positive Rate (1 - Specificity)', position: 'insideBottom', offset: -10, fill: '#94a3b8', fontSize: 10 }}
                    />
                    <YAxis
                      domain={[0, 1]}
                      stroke="#64748b"
                      label={{ value: 'True Positive Rate (Sensitivity)', angle: -90, position: 'insideLeft', fill: '#94a3b8', fontSize: 10 }}
                    />
                    <Tooltip
                      contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '8px', fontSize: '11px', color: '#fff' }}
                    />
                    <ReferenceLine segment={[{ x: 0, y: 0 }, { x: 1, y: 1 }]} stroke="#475569" strokeDasharray="4 4" />
                    <Line
                      type="monotone"
                      dataKey="tpr"
                      stroke="#38bdf8"
                      strokeWidth={3}
                      dot={{ r: 4, fill: '#38bdf8' }}
                      activeDot={{ r: 6 }}
                    />
                  </LineChart>
                </ResponsiveContainer>
              </div>
              <p className="text-[11px] text-slate-400 mt-2 font-mono">
                The cyan curve illustrates discrimination threshold trade-offs; the diagonal dashed line depicts random chance classification (AUC = 0.50).
              </p>
            </div>

            {/* Confusion Matrix */}
            <div className="aviation-card flex flex-col justify-between">
              <div>
                <h3 className="font-bold text-white text-sm font-mono mb-4 flex items-center space-x-2">
                  <Activity className="w-4 h-4 text-sky-400" />
                  <span>Out-of-Fold Confusion Matrix</span>
                </h3>
                {data.confusion_matrix && (
                  <div className="grid grid-cols-2 gap-3 text-center font-mono my-4">
                    <div className="p-4 rounded-xl bg-slate-950/80 border border-slate-800">
                      <span className="text-[10px] text-slate-400 block">TRUE NEGATIVE (TN)</span>
                      <span className="text-3xl font-black text-white mt-1 block">{data.confusion_matrix[0][0]}</span>
                      <span className="text-[10px] text-slate-400 block mt-1">Correctly rejected non-tier-1</span>
                    </div>
                    <div className="p-4 rounded-xl bg-slate-950/80 border border-slate-800">
                      <span className="text-[10px] text-rose-400 block">FALSE POSITIVE (FP)</span>
                      <span className="text-3xl font-black text-rose-400 mt-1 block">{data.confusion_matrix[0][1]}</span>
                      <span className="text-[10px] text-slate-400 block mt-1">Type I Error</span>
                    </div>
                    <div className="p-4 rounded-xl bg-slate-950/80 border border-slate-800">
                      <span className="text-[10px] text-amber-400 block">FALSE NEGATIVE (FN)</span>
                      <span className="text-3xl font-black text-amber-400 mt-1 block">{data.confusion_matrix[1][0]}</span>
                      <span className="text-[10px] text-slate-400 block mt-1">Type II Error</span>
                    </div>
                    <div className="p-4 rounded-xl bg-slate-950/80 border border-slate-800">
                      <span className="text-[10px] text-emerald-400 block">TRUE POSITIVE (TP)</span>
                      <span className="text-3xl font-black text-emerald-400 mt-1 block">{data.confusion_matrix[1][1]}</span>
                      <span className="text-[10px] text-slate-400 block mt-1">Correctly identified tier-1</span>
                    </div>
                  </div>
                )}
              </div>
              <div className="text-[11px] text-slate-400 font-mono pt-3 border-t border-slate-800">
                Evaluation performed using Stratified K-Fold cross validation to prevent training leakage across evaluation folds.
              </div>
            </div>
          </div>

          {/* Feature Coefficients & Odds Ratios Table */}
          <div className="aviation-card">
            <h3 className="font-bold text-white text-sm font-mono mb-4 flex items-center space-x-2">
              <BarChart3 className="w-4 h-4 text-sky-400" />
              <span>Predictor Coefficients (\u03b2) & Odds Ratios (e^\u03b2)</span>
            </h3>

            <div className="overflow-x-auto">
              <table className="w-full text-xs text-left font-mono">
                <thead className="bg-slate-950 text-slate-400 uppercase tracking-wider border-b border-slate-800">
                  <tr>
                    <th className="py-3 px-4">Predictor Feature</th>
                    <th className="py-3 px-4 text-right">Coefficient (\u03b2)</th>
                    <th className="py-3 px-4 text-right">Odds Ratio (OR)</th>
                    <th className="py-3 px-4">Interpreted Impact Direction</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/60">
                  {Object.entries(data.coefficients).map(([feat, coef]) => {
                    const odds = data.odds_ratios[feat];
                    const isPositive = coef > 0;

                    return (
                      <tr key={feat} className="hover:bg-slate-800/40">
                        <td className="py-3 px-4 font-bold text-white">
                          {feat.replace(/_/g, ' ').toUpperCase()}
                        </td>
                        <td className={`py-3 px-4 text-right font-bold ${isPositive ? 'text-emerald-400' : 'text-rose-400'}`}>
                          {coef > 0 ? `+${coef.toFixed(4)}` : coef.toFixed(4)}
                        </td>
                        <td className="py-3 px-4 text-right text-white font-bold">
                          {odds.toFixed(4)}x
                        </td>
                        <td className="py-3 px-4">
                          <span className={`px-2 py-0.5 rounded text-[10px] ${
                            isPositive
                              ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'
                              : 'bg-rose-500/10 text-rose-400 border border-rose-500/20'
                          }`}>
                            {isPositive ? 'Increases Suitability Likelihood' : 'Decreases Suitability Likelihood'}
                          </span>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>

          {/* School Probabilities Table */}
          {data.school_probabilities && (
            <div className="aviation-card">
              <h3 className="font-bold text-white text-sm font-mono mb-4">
                FTO-Level Predicted Probabilities
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                {data.school_probabilities.map((sp) => (
                  <div key={sp.school_id} className="p-3 rounded-lg bg-slate-950/70 border border-slate-800 text-xs font-mono flex items-center justify-between">
                    <div>
                      <span className="font-bold text-slate-200 block truncate max-w-[180px]">{sp.name}</span>
                      <span className="text-[10px] text-slate-400">{sp.school_id}</span>
                    </div>
                    <div className="text-right">
                      <span className="text-sm font-bold text-sky-400 block">{(sp.suitability_probability * 100).toFixed(1)}%</span>
                      <span className="text-[10px] text-slate-400">P(Tier-1)</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Academic Transparency Note */}
          <div className="p-4 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-400 space-y-2">
            <div className="font-bold text-slate-200 flex items-center space-x-1.5 font-mono">
              <Info className="w-4 h-4 text-sky-400" />
              <span>Statistical Inference Integrity Notice</span>
            </div>
            <p>
              In accordance with Section 7 of the academic master prompt, these metrics are generated through computational execution of scikit-learn on genuine institutional DGCA audit observations. No synthetic student records are presented as real-world predictive accuracy.
            </p>
          </div>
        </div>
      )}
    </div>
  );
};
