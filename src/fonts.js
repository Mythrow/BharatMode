// Shared Google Fonts for Remotion. Do not commit font binaries.
// License: OFL 1.1; see docs/BRAND.md.
import {loadFont as loadBricolage} from '@remotion/google-fonts/BricolageGrotesque';
import {loadFont as loadManrope} from '@remotion/google-fonts/Manrope';

const display = loadBricolage('normal', {
  weights: ['400', '600', '700', '800'],
  subsets: ['latin']
});
const reading = loadManrope('normal', {
  weights: ['400', '500', '600', '700', '800'],
  subsets: ['latin']
});
export const DISPLAY_FONT = display.fontFamily;
export const BODY_FONT = reading.fontFamily;
export const waitForFonts = async () => {
  await Promise.all([display.waitUntilDone(), reading.waitUntilDone()]);
};
