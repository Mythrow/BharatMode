/** Approved artwork supplied by the channel owner.
 * These are exact, self-contained SVG assets stored in public/brand.
 * Do NOT recreate, recolor or substitute draft logo paths.
 */
import React from 'react';
import {Img, staticFile} from 'remotion';

export const BrandAvatar=({size=76,style={}})=>(
  <Img
    src={staticFile('brand/bharat-mode-avatar.svg')}
    style={{width:size,height:size,objectFit:'contain',flexShrink:0,...style}}
  />
);
export const BrandBadge=({width=860,style={}})=>(
  <Img
    src={staticFile('brand/bharat-mode-badge.svg')}
    style={{width,height:'auto',objectFit:'contain',maxWidth:'100%',...style}}
  />
);
