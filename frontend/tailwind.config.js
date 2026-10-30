/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        aviation: {
          navy: "#0a192f",
          dark: "#0b1526",
          midnight: "#0f203c",
          surface: "#172a45",
          border: "#233554",
          card: "#112240",
          sky: "#38bdf8",
          cyan: "#00f0ff",
          cloud: "#e2e8f0",
          silver: "#94a3b8",
          amber: "#f59e0b",
          green: "#10b981",
          red: "#ef4444"
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      }
    },
  },
  plugins: [],
}
