import { motion } from 'motion/react';
import { TrendingUp, TrendingDown } from 'lucide-react';

interface TrendingCoin {
  rank: number;
  symbol: string;
  socialVol: string;
  change: number;
}

export function TrendingCoins() {
  const coins: TrendingCoin[] = [
    { rank: 1, symbol: 'PEPE', socialVol: '45.2K', change: 125 },
    { rank: 2, symbol: 'DOGE', socialVol: '102.1K', change: 88 },
    { rank: 3, symbol: 'SHIB', socialVol: '76.8K', change: 72 },
    { rank: 4, symbol: 'BTC', socialVol: '2.3M', change: -8 },
    { rank: 5, symbol: 'ETH', socialVol: '1.1M', change: -2 },
  ];

  return (
    <div className="bg-gray-900/30 border border-gray-800 rounded p-3">
      <h2 className="text-yellow-400 mb-3 uppercase tracking-wider text-xs">
        Top 5 Trending Coins
      </h2>
      <div className="space-y-2">
        {coins.map((coin, index) => (
          <motion.div
            key={coin.symbol}
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.1 }}
            whileHover={{ x: 3, backgroundColor: 'rgba(250, 204, 21, 0.05)' }}
            className="flex items-center justify-between text-xs rounded cursor-pointer transition-colors"
          >
            <div className="flex items-center gap-2">
              <span className="text-gray-500">{coin.rank}.</span>
              <span className="text-white">{coin.symbol}</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-gray-500">
                {coin.socialVol}
              </span>
              <div className={`flex items-center gap-1 ${coin.change > 0 ? 'text-green-400' : 'text-red-400'}`}>
                {coin.change > 0 ? (
                  <TrendingUp className="w-3 h-3" />
                ) : (
                  <TrendingDown className="w-3 h-3" />
                )}
                <span>{coin.change > 0 ? '+' : ''}{coin.change}%</span>
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </div>
  );
}
