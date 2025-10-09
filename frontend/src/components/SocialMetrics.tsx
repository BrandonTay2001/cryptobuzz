import { motion } from 'motion/react';

export function SocialMetrics() {
  const fearGreedValue = 72;

  return (
    <div className="bg-gray-900/30 border border-gray-800 rounded p-3">
      <h2 className="text-yellow-400 mb-3 uppercase tracking-wider text-xs">
        Social Metrics
      </h2>
      
      {/* Fear & Greed Index */}
      <div className="mb-4">
        <div className="text-gray-500 text-xs mb-2 uppercase tracking-wider">
          Fear & Greed Index
        </div>
        
        {/* Gauge */}
        <div className="relative h-2 bg-gray-800 rounded-full overflow-hidden mb-2">
          <div className="absolute inset-0 flex">
            <div className="flex-1 bg-red-500" style={{ flexBasis: '33%' }} />
            <div className="flex-1 bg-yellow-500" style={{ flexBasis: '33%' }} />
            <div className="flex-1 bg-green-500" style={{ flexBasis: '34%' }} />
          </div>
          
          {/* Indicator */}
          <motion.div
            className="absolute top-1/2 -translate-y-1/2 w-1 h-4 bg-white rounded-full shadow-lg"
            initial={{ left: '0%' }}
            animate={{ left: `${fearGreedValue}%` }}
            transition={{ duration: 1, ease: 'easeOut' }}
          />
        </div>
        
        <div className="flex justify-between text-xs text-gray-600 mb-2">
          <span>Extreme Fear</span>
          <span>Greed</span>
          <span>Extreme Greed</span>
        </div>
        
        <motion.div
          className="text-center"
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.5, type: 'spring' }}
        >
          <div className="text-green-400">{fearGreedValue} (Greed)</div>
        </motion.div>
      </div>

      {/* Crypto Total Social Volume */}
      <div>
        <div className="text-gray-500 text-xs mb-2 uppercase tracking-wider">
          Crypto Total Social Volume
        </div>
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.7 }}
        >
          <div className="text-white mb-1">
            <motion.span
              animate={{ opacity: [1, 0.7, 1] }}
              transition={{ duration: 2, repeat: Infinity }}
            >
              1.2M
            </motion.span>{' '}
            <span className="text-gray-500 text-xs">mentions</span>
          </div>
          <div className="text-xs text-green-400">+5.8% vs last 24h</div>
        </motion.div>
      </div>
    </div>
  );
}
