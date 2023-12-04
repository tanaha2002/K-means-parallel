#!/usr/bin/env python3
"""kmeans_mapper.py"""

import sys
import csv
import math

centroids = [] 

# read initial centroids
with open('/home/ubuntu/k_mean/parallel_hdfs/centroids.txt') as f:
  reader = csv.reader(f)
  for row in reader:
    centroids.append([float(x) for x in row])

# read iris data  
# read iris data  
for line in sys.stdin:
    point = line.strip().split(",")  # Split the line by commas directly
    point = [float(x) for x in point]  # Convert values to float

    # calculate distance to each centroid
    distances = []
    for centroid in centroids:
        dist = math.sqrt(sum([(p - c) ** 2 for p, c in zip(point, centroid)]))
        distances.append(dist)

    # output closest centroid
    min_dist = min(distances)
    centroid_idx = distances.index(min_dist)
    print("{}\t{}".format(centroid_idx, "\t".join([str(x) for x in point])))
