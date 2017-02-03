####################################################################################################
#   References:                                                                                    #
#   Dorin Comaniciu and Peter Meer, “Mean Shift: A robust approach toward feature space analysis”. #
#   IEEE Transactions on Pattern Analysis and Machine Intelligence. 2002. pp. 603-619.             #
#                                                                                                  #
#   www.youtube.com/watch?v=2lpS6gUwiJQ&t=332s                                                     #
####################################################################################################
import numpy as np
import timeit
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import style
from itertools import cycle
# from intuitRitChallenge.data_table import generate_table
style.use("ggplot")


centers = [[1, 1, 1], [5, 5, 5], [3, 10, 10]]
X, _ = make_blobs(n_samples=100, centers=centers, cluster_std=1)
# X = generate_table()

start = timeit.default_timer()

ms = MeanShift()
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
print(cluster_centers)

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

end = timeit.default_timer()

print("Number of estimated clusters : %d" % n_clusters_)
print("Took {} to find".format(end-start))


# Visualizations for troubleshooting (and because they look cool):
colors = 10*['r', 'g', 'b', 'c', 'k', 'y', 'm']
fig = plt.figure()
# plt.clf()
ax = fig.add_subplot(111, projection='3d')

# colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
# for k, col in zip(range(n_clusters_), colors):
#     my_members = labels == k
#     cluster_center = cluster_centers[k]
#     plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
#     plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=14)

for i in range(len(X)):
    ax.scatter(X[i][0], X[i][1], X[i][2], c=colors[labels[i]], marker='o')

ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], cluster_centers[:, 2],
           marker="x", color='k', s=150, linewidths=5, zorder=10)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
