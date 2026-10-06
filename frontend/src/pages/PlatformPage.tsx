import React from 'react';
import { useParams } from 'react-router-dom';
import SolutionCard from '../components/SolutionCard';
import solutionsData from '../data/solutions.json';

const PlatformPage: React.FC = () => {
  const { platform } = useParams<{ platform: string }>();
  
  // Cast data to expected type for easier handling
  const data = solutionsData as Record<string, any[]>;
  const solutions = platform ? data[platform] || [] : [];

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6 capitalize text-center">{platform} Solutions</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {solutions.length > 0 ? (
          solutions.map((sol, index) => (
            <SolutionCard key={index} {...sol} />
          ))
        ) : (
          <p className="text-center text-gray-500 col-span-full">No solutions found for this platform.</p>
        )}
      </div>
    </div>
  );
};

export default PlatformPage;
