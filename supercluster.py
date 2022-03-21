# -*- coding: cp1252 -*-
'''
Geomatics Masters Course: Web Feature Service
Assignment II
Author: Oliver Hennhoefer

Implementation a Point Clustering Algorithm
'''

import arcpy
import os
from math import *
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def shapefileToList(inputFeature):
    pointsList = []
    with arcpy.da.SearchCursor(inputFeature, "SHAPE@XY") as Reader:
        for feature in Reader:
            x = feature[0][0]
            y = feature[0][1]
            point = Point(x, y)
            pointsList.append(point)

    return pointsList

def deletePointsInCircle(centerPoint, pointsList, radius):
    deletionList = []
    for point in pointsList:
	diff_x = point.x - centerPoint.x
        diff_y = point.y - centerPoint.y
        distance  = 100000* (sqrt((diff_x)**2 + (diff_y)**2))
        arcpy.AddMessage(distance)
        #distance = sqrt((point.x-centerPoint.x)**2+(point.y-centerPoint.y)**2)
        if distance < radius:
            deletionList.append(pointsList.index(point))

    for index in sorted(deletionList, reverse=True):
        del pointsList[index]
 
    return pointsList

###########################################################
###########################################################
inputFeaturePoints = arcpy.GetParameter(0)
outputFeaturePoints = arcpy.GetParameterAsText(2)
radius = arcpy.GetParameterAsText(1)

arcpy.env.overWriteOutput = True
sR = arcpy.Describe(inputFeaturePoints).spatialReference
arcpy.env.outputCoordinateSystem = sR
arcpy.env.workspace = os.path.dirname(outputFeaturePoints)

unclusteredPointsList = shapefileToList(inputFeaturePoints)

radius = int(radius)
clusterPointsList = []
createClusters = True
while createClusters == True:
    randomCenterPoint = random.choice(unclusteredPointsList)
    clusterPointsList.append(randomCenterPoint)
    del unclusteredPointsList[unclusteredPointsList.index(randomCenterPoint)]
    unclusteredPointsList = deletePointsInCircle(randomCenterPoint, unclusteredPointsList, radius)
    if len(unclusteredPointsList) == 0:
        createClusters = False

pointArray = arcpy.Array()
for element in clusterPointsList:
    arcPoint = arcpy.Point(element.x, element.y)
    pointArray.add(arcPoint)

arcpy.CreateFeatureclass_management(os.path.dirname(outputFeaturePoints),\
os.path.basename(outputFeaturePoints),"POINT",\
template=inputFeaturePoints,\
spatial_reference=sR)

cursor = arcpy.da.InsertCursor(outputFeaturePoints, ['SHAPE@'])
for points in pointArray:
    cursor.insertRow([points])
del cursor

arcpy.SetParameter(1, outputFeaturePoints)
