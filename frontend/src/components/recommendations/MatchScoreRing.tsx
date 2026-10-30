import React from 'react';

interface MatchScoreRingProps {
  score: number;
  subscores: {
    cost: number;
    ranking: number;
    fleet: number;
    location: number;
    infrastructure: number;
  };
}

export const MatchScoreRing: React.FC<MatchScoreRingProps> = ({ score, subscores }) => {
  const getScoreColor = (val: number) => {
    if (val >= 85) return 'text-emerald-400 border-emerald-500';
    if (val >= 70) return 'text-sky-400 border-sky-500';
    if (val >= 55) return 'text-amber-400 border-amber-500';
    return 'text-rose-400 border-rose-500';
  };

  return (
    <div className="flex flex-col sm:flex-row items-center gap-6 p-4 rounded-xl bg-slate-950/70 border border-slate-800">
      {/* Circular score badge */}
      <div className="flex flex-col items-center justify-center">
        <div className={`w-20 h-20 rounded-full border-4 flex flex-col items-center justify-center bg-slate-900 shadow-xl ${getScoreColor(score)}`}>
          <span className="text-2xl font-black font-mono leading-none">{score.toFixed(0)}</span>
          <span className="text-[10px] font-semibold text-slate-400 mt-1">/100</span>
        </div>
        <span className="text-xs font-bold text-slate-300 mt-2 font-mono tracking-wider">MATCH SCORE</span>
      </div>

      {/* Subscore progress bars */}
      <div className="flex-1 w-full space-y-2 text-xs">
        <div>
          <div className="flex justify-between text-slate-400 font-mono mb-1 text-[11px]">
            <span>Affordability & Cost</span>
            <span className="text-emerald-400 font-semibold">{subscores.cost.toFixed(1)}%</span>
          </div>
          <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
            <div className="bg-emerald-500 h-full rounded-full transition-all duration-500" style={{ width: `${subscores.cost}%` }} />
          </div>
        </div>

        <div>
          <div className="flex justify-between text-slate-400 font-mono mb-1 text-[11px]">
            <span>DGCA Category & Ranking</span>
            <span className="text-sky-400 font-semibold">{subscores.ranking.toFixed(1)}%</span>
          </div>
          <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
            <div className="bg-sky-500 h-full rounded-full transition-all duration-500" style={{ width: `${subscores.ranking}%` }} />
          </div>
        </div>

        <div>
          <div className="flex justify-between text-slate-400 font-mono mb-1 text-[11px]">
            <span>Aircraft Fleet & Multi-Engine</span>
            <span className="text-blue-400 font-semibold">{subscores.fleet.toFixed(1)}%</span>
          </div>
          <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
            <div className="bg-blue-500 h-full rounded-full transition-all duration-500" style={{ width: `${subscores.fleet}%` }} />
          </div>
        </div>

        <div>
          <div className="flex justify-between text-slate-400 font-mono mb-1 text-[11px]">
            <span>Geographic & Relocation Fit</span>
            <span className="text-indigo-400 font-semibold">{subscores.location.toFixed(1)}%</span>
          </div>
          <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
            <div className="bg-indigo-500 h-full rounded-full transition-all duration-500" style={{ width: `${subscores.location}%` }} />
          </div>
        </div>

        <div>
          <div className="flex justify-between text-slate-400 font-mono mb-1 text-[11px]">
            <span>Airfield & ATC Infrastructure</span>
            <span className="text-cyan-400 font-semibold">{subscores.infrastructure.toFixed(1)}%</span>
          </div>
          <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
            <div className="bg-cyan-500 h-full rounded-full transition-all duration-500" style={{ width: `${subscores.infrastructure}%` }} />
          </div>
        </div>
      </div>
    </div>
  );
};
