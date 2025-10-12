import React from 'react';
import { Sun } from 'lucide-react';

interface HeaderProps {
  currentTime: string;
}

export function Header({ currentTime }: HeaderProps) {
  return (
    <header className="flex items-center justify-between">
      <h1 className="text-yellow-400 tracking-wider">CRYPTOBUZZ TERMINAL</h1>
      <div className="flex items-center gap-3">
        <span className="text-gray-400 text-sm">{currentTime}</span>
        <Sun className="w-4 h-4 text-gray-400" />
      </div>
    </header>
  );
}


