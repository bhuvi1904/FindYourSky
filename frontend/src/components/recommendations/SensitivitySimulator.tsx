import React from 'react';
import { ArrowUpRight, ArrowDownRight, Minus, Sliders } from 'lucide-react';

interface SensitivitySimulatorProps {
  sensitivityData: Record<string, Array<{
    short_name: string;
    base_score: number;
    simulated_score: number;
    score_delta: number;
  }>>;
}

export const SensitivitySimulator: React.FC<SensitivitySimulatorProps> = ({ sensitivityData }) => {
  if (!sensitivityData || Object.keys(sensitivityData).length === 0) return null;

  return (
    <div className="aviation-card mt-8">
      <div className="flex items-center space-x-2 mb-4">
        <Sliders className="w-5 h-5 text-sky-400" />
        <h3 className="font-bold text-white text-base">Weight Sensitivity Analysis</h3>
        <span className="text-xs px-2 py-0.5 rounded bg-sky-500/10 text-sky-400 border border-sky-500/20 font-mono">
          Simulated Weight Shifts (±20%)
        </span>
      </div>
      <p className="text-xs text-slate-400 mb-6 leading-relaxed">
        Observe how top recommendations respond dynamically when preferences shift toward budget, DGCA rank, or fleet capacity.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {Object.entries(sensitivityData).map(([scenarioName, items]) => (
          <div key={scenarioName} className="p-4 rounded-xl bg-slate-950/70 border border-slate-800">
            <h4 className="text-xs font-bold text-slate-200 mb-3 font-mono uppercase tracking-wider text-sky-400">
              {scenarioName}
            </h4>
            <div className="space-y-2">
              {items.map((it) => (
                <div key={it.short_name} className="flex items-center justify-between text-xs py-1.5 border-b border-slate-900 last:border-0">
                  <span className="font-medium text-slate-300">{it.short_name}</span>
                  <div className="flex items-center space-x-2 font-mono">
                    <span className="text-slate-400">{it.simulated_score.toFixed(1)}</span>
                    <span className={`text-[11px] font-semibold flex items-center ${
                      it.score_delta > 0
                        ? 'text-emerald-400'
                        : it.score_delta < 0
                        ? 'text-rose-400'
                        : 'text-slate-400'
                    }`}>
                      {it.score_delta > 0 && <ArrowUpRight className="w-3.5 h-3.5 inline mr-0.5" />}
                      {it.score_delta < 0 && <ArrowDownRight className="w-3.5 h-3.5 inline mr-0.5" />}
                      {it.score_delta === 0 && <Minus className="w-3.5 h-3.5 inline mr-0.5" />}
                      {it.score_delta > 0 ? `+${it.score_delta.toFixed(1)}` : it.score_delta.toFixed(1)}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
