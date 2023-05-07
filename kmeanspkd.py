import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# data
data = np.array([
    [7, 9],[21, 6],[14, 5], [21, 9],[7, 8],[9, 7], [14, 5],[15, 6],[16, 25]
])
# initialize k-means algorithm with 2 clusters
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
# get the coordinates of the centroids and labels of the clusters
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
# plot the data points with different colors for each cluster and their respective labels
for i, point in enumerate(data):
    plt.scatter(point[0], point[1], c=labels[i], cmap='rainbow', label=f'Cluster {labels[i]}')
plt.scatter(centroids[:,0], centroids[:,1], marker='o', color='black', s=100, label='Centroids')
plt.legend()
plt.show()


OUTPUT: dot dot graph
