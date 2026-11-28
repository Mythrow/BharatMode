#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p segments
cd src
python build_v5.py 990 1480 ../segments/map.mp4 >../segments/map.log 2>&1 & a=$!
python build_v5.py 1980 2470 ../segments/industry.mp4 >../segments/industry.log 2>&1 & b=$!
wait $a; wait $b
cd ..
base=${1:-/mnt/data/BM-007-narrated-preview-V5.mp4}
ffmpeg -v error -y -i "$base" -map 0:v -an -t 16.5 -c copy segments/pre.mp4
ffmpeg -v error -y -ss 24.666667 -i "$base" -map 0:v -an -t 8.333333 -c copy segments/mid.mp4
ffmpeg -v error -y -ss 41.166667 -i "$base" -map 0:v -an -c copy segments/post.mp4
for f in pre map mid industry post; do echo "file '$PWD/segments/$f.mp4'";done > segments/concat.txt
ffmpeg -v error -y -f concat -safe 0 -i segments/concat.txt -i "$base" -map 0:v:0 -map 1:a:0 -c copy -movflags +faststart /mnt/data/BM-007-narrated-preview-V7.mp4
touch done
