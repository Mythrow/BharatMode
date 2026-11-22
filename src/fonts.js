// Bharat Mode confirmed fonts. Do not commit font binaries.
import {loadFont as loadSora} from '@remotion/google-fonts/Sora';
import {loadFont as loadManrope} from '@remotion/google-fonts/Manrope';
const display=loadSora('normal',{weights:['400','600','700','800'],subsets:['latin']});
const reading=loadManrope('normal',{weights:['400','500','600','700','800'],subsets:['latin']});
export const DISPLAY_FONT=display.fontFamily;
export const BODY_FONT=reading.fontFamily;
export const waitForFonts=async()=>Promise.all([display.waitUntilDone(),reading.waitUntilDone()]);
