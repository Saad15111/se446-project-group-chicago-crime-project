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
        if len(fields) < 6:
            continue
        if fields[0].strip() == "ID":
            continue
        crime = fields[5].strip()
        if crime != "":
            print("{0}\t{1}".format(crime, 1))
