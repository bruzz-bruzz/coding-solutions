import React from 'react';
import { useParams } from 'react-router-dom';
import SolutionCard from '../components/SolutionCard';

// Dummy data structure
const platformData: Record<string, any[]> = {
  leetcode: [
    { title: "1. Two Sum", code: "def twoSum(nums, target): ...", logic: "Use hash map...", timeComplexity: "O(n)", spaceComplexity: "O(n)" }
  ],
  codeforces: [
    { title: "4A. Watermelon", code: "if n % 2 == 0 and n > 2: ...", logic: "Check evenness...", timeComplexity: "O(1)", spaceComplexity: "O(1)" }
  ]
  // ... other platforms
};

const PlatformPage: React.FC = () => {
  const { platform } = useParams<{ platform: string }>();
  const solutions = platformData[platform || ''] || [];

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6 capitalize">{platform} Solutions</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {solutions.map((sol, index) => (
          <SolutionCard key={index} {...sol} />
        ))}
      </div>
    </div>
  );
};

export default PlatformPage;
