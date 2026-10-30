import React, { useState, useEffect } from 'react';
import { Database, ExternalLink, ShieldCheck, CheckCircle2, FileText, Globe } from 'lucide-react';
import { fetchSources } from '../api/client';
import { DataSource } from '../types';

export const SourcesPage: React.FC = () => {
  const [sources, setSources] = useState<DataSource[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchSources()
      .then(setSources)
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div>
        <div className="flex items-center space-x-2 text-xs font-mono text-sky-400 font-semibold mb-2">
          <Database className="w-4 h-4" />
          <span>AUTHORITATIVE SOURCE REGISTRY & PROVENANCE</span>
        </div>
        <h1 className="text-3xl font-black text-white tracking-tight">
          Government & Regulatory Data Provenance
        </h1>
        <p className="text-xs sm:text-sm text-slate-400 mt-2 max-w-3xl leading-relaxed">
          FindYourSky enforces strict field-level provenance. All regulatory approvals, safety audit categories, aircraft fleet allotments, and institutional rankings cite official publications from the Directorate General of Civil Aviation (DGCA) and the Ministry of Civil Aviation (MoCA).
        </p>
      </div>

      {loading ? (
        <div className="py-20 text-center">
          <div className="w-12 h-12 border-4 border-sky-400 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-xs font-mono text-slate-400">Loading authoritative source registry...</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {sources.map((src) => (
            <div key={src.source_id} className="aviation-card flex flex-col justify-between space-y-4">
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-sky-500/10 text-sky-400 border border-sky-500/20">
                    {src.source_id}
                  </span>
                  <span className="flex items-center space-x-1 text-[11px] font-mono text-emerald-400">
                    <CheckCircle2 className="w-3.5 h-3.5" />
                    <span>{src.verification_status.toUpperCase()}</span>
                  </span>
                </div>

                <h3 className="font-bold text-base text-white leading-snug">
                  {src.name}
                </h3>

                <p className="text-xs text-slate-300 leading-relaxed">
                  {src.description}
                </p>

                <div className="space-y-1 text-xs text-slate-400 font-mono text-[11px] pt-2 border-t border-slate-800">
                  <div>Publisher: {src.publisher || 'Government of India'}</div>
                  <div>Source Category: {src.source_type.replace(/_/g, ' ').toUpperCase()}</div>
                  <div>Observation / Retrieval: {src.retrieval_date || 'October 2026'}</div>
                </div>
              </div>

              <div className="pt-3 border-t border-slate-800">
                <a
                  href={src.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center space-x-1.5 text-xs font-mono font-bold text-sky-400 hover:text-sky-300 transition-colors"
                >
                  <span className="truncate max-w-[280px] sm:max-w-md">{src.url}</span>
                  <ExternalLink className="w-3.5 h-3.5 flex-shrink-0" />
                </a>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Verification Protocol Callout */}
      <div className="aviation-card p-6 border-l-4 border-l-sky-400 space-y-2">
        <h4 className="font-bold text-white text-sm font-mono flex items-center space-x-2">
          <ShieldCheck className="w-4 h-4 text-sky-400" />
          <span>FTO Verification & Discrepancy Resolution Protocol</span>
        </h4>
        <p className="text-xs text-slate-400 leading-relaxed">
          In cases where school promotional materials conflict with official regulator disclosures, FindYourSky strictly prioritizes the latest applicable DGCA gazette or DigiGov audit notice. Marketing claims published on third-party aggregators are discarded.
        </p>
      </div>
    </div>
  );
};
