import { useState } from 'react';
import { motion } from 'motion/react';

interface CoinData {
  rank: number;
  symbol: string;
  percentage: number;
}

interface SocialDominanceChartProps {
  metric: string;
}

export function SocialDominanceChart({ metric }: SocialDominanceChartProps) {
  const [hoveredIndex, setHoveredIndex] = useState<number | null>(null);

  // Generate 100 coins with realistic distribution
  const getDataForMetric = (metric: string): CoinData[] => {
    const topCoins = [
      'BTC', 'SOL', 'ETH', 'DOGE', 'DOT', 'XRP', 'MATIC', 'LTC', 'ADA', 'BCH',
      'LINK', 'ATOM', 'ICP', 'LUNA', 'IKT', 'ETC', 'MST', 'XLM', 'HNM', 'BNB',
      'VYF', 'NPS', 'FIL', 'TRX', 'AVAX', 'SHIB', 'UNI', 'ALGO', 'VET', 'HBAR',
      'NEAR', 'APT', 'ARB', 'OP', 'IMX', 'SAND', 'MANA', 'AXS', 'GALA', 'ENJ',
      'FTM', 'AAVE', 'MKR', 'SNX', 'CRV', 'COMP', 'YFI', 'BAL', 'UMA', 'REN',
      'ZRX', 'BAT', 'KNC', 'LRC', 'STORJ', 'GRT', 'SKL', 'ANKR', 'NKN', 'OCEAN',
      'BAND', 'KAVA', 'RSR', 'RLC', 'NMR', 'MLN', 'REP', 'ZIL', 'ONT', 'ICX',
      'QTUM', 'ZEN', 'WAVES', 'LSK', 'SC', 'STEEM', 'DCR', 'DGB', 'RVN', 'MAID',
      'XEM', 'NANO', 'BTT', 'HOT', 'DENT', 'WIN', 'CHZ', 'CELR', 'ONE', 'TFUEL',
      'THETA', 'COTI', 'IOTX', 'FLUX', 'ERG', 'KDA', 'ROSE', 'CKB', 'GLMR', 'MOVR'
    ];

    // Generate percentages with exponential decay
    const baseData: CoinData[] = topCoins.map((symbol, index) => {
      let percentage: number;
      if (index === 0) percentage = 27.18;
      else if (index === 1) percentage = 16.24;
      else if (index === 2) percentage = 13.96;
      else if (index === 3) percentage = 6.52;
      else if (index === 4) percentage = 5.44;
      else if (index < 10) percentage = 5.0 - (index - 5) * 0.3;
      else if (index < 20) percentage = 3.5 - (index - 10) * 0.2;
      else if (index < 40) percentage = 1.5 - (index - 20) * 0.05;
      else if (index < 60) percentage = 0.8 - (index - 40) * 0.02;
      else if (index < 80) percentage = 0.5 - (index - 60) * 0.01;
      else percentage = 0.3 - (index - 80) * 0.005;

      return {
        rank: index + 1,
        symbol,
        percentage: Math.max(0.01, percentage)
      };
    });

    // Vary slightly for different metrics
    if (metric !== 'twitter') {
      const variation = metric === 'reddit' ? 0.15 : metric === 'telegram' ? 0.2 : 0.1;
      return baseData.map(item => ({
        ...item,
        percentage: item.percentage * (1 - variation + Math.random() * variation * 2),
      }));
    }
    
    return baseData;
  };

  const data = getDataForMetric(metric);
  const maxPercentage = Math.max(...data.map(d => d.percentage));

  // Rank 1: Crown/Royal effect with golden sparkles and shimmer
  const Rank1Effect = () => (
    <>
      {/* Golden shimmer waves */}
      <motion.div
        className="absolute inset-0 bg-gradient-to-r from-yellow-300/40 via-yellow-200/60 to-yellow-300/40"
        animate={{
          opacity: [0.3, 0.6, 0.3],
        }}
        transition={{
          duration: 3,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
      />
      {/* Crown sparkles - reduced count */}
      {[...Array(4)].map((_, i) => (
        <motion.div
          key={i}
          className="absolute w-1.5 h-1.5 bg-white rounded-full"
          style={{
            left: `${20 + i * 20}%`,
            top: '50%',
            boxShadow: '0 0 4px 1px rgba(255, 215, 0, 0.6)',
          }}
          animate={{
            opacity: [0, 1, 0],
            scale: [0, 1.2, 0],
            y: [0, -20],
          }}
          transition={{
            duration: 2,
            repeat: Infinity,
            delay: i * 0.5,
            ease: 'easeOut',
          }}
        />
      ))}
    </>
  );

  // Rank 2: Lightning/Electric effect with crackling bolts
  const Rank2Effect = () => (
    <>
      {/* Electric gradient */}
      <motion.div
        className="absolute inset-0 bg-gradient-to-r from-cyan-300/30 via-cyan-200/50 to-cyan-300/30"
        animate={{
          opacity: [0.3, 0.5, 0.3],
        }}
        transition={{
          duration: 1.5,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
      />
      {/* Lightning bolts - reduced count */}
      {[...Array(3)].map((_, i) => (
        <motion.div
          key={i}
          className="absolute h-full w-0.5 bg-white"
          style={{
            left: `${30 + i * 20}%`,
            boxShadow: '0 0 6px 1px rgba(100, 255, 255, 0.6)',
          }}
          animate={{
            opacity: [0, 0.8, 0],
            scaleY: [0.5, 1, 0.5],
          }}
          transition={{
            duration: 0.6,
            repeat: Infinity,
            delay: i * 0.3,
            repeatDelay: 1.2,
          }}
        />
      ))}
    </>
  );

  // Rank 3: Bubble/Wave effect with rising bubbles
  const Rank3Effect = () => (
    <>
      {/* Wavy gradient */}
      <motion.div
        className="absolute inset-0 bg-gradient-to-r from-purple-300/30 via-pink-300/50 to-purple-300/30"
        animate={{
          opacity: [0.3, 0.5, 0.3],
        }}
        transition={{
          duration: 3,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
      />
      {/* Rising bubbles - reduced count */}
      {[...Array(4)].map((_, i) => (
        <motion.div
          key={i}
          className="absolute rounded-full border border-white/50"
          style={{
            width: `${6 + (i % 2) * 3}px`,
            height: `${6 + (i % 2) * 3}px`,
            left: `${25 + i * 18}%`,
            bottom: '0',
            boxShadow: '0 0 4px 1px rgba(255, 255, 255, 0.3)',
          }}
          animate={{
            y: [0, -20],
            opacity: [0, 0.7, 0],
            scale: [0.6, 1, 1.1],
          }}
          transition={{
            duration: 2.5,
            repeat: Infinity,
            delay: i * 0.6,
            ease: 'easeOut',
          }}
        />
      ))}
    </>
  );

  // Rank 4: Bouncing coin particles
  const Rank4Effect = () => (
    <>
      {/* Orange glow */}
      <motion.div
        className="absolute inset-0 bg-gradient-to-r from-orange-300/30 via-orange-200/50 to-orange-300/30"
        animate={{
          opacity: [0.3, 0.5, 0.3],
        }}
        transition={{
          duration: 2,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
      />
      {/* Bouncing coins - reduced count */}
      {[...Array(3)].map((_, i) => (
        <motion.div
          key={i}
          className="absolute w-2 h-2 rounded-full bg-white/80 border border-orange-300"
          style={{
            left: `${30 + i * 20}%`,
            bottom: '2px',
            boxShadow: '0 0 4px 1px rgba(255, 180, 0, 0.4)',
          }}
          animate={{
            y: [0, -12, 0],
            rotate: [0, 180, 360],
          }}
          transition={{
            duration: 1.5,
            repeat: Infinity,
            delay: i * 0.5,
            ease: 'easeInOut',
          }}
        />
      ))}
    </>
  );

  // Rank 5: Pulse rings effect
  const Rank5Effect = () => (
    <>
      {/* Base gradient */}
      <motion.div
        className="absolute inset-0 bg-gradient-to-r from-emerald-300/30 via-green-300/50 to-emerald-300/30"
        animate={{
          opacity: [0.3, 0.5, 0.3],
        }}
        transition={{
          duration: 2.5,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
      />
      {/* Pulsing rings - reduced count */}
      {[...Array(2)].map((_, i) => (
        <motion.div
          key={i}
          className="absolute inset-0 border border-emerald-200/60 rounded-sm"
          animate={{
            opacity: [0.5, 0],
            scale: [1, 1.08],
          }}
          transition={{
            duration: 2,
            repeat: Infinity,
            delay: i * 1,
            ease: 'easeOut',
          }}
        />
      ))}
    </>
  );

  // Get effect component based on rank
  const getEffectForRank = (rank: number) => {
    switch (rank) {
      case 1: return <Rank1Effect />;
      case 2: return <Rank2Effect />;
      case 3: return <Rank3Effect />;
      case 4: return <Rank4Effect />;
      case 5: return <Rank5Effect />;
      default: return null;
    }
  };

  // Get bar color based on rank
  const getBarColorForRank = (rank: number) => {
    switch (rank) {
      case 1: return 'bg-gradient-to-r from-yellow-400 to-yellow-500'; // Gold
      case 2: return 'bg-gradient-to-r from-cyan-400 to-cyan-500'; // Cyan
      case 3: return 'bg-gradient-to-r from-purple-400 to-pink-400'; // Purple/Pink
      case 4: return 'bg-gradient-to-r from-orange-400 to-orange-500'; // Orange
      case 5: return 'bg-gradient-to-r from-emerald-400 to-green-500'; // Green
      default: return 'bg-yellow-500/70';
    }
  };

  return (
    <div className="space-y-1">
      {data.map((coin, index) => {
        const isTop5 = coin.rank <= 5;
        const widthPercentage = (coin.percentage / maxPercentage) * 100;

        return (
          <motion.div
            key={`${metric}-${coin.symbol}`}
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.01 }}
            className="relative group"
            onMouseEnter={() => setHoveredIndex(index)}
            onMouseLeave={() => setHoveredIndex(null)}
          >
            <div className="flex items-center gap-3 text-xs">
              {/* Rank */}
              <span className={`w-5 text-right ${
                coin.rank === 1 ? 'text-yellow-400' :
                coin.rank === 2 ? 'text-cyan-400' :
                coin.rank === 3 ? 'text-purple-400' :
                coin.rank === 4 ? 'text-orange-400' :
                coin.rank === 5 ? 'text-emerald-400' :
                'text-gray-600'
              }`}>
                {coin.rank}
              </span>

              {/* Symbol */}
              <span className={`w-12 ${
                isTop5 ? 'text-white' : 'text-gray-400'
              }`}>
                {coin.symbol}
              </span>

              {/* Bar Container */}
              <div className="flex-1 relative h-5 bg-transparent overflow-visible">
                {/* Background track - full width dark bar */}
                <div className="absolute inset-0 bg-gray-900/40 rounded-sm" />
                
                {/* Animated Bar */}
                <motion.div
                  className={`absolute left-0 top-0 h-full rounded-sm overflow-hidden ${
                    isTop5 
                      ? getBarColorForRank(coin.rank)
                      : 'bg-yellow-500/70'
                  }`}
                  initial={{ width: 0 }}
                  animate={{ width: `${widthPercentage}%` }}
                  transition={{ duration: 0.8, delay: index * 0.01 }}
                >
                  {/* Unique effect for each top 5 rank */}
                  {isTop5 && getEffectForRank(coin.rank)}

                  {/* Hover shine effect for non-top 5 bars */}
                  {hoveredIndex === index && !isTop5 && (
                    <motion.div
                      className="absolute inset-0 bg-gradient-to-r from-transparent via-white to-transparent opacity-30"
                      initial={{ x: '-100%' }}
                      animate={{ x: '200%' }}
                      transition={{
                        duration: 0.6,
                        ease: 'easeInOut',
                      }}
                    />
                  )}
                </motion.div>
              </div>

              {/* Percentage */}
              <motion.span
                className={`w-14 text-right ${
                  coin.rank === 1 ? 'text-yellow-400' :
                  coin.rank === 2 ? 'text-cyan-400' :
                  coin.rank === 3 ? 'text-purple-400' :
                  coin.rank === 4 ? 'text-orange-400' :
                  coin.rank === 5 ? 'text-emerald-400' :
                  'text-gray-500'
                }`}
                animate={{
                  scale: hoveredIndex === index ? 1.1 : 1,
                }}
              >
                {coin.percentage.toFixed(2)}%
              </motion.span>
            </div>

            {/* Tooltip on hover */}
            {hoveredIndex === index && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: 10 }}
                className={`absolute left-20 top-6 bg-gray-800 border px-2 py-1 rounded text-xs z-20 whitespace-nowrap pointer-events-none ${
                  coin.rank === 1 ? 'border-yellow-400' :
                  coin.rank === 2 ? 'border-cyan-400' :
                  coin.rank === 3 ? 'border-purple-400' :
                  coin.rank === 4 ? 'border-orange-400' :
                  coin.rank === 5 ? 'border-emerald-400' :
                  'border-yellow-400'
                }`}
              >
                <div className={
                  coin.rank === 1 ? 'text-yellow-400' :
                  coin.rank === 2 ? 'text-cyan-400' :
                  coin.rank === 3 ? 'text-purple-400' :
                  coin.rank === 4 ? 'text-orange-400' :
                  coin.rank === 5 ? 'text-emerald-400' :
                  'text-yellow-400'
                }>#{coin.rank} {coin.symbol}</div>
                <div className="text-gray-300">{coin.percentage.toFixed(2)}% dominance</div>
                {isTop5 && (
                  <div className={`text-xs mt-0.5 ${
                    coin.rank === 1 ? 'text-yellow-300' :
                    coin.rank === 2 ? 'text-cyan-300' :
                    coin.rank === 3 ? 'text-purple-300' :
                    coin.rank === 4 ? 'text-orange-300' :
                    coin.rank === 5 ? 'text-emerald-300' :
                    'text-yellow-300'
                  }`}>
                    {coin.rank === 1 && '👑 #1 King!'}
                    {coin.rank === 2 && '⚡ #2 Electric!'}
                    {coin.rank === 3 && '💫 #3 Bubbling!'}
                    {coin.rank === 4 && '🪙 #4 Bouncing!'}
                    {coin.rank === 5 && '💚 #5 Pulsing!'}
                  </div>
                )}
              </motion.div>
            )}
          </motion.div>
        );
      })}
      
      {/* Total coins indicator */}
      <div className="text-gray-600 text-xs mt-4 text-center">
        Tracking 100 coins
      </div>
    </div>
  );
}
