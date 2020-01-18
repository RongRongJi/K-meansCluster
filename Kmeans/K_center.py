# utf-8

class Kcenter:
    points = []  # 点集合
    K = 0  # K值参数
    centers = {}  # 中心点
    point_sets = {}  # 点分类

    def __init__(self, K, points):
        self.K = K
        self.points = points

    
