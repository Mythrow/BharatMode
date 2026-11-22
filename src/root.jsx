import React from 'react';
import {Composition, Still} from 'remotion';
import {BharatShort} from './short.jsx';
import {BharatThumbnail} from './thumbnail.jsx';
import example from '../stories/param-rudra.json';
import {BharatProofIvory,BharatProofDark,BharatProofSaffron} from './style-proofs.jsx';

const FPS = 30;
export const Root = () => <>
  <Still id="BharatProofIvory" component={BharatProofIvory} width={1080} height={1920} />
  <Still id="BharatProofDark" component={BharatProofDark} width={1080} height={1920} />
  <Still id="BharatProofSaffron" component={BharatProofSaffron} width={1080} height={1920} />
  <Composition
    id="BharatShort"
    component={BharatShort}
    fps={FPS}
    width={1080}
    height={1920}
    durationInFrames={48 * FPS}
    defaultProps={example}
    calculateMetadata={({props}) => ({
      durationInFrames: Math.max(FPS, Math.round(
        (props.story?.scenes || []).reduce((sum, scene) => sum + scene.duration, 0) * FPS
      ))
    })}
  />
  <Still
    id="BharatThumbnail"
    component={BharatThumbnail}
    width={1080}
    height={1920}
    defaultProps={example}
  />
</>;
