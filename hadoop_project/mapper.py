#!/usr/bin/env python3
"""Task 6"""
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(sep=',')

    print('{}\t{},{}'.format(words[0], words[1], words[3]))
