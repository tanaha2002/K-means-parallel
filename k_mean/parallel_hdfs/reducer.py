#!/usr/bin/env python3
"""kmeans_reducer.py"""

import sys
import re
from collections import defaultdict

centroids = []
counts = defaultdict(int)
sums = defaultdict(lambda: [0] * 2)

for line in sys.stdin:
    parts = re.split(r'\s+', line.strip())
    centroid_idx = int(parts[0])
    point = [float(x) for x in parts[1:]]

    counts[centroid_idx] += 1
    for i, v in enumerate(point):
        sums[centroid_idx][i] += v

for centroid_idx in sums:
    if counts[centroid_idx] != 0:  # Check if count is non-zero to avoid division by zero
        centroid = [v / counts[centroid_idx] for v in sums[centroid_idx]]
        centroids.append(centroid)

print("\n".join(["{}".format(",".join([str(x) for x in centroid])) for i, centroid in enumerate(centroids)]))
