### Revision 3 review delivery recovered — 24 November 2026

- The previous V3 encoded file was unavailable, so the main chat **reproduced** the V3 map/identity/camera revision from checksum-verified V2 (SHA-256 `6e4018988a67254b3db2273309c69dea5830c40be992489e37176b3a81448290`), committed Natural Earth geometry and the V3 rendering logic, including the documented L&T/NVIDIA marks. No Work video task and no new narration.
- New private output: `BM-0003-naturalearth-v3-rebuilt.mp4`. SHA-256 `60048b3db32c6e239d7dbbd4e1c32c8329088d662f835a2ff92c8865076f93a4`; **this is a fresh encode, not byte-identical to the earlier V3 video**. H.264/AAC, 1080×1920, 30fps, 1245 frames, 41.5s. Full decode passed. Natural Earth Chennai point lies within the stored Tamil Nadu polygon; inspected representative map frames.
- Audio codec-stream SHA-256 `f49909f808dd934d776df18cb481662d4888c1bee96ab23ba2bee2bc92991b9b` matches the original/V2/V3 record. Qwen voice and MUSIC-06 Option B unchanged.
- **Both actual review files now saved privately in ChatGPT Library /BharatMode/**: the rebuilt MP4 and self-contained `BM-0003-naturalearth-v3-review.html` with embedded video and six scene controls. Verified embedded bytes equal the rebuilt MP4. Delivered in chat. Neither file is committed to Git.
- **Next: owner visual review, then phone QA.** Do not reopen audio or map-tool approval. No publishing.

# Bharat Mode — Approved Maps and Camera Motion

**Approved by owner: 23 November 2026.** Use **Natural Earth** geographic data plus the approved **Remotion/V6** template for accurate, repeatable map animations. No paid Google Earth Studio, Cesium terrain provider, GEOlayers or subscriber map tiles are necessary for this BM-0003 country/state/city explanation.

## Geographic data, not generated map shapes

- **Natural Earth 1:10m Admin-0 Countries: India POV.** The viewer sees the Natural Earth India point-of-view country boundary, which avoids silently substituting the global de-facto display for this India-focused story. Official source: [Natural Earth 10m cultural vectors](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/) · [India POV GeoJSON](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_10m_admin_0_countries_ind.geojson), original Git blob `852f3fdf92c01811d433e258b1475179184bd9b0`.
- **Natural Earth 1:10m Admin-1 States, Provinces.** Tamil Nadu, Andhra Pradesh, Karnataka, Kerala outlines are sourced from [Natural Earth Admin-1](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_10m_admin_1_states_provinces.geojson), Git blob `4a8438f98ac7dfec7dc1739b1eaf91398ad33f22`. These are map features, not artistic drawings.
- **Chennai city center:** from [Natural Earth populated places (10m)](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_10m_populated_places_simple.geojson), Git blob `4da9c6b27b5cd41d7c930ea9cd0c1f84548b65fb`: **80.278053° E, 13.091934° N**. A city-center marker is **NOT** claimed as the L&T Vyoma campus location.
- **Stored derived vector data:** [data/maps/naturalearth-bm0003.json](../data/maps/naturalearth-bm0003.json), Ramer–Douglas–Peucker simplification of the selected largest outer rings to fit mobile display (country tolerance ~0.14°, Tamil Nadu ~0.07°, neighbors ~0.11°), encoded as longitude/latitude polyline at 1e−4° resolution. This simplifies small coastal features and offshore islands; **not suitable for surveying, navigation, legal borders or cadastral use**. Record exact project source files and simplification in provenance.
- Natural Earth vector data is **public domain**: [Natural Earth home](https://www.naturalearthdata.com/). No tile subscriptions or paid mapping APIs required. Political-border representation and any distribution should be independently checked against applicable local mapping requirements; Natural Earth's India POV does not amount to legal certification of disputed border claims.

## Approved on-screen animation

**Story-specific BM-0003 shot:** in a 9:16 frame, reveal the Indian subcontinent, move the virtual camera south, highlight the actual Tamil Nadu polygon in classic saffron, then dolly toward the actual Chennai city coordinate. Pin pulses; show **"Chennai, Tamil Nadu"**. Overlay verified organization labels **L&T → Vyoma.AI → LTN Compute** and NVIDIA B300 technology identification. Never invent an exact site pin; the filing describes the Chennai campus without coordinates. Do not label all planned GPUs as already installed.

The map is a **story graphic/hero** beneath the locked V6 title and center-word-follow captions. Retain the original Bharat Mode avatar, topic pill, perfectly centered chapter bars, 0.34s quiet scene dissolve, typography and palette. No persistent map source/date footer; full dataset attributions live in the description/documentation.

### Animated/coded implementation

- **Reusable Remotion map component:** [src/natural-earth-map.jsx](../src/natural-earth-map.jsx) uses [src/natural-earth-geo.mjs](../src/natural-earth-geo.mjs), actual encoded map boundaries, geographic camera position and cinematic interpolated zoom. Wired into BM-0003 Remotion pilot only for its Chennai beat; approved V6 chrome remains untouched.
- **Actual current in-chat video:** [scripts/render_bm0003_map_v3.py](../scripts/render_bm0003_map_v3.py) uses Python OpenCV + FFmpeg to apply the same geographic data and virtual camera to the historical 41.5s Revision 2 cut, preserving the existing AAC audio bitstream byte-for-byte. This is a **visual iteration bridge**, not a claim that the V3 MP4 was encoded by Remotion. Full future videos are to be composed from **audio-only Work outputs in this main conversation**, preferably using the supplied Remotion component and approved V6 renderer.
- **Test:** `node scripts/test-natural-earth.mjs` checks geometries, India overview, Chennai point containment in Tamil Nadu, camera behavior and SVG path generation. Local test PASSED (23 Nov 2026).
- **Verified V3 technical output (private, not in public Git):** `BM-0003-naturalearth-v3.mp4`; **41.5 seconds, 1245 frames, 1080×1920, 30fps, H.264/AAC**, SHA-256 `6aa5cb03e4448819dae65f04fa669fb1233c269a137d93d6bee1291f62224f9e`. Audio codec-stream SHA-256 is identical before/after `f49909f808dd934d776df18cb481662d4888c1bee96ab23ba2bee2bc92991b9b` (voice/music Option B unchanged).
- **Company marks:** L&T symbol in the private review was sourced from [TradingView icon archived by Shareperks](https://github.com/shareperks/indian-listed-company-logos/blob/main/nse/NSE_LT.svg); NVIDIA mark from [Simple Icons NVIDIA](https://github.com/simple-icons/simple-icons/blob/develop/icons/nvidia.svg). Vyoma.AI and LTN Compute are exact name labels, **not invented official logos**. Marks shown for editorial identification only, not endorsement. Do not check third-party symbol master files into public Git without redistribution rights.
- **Private visuals:** The MP4 and self-contained HTML review are private ChatGPT artifacts. Original server racks, GPU illustrations and network imagery are **schematic CGI**, never described as the real L&T Chennai site.

## Production responsibility / approval

Work Mode: **only Qwen audio + spoken transcript QA + word-timing alignment**. Main ChatGPT conversation: **all graphics, map animation, music placement, editing and MP4 rendering**. Source: [Production Responsibilities](PRODUCTION_RESPONSIBILITIES.md).

**Status:** map/tool choice APPROVED; V3 actual video generated here for owner review. **Not yet approved for publication**, and genuine Remotion end-to-end production from Work-supplied audio remains a follow-up.
