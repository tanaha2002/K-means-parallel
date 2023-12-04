#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

centroids = np.loadtxt('/home/ubuntu/k_mean/parallel_hdfs/new_centroids.txt', delimiter=',')
data = np.loadtxt('/home/ubuntu/k_mean/datagen/dataset.txt', delimiter=',')


plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c='blue', cmap='viridis', s=10)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='red', s=200, label='Centroids')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
