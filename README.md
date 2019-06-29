# ArcPy Supercluster for ArcGIS
An Implementation of the simple and fast spatial clustering algorithm *'supercluster'* (e.g. used by Mapbox) for ArcGIS that efficiently  clustering huge datasets of points.

# Steps:<br/>
1 Start with a random point of the dataset<br/>
2 Find every point that lies within the given radius around this point<br/>
3 Form a cluster with the nearby points<br/>
4 Randomly select a new point of the dataset that isn't part of a cluster and repeat the previos steps.

![alt text](https://github.com/OliverHennhoefer/ArcPy_Supercluster/blob/master/supercluster_result.PNG)


(Trial project. Implemented to get familiar with Python Syntax and the ArcPy interface for ArcGIS.)
