import numpy as np
import time 

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Function for K-means clustering
def kmeans_clustering(data, k,init_centroids, max_iters=100):
    
    centroids = init_centroids.copy()

    for _ in range(max_iters):
        print("interation: ", _+1)
        # Assign each data point to the nearest centroid
        clusters = []
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_label = np.argmin(distances)
            clusters.append(cluster_label)

        # Update centroids by calculating mean of assigned data points
        new_centroids = []
        for cluster in range(k):
            cluster_points = [data[i] for i, c in enumerate(clusters) if c == cluster]
            new_centroid = np.mean(cluster_points, axis=0)
            new_centroids.append(new_centroid)
        
        new_centroids = np.array(new_centroids)
        
        #check convergence if threshold of 0.15 is reached
        if np.sum(np.absolute(new_centroids - centroids)) < 0.15:
            centroids = new_centroids
            break
        
        
        centroids = new_centroids
        
    return centroids, clusters

# Loading dataset and initial centroids
data = np.loadtxt('/home/ubuntu/k_mean/datagen/dataset.txt', delimiter=',')
initial_centroids = np.loadtxt('/home/ubuntu/k_mean/datagen/init_centroids.txt', delimiter=',')

start_time = time.time()

# Perform K-means clustering
num_clusters = len(initial_centroids)
final_centroids, cluster_labels = kmeans_clustering(data, num_clusters,initial_centroids)

end_time = time.time()
print("Time taken to run the algorithm: ", end_time - start_time)
with open('/home/ubuntu/k_mean/sequential/total_time.txt','w') as f:
	f.write(str(end_time - start_time))
# Visualizing the clustered data with final centroids
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c=cluster_labels, cmap='viridis', s=10)
plt.scatter(final_centroids[:, 0], final_centroids[:, 1], marker='*', c='red', s=200, label='Centroids')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
# plt.show()

plt.savefig('/home/ubuntu/k_mean/sequential/cluster.png')
#save centroids
np.savetxt('/home/ubuntu/k_mean/sequential/new_centroids.txt', final_centroids, delimiter=',')

labeled_data = np.hstack((data, np.array([cluster_labels]).T))
np.savetxt('/home/ubuntu/k_mean/sequential/labeled_data.txt', labeled_data, delimiter=',')
