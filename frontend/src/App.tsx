import { useState, useEffect } from 'react';
import { HorizontalBarChart } from './components/HorizontalBarChart';
import { TrendingCoins } from './components/TrendingCoins';
import { TrendingTopics } from './components/TrendingTopics';
import { SocialMetrics } from './components/SocialMetrics';
import { Sun, Twitter } from 'lucide-react';

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
    <div className="h-screen bg-black text-white p-4 font-mono overflow-hidden flex flex-col">
      {/* Header */}
      <header className="flex items-center justify-between mb-4">
        <h1 className="text-yellow-400 tracking-wider">CRYPTOBUZZTERMINAL</h1>
        <div className="flex items-center gap-3">
          <span className="text-gray-400 text-sm">{currentTime}</span>
          <Sun className="w-4 h-4 text-gray-400" />
        </div>
      </header>

      {/* Main Content */}
      <div className="flex-1 grid grid-cols-1 lg:grid-cols-[1fr_320px] gap-4 overflow-hidden">
        {/* Left Section - Chart */}
        <div className="flex flex-col overflow-hidden">
          {/* Chart Header */}
          <div className="flex items-center justify-between mb-3">
            <span className="text-gray-600 text-xs uppercase tracking-wider">Metric</span>
            <div className="flex items-center gap-2">
              <Twitter className="w-4 h-4 text-gray-400" />
              <select
                value={selectedMetric}
                onChange={(e) => setSelectedMetric(e.target.value)}
                className="bg-black border border-gray-800 text-white text-sm px-3 py-1 rounded appearance-none cursor-pointer hover:border-yellow-400 transition-colors focus:outline-none focus:border-yellow-400"
              >
                {metricOptions.map((metric) => (
                  <option key={metric.value} value={metric.value}>
                    {metric.label}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Chart Area with Scroll */}
          <div className="flex-1 overflow-y-auto pr-2 scrollbar-thin scrollbar-thumb-gray-800 scrollbar-track-transparent">
            <HorizontalBarChart metric={selectedMetric} />
          </div>
        </div>

        {/* Right Section - Stats */}
        <div className="flex flex-col gap-4 overflow-y-auto scrollbar-thin scrollbar-thumb-gray-800 scrollbar-track-transparent">
          <TrendingCoins />
          <TrendingTopics />
          <SocialMetrics />
        </div>
      </div>
    </div>
  );
}
