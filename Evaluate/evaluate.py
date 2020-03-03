import numpy as np


class evaluate:

    def __init__(self, center_num, point_set, means):
        self.center_num = center_num
        self.point_set = point_set
        self.means = means

    # 紧密性
    # 越低意味着类内聚类距离越近，但没有考虑类间效果
    def compactness(self):
        cp = 0
        for i in range(0, self.center_num):
            total, mean = 0, self.means[i]
            for point in self.point_set[i]:
                total += np.sqrt(np.power(point[0]-mean[0],2)+np.power(point[1]-mean[1],2))
            total /= len(self.point_set[i])
            cp += total
        return cp / self.center_num

    # 间隔性
    # 越高意味着类间聚类距离越远，但没有考虑类内效果
    def separation(self):
        sp = 0
        for i in range(0, self.center_num):
            for j in range(i, self.center_num):
                mi, mj = self.means[i], self.means[j]
                sp += np.sqrt(np.power(mi[0]-mj[0],2)+np.power(mi[1]-mj[1],2))
        return 2*sp/(self.center_num*self.center_num-self.center_num)

    # 戴维森堡丁指数 DBI
    # DBI越小意味着类内距离小，同时类间距离大
    # 不适合环状分布
    def davies_bouldin_index(self):
        db = 0
        for i in range(0, self.center_num):
            large, mi, ci = 0, self.means[i], 0
            for point in self.point_set[i]:
                ci += np.sqrt(np.power(point[0] - mi[0], 2) + np.power(point[1] - mi[1], 2))
            ci /= len(self.point_set[i])
            for j in range(0, self.center_num):
                if i != j:
                    cj, mj = 0, self.means[j]
                    for point in self.point_set[j]:
                        cj += np.sqrt(np.power(point[0] - mj[0], 2) + np.power(point[1] - mj[1], 2))
                    cj /= len(self.point_set[j])
                    tmp = (ci + cj) / np.sqrt(np.power(mi[0]-mj[0],2)+np.power(mi[1]-mj[1],2))
                    if tmp > large:
                        large = tmp
            db += large
        return db / self.center_num

    # 邓恩指数 DVI
    # DVI越大意味着类间距离越大， 同时类内距离越小
    # 对离散点的聚类测评效果好， 但对环状分布测评效果差
    def dunn_validity_index(self):
        min, max = np.inf, 0
        for i in range(0, self.center_num):
            maxest = 0
            for p1 in self.point_set[i]:
                for p2 in self.point_set[i]:
                    dist = np.sqrt(np.power(p1[0]-p2[0],2)+np.power(p1[1]-p2[1],2))
                    if maxest < dist:
                        maxest = dist
            if max < maxest:
                max = maxest
            for j in range(0, self.center_num):
                if i!=j:
                    minest = np.inf
                    for pi in self.point_set[i]:
                        for pj in self.point_set[j]:
                            dist = np.sqrt(np.power(pi[0]-pj[0],2)+np.power(pi[1]-pj[1],2))
                            if minest > dist:
                                minest = dist
                    if min > minest:
                        min = minest
        return min / max

    # 代价函数
    # 用于肘部法则
    def cost_function(self):
        total = 0
        for i in range(0, self.center_num):
            tmp, mean = 0, self.means[i]
            for point in self.point_set[i]:
                tmp += np.power(point[0]-mean[0],2) + np.power(point[1]-mean[1],2)
            total += tmp
        return total

    # 各点轮廓系数
    def silhouette_coefficient(self, point, i):
        dis_out, tmp = 0, 0
        for p in self.point_set[i]:
            tmp += np.sqrt(np.power(point[0]-p[0],2)+np.power(point[1]-p[1],2))
        dis_in = tmp / (len(self.point_set[i])-1)
        tmp = 0
        for j in range(0, self.center_num):
            if j != i:
                for p in self.point_set[j]:
                    dis_out += np.sqrt(np.power(point[0] - p[0], 2) + np.power(point[1] - p[1], 2))
                tmp += len(self.point_set[j])
        dis_out /= tmp
        if dis_out > dis_in:
            return (dis_out-dis_in)/dis_out
        else:
            return (dis_out-dis_in)/dis_in

    # 总轮廓系数
    def silhouette_score(self):
        score, total = 0, 0
        for i in range(0, self.center_num):
            total += len(self.point_set[i])
            for p in self.point_set[i]:
                score += self.silhouette_coefficient(p, i)
        return score / total




    def __print__(self):
        print(self.center_num)
        print("紧密性: ", self.compactness())
        print("间隔性: ", self.separation())
        print("DBI: ", self.davies_bouldin_index())
        print("DVI: ", self.dunn_validity_index())

