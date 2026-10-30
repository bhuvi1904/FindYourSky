import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Navbar } from './components/layout/Navbar';
import { Footer } from './components/layout/Footer';
import { LandingPage } from './pages/LandingPage';
import { SchoolDirectoryPage } from './pages/SchoolDirectoryPage';
import { SchoolDetailPage } from './pages/SchoolDetailPage';
import { QuestionnairePage } from './pages/QuestionnairePage';
import { RecommendationsPage } from './pages/RecommendationsPage';
import { ComparePage } from './pages/ComparePage';
import { AnalyticsOverviewPage } from './pages/AnalyticsOverviewPage';
import { LogisticRegressionPage } from './pages/LogisticRegressionPage';
import { FactorAnalysisPage } from './pages/FactorAnalysisPage';
import { ClusteringPage } from './pages/ClusteringPage';
import { EvaluationPage } from './pages/EvaluationPage';
import { SourcesPage } from './pages/SourcesPage';
import { AdminDataPage } from './pages/AdminDataPage';
import { MethodologyPage } from './pages/MethodologyPage';

export const App: React.FC = () => {
  return (
    <Router>
      <div className="min-h-screen flex flex-col bg-slate-950 text-slate-100 selection:bg-sky-500 selection:text-white">
        <Navbar />
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/schools" element={<SchoolDirectoryPage />} />
            <Route path="/schools/:id" element={<SchoolDetailPage />} />
            <Route path="/questionnaire" element={<QuestionnairePage />} />
            <Route path="/recommendations" element={<RecommendationsPage />} />
            <Route path="/compare" element={<ComparePage />} />
            <Route path="/analytics" element={<AnalyticsOverviewPage />} />
            <Route path="/analytics/logistic-regression" element={<LogisticRegressionPage />} />
            <Route path="/analytics/factor-analysis" element={<FactorAnalysisPage />} />
            <Route path="/analytics/clustering" element={<ClusteringPage />} />
            <Route path="/evaluation" element={<EvaluationPage />} />
            <Route path="/sources" element={<SourcesPage />} />
            <Route path="/admin/data" element={<AdminDataPage />} />
            <Route path="/about/methodology" element={<MethodologyPage />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
};

export default App;
