#!/bin/bash

# Check if the required number of command-line arguments is provided.
# Expected: Number of clusters (K) and number of iterations (V).
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <number_of_clusters> <number_of_iterations>"
    exit 1  # Exit the script with an error code.
fi

# Assign command-line arguments to variables.
K=$1  # Number of clusters
V=$2  # Number of iterations

# Initialize the iteration counter.
i=1

# Remove any existing MapReduce output directories from HDFS.
hadoop fs -rm -r /output/task2/mapreduce-output*

# Loop for the specified number of iterations.
while [ "$i" -le "$V" ]
do
    # Run the MapReduce job using Hadoop streaming.
    hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D mapred.reduce.tasks=$K \
    -D mapred.text.key.partitioner.options=-k1 \
    -files centroids.txt,./mapper_t2.py,./reducer_t2.py \
    -mapper ./mapper_t2.py \
    -reducer ./reducer_t2.py \
    -input /input/Trips.txt \
    -output /output/task2/mapreduce-output$i \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
    
    # Remove any existing centroids1.txt file.
    rm -f centroids1.txt

    # Merge the output parts from HDFS to a single file: centroids1.txt.
    hadoop fs -getmerge /output/task2/mapreduce-output$i/part-0000* centroids1.txt

    # Run the Python script to check if centroids have converged.
    seeiftrue=$(python reader_t2.py)

    # Check the output of the Python script. If it returns 1, centroids have converged; exit the loop.
    if [ "$seeiftrue" = "1" ]; then
        break
    else
        # Otherwise, copy the new centroids to be used in the next iteration.
        cp centroids1.txt centroids.txt
    fi
    
    # Increment the iteration counter.
    i=$((i+1))
done
