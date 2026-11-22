import React from 'react';
import {Composition, Still} from 'remotion';
import {BharatShort} from './short.jsx';
import {BharatThumbnail} from './thumbnail.jsx';
import {BharatMotionPreview} from './motion-preview.jsx';
import {BharatMotionPreviewV2} from './motion-v2.jsx';
import {BharatMotionPreviewV3} from './motion-v3.jsx';
import {BharatMotionPreviewV4} from './motion-v4.jsx';
import {BharatMotionPreviewV5} from './motion-v5.jsx';
import {BharatMotionPreviewV6} from './motion-v6.jsx';
import example from '../stories/param-rudra.json';
import {BharatProofIvory,BharatProofDark,BharatProofSaffron} from './style-proofs.jsx';

const FPS = 30;
export const Root = () => <>
  <Composition id="BharatMotionPreviewV6" component={BharatMotionPreviewV6}
    fps={30} width={1080} height={1920} durationInFrames={480}/>
  <Composition id="BharatMotionPreviewV5" component={BharatMotionPreviewV5}
    fps={30} width={1080} height={1920} durationInFrames={480}/>
  <Composition id="BharatMotionPreviewV4" component={BharatMotionPreviewV4}
    fps={30} width={1080} height={1920} durationInFrames={480}/>
  <Composition id="BharatMotionPreviewV3" component={BharatMotionPreviewV3}
    fps={30} width={1080} height={1920} durationInFrames={480}/>
  <Composition id="BharatMotionPreviewV2" component={BharatMotionPreviewV2} fps={30}
    width={1080} height={1920} durationInFrames={480} />
  <Composition id="BharatMotionPreview" component={BharatMotionPreview} fps={30}
    width={1080} height={1920} durationInFrames={420} />
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
