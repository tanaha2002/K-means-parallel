import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate a large dataset with two features
num_samples = 1000000
num_features = 2
random_state = 45
num_clusters = 4

# Creating a synthetic dataset with make_blobs
X, y = make_blobs(n_samples=num_samples, 
                            n_features=num_features, 
                            centers=num_clusters, 
                            shuffle=True, 
                            random_state=random_state)


# Visualizing the generated dataset with ground truth labels
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', s=10)
plt.title('Generated Dataset with Ground Truth Labels')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
#plt.colorbar(label='Class')
plt.savefig('/home/ubuntu/k_mean/datagen/ground_truth.png')

# Saving the dataset without labels to a file for K-means
np.savetxt('/home/ubuntu/k_mean/datagen/dataset.txt', X, delimiter=',')

# Generating the dataset with labels for visualization
data_with_labels = np.column_stack((X, y))
np.savetxt('/home/ubuntu/k_mean/datagen/dataset_with_labels.txt', data_with_labels, delimiter=',')

# Initializing centroids for K-means
init_centroids = X[np.random.choice(X.shape[0], num_clusters, replace=False)]
np.savetxt('/home/ubuntu/k_mean/datagen/init_centroids.txt', init_centroids, delimiter=',')

# Visualizing the generated dataset with initial centroids
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], s=10)
plt.title('Generated Dataset with Initial Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.scatter(init_centroids[:, 0], init_centroids[:, 1], marker='*', c='red', s=150)
plt.savefig('/home/ubuntu/k_mean/datagen/init_centroids.png')

