#!/usr/bin/env python3
import sys
from math import sqrt

def getCentroids(filepath):
    """
    Retrieve centroids from a given file.
    
    Parameters:
        filepath (str): The path of the file containing centroids.
        
    Returns:
        list: A list of centroids, each represented as a list [x, y].
    """
    centroids = []  # Initialize an empty list to store centroids.
    with open(filepath) as fp:  # Open the file with the given filepath.
        for line in fp:  # Iterate over each line in the file.
            cord = line.strip().split(', ')  # Remove leading/trailing whitespace and split by ', '.
            centroids.append([float(cord[0]), float(cord[1])])  # Convert to floats and append to centroids list.
    return centroids

def checkCentroidsDistance(centroids, centroids1):
    """
    Check the distance between each pair of centroids in two lists.
    
    Prints '0' if any centroid pair has a distance of 1 or greater.
    Prints '1' otherwise.
    
    Parameters:
        centroids (list): The first list of centroids.
        centroids1 (list): The second list of centroids.
    """
    for c1, c2 in zip(centroids, centroids1):  # Pair up corresponding centroids from the two lists.
        dist = sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)  # Calculate the Euclidean distance between the centroids.
        if dist >= 1:  # If distance is 1 or greater, print '0' and return, which means that the algorithm didn't converge yet.
            print(0)
            return
    print(1)  # If function hasn't returned by this point, print '1'.

if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')  # Get centroids from 'centroids.txt'.
    centroids1 = getCentroids('centroids1.txt')  # Get centroids from 'centroids1.txt'.
    checkCentroidsDistance(centroids, centroids1)  # Check distances between corresponding centroids.
