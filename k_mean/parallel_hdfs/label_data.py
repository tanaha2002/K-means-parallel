import numpy as np

# Load the data
data = np.loadtxt('/home/ubuntu/k_mean/datagen/dataset.txt', delimiter=',') 

# Load the new centroids 
centroids = np.loadtxt('/home/ubuntu/k_mean/parallel_hdfs/new_centroids.txt', delimiter=',')

# Initialize labels array
num_samples = data.shape[0]
labels = np.zeros(num_samples, dtype=int) 

# Label each sample based on closest centroid
for i in range(num_samples):
    distances = np.linalg.norm(data[i,:] - centroids, axis=1)
    labels[i] = np.argmin(distances)

# Save labeled data  
labeled_data = np.column_stack((data, labels))
np.savetxt('/home/ubuntu/k_mean/parallel_hdfs/labeled_data.txt', labeled_data, delimiter=',')
