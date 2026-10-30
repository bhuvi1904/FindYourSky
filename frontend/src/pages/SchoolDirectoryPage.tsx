import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Compass, Scale, AlertCircle, RefreshCw, Layers, ShieldCheck } from 'lucide-react';
import { fetchSchools } from '../api/client';
import { SchoolSummary } from '../types';
import { SchoolCard } from '../components/schools/SchoolCard';
import { SchoolFilterBar } from '../components/schools/SchoolFilterBar';

export const SchoolDirectoryPage: React.FC = () => {
  const navigate = useNavigate();
  const [schools, setSchools] = useState<SchoolSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Filters
  const [search, setSearch] = useState('');
  const [region, setRegion] = useState('');
  const [category, setCategory] = useState('');
  const [hasMultiEngine, setHasMultiEngine] = useState(false);
  const [maxBudget, setMaxBudget] = useState(6500000);

  // Comparison selection
  const [selectedForCompare, setSelectedForCompare] = useState<string[]>([]);

  const loadSchools = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchSchools({
        region: region || undefined,
        ranking_category: category || undefined,
        has_multi_engine: hasMultiEngine ? true : undefined,
        max_budget: maxBudget,
        search: search || undefined,
      });
      setSchools(data);
    } catch (err: any) {
      setError(err.message || 'Failed to load school directory.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadSchools();
  }, [region, category, hasMultiEngine, maxBudget]);

  // Debounced search
  useEffect(() => {
    const handler = setTimeout(() => {
      loadSchools();
    }, 300);
    return () => clearTimeout(handler);
  }, [search]);

  const handleToggleCompare = (schoolId: string) => {
    if (selectedForCompare.includes(schoolId)) {
      setSelectedForCompare(selectedForCompare.filter(id => id !== schoolId));
    } else {
      if (selectedForCompare.length >= 5) {
        alert('You can select a maximum of 5 schools for comparison.');
        return;
      }
      setSelectedForCompare([...selectedForCompare, schoolId]);
    }
  };

  const handleResetFilters = () => {
    setSearch('');
    setRegion('');
    setCategory('');
    setHasMultiEngine(false);
    setMaxBudget(6500000);
  };

  const handleLaunchCompare = () => {
    if (selectedForCompare.length < 2) {
      alert('Please select at least 2 schools to compare.');
      return;
    }
    navigate(`/compare?ids=${selectedForCompare.join(',')}`);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="mb-6">
        <div className="flex items-center space-x-2 text-xs font-mono text-sky-400 font-semibold mb-2">
          <Compass className="w-4 h-4" />
          <span>AUTHORITATIVE FTO DIRECTORY</span>
        </div>
        <h1 className="text-3xl font-black text-white tracking-tight">
          DGCA-Approved Flying Training Organisations
        </h1>
        <p className="text-sm text-slate-400 mt-2 max-w-3xl leading-relaxed">
          Search and filter all 41 verified Indian flying schools by geographic location, official DGCA ranking audit category, multi-engine training availability, and comparable tuition budgets.
        </p>
      </div>

      {/* Official DGCA Ranking Framework Notice Banner */}
      <div className="mb-6 p-4 rounded-xl bg-sky-950/40 border border-sky-500/30 text-sky-200 text-xs flex items-start space-x-3">
        <ShieldCheck className="w-5 h-5 text-sky-400 flex-shrink-0 mt-0.5" />
        <div className="space-y-1">
          <p className="font-bold text-white tracking-wide">
            Official DGCA Performance Ranking Framework Notice (Phase 2 — April 2026, MoCA / PIB Release)
          </p>
          <p className="text-slate-300 leading-relaxed">
            Under the official DGCA ranking framework, no FTO in India has yet achieved Category A+ (≥85%). 
            <strong className="text-sky-300"> Avyanna Aviation</strong> (Kishangarh, Rajasthan) is currently the sole institution in India to achieve <strong className="text-emerald-400">Category A</strong> (70%–84%). 
            Premier national academies (such as IGRUA, CAE Gondia, Chimes Aviation, Redbird, and Carver) are categorized under <strong className="text-blue-300">Category B</strong> (50%–69%). 
            Schools requiring performance improvements are listed under <strong className="text-amber-300">Category C</strong> (&lt;50%), and newly operationalized schools (&lt;18 months) are classified as <strong className="text-slate-300">Exempt / Under Assessment</strong>.
          </p>
        </div>
      </div>

      {/* Filter Bar */}
      <SchoolFilterBar
        search={search}
        setSearch={setSearch}
        region={region}
        setRegion={setRegion}
        category={category}
        setCategory={setCategory}
        hasMultiEngine={hasMultiEngine}
        setHasMultiEngine={setHasMultiEngine}
        maxBudget={maxBudget}
        setMaxBudget={setMaxBudget}
        onReset={handleResetFilters}
      />

      {/* Status / Count */}
      <div className="flex items-center justify-between text-xs text-slate-400 mb-6 font-mono">
        <span>
          Showing <span className="text-white font-bold">{schools.length}</span> verified institutions
        </span>
        {selectedForCompare.length > 0 && (
          <span className="text-sky-400 font-bold">
            {selectedForCompare.length} selected for comparison
          </span>
        )}
      </div>

      {/* Error display */}
      {error && (
        <div className="p-4 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-400 text-sm mb-6 flex items-center space-x-2">
          <AlertCircle className="w-5 h-5 flex-shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {/* Loading Skeletons */}
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3, 4, 5, 6].map((i) => (
            <div key={i} className="aviation-card h-72 animate-pulse flex flex-col justify-between">
              <div className="space-y-3">
                <div className="w-24 h-4 bg-slate-800 rounded" />
                <div className="w-3/4 h-6 bg-slate-800 rounded" />
                <div className="w-1/2 h-4 bg-slate-800 rounded" />
              </div>
              <div className="w-full h-12 bg-slate-800 rounded" />
            </div>
          ))}
        </div>
      ) : schools.length === 0 ? (
        <div className="text-center py-16 aviation-card">
          <Layers className="w-12 h-12 text-slate-600 mx-auto mb-4" />
          <h3 className="text-lg font-bold text-white">No Flying Schools Match Your Filters</h3>
          <p className="text-xs text-slate-400 max-w-md mx-auto mt-2">
            Try broadening your budget threshold, unchecking multi-engine requirement, or selecting 'All Regions'.
          </p>
          <button
            onClick={handleResetFilters}
            className="mt-4 px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-sky-400 text-xs font-semibold"
          >
            Reset All Filters
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {schools.map((school) => (
            <SchoolCard
              key={school.school_id}
              school={school}
              isSelectedForCompare={selectedForCompare.includes(school.school_id)}
              onToggleCompare={handleToggleCompare}
            />
          ))}
        </div>
      )}

      {/* Floating Compare Action Pill */}
      {selectedForCompare.length >= 2 && (
        <div className="fixed bottom-6 left-1/2 -translate-x-1/2 z-40 bg-slate-900 border border-sky-400/50 shadow-2xl rounded-full px-6 py-3 flex items-center space-x-4 backdrop-blur-xl animate-bounce">
          <div className="flex items-center space-x-2">
            <Scale className="w-5 h-5 text-sky-400" />
            <span className="text-xs text-slate-200 font-semibold font-mono">
              {selectedForCompare.length} FTOs Selected
            </span>
          </div>
          <button
            onClick={handleLaunchCompare}
            className="px-4 py-1.5 rounded-full bg-sky-400 hover:bg-sky-300 text-slate-950 font-bold text-xs shadow-md transition-colors"
          >
            Compare Now →
          </button>
        </div>
      )}
    </div>
  );
};
