import React from 'react';
import { Wallet, Award, Compass, Building2, Sliders, Check } from 'lucide-react';
import { PreferenceWeights } from '../../types';

interface PresetSelectorProps {
  currentPreset: string;
  onSelectPreset: (presetName: string, weights: PreferenceWeights) => void;
}

export const PRESETS: Record<string, { label: string; desc: string; icon: any; weights: PreferenceWeights }> = {
  budget_first: {
    label: 'Budget-First',
    desc: 'Prioritizes lower tuition fees, state subsidies, and affordable living expenses.',
    icon: Wallet,
    weights: { cost: 0.50, ranking: 0.15, fleet: 0.15, location: 0.10, infrastructure: 0.10 }
  },
  balanced: {
    label: 'Balanced',
    desc: 'Evenly distributes importance across budget, DGCA category, and fleet capacity.',
    icon: Sliders,
    weights: { cost: 0.25, ranking: 0.25, fleet: 0.20, location: 0.15, infrastructure: 0.15 }
  },
  quality_first: {
    label: 'DGCA Quality & Performance',
    desc: 'Prioritizes official DGCA ranking audits, safety scores, and airline cadet track records.',
    icon: Award,
    weights: { cost: 0.10, ranking: 0.45, fleet: 0.25, location: 0.10, infrastructure: 0.10 }
  },
  infrastructure: {
    label: 'Training Infrastructure',
    desc: 'Focuses on long runways, night operations, Garmin glass cockpits, and on-campus hostels.',
    icon: Building2,
    weights: { cost: 0.15, ranking: 0.20, fleet: 0.30, location: 0.10, infrastructure: 0.25 }
  },
  location_first: {
    label: 'Location-First',
    desc: 'Focuses on training proximity to your home state or preferred geographical zone.',
    icon: Compass,
    weights: { cost: 0.20, ranking: 0.20, fleet: 0.15, location: 0.35, infrastructure: 0.10 }
  },
  custom: {
    label: 'Custom Weights',
    desc: 'Manually configure individual sliders for each measurable decision criterion.',
    icon: Sliders,
    weights: { cost: 0.25, ranking: 0.25, fleet: 0.20, location: 0.15, infrastructure: 0.15 }
  }
};

export const PresetSelector: React.FC<PresetSelectorProps> = ({
  currentPreset,
  onSelectPreset,
}) => {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 mb-6">
      {Object.entries(PRESETS).map(([key, item]) => {
        const Icon = item.icon;
        const isSelected = currentPreset === key;

        return (
          <div
            key={key}
            onClick={() => onSelectPreset(key, item.weights)}
            className={`p-4 rounded-xl border cursor-pointer transition-all ${
              isSelected
                ? 'bg-sky-500/15 border-sky-400 ring-2 ring-sky-500/20 shadow-lg'
                : 'bg-slate-900/60 border-slate-800 hover:border-slate-700 hover:bg-slate-900'
            }`}
          >
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center space-x-2">
                <div className={`p-2 rounded-lg ${isSelected ? 'bg-sky-500/20 text-sky-400' : 'bg-slate-800 text-slate-400'}`}>
                  <Icon className="w-4 h-4" />
                </div>
                <h4 className={`text-sm font-bold ${isSelected ? 'text-white' : 'text-slate-300'}`}>
                  {item.label}
                </h4>
              </div>
              {isSelected && <Check className="w-4 h-4 text-sky-400 stroke-[3]" />}
            </div>
            <p className="text-xs text-slate-400 leading-relaxed">
              {item.desc}
            </p>
          </div>
        );
      })}
    </div>
  );
};
