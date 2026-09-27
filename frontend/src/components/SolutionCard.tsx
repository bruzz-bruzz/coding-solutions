import React from 'react';

interface SolutionCardProps {
  title: string;
  code: string;
  logic: string;
  timeComplexity: string;
  spaceComplexity: string;
}

const SolutionCard: React.FC<SolutionCardProps> = ({ title, code, logic, timeComplexity, spaceComplexity }) => {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md border border-gray-200">
      <h3 className="text-lg font-bold text-gray-800 mb-2">{title}</h3>
      <div className="bg-gray-800 text-gray-200 p-4 rounded-md mb-4 overflow-x-auto text-sm">
        <pre><code>{code}</code></pre>
      </div>
      <p className="text-gray-600 mb-2"><strong>Logic:</strong> {logic}</p>
      <div className="flex gap-4 text-sm text-gray-500">
        <p><strong>Time:</strong> {timeComplexity}</p>
        <p><strong>Space:</strong> {spaceComplexity}</p>
      </div>
    </div>
  );
};

export default SolutionCard;
