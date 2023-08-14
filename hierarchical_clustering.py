import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Generate random data
np.random.seed(0)
data = np.random.rand(10, 2)

# Perform hierarchical clustering
linkage_matrix = linkage(data, method='ward')

# Plot dendrogram
plt.figure(figsize=(8, 6))
dendrogram(linkage_matrix)
plt.show()

