#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p segments
python render_motion.py 0 480 segments/s1.mp4 >segments/s1.log 2>&1 & a=$!
python render_motion.py 1620 2280 segments/s4.mp4 >segments/s4.log 2>&1 & b=$!
python render_motion.py 2280 2820 segments/s5.mp4 >segments/s5.log 2>&1 & c=$!
wait "$a"; wait "$b"; wait "$c"
touch segments/ready
