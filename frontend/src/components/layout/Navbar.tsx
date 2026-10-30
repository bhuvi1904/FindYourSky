import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Plane, Compass, BarChart3, Scale, Database, ShieldCheck, BookOpen, Menu, X, ChevronDown } from 'lucide-react';

export const Navbar: React.FC = () => {
  const location = useLocation();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [analyticsDropdown, setAnalyticsDropdown] = useState(false);

  const isActive = (path: string) => {
    if (path === '/' && location.pathname === '/') return true;
    if (path !== '/' && location.pathname.startsWith(path)) return true;
    return false;
  };

  return (
    <nav className="sticky top-0 z-50 aviation-glass border-b border-slate-800/80 bg-slate-950/90 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-3 group">
            <div className="w-10 h-10 rounded-lg bg-sky-500/10 border border-sky-400/30 flex items-center justify-center text-sky-400 group-hover:bg-sky-500/20 group-hover:scale-105 transition-all">
              <Plane className="w-6 h-6 transform -rotate-45" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="font-extrabold text-lg text-white tracking-tight">FindYour<span className="text-sky-400">Sky</span></span>
                <span className="text-[10px] uppercase font-semibold px-1.5 py-0.5 rounded bg-sky-500/10 text-sky-400 border border-sky-500/20">
                  DGCA FTO
                </span>
              </div>
              <span className="text-[11px] text-slate-400 block -mt-0.5 font-mono">Statistical Recommendation System</span>
            </div>
          </Link>

          {/* Desktop Nav Links */}
          <div className="hidden lg:flex items-center space-x-1">
            <Link
              to="/schools"
              className={`px-3 py-2 rounded-md text-sm font-medium transition-colors flex items-center space-x-1.5 ${
                isActive('/schools') ? 'bg-sky-500/15 text-sky-400 border border-sky-500/30' : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
              }`}
            >
              <Compass className="w-4 h-4" />
              <span>Schools</span>
            </Link>

            <Link
              to="/compare"
              className={`px-3 py-2 rounded-md text-sm font-medium transition-colors flex items-center space-x-1.5 ${
                isActive('/compare') ? 'bg-sky-500/15 text-sky-400 border border-sky-500/30' : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
              }`}
            >
              <Scale className="w-4 h-4" />
              <span>Compare</span>
            </Link>

            {/* Analytics Lab Dropdown */}
            <div className="relative">
              <button
                onClick={() => setAnalyticsDropdown(!analyticsDropdown)}
                className={`px-3 py-2 rounded-md text-sm font-medium transition-colors flex items-center space-x-1.5 ${
                  isActive('/analytics') ? 'bg-sky-500/15 text-sky-400 border border-sky-500/30' : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
                }`}
              >
                <BarChart3 className="w-4 h-4" />
                <span>Analytics Lab</span>
                <ChevronDown className="w-3.5 h-3.5 opacity-70" />
              </button>

              {analyticsDropdown && (
                <div
                  className="absolute left-0 mt-2 w-56 rounded-xl bg-slate-900 border border-slate-800 shadow-2xl py-2 z-50"
                  onMouseLeave={() => setAnalyticsDropdown(false)}
                >
                  <Link
                    to="/analytics"
                    onClick={() => setAnalyticsDropdown(false)}
                    className="block px-4 py-2 text-sm text-slate-300 hover:bg-slate-800/80 hover:text-sky-400"
                  >
                    Overview Dashboard
                  </Link>
                  <Link
                    to="/analytics/logistic-regression"
                    onClick={() => setAnalyticsDropdown(false)}
                    className="block px-4 py-2 text-sm text-slate-300 hover:bg-slate-800/80 hover:text-sky-400"
                  >
                    Logistic Regression
                  </Link>
                  <Link
                    to="/analytics/factor-analysis"
                    onClick={() => setAnalyticsDropdown(false)}
                    className="block px-4 py-2 text-sm text-slate-300 hover:bg-slate-800/80 hover:text-sky-400"
                  >
                    Factor Analysis (EFA)
                  </Link>
                  <Link
                    to="/analytics/clustering"
                    onClick={() => setAnalyticsDropdown(false)}
                    className="block px-4 py-2 text-sm text-slate-300 hover:bg-slate-800/80 hover:text-sky-400"
                  >
                    K-Means Clustering
                  </Link>
                </div>
              )}
            </div>

            <Link
              to="/evaluation"
              className={`px-3 py-2 rounded-md text-sm font-medium transition-colors flex items-center space-x-1.5 ${
                isActive('/evaluation') ? 'bg-sky-500/15 text-sky-400 border border-sky-500/30' : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
              }`}
            >
              <ShieldCheck className="w-4 h-4" />
              <span>Model Evaluation</span>
            </Link>

            <Link
              to="/sources"
              className={`px-3 py-2 rounded-md text-sm font-medium transition-colors flex items-center space-x-1.5 ${
                isActive('/sources') ? 'bg-sky-500/15 text-sky-400 border border-sky-500/30' : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
              }`}
            >
              <Database className="w-4 h-4" />
              <span>Sources</span>
            </Link>

            <Link
              to="/about/methodology"
              className={`px-3 py-2 rounded-md text-sm font-medium transition-colors flex items-center space-x-1.5 ${
                isActive('/about/methodology') ? 'bg-sky-500/15 text-sky-400 border border-sky-500/30' : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
              }`}
            >
              <BookOpen className="w-4 h-4" />
              <span>Methodology</span>
            </Link>
          </div>

          {/* Action CTA */}
          <div className="hidden sm:flex items-center space-x-3">
            <Link
              to="/questionnaire"
              className="inline-flex items-center justify-center px-4 py-2 rounded-lg text-sm font-medium text-slate-950 bg-sky-400 hover:bg-sky-300 shadow-md shadow-sky-500/20 transition-all font-semibold"
            >
              Match School
            </Link>
          </div>

          {/* Mobile menu button */}
          <div className="flex lg:hidden">
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-2 rounded-md text-slate-400 hover:text-white hover:bg-slate-800"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      {mobileMenuOpen && (
        <div className="lg:hidden px-4 pt-2 pb-6 space-y-1 bg-slate-900 border-b border-slate-800">
          <Link
            to="/schools"
            onClick={() => setMobileMenuOpen(false)}
            className="block px-3 py-2 rounded-md text-base font-medium text-slate-200 hover:bg-slate-800"
          >
            Schools Directory
          </Link>
          <Link
            to="/questionnaire"
            onClick={() => setMobileMenuOpen(false)}
            className="block px-3 py-2 rounded-md text-base font-medium text-sky-400 hover:bg-slate-800"
          >
            Questionnaire & Recommendations
          </Link>
          <Link
            to="/compare"
            onClick={() => setMobileMenuOpen(false)}
            className="block px-3 py-2 rounded-md text-base font-medium text-slate-200 hover:bg-slate-800"
          >
            Compare Schools
          </Link>
          <Link
            to="/analytics"
            onClick={() => setMobileMenuOpen(false)}
            className="block px-3 py-2 rounded-md text-base font-medium text-slate-200 hover:bg-slate-800"
          >
            Analytics Lab
          </Link>
          <Link
            to="/evaluation"
            onClick={() => setMobileMenuOpen(false)}
            className="block px-3 py-2 rounded-md text-base font-medium text-slate-200 hover:bg-slate-800"
          >
            Model Evaluation
          </Link>
          <Link
            to="/sources"
            onClick={() => setMobileMenuOpen(false)}
            className="block px-3 py-2 rounded-md text-base font-medium text-slate-200 hover:bg-slate-800"
          >
            Authoritative Sources
          </Link>
          <Link
            to="/about/methodology"
            onClick={() => setMobileMenuOpen(false)}
            className="block px-3 py-2 rounded-md text-base font-medium text-slate-200 hover:bg-slate-800"
          >
            Statistical Methodology
          </Link>
        </div>
      )}
    </nav>
  );
};
