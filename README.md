# ArcPy "Supercluster" algorithm for ArcGIS
An Implementation of the simple and fast spatial clustering algorithm *'supercluster'* (e.g. used by *Mapbox*) for ArcGIS that efficiently  clusters huge datasets of points. Primarily suitable for creating maps of smaller scales. 

&#x1F4D7; Trial project. Primarily implemented to get familiar with the python syntax and the ArcPy interface for ArcGIS.

## Parameters:<br/>
- Input: FeatureClass (Point)<br/>
- Input: Cluster radius (in meter)<br/>
- Output: FeatureClass (Point)<br/>

## Steps:<br/>
1. Start with a random point of the dataset<br/>
2. Find every point that lies within the given radius around this point<br/>
3. Form a cluster with the nearby points<br/>
4. Randomly select a new point of the dataset that isn't part of a cluster and repeat the previos steps.

## Result:<br/>
![#1589f0](https://placehold.it/15/1589f0/000000?text=+) Original point data </br>
![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Result for a (cluster-)radius of 500 meters </br>
![#fffa00](https://placehold.it/15/fffa00/000000?text=+) Result for a (cluster-)radius of 1000 meters </br>

![alt text](https://github.com/OliverHennhoefer/ArcPy_Supercluster/blob/master/supercluster_result.PNG)
*Note: Since the algorithm randomly chooses points for clustering, the results vary for every application of 'supercluster'*

## Future Improvements:<br/>
- Calculate the mean position out of the points of one cluster to get more representative cluster locations.
- Add the possibility to fit additional attributes to the corresponding cluster (e.g. by calculating the mean for the points of the same cluster)
