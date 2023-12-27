#!/usr/bin/env python3
import sys
from math import sqrt

def getCentroids(filepath):
    """
    Read the centroid coordinates from a file and return them as a list of lists.
    
    Parameters:
        filepath (str): The path of the file containing the centroids.

    Returns:
        centroids (list): List of centroids where each centroid is a list of its x and y coordinates.
    """
    centroids = []  # Initialize an empty list to hold the centroids.
    
    # Open the file in read mode.
    with open(filepath) as fp:
        for line in fp:
            cord = line.strip().split(', ')
            # Convert the coordinates from string to float and append to the list.
            centroids.append([float(cord[0]), float(cord[1])])
            
    return centroids

def createClusters(centroids):
    """
    Create clusters based on the distance from each point to the centroids.
    
    Parameters:
        centroids (list): List of centroids where each centroid is a list of its x and y coordinates.
    """
    
    # Iterate over each line from standard input.
    for line in sys.stdin: # this reads Trips.txt x,y coordinates - trips locations
        fields = line.strip().split(',')
        
        try:
            pickup_x = float(fields[4])  # X-coordinate
            pickup_y = float(fields[5])  # Y-coordinate
        except ValueError:
            # Skip the line if the coordinates are not valid numbers.
            continue
        
        min_dist = float("inf")  # Initialize minimum distance as infinity.
        index = -1  # Initialize the index for the closest centroid.
        
        # Calculate the distance from the point to each centroid.
        for i, centroid in enumerate(centroids):
            cur_dist = sqrt((pickup_x - centroid[0])**2 + (pickup_y - centroid[1])**2)
            # Update minimum distance and index if a closer centroid is found.
            if cur_dist < min_dist:
                min_dist = cur_dist
                index = i
                
        # Output the index of the closest centroid along with the coordinates of the point.
        print("{}\t{}\t{}".format(index, pickup_x, pickup_y))

if __name__ == "__main__":
    # Read centroids from the 'centroids.txt' file.
    centroids = getCentroids('centroids.txt')
    # Create clusters based on the centroids.
    createClusters(centroids)