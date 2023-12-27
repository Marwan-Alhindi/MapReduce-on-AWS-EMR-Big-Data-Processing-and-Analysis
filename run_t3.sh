#!/bin/bash

# Remove existing output directory from HDFS
hadoop fs -rm -r /output/task3

# Run the join operation using Hadoop Streaming
hadoop jar ./hadoop-streaming-3.1.4.jar \
-files mapper_t3.py,reducer_t3.py -mapper 'mapper_t3.py join' -reducer 'reducer_t3.py join' \
-input /input/Taxis.txt,/input/Trips.txt -output /output/task3/join

# Run the count operation using Hadoop Streaming with 3 reducers
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapreduce.job.reduces=3 \
-files mapper_t3.py,reducer_t3.py -mapper 'mapper_t3.py count' -reducer 'reducer_t3.py count' \
-input /output/task3/join -output /output/task3/count
