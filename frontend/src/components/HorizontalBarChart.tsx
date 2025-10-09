import { useState } from 'react';
import { motion } from 'motion/react';

interface ChartData {
  rank: number;
  symbol: string;
  percentage: number;
}

interface HorizontalBarChartProps {
  metric: string;
}

export function HorizontalBarChart({ metric }: HorizontalBarChartProps) {
  const [hoveredIndex, setHoveredIndex] = useState<number | null>(null);

  // Generate 100 coins with realistic distribution
  const getDataForMetric = (metric: string): ChartData[] => {
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
    const baseData: ChartData[] = topCoins.map((symbol, index) => {
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

    // Vary slightly for different metrics with consistent offsets
    if (metric !== 'twitter') {
      const multiplier = metric === 'reddit' ? 0.92 : metric === 'telegram' ? 0.88 : metric === 'discord' ? 0.95 : 0.90;
      return baseData.map(item => ({
        ...item,
        percentage: item.percentage * multiplier,
      }));
    }
    
    return baseData;
  };

  const data = getDataForMetric(metric);
  const maxPercentage = Math.max(...data.map(d => d.percentage));

  // Rank 1: Golden pulsing glow
  const Rank1Effect = () => (
    <>
      {/* Pulsing golden glow */}
      <div className="absolute inset-0 bg-gradient-to-r from-yellow-400/30 via-yellow-300/50 to-yellow-400/30 animate-pulse-glow" />
      {/* Subtle sparkles */}
      <div
        className="absolute w-1 h-1 bg-yellow-200 rounded-full animate-sparkle"
        style={{
          left: '30%',
          top: '40%',
          boxShadow: '0 0 3px 1px rgba(255, 215, 0, 0.8)',
        }}
      />
      <div
        className="absolute w-1 h-1 bg-yellow-200 rounded-full animate-sparkle-delay-1"
        style={{
          left: '50%',
          top: '40%',
          boxShadow: '0 0 3px 1px rgba(255, 215, 0, 0.8)',
        }}
      />
      <div
        className="absolute w-1 h-1 bg-yellow-200 rounded-full animate-sparkle-delay-2"
        style={{
          left: '70%',
          top: '40%',
          boxShadow: '0 0 3px 1px rgba(255, 215, 0, 0.8)',
        }}
      />
    </>
  );

  // Rank 2: Cyan electric pulse
  const Rank2Effect = () => (
    <>
      {/* Pulsing electric glow */}
      <div className="absolute inset-0 bg-gradient-to-r from-cyan-400/30 via-cyan-300/50 to-cyan-400/30 animate-pulse-glow" />
      {/* Vertical accent lines */}
      <div
        className="absolute h-full w-px bg-cyan-200 animate-pulse-glow"
        style={{
          left: '40%',
          boxShadow: '0 0 4px 1px rgba(100, 255, 255, 0.5)',
        }}
      />
      <div
        className="absolute h-full w-px bg-cyan-200 animate-pulse-glow-fast"
        style={{
          left: '60%',
          boxShadow: '0 0 4px 1px rgba(100, 255, 255, 0.5)',
        }}
      />
    </>
  );

  // Rank 3: Purple/Pink shimmer
  const Rank3Effect = () => (
    <>
      {/* Pulsing gradient */}
      <div className="absolute inset-0 bg-gradient-to-r from-purple-400/30 via-pink-300/50 to-purple-400/30 animate-pulse-glow" />
      {/* Gentle sparkle dots */}
      <div
        className="absolute w-1 h-1 bg-pink-200 rounded-full animate-sparkle"
        style={{
          left: '25%',
          top: '50%',
          boxShadow: '0 0 3px 1px rgba(255, 182, 193, 0.6)',
        }}
      />
      <div
        className="absolute w-1 h-1 bg-pink-200 rounded-full animate-sparkle-delay-1"
        style={{
          left: '50%',
          top: '50%',
          boxShadow: '0 0 3px 1px rgba(255, 182, 193, 0.6)',
        }}
      />
      <div
        className="absolute w-1 h-1 bg-pink-200 rounded-full animate-sparkle-delay-2"
        style={{
          left: '75%',
          top: '50%',
          boxShadow: '0 0 3px 1px rgba(255, 182, 193, 0.6)',
        }}
      />
    </>
  );

  // Rank 4: Orange heat wave
  const Rank4Effect = () => (
    <>
      {/* Heat wave pulse */}
      <div className="absolute inset-0 bg-gradient-to-r from-orange-400/30 via-orange-300/50 to-orange-400/30 animate-pulse-glow" />
      {/* Small glowing embers */}
      <div
        className="absolute w-1.5 h-1.5 rounded-full bg-orange-200 animate-sparkle"
        style={{
          left: '35%',
          top: '45%',
          boxShadow: '0 0 4px 1px rgba(255, 165, 0, 0.6)',
        }}
      />
      <div
        className="absolute w-1.5 h-1.5 rounded-full bg-orange-200 animate-sparkle-delay-1"
        style={{
          left: '60%',
          top: '45%',
          boxShadow: '0 0 4px 1px rgba(255, 165, 0, 0.6)',
        }}
      />
    </>
  );

  // Rank 5: Emerald soft pulse
  const Rank5Effect = () => (
    <>
      {/* Gentle emerald pulse */}
      <div className="absolute inset-0 bg-gradient-to-r from-emerald-400/30 via-green-300/50 to-emerald-400/30 animate-pulse-glow" />
      {/* Thin ring pulse */}
      <div className="absolute inset-0 border border-emerald-200/60 rounded-sm animate-pulse-ring" />
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

  // Get bar color based on rank (base fill)
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

  // Get animated gradient class based on rank (overlay)
  const getAnimatedGradientForRank = (rank: number) => {
    switch (rank) {
      case 1: return 'animated-gradient gradient-gold';
      case 2: return 'animated-gradient gradient-cyan';
      case 3: return 'animated-gradient gradient-purple';
      case 4: return 'animated-gradient gradient-orange';
      case 5: return 'animated-gradient gradient-emerald';
      default: return '';
    }
  };

  // Get border pulse class based on rank
  const getPulseClassForRank = (rank: number) => {
    switch (rank) {
      case 1: return 'bar-pulse-gold';
      case 2: return 'bar-pulse-cyan';
      case 3: return 'bar-pulse-purple';
      case 4: return 'bar-pulse-orange';
      case 5: return 'bar-pulse-emerald';
      default: return '';
    }
  };

  // Get sparkler color based on rank
  const getSparklerColor = (rank: number) => {
    switch (rank) {
      case 1: return 'spark-gold';
      case 2: return 'spark-cyan';
      case 3: return 'spark-purple';
      case 4: return 'spark-orange';
      case 5: return 'spark-emerald';
      default: return 'spark-gold';
    }
  };

  // Sparkler component
  const Sparkler = ({ color }: { color: string }) => (
    <div className="absolute" style={{ right: '0', top: '50%', pointerEvents: 'none', transform: 'translateY(-50%)' }}>
      {[1, 2, 3, 4, 5, 6].map((i) => (
        <div key={i} className={`spark spark-${i} ${color}`} />
      ))}
    </div>
  );

  return (
    <div className="space-y-1">
      {data.map((item, index) => {
        const isTop5 = item.rank <= 5;
        const widthPercentage = (item.percentage / maxPercentage) * 100;

        return (
          <motion.div
            key={`${metric}-${item.symbol}`}
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
                item.rank === 1 ? 'text-yellow-400' :
                item.rank === 2 ? 'text-cyan-400' :
                item.rank === 3 ? 'text-purple-400' :
                item.rank === 4 ? 'text-orange-400' :
                item.rank === 5 ? 'text-emerald-400' :
                'text-gray-600'
              }`}>
                {item.rank}
              </span>

              {/* Symbol */}
              <span className={`w-12 ${
                isTop5 ? 'text-white' : 'text-gray-400'
              }`}>
                {item.symbol}
              </span>

              {/* Bar Container */}
              <div className="flex-1 relative h-5 bg-transparent overflow-visible">
                {/* Background track - full width dark bar */}
                <div className="absolute inset-0 bg-gray-900/40 rounded-sm" />
                
                {/* Bar */}
                <div
                  className={`absolute left-0 top-0 h-full rounded-sm overflow-visible ${
                    isTop5 
                      ? `${getBarColorForRank(item.rank)} ${getPulseClassForRank(item.rank)}`
                      : 'bg-yellow-500/70'
                  }`}
                  style={{ width: `${widthPercentage}%` }}
                >
                  {/* Animated gradient sweep overlay for top 5 */}
                  {isTop5 && (
                    <div
                      className={`absolute inset-0 opacity-70 pointer-events-none ${getAnimatedGradientForRank(item.rank)}`}
                    />
                  )}

                  {/* Unique effect for each top 5 rank */}
                  {isTop5 && getEffectForRank(item.rank)}
                  
                  {/* Sparkler at end of bar for top 5 */}
                  {isTop5 && <Sparkler color={getSparklerColor(item.rank)} />}

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
                </div>
              </div>

              {/* Percentage */}
              <motion.span
                className={`w-14 text-right ${
                  item.rank === 1 ? 'text-yellow-400' :
                  item.rank === 2 ? 'text-cyan-400' :
                  item.rank === 3 ? 'text-purple-400' :
                  item.rank === 4 ? 'text-orange-400' :
                  item.rank === 5 ? 'text-emerald-400' :
                  'text-gray-500'
                }`}
                animate={{
                  scale: hoveredIndex === index ? 1.1 : 1,
                }}
              >
                {item.percentage.toFixed(2)}%
              </motion.span>
            </div>

            {/* Tooltip on hover */}
            {hoveredIndex === index && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: 10 }}
                className={`absolute left-20 top-6 bg-gray-800 border px-2 py-1 rounded text-xs z-20 whitespace-nowrap pointer-events-none ${
                  item.rank === 1 ? 'border-yellow-400' :
                  item.rank === 2 ? 'border-cyan-400' :
                  item.rank === 3 ? 'border-purple-400' :
                  item.rank === 4 ? 'border-orange-400' :
                  item.rank === 5 ? 'border-emerald-400' :
                  'border-yellow-400'
                }`}
              >
                <div className={
                  item.rank === 1 ? 'text-yellow-400' :
                  item.rank === 2 ? 'text-cyan-400' :
                  item.rank === 3 ? 'text-purple-400' :
                  item.rank === 4 ? 'text-orange-400' :
                  item.rank === 5 ? 'text-emerald-400' :
                  'text-yellow-400'
                }>#{item.rank} {item.symbol}</div>
                <div className="text-gray-300">{item.percentage.toFixed(2)}% dominance</div>
                {isTop5 && (
                  <div className={`text-xs mt-0.5 ${
                    item.rank === 1 ? 'text-yellow-300' :
                    item.rank === 2 ? 'text-cyan-300' :
                    item.rank === 3 ? 'text-purple-300' :
                    item.rank === 4 ? 'text-orange-300' :
                    item.rank === 5 ? 'text-emerald-300' :
                    'text-yellow-300'
                  }`}>
                    {item.rank === 1 && '👑 #1 Golden!'}
                    {item.rank === 2 && '⚡ #2 Electric!'}
                    {item.rank === 3 && '💫 #3 Shimmering!'}
                    {item.rank === 4 && '🔥 #4 Heat Wave!'}
                    {item.rank === 5 && '💚 #5 Pulsing!'}
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