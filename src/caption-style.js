// Owner-requested post-BM-0003 refinement. Native 1080px canvas units.
// Pure alpha backing: no sampled backdrop, blur, shadow, or colored tint.
export const CAPTION_RADIUS=24;
export const captionBacking=theme=>theme==='ivory'?'rgba(11,16,24,.10)':theme==='midnight'?'rgba(11,16,24,.30)':'rgba(11,16,24,.18)';
export const captionSurfaceStyle=theme=>({borderRadius:CAPTION_RADIUS,background:captionBacking(theme),boxShadow:'none',backdropFilter:'none'});
export const captionInkStyle=Object.freeze({textShadow:'none'});
