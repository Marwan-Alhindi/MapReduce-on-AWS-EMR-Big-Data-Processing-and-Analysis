#!/bin/bash

# Remove existing output directory, if it exists
hdfs dfs -rm -r /output/task1

# Run Hadoop MapReduce job
hadoop jar ./hadoop-streaming-3.1.4.jar \
-files mapper_t1.py,reducer_t1.py \
-mapper mapper_t1.py \
-reducer reducer_t1.py \
-numReduceTasks 3 \
-input /input/Trips.txt \
-output /output/task1

# Retrieve the output
hdfs dfs -getmerge /output/task1/ output_task1.txt
