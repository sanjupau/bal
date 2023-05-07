import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
X = np.random.rand(100, 2)
wcss = []
for i in range(1, 11):
 
 kmeans = KMeans(n_clusters=i)
 
 kmeans.fit(X)
 wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
k = np.argmin(np.diff(wcss, 2)) + 2
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)
centers = kmeans.cluster_centers_
labels = kmeans.labels_
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], marker='x', s=200, linewidths=3, color='r')
plt.show()
