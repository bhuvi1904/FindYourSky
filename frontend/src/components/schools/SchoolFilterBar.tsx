import React from 'react';
import { Search, Filter, RotateCcw } from 'lucide-react';

interface SchoolFilterBarProps {
  search: string;
  setSearch: (s: string) => void;
  region: string;
  setRegion: (r: string) => void;
  category: string;
  setCategory: (c: string) => void;
  hasMultiEngine: boolean;
  setHasMultiEngine: (b: boolean) => void;
  maxBudget: number;
  setMaxBudget: (b: number) => void;
  onReset: () => void;
}

export const SchoolFilterBar: React.FC<SchoolFilterBarProps> = ({
  search,
  setSearch,
  region,
  setRegion,
  category,
  setCategory,
  hasMultiEngine,
  setHasMultiEngine,
  maxBudget,
  setMaxBudget,
  onReset,
}) => {
  return (
    <div className="aviation-card mb-8">
      <div className="flex flex-col md:flex-row items-center gap-4 mb-4">
        {/* Search input */}
        <div className="relative flex-1 w-full">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search by school name, city, state, or airport..."
            className="w-full bg-slate-950/80 border border-slate-800 rounded-lg pl-10 pr-4 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-sky-500 transition-colors"
          />
        </div>

        {/* Region Select */}
        <div className="w-full md:w-48">
          <select
            value={region}
            onChange={(e) => setRegion(e.target.value)}
            className="w-full bg-slate-950/80 border border-slate-800 rounded-lg px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-sky-500 transition-colors"
          >
            <option value="">All Regions</option>
            <option value="North">North India</option>
            <option value="South">South India</option>
            <option value="West">West India</option>
            <option value="East">East India</option>
            <option value="Central">Central India</option>
          </select>
        </div>

        {/* DGCA Category Select */}
        <div className="w-full md:w-56">
          <select
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            className="w-full bg-slate-950/80 border border-slate-800 rounded-lg px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-sky-500 transition-colors"
          >
            <option value="">All DGCA Categories</option>
            <option value="Category A">Category A (Top National Tier - Avyanna)</option>
            <option value="Category B">Category B (Premier Academies & Clubs)</option>
            <option value="Category C">Category C (Under Review / Notice)</option>
            <option value="Exempt / Under Assessment">Exempt / Under Assessment</option>
          </select>
        </div>

        {/* Reset button */}
        <button
          onClick={onReset}
          className="p-2.5 rounded-lg border border-slate-800 text-slate-400 hover:text-white hover:bg-slate-800 transition-colors flex items-center justify-center"
          title="Reset filters"
        >
          <RotateCcw className="w-4 h-4" />
        </button>
      </div>

      {/* Secondary filter toggles */}
      <div className="flex flex-wrap items-center justify-between gap-4 pt-3 border-t border-slate-800/80 text-xs">
        <div className="flex items-center space-x-4">
          <label className="flex items-center space-x-2 cursor-pointer select-none">
            <input
              type="checkbox"
              checked={hasMultiEngine}
              onChange={(e) => setHasMultiEngine(e.target.checked)}
              className="w-4 h-4 rounded bg-slate-950 border-slate-700 text-sky-500 focus:ring-0 focus:ring-offset-0"
            />
            <span className="text-slate-300 font-medium">Require Multi-Engine Aircraft</span>
          </label>
        </div>

        {/* Budget slider */}
        <div className="flex items-center space-x-3 w-full sm:w-auto">
          <span className="text-slate-400 font-mono">Max Budget:</span>
          <input
            type="range"
            min={3000000}
            max={7000000}
            step={250000}
            value={maxBudget}
            onChange={(e) => setMaxBudget(Number(e.target.value))}
            className="w-36 accent-sky-400"
          />
          <span className="font-mono text-emerald-400 font-semibold w-24">
            ₹{(maxBudget / 100000).toFixed(0)} Lakhs
          </span>
        </div>
      </div>
    </div>
  );
};
