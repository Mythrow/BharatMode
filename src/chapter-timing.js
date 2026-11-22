/**
 * Story-driven editorial chapters. A chapter may span any number of scenes.
 * Each story can declare its own boundaries using sceneStartIndex.
 * No fixed "hook/context/proof/impact/takeaway" structure is imposed.
 */
export const resolveStoryChapters = (story) => {
  const scenes=story?.scenes||[];
  if (!scenes.length) return [];
  const starts=[0];
  for (const scene of scenes) {
    starts.push(starts[starts.length-1]+Number(scene.duration||0));
  }
  const configured=Array.isArray(story.chapters)&&story.chapters.length
    ? story.chapters
    : scenes.map((scene,i)=>({
        id:'scene-'+i,
        title:scene.kicker||scene.kind||'Beat '+(i+1),
        sceneStartIndex:i
      }));
  return configured.map((chapter,i)=>({
    id:chapter.id||'chapter-'+i,
    title:chapter.title||chapter.id||'Chapter '+(i+1),
    startSec:starts[chapter.sceneStartIndex],
    endSec:i+1<configured.length
      ? starts[configured[i+1].sceneStartIndex]
      : starts[starts.length-1]
  }));
};
