/**
 * Bharat Mode official brand colors — confirmed 22 Nov 2026.
 * Never use the hero saffron for small text on ivory; use saffronText.
 * Graphite Navy is neutral text, Ocean Teal is an accent, and
 * Deep Charcoal is the dramatically darker alternate background.
 */
export const BRAND = {
  name: 'BHARAT MODE',
  tagline: 'BIG IDEAS. REAL PROGRESS.',
  primary: '#E8752E',       // Classic Saffron — hero accent
  ivory: '#FFF7EB',         // Warm Ivory — light canvas
  teal: '#117A7A',          // Ocean Teal — secondary data accent
  graphite: '#283039',      // Graphite Navy — neutral dark text
  charcoal: '#0B1018',      // Deep Charcoal — cinematic dark canvas

  // Accessible support tones, not replacement brand primaries.
  saffronText: '#A63F17',
  saffronOnDark: '#FFBE91',
  tealOnDark: '#70D3CC',
  tealSoft: '#E0F0EC',
  peach: '#FFE3CC',
  muted: '#585F66',
  ivorySurface: '#FFFCF6'
};

export const THEME_NAMES = ['ivory', 'midnight', 'saffron'];

export const THEMES = {
  ivory: {
    bg: BRAND.ivory,
    text: BRAND.graphite,
    muted: BRAND.muted,
    accent: BRAND.primary,
    accentText: BRAND.saffronText,
    dataColor: BRAND.saffronText,
    teal: BRAND.teal,
    surface: BRAND.ivorySurface,
    soft: BRAND.peach,
    border: '#EAD6C2',
    glow: BRAND.tealSoft
  },
  midnight: {
    bg: BRAND.charcoal,
    text: BRAND.ivory,
    muted: '#C7D1D6',
    accent: BRAND.primary,
    accentText: BRAND.saffronOnDark,
    dataColor: BRAND.saffronOnDark,
    teal: BRAND.tealOnDark,
    surface: '#1A232E',
    soft: '#302A2A',
    border: '#47454A',
    glow: '#1A373A'
  },
  saffron: {
    bg: BRAND.primary,
    text: BRAND.charcoal,
    muted: BRAND.graphite,
    accent: BRAND.charcoal,
    accentText: BRAND.charcoal,
    dataColor: BRAND.charcoal,
    teal: '#0E585A',
    surface: BRAND.ivory,
    soft: '#FFD1AD',
    border: '#A85423',
    glow: '#F8B77D'
  }
};

export const getTheme = (name) => THEMES[name] || THEMES.ivory;
