import React, { useState, useEffect } from 'react';
import { HorizontalBarChart } from './components/HorizontalBarChart';
import { TrendingCoins } from './components/TrendingCoins';
import { TrendingTopics } from './components/TrendingTopics';
import { SocialMetrics } from './components/SocialMetrics';
import { NewsTicker } from './components/NewsTicker';
import { Header } from './components/Header';
import { ChartPanel } from './components/ChartPanel';
import { RightSidebar } from './components/RightSidebar';

export default function App() {
  const [selectedMetric, setSelectedMetric] = useState('twitter');
  const [currentTime, setCurrentTime] = useState('01:23:01');

  // Update time every second
  useEffect(() => {
    const interval = setInterval(() => {
      const now = new Date();
      const hours = String(now.getHours()).padStart(2, '0');
      const minutes = String(now.getMinutes()).padStart(2, '0');
      const seconds = String(now.getSeconds()).padStart(2, '0');
      setCurrentTime(`${hours}:${minutes}:${seconds}`);
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  const metricOptions = [
    { value: 'twitter', label: 'Twitter Social Dominance' },
    { value: 'reddit', label: 'Reddit Social Dominance' },
    { value: 'telegram', label: 'Telegram Social Dominance' },
    { value: 'discord', label: 'Discord Social Dominance' },
    { value: 'overall', label: 'Overall Social Dominance' },
  ];

  const currentMetric = metricOptions.find(m => m.value === selectedMetric)?.label || 'Twitter Social Dominance';

  return (
    <div className="h-screen bg-black text-white p-4 font-mono overflow-hidden flex flex-col gap-y-8">
      {/* Header */}
      <Header currentTime={currentTime} />

      {/* News Ticker below title */}
      <NewsTicker
        headlines={[
          'BTC dominance rises as market eyes ETF inflows',
          'SOL ecosystem sees surge in developer activity',
          'ETH gas fees cool amid L2 adoption',
          'Memecoins rally on social buzz spike',
          'On-chain metrics signal accumulation phase',
          'DeFi TVL ticks up across major protocols',
        ]}
        speed={140}
        className="mt-0 mb-0"
      />

      {/* Main Content */}
      <div className="flex-1 grid grid-cols-1 lg:grid-cols-[1fr_320px] gap-4 overflow-hidden">
        {/* Left Section - Chart */}
        <ChartPanel
          selectedMetric={selectedMetric}
          onChangeSelectedMetric={setSelectedMetric}
          metricOptions={metricOptions}
        />

        {/* Right Section - Stats */}
        <RightSidebar />
      </div>
    </div>
  );
}
