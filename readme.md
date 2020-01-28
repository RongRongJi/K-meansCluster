# K-means Algorithm

> Last Update Date: 2020-1-28

## Project Introduction

The goal of this project is to implement the K-means algorithm and use the k-center algorithm for center initialization.

* Dataset
    * `data/bgau.txt` is synthetic 2-d data with N=5000 vectors and k=15 Gaussian clusters with different degree of cluster overlap.
    * P. Fränti and O. Virmajoki, "Iterative shrinking method for clustering problems", Pattern Recognition, 39 (5), 761-765.
    * Each line has the following format:  x  y  , which represent the x- and y-coordinates of a point.

* Project Output
    * A visualization of each cluster

* Project Environment
    * python3

## K-means
### Introduction
K-means clustering algorithm is an iterative clustering analysis algorithm. It steps are to randomly select K objects as the initial clustering center, then calculate the distance between each object and each seed clustering center, and assign each object to the nearest clustering.

### Advantage & Disadvantage
* The advantages of K-means
    * Simple principle, coonvenient implementation and fast convergence
    * The clustering effect is better
    * The interpretability of the model is strong
    * Only cluster number K is needed for parameter adjustment
* The disadvantage of K-means
    * It often ends with local optimization and is sensitive to noise and isolated points. Moreover, this method is not suitable for finding clusters with non convex shape or with large difference in size
    * The number of clustering centers K needs to be given in advance, but in practice, the selection of K is very difficult to estimate. In many cases, it's not known in advance how many categories a given dataset should be divied into before it's most appropriate
    * K-means needs to determine the initial clustering centers artificially. Different initial clustering centers may lead to completely different clustering results.

### Optimize the selection of initial clustering centers
K-means algorithm depends on the selection of inital solution. We introduce K-center clustering algorithm. The K-center method uses the center points to define the prototype, in which the center points are the most representative points of a group of points, and uses the distance between the spatial point groups to find the typical points as the seed objects of clustering.

### K-center algorithm
* Step 1: Create a single cluster of all nodes.
* Step 2: Suppose in the current iteration, there are x existing clusters, and a distance d is the current maximum distance between any node and its hub. We find such a node v that the distance between v and its hub is d.
* Step 3: Continue at iteration x, Create a new cluster with v as the only node. Then for each point, if we find that the dist(point, its hub) > dist(point, v), that is, the point is closer to the new cluster hub than it is to its old hub, we move the point from its old cluster to the new cluster.
* Step 4: Iterate the Step 2 and 3 for K-1 times, and we finally get K clusters with corresponding hub nodes as output.

#### K-means clustering results with randomly selected initial points
![avatar](https://github.com/RongRongJi/K-meansCluster/blob/master/data/init_with_random.jpg?raw=true)

#### K-means clustering results using K-center for center initialization
![avatar](https://github.com/RongRongJi/K-meansCluster/blob/master/data/init_with_kcenter.jpg?raw=true)

## Usage
### Basic example
```python
from entry import k_means_cluster
k_means_cluster(True, 'init_with_kcenter')
k_means_cluster(False, 'init_with_random')
```

### Functions
`k_means_cluster(using_kcenter, picture_name)` `Function`<br>
The function is used to read the dataset, and use k-means algorithm to cluster the dataset, and output it in the form of image.<br>
Props: <br>
`using_kcenter` decide whether to use k-center algorithm to initialize centers of the dataset. `True` for use, while `False` for not, default `True`.
`picture_name` decide the name of the output image. Default `picture`.


****

|Author|RongRongJi|
|---|---
|Contact|[homepage](https://github.com/RongRongJi)

