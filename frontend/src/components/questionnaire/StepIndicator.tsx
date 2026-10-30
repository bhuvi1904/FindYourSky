import React from 'react';
import { Check } from 'lucide-react';

interface StepIndicatorProps {
  steps: string[];
  currentStep: number;
  onStepClick?: (step: number) => void;
}

export const StepIndicator: React.FC<StepIndicatorProps> = ({
  steps,
  currentStep,
  onStepClick,
}) => {
  return (
    <div className="w-full py-4 mb-8">
      <div className="flex items-center justify-between max-w-3xl mx-auto relative">
        {/* Background track line */}
        <div className="absolute left-0 top-1/2 -translate-y-1/2 w-full h-0.5 bg-slate-800 -z-0" />
        
        {/* Active progress bar */}
        <div
          className="absolute left-0 top-1/2 -translate-y-1/2 h-0.5 bg-gradient-to-r from-sky-500 to-cyan-400 transition-all duration-300 -z-0"
          style={{ width: `${(currentStep / (steps.length - 1)) * 100}%` }}
        />

        {steps.map((label, idx) => {
          const isCompleted = idx < currentStep;
          const isCurrent = idx === currentStep;

          return (
            <div
              key={label}
              className="flex flex-col items-center cursor-pointer group z-10"
              onClick={() => onStepClick && onStepClick(idx)}
            >
              <div
                className={`w-9 h-9 rounded-full flex items-center justify-center font-mono text-xs font-bold transition-all duration-300 border-2 ${
                  isCompleted
                    ? 'bg-sky-500 text-slate-950 border-sky-400 shadow-md shadow-sky-500/30'
                    : isCurrent
                    ? 'bg-slate-950 text-sky-400 border-sky-400 ring-4 ring-sky-500/20 shadow-lg'
                    : 'bg-slate-900 text-slate-400 border-slate-700 group-hover:border-slate-500'
                }`}
              >
                {isCompleted ? <Check className="w-4 h-4 stroke-[3]" /> : idx + 1}
              </div>
              <span
                className={`text-[11px] mt-2 font-medium hidden sm:block ${
                  isCurrent ? 'text-sky-400 font-bold' : isCompleted ? 'text-slate-300' : 'text-slate-400'
                }`}
              >
                {label}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
};
