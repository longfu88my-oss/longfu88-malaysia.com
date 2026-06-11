/** @type {import('tailwindcss').Config} */
// Longfu88 Malaysia — design tokens straight from the brand CI (CLAUDE.md §3).
// Colours are exposed as `brand-*` tokens so they are never hard-coded ad hoc.
module.exports = {
  content: ['./**/*.html', './author/**/*.html'],
  theme: {
    // Sharp, bold aesthetic — 0px radius everywhere (CLAUDE.md §3).
    borderRadius: {
      none: '0px',
      DEFAULT: '0px',
    },
    extend: {
      colors: {
        brand: {
          bg: '#FFFFFF',
          primary: '#C70028',   // brand red — primary CTAs, key accents
          secondary: '#9F0020', // darker red — hover/active, depth
          accent: '#EB002F',    // bright red — highlights
          link: '#EB002F',
          text: '#635B5B',      // body copy — warm grey
        },
      },
      fontFamily: {
        // Headings AND body both use Sofia Sans.
        sans: ['"Sofia Sans"', 'system-ui', 'sans-serif'],
      },
      fontSize: {
        // Brand baseline: H1/H2 28px, body 14px.
        body: ['14px', { lineHeight: '1.7' }],
        h1: ['28px', { lineHeight: '1.2', fontWeight: '800' }],
        h2: ['28px', { lineHeight: '1.25', fontWeight: '700' }],
      },
    },
  },
  plugins: [],
}
