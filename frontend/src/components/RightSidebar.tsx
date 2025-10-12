import React from 'react';
import { TrendingCoins } from './TrendingCoins';
import { TrendingTopics } from './TrendingTopics';
import { SocialMetrics } from './SocialMetrics';

export function RightSidebar() {
  return (
    <div className="flex flex-col gap-4 overflow-y-auto scrollbar-thin scrollbar-thumb-gray-800 scrollbar-track-transparent">
      <TrendingCoins />
      <TrendingTopics />
      <SocialMetrics />
    </div>
  );
}


