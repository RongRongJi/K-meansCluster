from Kmeans.util import read_file
from Kmeans.K_means import Kmeans
import matplotlib.pyplot as plt
from Kmeans.draw import draw_point

points = read_file()
cluster = Kmeans(8, points)
cluster.cluster()
colors = ['red','orange','yellow','green','cyan','deepskyblue','slateblue','pink']
for i in range(8):
    draw_point(cluster.point_sets[i],colors[i])

plt.savefig('data/pure_kmeans.jpg')
plt.show()