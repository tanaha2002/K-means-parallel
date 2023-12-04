

import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score, davies_bouldin_score, adjusted_rand_score

def load_data(seq_data, par_data, ground_truth_data):
    """
    Load data from sequential and parallel output.
    seq_data: path to sequential data.
    par_data: path to parallel data.
    """
    seq_data = np.loadtxt(seq_data, delimiter=',')
    par_data = np.loadtxt(par_data, delimiter=',')
    ground_truth = np.loadtxt(ground_truth_data, delimiter=',')
    return seq_data, par_data, ground_truth

def compare_evaluation_metric(seq_data_labels, par_centroids_labels, ground_truth):
    """
    Compare the centroids with many methods like Inertia, Silhouette, Davies-Bouldin.
    seq_data_labels: feature1, feature2, label.
    par_centroids_labels: feature1, feature2, label.
    ground_truth: feature1, feature2, label.
    """

    seq_labels = seq_data_labels[:, -1].astype(int)  # Assuming the last column contains labels
    par_labels = par_centroids_labels[:, -1].astype(int)
    true_labels = ground_truth[:, -1].astype(int)

    seq_silhouette = silhouette_score(seq_data_labels[:, :-1], seq_labels)
    par_silhouette = silhouette_score(par_centroids_labels[:, :-1], par_labels)

    seq_dbi = davies_bouldin_score(seq_data_labels[:, :-1], seq_labels)
    par_dbi = davies_bouldin_score(par_centroids_labels[:, :-1], par_labels)

    seq_ari = adjusted_rand_score(true_labels, seq_labels)
    par_ari = adjusted_rand_score(true_labels, par_labels)

    print("Silhouette: sequential = {}, parallel = {}".format(seq_silhouette, par_silhouette))
    print("Davies-Bouldin: sequential = {}, parallel = {}".format(seq_dbi, par_dbi))
    print("Adjusted Rand Index: sequential = {}, parallel = {}".format(seq_ari, par_ari))



def compare_speed(sequential_time,parallel_time):
    with open(sequential_time, 'r') as f:
        seq_time = np.loadtxt(f)
    with open(parallel_time, 'r') as f:
        par_time = np.loadtxt(f)

    seq_time = float(seq_time)
    #convert parallel time from ms to s
    par_time = float(par_time)/1000

    print("Time: sequential = {}, parallel = {}".format(seq_time, par_time))
    plt.figure()
    plt.title("Time")
    plt.bar(["Sequential", "Parallel"], [seq_time, par_time])
    plt.ylabel("Time (s)")
    plt.savefig("speed_compare.png")
    plt.show()



if __name__ == "__main__":
    sequential_data_path = "/home/ubuntu/k_mean/sequential/labeled_data.txt"
    parallel_data_path = "/home/ubuntu/k_mean/parallel_hdfs/labeled_data.txt"
    ground_truth_path = "/home/ubuntu/k_mean/datagen/dataset_with_labels.txt"
    sequential_time = "/home/ubuntu/k_mean/sequential/total_time.txt"
    parallel_time = "/home/ubuntu/k_mean/parallel_hdfs/total_time.txt"
    

    # seq_data_label, par_data_label,ground_truth = load_data(sequential_data_path, parallel_data_path,ground_truth_path)
    # compare_evaluation_metric(seq_data_label, par_data_label,ground_truth)
    compare_speed(sequential_time,parallel_time)
