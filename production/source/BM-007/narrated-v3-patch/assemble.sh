#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
BASE="${1:-/mnt/data/bm007_narrated_v2/BM-007-narrated-preview-V2.mp4}"
mkdir -p segments
ffmpeg -v error -y -i "$BASE" -map 0:v:0 -an -t 32 -c copy segments/00.mp4
cd src
python patch.py 1920 2180 ../segments/01.mp4 >../segments/01.log 2>&1 & a=$!
python patch.py 2180 2440 ../segments/02.mp4 >../segments/02.log 2>&1 & b=$!
python patch.py 2440 2700 ../segments/03.mp4 >../segments/03.log 2>&1 & c=$!
python patch.py 2700 2960 ../segments/04.mp4 >../segments/04.log 2>&1 & d=$!
wait $a;wait $b;wait $c;wait $d
cd ..
for f in segments/0[0-4].mp4; do echo "file '$PWD/$f'"; done > segments/concat.txt
ffmpeg -v error -y -f concat -safe 0 -i segments/concat.txt -i "$BASE" -map 0:v:0 -map 1:a:0 -c copy -movflags +faststart /mnt/data/BM-007-narrated-preview-V3.mp4
printf 'done\n' > render.done
