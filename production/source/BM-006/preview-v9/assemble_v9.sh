#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
old=${1:?Supply verified V8 MP4}; out=${2:?Supply V9 output path}
for pair in 's3a 206' 's3b 206' 's3c 205'; do
 set -- $pair
 test "$(ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of csv=p=0 segments/$1.mp4)" = "$2"
done
ffmpeg -v error -y -threads 3 -i "$old" -threads 2 -i segments/s3a.mp4 -threads 2 -i segments/s3b.mp4 -threads 2 -i segments/s3c.mp4 -filter_complex_threads 2 -filter_complex '[0:v]split=2[a0][b0];[a0]trim=end_frame=1056,setpts=PTS-STARTPTS[a];[b0]trim=start_frame=1673,setpts=PTS-STARTPTS[b];[1:v]setpts=PTS-STARTPTS[c];[2:v]setpts=PTS-STARTPTS[d];[3:v]setpts=PTS-STARTPTS[e];[a][c][d][e][b]concat=n=5:v=1:a=0,format=yuv420p[v]' -map '[v]' -map 0:a:0 -c:v libx264 -threads 4 -preset veryfast -crf 17 -pix_fmt yuv420p -r 60 -colorspace bt709 -color_primaries bt709 -color_trc bt709 -c:a copy -movflags +faststart "$out"
