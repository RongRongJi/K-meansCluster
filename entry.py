from Kmeans.util import read_file
from Kmeans.K_means import Kmeans
import matplotlib.pyplot as plt
from Kmeans.draw import draw_point
from Evaluate.evaluate import evaluate


def k_means_cluster(k_center, center_num, picName='picture'):
    points = read_file()
    cluster = Kmeans(center_num, points, k_center)
    cluster.cluster()
    colors = ['red','orange','yellow','green','cyan','deepskyblue','slateblue','pink',
              'beige','chocolate','coral','dimgray','gold','greenyellow','maroon',
              'mediumblue','orchid','plum','snow','teal','violet']
    centers = []
    for i in range(center_num):
        draw_point(cluster.point_sets[i],colors[i])
        centers.append(cluster.means[i])
    draw_point(centers,'black')
    plt.savefig('data/'+picName+'.jpg')
    plt.show()
    # 聚类评价
    eva = evaluate(center_num,cluster.point_sets,cluster.means)
    # eva.__print__()
    print(center_num, ' ', eva.silhouette_score(),' ',eva.__print__())



if __name__ == '__main__':
    # for i in range(8, 17):
    #    k_means_cluster(True, i, 'init_with_kcenter')
    #    k_means_cluster(False, i, 'init_with_random')
    # k_means_cluster(True, 15, 'init_with_kcenter')
    k_means_cluster(False, 15, 'init_with_random')


