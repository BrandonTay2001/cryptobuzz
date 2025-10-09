import { motion } from 'motion/react';
import { Hash } from 'lucide-react';

interface TrendingTopic {
  rank: number;
  topic: string;
  change: number;
}

export function TrendingTopics() {
  const topics: TrendingTopic[] = [
    { rank: 1, topic: '#memecoin', change: 258 },
    { rank: 2, topic: '"SEC"', change: -15 },
    { rank: 3, topic: '"ETF Approval"', change: 180 },
    { rank: 4, topic: '"Airdrop"', change: 95 },
    { rank: 5, topic: '"Halving"', change: 40 },
  ];

  return (
    <div className="bg-gray-900/30 border border-gray-800 rounded p-3">
      <h2 className="text-yellow-400 mb-3 uppercase tracking-wider text-xs">
        Top 5 Trending Topics
      </h2>
      <div className="space-y-2">
        {topics.map((topic, index) => (
          <motion.div
            key={topic.topic}
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.1 + 0.5 }}
            whileHover={{ x: 3, backgroundColor: 'rgba(250, 204, 21, 0.05)' }}
            className="flex items-center justify-between text-xs rounded cursor-pointer transition-colors"
          >
            <div className="flex items-center gap-2">
              <span className="text-gray-500">{topic.rank}.</span>
              <Hash className="w-3 h-3 text-yellow-500" />
              <span className="text-white">{topic.topic}</span>
            </div>
            <span className={topic.change > 0 ? 'text-green-400' : 'text-red-400'}>
              {topic.change > 0 ? '+' : ''}{topic.change}%
            </span>
          </motion.div>
        ))}
      </div>
    </div>
  );
}
