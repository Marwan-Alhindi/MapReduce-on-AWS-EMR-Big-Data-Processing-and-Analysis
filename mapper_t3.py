#!/usr/bin/env python3
import sys

# Read the task type ("join" or "count") from command line arguments
task = sys.argv[1]

# If the task is to join the two tables
if task == "join":
    # Read each line from standard input
    for line in sys.stdin:
        line = line.strip()  # Remove leading and trailing whitespaces
        fields = line.split(",")  # Split the line by commas into a list
        
        # If the line has 4 fields, it comes from Taxis.txt
        if len(fields) == 4: # if line has 4 fields, then its from Taxis.txt
            # Output the taxi ID, a flag "T" to indicate the source table, and the company name
            print(f"{fields[0]}\tT\t{fields[1]}")
        
        # If the line has 8 fields, it comes from Trips.txt
        elif len(fields) == 8:
            # Output the taxi ID, a flag "R" to indicate the source table, and the trip ID
            print(f"{fields[1]}\tR\t{fields[0]}")
            
# If the task is to count the number of trips for each company
elif task == "count":
    # Read each line from standard input
    for line in sys.stdin:
        line = line.strip()  # Remove leading and trailing whitespaces
        company, trip = line.split("\t")  # Split the line by tab into company and trip
        # Output the company and a count of 1
        print(f"{company}\t1")
