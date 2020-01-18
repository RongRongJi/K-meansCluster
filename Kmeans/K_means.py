# utf-8
import numpy as np
import copy

class Kmeans:
    points = []  # 点集合
    K = 0  # K值参数
    means = {}  # 集合中心
    point_sets = {}  # 点分类
    visits = []  # 计算中需要使用的变量

    def __init__(self, K, points):
        self.K = K
        self.points = points
        self.visits = copy.deepcopy(points)
        for i in range(K):
            self.point_sets[i] = []

    # 选择初始质心
    def select_init_centroid(self):
        for i in range(self.K):
            self.means[i] = self.visits[0]
            del self.visits[0]

    # 划分集合
    def divide_set(self):
        while len(self.visits) != 0:
            point = self.visits[0]
            distance = np.inf
            set_num = -1
            for key, value in self.means.items():
                dis = np.power(value[0]-point[0],2)+np.power(value[1]-point[1],2)
                if dis < distance:
                    distance = dis
                    set_num = int(key)
            self.point_sets[set_num].append(point)
            del self.visits[0]

    # 选择新质心
    def select_new_centroid(self):
        is_change = False
        for key, sets in self.point_sets.items():
            index = int(key)
            aver_x ,aver_y = 0, 0
            for point in sets:
                aver_x += point[0]
                aver_y += point[1]
            aver_x /= len(sets)
            aver_y /= len(sets)
            if self.means[index] != (aver_x, aver_y):
                is_change = True
            self.means[index] = (aver_x, aver_y)
            index += 1
        return is_change

    # K-means
    def cluster(self):
        self.select_init_centroid()
        self.divide_set()
        is_change = self.select_new_centroid()
        times = 1
        while is_change:
            self.visits = copy.deepcopy(self.points)
            for i in range(self.K):
                self.point_sets[i] = []
            self.divide_set()
            is_change = self.select_new_centroid()
            times+=1
            print("=========",times,'==========')
            print(self.means)
        print("计算完成")
        print(self.means)
        print(self.point_sets)




