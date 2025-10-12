import React from 'react';
import { Twitter } from 'lucide-react';
import { HorizontalBarChart } from './HorizontalBarChart';

interface MetricOption {
  value: string;
  label: string;
}

interface ChartPanelProps {
  selectedMetric: string;
  onChangeSelectedMetric: (value: string) => void;
  metricOptions: MetricOption[];
}

export function ChartPanel({ selectedMetric, onChangeSelectedMetric, metricOptions }: ChartPanelProps) {
  return (
    <div className="flex flex-col overflow-hidden">
      {/* Chart Header */}
      <div className="flex items-center justify-between mb-3">
        <span className="text-gray-600 text-xs uppercase tracking-wider">Metric</span>
        <div className="flex items-center gap-2">
          <Twitter className="w-4 h-4 text-gray-400" />
          <select
            value={selectedMetric}
            onChange={(e) => onChangeSelectedMetric(e.target.value)}
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
  );
}


