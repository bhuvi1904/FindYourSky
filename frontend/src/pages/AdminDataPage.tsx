import React, { useState } from 'react';
import { Database, ShieldAlert, RefreshCw, Upload, CheckCircle2, AlertTriangle, Key } from 'lucide-react';

export const AdminDataPage: React.FC = () => {
  const [adminKey, setAdminKey] = useState('admin-secret-dgca-2026');
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleRefresh = async () => {
    setLoading(true);
    setMessage(null);
    setError(null);
    try {
      const res = await fetch('/api/admin/refresh', {
        method: 'POST',
        headers: {
          'X-Admin-Key': adminKey,
        },
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Data refresh failed.');
      setMessage('Official database refreshed successfully from seed sources.');
    } catch (err: any) {
      setError(err.message || 'Error executing data refresh.');
    } finally {
      setLoading(false);
    }
  };

  const handleFileUpload = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedFile) {
      alert('Please select a JSON file to upload.');
      return;
    }
    setLoading(true);
    setMessage(null);
    setError(null);

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const res = await fetch('/api/admin/import', {
        method: 'POST',
        headers: {
          'X-Admin-Key': adminKey,
        },
        body: formData,
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Import failed.');
      setMessage(data.message || 'File uploaded and parsed successfully.');
    } catch (err: any) {
      setError(err.message || 'Import failed.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div>
        <div className="flex items-center space-x-2 text-xs font-mono text-amber-400 font-semibold mb-2">
          <ShieldAlert className="w-4 h-4" />
          <span>RESTRICTED ADMINISTRATIVE CONSOLE</span>
        </div>
        <h1 className="text-3xl font-black text-white tracking-tight">
          Data Management & Ingestion Pipeline
        </h1>
        <p className="text-xs sm:text-sm text-slate-400 mt-2 max-w-2xl leading-relaxed">
          Manage database state, execute administrative audits, trigger official DGCA seed sync, and validate newly imported flying training organisation records.
        </p>
      </div>

      {/* Admin Key Card */}
      <div className="aviation-card space-y-4">
        <h3 className="font-bold text-white text-sm font-mono flex items-center space-x-2">
          <Key className="w-4 h-4 text-sky-400" />
          <span>Administrative Credentials</span>
        </h3>
        <div>
          <label className="block text-xs font-mono text-slate-400 mb-1">X-ADMIN-KEY</label>
          <input
            type="password"
            value={adminKey}
            onChange={(e) => setAdminKey(e.target.value)}
            className="w-full bg-slate-950/80 border border-slate-800 rounded-lg px-4 py-2 text-sm text-white font-mono focus:outline-none focus:border-sky-500"
          />
        </div>
      </div>

      {/* Feedback & Alert Display */}
      {message && (
        <div className="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-mono flex items-center space-x-2">
          <CheckCircle2 className="w-4 h-4 flex-shrink-0" />
          <span>{message}</span>
        </div>
      )}
      {error && (
        <div className="p-4 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-400 text-xs font-mono flex items-center space-x-2">
          <AlertTriangle className="w-4 h-4 flex-shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {/* Action 1: Refresh Database from Official Seeds */}
      <div className="aviation-card space-y-4">
        <h3 className="font-bold text-white text-sm font-mono flex items-center space-x-2">
          <RefreshCw className="w-4 h-4 text-sky-400" />
          <span>Action 1: Refresh Official Database</span>
        </h3>
        <p className="text-xs text-slate-400 leading-relaxed">
          Re-syncs institutional rankings, fleet records, and airfield databases from verified DGCA files (`dgca_sources.json` and `fto_seed_data.json`).
        </p>
        <button
          onClick={handleRefresh}
          disabled={loading}
          className="px-5 py-2.5 rounded-lg bg-sky-500 hover:bg-sky-400 text-slate-950 font-bold text-xs font-mono flex items-center space-x-2 transition-all"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
          <span>{loading ? 'Refreshing...' : 'Execute Official Data Refresh'}</span>
        </button>
      </div>

      {/* Action 2: Upload Custom JSON Dataset */}
      <div className="aviation-card space-y-4">
        <h3 className="font-bold text-white text-sm font-mono flex items-center space-x-2">
          <Upload className="w-4 h-4 text-emerald-400" />
          <span>Action 2: Import Custom FTO Records (JSON)</span>
        </h3>
        <p className="text-xs text-slate-400 leading-relaxed">
          Upload validated flying school JSON dataset conforming to the relational `School` schema. Records will be parsed and validated without violating primary key constraints.
        </p>
        <form onSubmit={handleFileUpload} className="space-y-4">
          <input
            type="file"
            accept=".json"
            onChange={(e) => setSelectedFile(e.target.files ? e.target.files[0] : null)}
            className="block w-full text-xs text-slate-400 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-xs file:font-semibold file:bg-slate-800 file:text-slate-200 hover:file:bg-slate-700"
          />
          <button
            type="submit"
            disabled={loading || !selectedFile}
            className="px-5 py-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs font-mono flex items-center space-x-2 disabled:opacity-40"
          >
            <Upload className="w-3.5 h-3.5" />
            <span>Upload & Validate Dataset</span>
          </button>
        </form>
      </div>
    </div>
  );
};
