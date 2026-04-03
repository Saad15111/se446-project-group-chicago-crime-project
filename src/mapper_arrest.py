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
        if len(fields) < 9:
            continue
        if fields[0].strip() == "ID":
            continue
        arrested = fields[8].strip().lower()
        if arrested == "true" or arrested == "false":
            print("{0}\t{1}".format(arrested, 1))
