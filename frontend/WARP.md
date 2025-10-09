# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

**CryptoBuzz** is a terminal-style React application for visualizing cryptocurrency social media metrics. The app displays interactive crypto social dominance charts, trending coins, topics, and social metrics in a dark terminal theme.

**Original Design**: Based on Figma design at https://www.figma.com/design/oQda0wWdX6ayFNtC9cTYqI/Interactive-Crypto-Metrics-Visualization

## Architecture

### Frontend Structure
- **Framework**: React 18.3 with TypeScript and Vite 6.3
- **Styling**: Tailwind CSS with custom terminal-style design system
- **UI Library**: Extensive Radix UI components with shadcn/ui patterns
- **Animation**: Motion (Framer Motion) for complex interactive animations
- **Build Tool**: Vite with SWC for fast compilation

### Key Components
- `HorizontalBarChart.tsx` - Reusable animated horizontal bar chart with 100 crypto rankings, special visual effects for top 5
- `TrendingCoins.tsx` - Top 5 trending coins with social volume and change indicators
- `TrendingTopics.tsx` - Trending social topics with hashtags and change percentages
- `SocialMetrics.tsx` - Fear & Greed index gauge and social volume metrics
- `App.tsx` - Main layout with header, time display, and responsive grid

### Design System
- **Theme**: Dark terminal aesthetic with yellow (#FBBF24) accent color
- **Typography**: Monospace font (`font-mono`)
- **Colors**: Terminal-inspired with grays, yellows, and status colors (green/red/cyan/orange/purple)
- **Layout**: CSS Grid with responsive `lg:grid-cols-[1fr_320px]` main layout

## Common Development Commands

### Development Server
```bash
cd frontend
npm run dev
```
- Starts Vite dev server on port 3000
- Opens browser automatically
- Hot reload enabled

### Build for Production
```bash
cd frontend
npm run build
```
- Outputs to `frontend/build` directory
- Uses ES2022+ target for modern browsers

### Install Dependencies
```bash
cd frontend
npm install
```

## Code Architecture Patterns

### State Management
- Uses React hooks (useState, useEffect) for local state
- Real-time clock updates every second in main App component
- No external state management library (Redux/Zustand)

### Animation Patterns
- Motion components for page transitions and micro-interactions
- Staggered animations with `delay: index * 0.1` for lists
- Special rank-based effects in HorizontalBarChart (gold shimmer, lightning, bubbles, etc.)
- Hover animations with `whileHover` for interactive elements

### Data Patterns
- Static mock data for demonstration (realistic crypto metrics)
- Percentage-based calculations for chart widths
- Different metric variations (Twitter, Reddit, Telegram, Discord, Overall)

### Responsive Design
- Mobile-first approach with `lg:` breakpoint for desktop
- Scrollable areas with custom scrollbars (`scrollbar-thin scrollbar-thumb-gray-800`)
- Flexible grid system adapting from single to two-column layout

## Special Features

### Interactive Chart Effects
- **Rank 1**: Golden shimmer with crown sparkles
- **Rank 2**: Electric lightning bolts with cyan colors  
- **Rank 3**: Rising bubbles with purple/pink gradients
- **Rank 4**: Bouncing coin particles with orange glow
- **Rank 5**: Pulse rings with emerald colors

### Terminal Aesthetics
- Header shows "CRYPTOBUZZTERMINAL" with live clock
- Monospace fonts throughout
- Gray-on-black color scheme with yellow accents
- Uppercase labels with wider tracking

## Important File Locations

- Main app entry: `frontend/src/App.tsx`
- Component library: `frontend/src/components/`
- UI primitives: `frontend/src/components/ui/` (shadcn/ui components)
- Styles: `frontend/src/index.css` (Tailwind + custom CSS variables)
- Build config: `frontend/vite.config.ts`
- Dependencies: `frontend/package.json`

## React Development Guidelines

When working with this codebase:
- Always use functional components with hooks (no class components)
- Use TypeScript for type safety
- Follow existing component patterns for consistency
- Use Tailwind classes for styling, avoid custom CSS
- Leverage Motion library for animations
- Maintain terminal aesthetic with existing color scheme