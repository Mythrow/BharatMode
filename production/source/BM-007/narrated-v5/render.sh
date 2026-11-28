#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/src"
python build_v5.py 0 740 ../segments/00.mp4 >../segments/00.log 2>&1 & a=$!
python build_v5.py 740 1480 ../segments/01.mp4 >../segments/01.log 2>&1 & b=$!
python build_v5.py 1480 2220 ../segments/02.mp4 >../segments/02.log 2>&1 & c=$!
python build_v5.py 2220 2960 ../segments/03.mp4 >../segments/03.log 2>&1 & d=$!
wait $a;wait $b;wait $c;wait $d
cd ..
for f in segments/0[0-3].mp4;do echo "file '$PWD/$f'";done > segments/concat.txt
ffmpeg -v error -y -f concat -safe 0 -i segments/concat.txt -i /mnt/data/BM-007-narrated-preview-V3.mp4 -map 0:v:0 -map 1:a:0 -c copy -movflags +faststart /mnt/data/BM-007-narrated-preview-V5.mp4
printf 'done\n' > render.done
