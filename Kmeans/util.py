# utf-8
import codecs


def read_file():
    # 读入数据
    f = codecs.open('data/Bgau.txt','r')
    line = f.readline()
    points = []
    while line:
        x, y = split_x_y(line)
        points.append((x,y))
        line = f.readline()
    print(len(points))
    return points


def split_x_y(line):
    # x,y 点分割
    pointCut = line.strip('\n').split("    ")
    x = float(pointCut[1])
    y = float(pointCut[2])
    return x, y

