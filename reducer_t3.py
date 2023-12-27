#!/usr/bin/env python3
import sys

# Read the task type ("join" or "count") from command line arguments
task = sys.argv[1]

# If the task is to join the two tables
if task == "join":
    current_taxi = None
    current_company = None

    # Read each line from standard input
    for line in sys.stdin: # read from mapper.py output print(f"{fields[0]}\tT\t{fields[1]}") or print(f"{fields[1]}\tR\t{fields[0]}")
        line = line.strip()  # Remove leading and trailing whitespaces
        taxi, flag, info = line.split("\t")  # Split the line by tab

        # If the current taxi is the same as the previous, and the flag indicates a trip ("R")
        if current_taxi == taxi:
            if flag == "R":
                # Output the company and the trip ID
                print(f"{current_company}\t{info}")
        else:
            if flag == "T":
                current_company = info  # Update the current company if the flag is "T"
            current_taxi = taxi  # Update the current taxi ID
            
# If the task is to count the number of trips for each company
elif task == "count":
    current_company = None
    current_count = 0

    # Read each line from standard input
    for line in sys.stdin:  # reading print(f"{company}\t1")
        line = line.strip()  # Remove leading and trailing whitespaces
        company, count = line.split("\t")  # Split the line by tab
        count = int(count)  # Convert the count to integer
        
        # If the current company is the same as the previous
        if current_company == company:
            current_count += count  # Add to the current count
        else:
            # If there was a previous company, output its total count
            if current_company:
                print(f"{current_company}\t{current_count}")
            current_count = count  # Reset the count for the new company
            current_company = company  # Update the current company

    # Output the total count for the last company
    if current_company:
        print(f"{current_company}\t{current_count}")
