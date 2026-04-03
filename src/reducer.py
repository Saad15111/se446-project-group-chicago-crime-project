#!/usr/bin/env python3
import sys

current_key = None
total = 0

for record in sys.stdin:
    record = record.strip()
    if not record:
        continue

    tokens = record.split('\t')
    if len(tokens) < 2:
        continue

    key = tokens[0]
    try:
        val = int(tokens[1])
    except ValueError:
        continue

    if key != current_key:
        if current_key is not None:
            print("{0}\t{1}".format(current_key, total))
        current_key = key
        total = val
    else:
        total += val

if current_key is not None:
    print("{0}\t{1}".format(current_key, total))
