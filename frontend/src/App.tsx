import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import PlatformPage from './pages/PlatformPage';

const App: React.FC = () => {
  const platforms = ['LeetCode', 'Codeforces', 'AtCoder', 'CodeChef'];

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <Routes>
        <Route path="/" element={
          <>
            <h1 className="text-3xl font-bold mb-6 text-center text-gray-800">
              Solutions Explorer
            </h1>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              {platforms.map((platform) => (
                <Link key={platform} to={`/${platform.toLowerCase()}`} className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
                  <h2 className="text-xl font-semibold text-gray-700">{platform}</h2>
                  <p className="text-gray-500 mt-2">View {platform} questions.</p>
                </Link>
              ))}
            </div>
          </>
        } />
        <Route path="/:platform" element={<PlatformPage />} />
      </Routes>
    </div>
  );
};

export default App;
