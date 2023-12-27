#!/usr/bin/env python3

import sys

# Initialize variables to track the current taxi and its total distance and trip count
current_taxi = None
total_distance = 0
trip_count = 0

for line in sys.stdin: # for every line in the input
    line = line.strip() # remove leading and trailing whitespaces
    if line: # if line is not empty
        taxi, values = line.split('\t') # split the line into taxi and values
        distance, count = map(float, values.split(',')) # split the values into distance and count

        if current_taxi == taxi: 
            # If the taxi hasn't changed, add the distance and count to the running total
            total_distance += distance
            trip_count += count
        else:
            # If the taxi has changed, emit the average distance for the previous taxi
            # This is OK, Because the MapReduce framework sorts and groups the output from the mappers before sending it to the reducers, you can be sure that you have seen all the records for current_taxi.
            if current_taxi: # if current_taxi is not empty
                # Calculate the average distance for the previous taxi
                avg_distance = total_distance / trip_count
                # Emit the previous taxi ID and its average distance and trip count
                print(f"{current_taxi}\t{trip_count},{avg_distance}")

            # Reset the running total and trip count for the new taxi
            current_taxi = taxi
            total_distance = distance
            trip_count = count

# The last taxi won't be emitted in the for loop, so emit it now
if current_taxi:
    avg_distance = total_distance / trip_count
    print(f"{current_taxi}\t{trip_count},{avg_distance}")
