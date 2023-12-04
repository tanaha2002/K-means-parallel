#!/bin/bash

DATAPATH="/home/ubuntu/k_mean/datagen/dataset.txt"
INPUT="/data/input/"
OUTPUT="/data/output"

# Check if the HDFS path exists
if hdfs dfs -test -e $INPUT; then
    echo "HDFS path $INPUT already exists."
    hdfs dfs -rm -r $INPUT
    echo "remove old data successfully"
fi

if hdfs dfs -test -e $OUTPUT; then
   echo "Found old output."
   hdfs dfs -rm -r $OUTPUT
   echo "remove old output successfully."
fi
# Create the HDFS path
hdfs dfs -mkdir -p $INPUT
echo "Created HDFS path: $INPUT"

#put data to HDFS
hdfs dfs -put /home/ubuntu/k_mean/datagen/dataset.txt /data/input

echo "Successfully put data to HDFS"


if [ -d "/home/ubuntu/hadoop-3.3.6/logs/userlogs/" ]; then
    rm -r -f /home/ubuntu/hadoop-3.3.6/logs/userlogs/*
    echo "Successfully remove old logs"
fi

