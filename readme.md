# K-means Algorithm

> Last Update Date: 2020-1-18

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

#### K-means clustering results with randomly selected initial points
![avatar](https://github.com/RongRongJi/K-meansCluster/blob/master/data/pure_kmeans.jpg?raw=true)

#### K-means clustering results using K-center for center initialization



## Usage

Update later

****

|Author|RongRongJi|
|---|---
|Contact|[homepage](https://github.com/RongRongJi)

