import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate synthetic data with blobs
data, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Perform k-means clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(data)
labels = kmeans.predict(data)
centers = kmeans.cluster_centers_

# Plot the clusters and centroids
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering')
plt.show()

