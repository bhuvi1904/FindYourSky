import React from 'react';
import { Plane, ExternalLink, ShieldCheck, Heart } from 'lucide-react';
import { Link } from 'react-router-dom';

export const Footer: React.FC = () => {
  return (
    <footer className="border-t border-slate-800 bg-slate-950 text-slate-400 py-12 px-4 sm:px-6 lg:px-8 mt-24">
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
        <div className="space-y-4 md:col-span-1">
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 rounded-lg bg-sky-500/10 border border-sky-400/30 flex items-center justify-center text-sky-400">
              <Plane className="w-5 h-5 -rotate-45" />
            </div>
            <span className="font-bold text-white text-base tracking-tight">FindYour<span className="text-sky-400">Sky</span></span>
          </div>
          <p className="text-xs text-slate-400 leading-relaxed">
            Data-driven decision support system evaluating DGCA-approved Flying Training Organisations (FTOs) in India using transparent statistical modeling and multi-criteria preference analysis.
          </p>
          <div className="flex items-center space-x-2 text-xs text-emerald-400 font-mono">
            <ShieldCheck className="w-4 h-4" />
            <span>DGCA CAR Section 7 Compliant</span>
          </div>
        </div>

        <div>
          <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-200 mb-3 font-mono">Platform</h4>
          <ul className="space-y-2 text-xs">
            <li><Link to="/schools" className="hover:text-sky-400 transition-colors">School Directory</Link></li>
            <li><Link to="/questionnaire" className="hover:text-sky-400 transition-colors">Personalized Questionnaire</Link></li>
            <li><Link to="/compare" className="hover:text-sky-400 transition-colors">Compare Shortlisted FTOs</Link></li>
            <li><Link to="/sources" className="hover:text-sky-400 transition-colors">Authoritative Sources Registry</Link></li>
            <li><Link to="/admin/data" className="hover:text-sky-400 transition-colors">Data Management (Admin)</Link></li>
          </ul>
        </div>

        <div>
          <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-200 mb-3 font-mono">Analytics Lab</h4>
          <ul className="space-y-2 text-xs">
            <li><Link to="/analytics/logistic-regression" className="hover:text-sky-400 transition-colors">Logistic Regression Model</Link></li>
            <li><Link to="/analytics/factor-analysis" className="hover:text-sky-400 transition-colors">Exploratory Factor Analysis (EFA)</Link></li>
            <li><Link to="/analytics/clustering" className="hover:text-sky-400 transition-colors">K-Means Cluster Profiling</Link></li>
            <li><Link to="/evaluation" className="hover:text-sky-400 transition-colors">Model Evaluation & Metrics</Link></li>
            <li><Link to="/about/methodology" className="hover:text-sky-400 transition-colors">Statistical Methodology</Link></li>
          </ul>
        </div>

        <div>
          <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-200 mb-3 font-mono">Official Regulators</h4>
          <ul className="space-y-2 text-xs">
            <li>
              <a href="https://www.dgca.gov.in" target="_blank" rel="noopener noreferrer" className="hover:text-sky-400 transition-colors flex items-center space-x-1">
                <span>Directorate General of Civil Aviation</span>
                <ExternalLink className="w-3 h-3" />
              </a>
            </li>
            <li>
              <a href="https://www.civilaviation.gov.in" target="_blank" rel="noopener noreferrer" className="hover:text-sky-400 transition-colors flex items-center space-x-1">
                <span>Ministry of Civil Aviation</span>
                <ExternalLink className="w-3 h-3" />
              </a>
            </li>
            <li>
              <a href="https://www.dgca.gov.in/digigov-portal/" target="_blank" rel="noopener noreferrer" className="hover:text-sky-400 transition-colors flex items-center space-x-1">
                <span>eGCA / DigiGov Portal</span>
                <ExternalLink className="w-3 h-3" />
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div className="max-w-7xl mx-auto border-t border-slate-900 mt-8 pt-6 flex flex-col sm:flex-row items-center justify-between text-[11px] text-slate-500">
        <p>© 2026 FindYourSky India. Built for Business Analytics & Aviation Decision Support.</p>
        <p className="mt-2 sm:mt-0 text-slate-500">
          Disclaimer: Recommendations do not guarantee DGCA pilot license issuance, course duration, or airline placement.
        </p>
      </div>
    </footer>
  );
};
