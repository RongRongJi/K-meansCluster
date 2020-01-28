# utf-8
import copy
import numpy as np

class Kcenter:
    points = []  # 点集合
    K = 0  # K值参数
    centers = {}  # 中心点
    point_sets = {}  # 点分类
    visits = []  # 计算中需要使用的变量

    def __init__(self, K, points):
        self.K = K
        self.points = points
        self.visits = copy.deepcopy(points)

    '''
    Step 1: Initialization: Create a single cluster of all nodes.
    
    Step 2: Our goal is to create k clusters, adding one cluster
    at each iteration. Suppose in the current iteration, there are
    x existing clusters, and a distance d is the current maximum 
    distance between any node and its hub.
    
    Step 3: Continue at iteration x, Create a new cluster B(x+1) with
    H(x+1) = v as the only node. if we find that dist(v,hj) > dist(v, hi)
    , that is, v is closer to the new cluster hub than it is to its old
    hub, we move it from its old cluster to the new cluster.
    
    Step 4: Iterate the previous two steps for K-1 times, and we finally get
    k clusters with corresponding hub nodes as output.
    '''
    def cluster(self):
        count = 0
        # Step 1
        self.centers[0] = self.visits[0]
        self.point_sets[count] = []
        for visit in self.visits:
            self.point_sets[0].append(visit)
        count += 1
        while count <= self.K - 1:
            # Step 2
            max_dist = 0
            current_point = (-1,-1)
            for k, v in self.point_sets.items():
                index = int(k)
                centriod = self.centers[index]
                for point in v:
                    dis = np.power(centriod[0] - point[0], 2) + np.power(centriod[1] - point[1], 2)
                    if dis > max_dist:
                        max_dist = dis
                        current_point = point
            self.centers[count] = current_point
            # Step 3
            for i in range(count+1):
                self.point_sets[i] = []
            self.point_sets[count] = []
            for point in self.visits:
                min_dist = np.inf
                current_part = -1
                for i, center in self.centers.items():
                    dis = np.power(center[0] - point[0], 2) + np.power(center[1] - point[1], 2)
                    if dis < min_dist:
                        min_dist = dis
                        current_part = i
                # 重新划分点
                self.point_sets[current_part].append(point)
            count += 1
            print("=========", count, '==========')
            print(self.centers)
        print("计算完成")
        print(self.centers)
        print(self.point_sets)















