/**
 * Bharat Mode design tokens — saffron primary, warm ivory, deep teal.
 * Selected direction, v1 proposed values; review export readability before freeze.
 * Pastels are surfaces only: never put pale saffron as small text on ivory.
 */
export const BRAND = {
  name: 'BHARAT MODE',
  tagline: 'BIG IDEAS. REAL PROGRESS.',
  primary: '#E8752E',
  saffronText: '#A63F17',
  ivory: '#FFF7EB',
  teal: '#117A7A',
  tealSoft: '#E0F0EC',
  ink: '#183139',
  muted: '#57686D',
  peach: '#FFE3CC',
  white: '#FFFFFF',
  dark: '#183139'
};
export const THEME_NAMES = ['ivory', 'midnight', 'saffron'];
export const THEMES = {
  ivory: {
    bg: BRAND.ivory, ink: BRAND.ink, muted: BRAND.muted,
    accent: BRAND.primary, accentText: BRAND.saffronText, dataColor: BRAND.saffronText,
    teal: BRAND.teal, surface: '#FFFFFF', soft: BRAND.peach,
    border: '#F0D5BF', glow: BRAND.tealSoft
  },
  midnight: {
    bg: BRAND.ink, ink: BRAND.ivory, muted: '#BFD3D0',
    accent: '#F4A767', accentText: '#F4A767', dataColor: '#F4A767',
    teal: '#81D5C9', surface: '#264951', soft: '#385660',
    border: '#46646B', glow: '#244C51'
  },
  saffron: {
    bg: BRAND.primary, ink: BRAND.ink, muted: '#3E4645',
    accent: BRAND.ink, accentText: BRAND.ink, dataColor: BRAND.ink,
    teal: '#17595E', surface: BRAND.ivory, soft: '#F8C69D',
    border: '#BE5922', glow: '#F4B57F'
  }
};
export const getTheme = (name) => THEMES[name] || THEMES.ivory;
