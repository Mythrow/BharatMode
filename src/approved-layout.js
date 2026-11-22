/**
 * Bharat Mode approved Shorts frame geometry (owner approved 23 Nov 2026).
 * These pure numbers are safe to import in tests and in Remotion.
 * Visual approval does not imply audio/TTS/render quality certification.
 */
export const SHORTS_WIDTH=1080;
export const SHORTS_HEIGHT=1920;
export const SHORTS_FPS=30;
/** Symmetric chapter-bar inset: (1080-2*84)=912px total width; x-center 540px. */
export const APPROVED_PROGRESS_GUTTER=84;
export const APPROVED_PROGRESS_BOTTOM=250;
export const APPROVED_PROGRESS_HEIGHT=13;
export const APPROVED_PROGRESS_GAP=14;
export const approvedProgressBounds=(width=SHORTS_WIDTH,inset=APPROVED_PROGRESS_GUTTER)=>({
  left:inset,
  right:inset,
  width:Math.max(0,width-2*inset),
  center:width/2,
});
