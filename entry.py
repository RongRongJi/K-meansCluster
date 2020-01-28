from Kmeans.util import read_file
from Kmeans.K_means import Kmeans
import matplotlib.pyplot as plt
from Kmeans.draw import draw_point


def k_means_cluster(k_center=True, picName='picture'):
    points = read_file()
    cluster = Kmeans(8, points, k_center)
    cluster.cluster()
    colors = ['red','orange','yellow','green','cyan','deepskyblue','slateblue','pink']
    centers = []
    for i in range(8):
        draw_point(cluster.point_sets[i],colors[i])
        centers.append(cluster.means[i])
    draw_point(centers,'black')
    plt.savefig('data/'+picName+'.jpg')
    plt.show()


if __name__ == '__main__':
    k_means_cluster(True, 'init_with_kcenter')
    k_means_cluster(False, 'init_with_random')


