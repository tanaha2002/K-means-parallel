#!/usr/bin/env python3

import sys
import csv
import math

def combine_centroids(old_centroids_file, new_centroids_file):
    centroids_old = []
    centroids_new = []
    with open(old_centroids_file) as f1, open(new_centroids_file) as f2:
        reader1 = csv.reader(f1)
        for row in reader1:
            centroids_old.append([float(x) for x in row])
        reader2 = csv.reader(f2)
        for row in reader2:
            centroids_new.append([float(x) for x in row])

    if len(centroids_old) != len(centroids_new):
        return False

    for i in range(len(centroids_old)):
        #euclid < 0.15
        euclid = math.sqrt((centroids_old[i][0]-centroids_new[i][0])**2 + (centroids_old[i][1]-centroids_new[i][1])**2)
        if euclid > 0.15:
            return False
    return True


if __name__ == "__main__":
    old_centroids_file = '/home/ubuntu/k_mean/parallel_hdfs/centroids.txt'
    new_centroids_file = '/home/ubuntu/k_mean/parallel_hdfs/new_centroids.txt'
    
    print(combine_centroids(old_centroids_file, new_centroids_file))
