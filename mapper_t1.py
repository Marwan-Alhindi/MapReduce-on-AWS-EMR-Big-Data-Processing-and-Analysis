#!/usr/bin/env python3

import sys

for line in sys.stdin: # reading from standard input Tripx.txt
    line = line.strip()
    if line: # if line is not empty
        trip, taxi, fare, distance, _, _, _, _ = line.split(',') # picking taxi and distance

        # Skip the header line
        if trip == "Trip#":
            continue

        # Emit the taxi ID, distance, and count (which is always 1)
        print(f"{taxi}\t{float(distance)},{1}")

# output example:
#taxi1    3.4,1
#taxi2    5.6,1
#taxi1    2.1,1