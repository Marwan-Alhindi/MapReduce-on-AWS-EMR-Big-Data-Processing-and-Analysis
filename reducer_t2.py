#!/usr/bin/env python3
import sys
from math import sqrt

def calculateNewMedoids():
    """
    Calculate the new medoids for each cluster based on the input points.
    
    The function reads from standard input, expecting each line to contain a cluster index,
    and the x and y coordinates of a point, separated by tabs.
    
    The function prints the new medoid for each cluster to standard output.
    """
    
    current_cluster = None  # The cluster being currently processed.
    points = []  # List of points belonging to the current cluster.

    def updateMedoid():
        """
        Update the medoid of the current cluster.
        
        A medoid is defined as the point in the cluster which has the minimum sum of distances
        to all other points in the same cluster.
        """
        
        # Calculate the new medoid for the current cluster by finding the point that minimizes the sum of euclidean distances of all other points.
        new_medoid = min(points, key=lambda p: sum(sqrt((p[0] - px) ** 2 + (p[1] - py) ** 2) for px, py in points))
        
        # Print the new medoid.
        print(f"{new_medoid[0]}, {new_medoid[1]}")
        
    # Read each line from standard input.
    for line in sys.stdin: # this reads mapper.py output which is print("{}\t{}\t{}".format(index, pickup_x, pickup_y))
        
        # Split the line into elements.
        elements = line.strip().split('\t')
        
        # Skip lines with the wrong number of fields.
        if len(elements) != 3:
            print(f"Skipping line: Expected 3 fields, got {len(elements)}", file=sys.stderr)
            continue
        
        # Parse the cluster index and coordinates.
        cluster_index, x, y = elements
        x, y = float(x), float(y)
        
        # If this point belongs to the current cluster, add it to the list of points.
        if current_cluster == int(cluster_index):
            points.append([x, y])
        
        # If this is a new cluster, update the medoid for the old cluster and start a new list of points.
        else:
            if current_cluster is not None:
                updateMedoid()
                
            current_cluster = int(cluster_index)
            points = [[x, y]]

    # Update the medoid for the last cluster.
    if points:
        updateMedoid()
    else:
        print("AHA!!!!")

if __name__ == "__main__":
    calculateNewMedoids()
