#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
  line = lines[i]
  line = line.strip()
  output = line[1:len(line) - 1]
  if len(output) > 0:
    print(output)
  i += 1
