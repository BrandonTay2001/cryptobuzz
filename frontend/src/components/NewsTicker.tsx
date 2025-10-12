import React, { useEffect, useMemo, useRef, useState } from 'react';
import { motion } from 'motion/react';

interface NewsTickerProps {
  headlines: string[];
  speed?: number; // pixels per second
  className?: string;
}

// Simple emoji pool for variety
const EMOJIS = ['🚀', '🔥', '💎', '🧠', '⚡️', '🌕', '📈', '📰', '💥', '✨', '📊', '💬', '🧱', '🛡️', '🎯'];

export function NewsTicker({ headlines, speed = 120, className }: NewsTickerProps) {
  // Pair each headline with a stable random emoji (per initial render)
  const items = useMemo(() => {
    return headlines.map((h, i) => ({
      text: h,
      emoji: EMOJIS[(Math.floor(Math.random() * EMOJIS.length) + i) % EMOJIS.length],
      key: `${i}-${h}`,
    }));
  }, [headlines]);

  // Measure the exact width of one full track so we can loop seamlessly
  const contentRef = useRef<HTMLDivElement | null>(null);
  const [contentWidth, setContentWidth] = useState(0);

  useEffect(() => {
    const measure = () => {
      if (!contentRef.current) return;
      const width = contentRef.current.scrollWidth;
      if (width !== contentWidth) setContentWidth(width);
    };

    // Measure after paint
    const raf = requestAnimationFrame(measure);
    // Re-measure on resize
    window.addEventListener('resize', measure);
    return () => {
      cancelAnimationFrame(raf);
      window.removeEventListener('resize', measure);
    };
  }, [items, contentWidth]);

  const duration = contentWidth > 0 ? contentWidth / speed : 1;

  return (
    <div className={`relative w-full overflow-hidden border-y border-gray-800 bg-black/60 mt-8 mb-0`}>
      {/* Gradient edges for nicer fade */}
      <div className="pointer-events-none absolute left-0 top-0 h-full w-16 bg-gradient-to-r from-black to-transparent z-10" />
      <div className="pointer-events-none absolute right-0 top-0 h-full w-16 bg-gradient-to-l from-black to-transparent z-10" />

      <div className="w-full">{/* full width without label offset */}
        <motion.div
          className="flex whitespace-nowrap py-1.5 text-sm will-change-transform"
          animate={contentWidth > 0 ? { x: [0, -contentWidth] } : undefined}
          transition={contentWidth > 0 ? { duration, repeat: Infinity, ease: 'linear' } : undefined}
        >
          {/* Track A: measured for exact width */}
          <div ref={contentRef} className="flex gap-8">
            {items.map((item) => (
              <div
                key={item.key}
                className="flex items-center gap-2 text-gray-200"
              >
                <span className="text-base">{item.emoji}</span>
                <span className="text-gray-400">•</span>
                <span className="text-yellow-400">{item.text}</span>
              </div>
            ))}
          </div>
          {/* Track B: placed immediately after A for seamless looping */}
          <div className="flex gap-8" aria-hidden>
            {items.map((item, idx) => (
              <div
                key={`${item.key}-dup-${idx}`}
                className="flex items-center gap-2 text-gray-200"
              >
                <span className="text-base">{item.emoji}</span>
                <span className="text-gray-400">•</span>
                <span className="text-yellow-400">{item.text}</span>
              </div>
            ))}
          </div>
        </motion.div>
      </div>
    </div>
  );
}