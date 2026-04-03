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
        if len(fields) < 8:
            continue
        if fields[0].strip() == "ID":
            continue
        place = fields[7].strip()
        if place != "":
            print("{0}\t{1}".format(place, 1))
