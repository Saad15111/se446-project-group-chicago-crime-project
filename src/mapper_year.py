#!/usr/bin/env python3
import sys
import csv
import io

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    reader = csv.reader(io.StringIO(line))
    for fields in reader:
        if len(fields) < 3:
            continue
        if fields[0].strip() == "ID":
            continue
        date_str = fields[2].strip()
        try:
            date_part = date_str.split()[0]
            segments = date_part.split("/")
            yr = segments[2]
            print("{0}\t{1}".format(yr, 1))
        except IndexError:
            continue
