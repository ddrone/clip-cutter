#!/usr/bin/env python3

command = 'ffmpeg -ss 05:05 -i IMG_6966.MOV -c:v libx264 -t 25 clip1.mov'

import sys
import subprocess

def to_seconds(ts):
  [minutes, seconds] = ts.split(':')
  total_seconds = int(minutes) * 60 + int(seconds)
  return total_seconds

def cut_via_ffmpeg(video, start_s, end_s, name):
  cmd = ['ffmpeg', '-ss', str(start_s), '-i', video, '-c:v', 'libx264', '-t', str(end_s - start_s), name]
  subprocess.call(cmd)


def main():
  [_, video, tss] = sys.argv
  with open(tss) as f:
    for i, line in enumerate(f):
      parts = line.split(' ')
      start = parts[0]
      end = parts[1]
      comment = '_' + parts[2].strip() if len(parts) > 2 else ''
      start_s = to_seconds(start)
      end_s = to_seconds(end)
      cut_via_ffmpeg(video, start_s, end_s, f'clip_{i}{comment}.mov')

if __name__ == "__main__":
  main()
