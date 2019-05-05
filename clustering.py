#Ben and Rónán
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3D clustering
def create_centroids(K):    
    return np.random.random((K,3))

def assign(centroids, humidity, pressure, visibility):
    K = centroids.shape[0]
    distances = np.zeros((K, visibility.size))
    
    for i in range(K):
        z = centroids[i,2]
        y = centroids[i,1] 
        x = centroids[i,0] 
        
        distances[i] = np.sqrt(((x-humidity)**2)+((y-visibility)**2)+((z-pressure)**2))
        
    assignments = np.argmin(distances, axis = 0)  
    
    if (0 in assignments) and (1 in assignments):
        return assignments
    else:
        centroids = create_centroids(K)
        assignments = assign(centroids, humidity, pressure, visibility)
        return assignments
    
def updateCent(centroids, assignments, humidity, pressure, visibility):
    K = centroids.shape[0]
    
    newCentroids = np.zeros(centroids.shape)
    
    for i in range(K): 
        hum = [] 
        press = []
        vis = []
        for j in range(assignments.size): 
            if assignments[j] == i: 
                hum.append(humidity[j])
                press.append(pressure[j])
                vis.append(visibility[j])
        newCentroids[i,0] = np.mean(hum)
        newCentroids[i,1] = np.mean(vis)
        newCentroids[i,2] = np.mean(press)
        
    return newCentroids 

def iteration(centroids, humidity, pressure, visibility):    
    assignments = assign(centroids, humidity, pressure, visibility) 
    newcentroids = updateCent(centroids, assignments, humidity, pressure, visibility)
    
    discent = centroids - newcentroids  
    maxdist = np.abs(np.amax(discent))
    
    centroids = newcentroids
    
    while (maxdist >= (10**(-100))): 
        newassignments = assign(centroids, humidity, pressure, visibility) 
        newcentroids = updateCent(centroids, newassignments, humidity, pressure, visibility)
         
        discent = centroids - newcentroids 
        
        maxdist = np.amax(np.abs(discent)) 
        
        centroids = newcentroids 
        assignments = newassignments
        
    assignments = assign(centroids, humidity, pressure, visibility)
    
    return centroids, assignments 

def clusterAccuracy(humidity, visibility, pressure, assignments, rain, finalCentroids):
    K = finalCentroids.shape[0]
    newCentroids = finalCentroids
    newAssignments = assignments
    falsePositives = 0
    falseNegatives = 0
    truePositives = 0
    trueNegatives = 0
    positives = 0 
    negatives = 0
    
    
    while (((np.median(visibility[newAssignments == 0])) == 1) and (np.median(visibility[newAssignments == 1]) == 1)):
        newCentroids = create_centroids(K)
        newCentroids, newAssignments = iteration(newCentroids, humidity, pressure, visibility)
        
    if (np.median(newAssignments) == 0):
        for i in range(newAssignments.size):
                if ((newAssignments[i] == 1) and (rain[i] != 0)):
                    truePositives += 1
                    positives += 1
                elif((newAssignments[i] == 0) and (rain[i] == 0)):
                    trueNegatives += 1
                    negatives += 1
                elif((newAssignments[i] == 1) and (rain[i] == 0)):
                    falsePositives += 1
                    negatives += 1
                else:
                    falseNegatives += 1
                    positives += 1
    else:
        for i in range(newAssignments.size):
                if ((newAssignments[i] == 0) and (rain[i] != 0)):
                    truePositives += 1
                    positives += 1
                elif((newAssignments[i] == 1) and (rain[i] == 0)):
                    trueNegatives += 1
                    negatives += 1
                elif((newAssignments[i] == 0) and (rain[i] == 0)):
                    falsePositives += 1
                    negatives += 1
                else:
                    falseNegatives += 1
                    positives += 1
    
    print('\nFalse Positives Rate: ' + str(round(((falsePositives/positives)*100), 2)) + '%')
    print('False Negatives Rate: ' + str(round(((falseNegatives/negatives)*100), 2)) + '%')
    print('True Positives Rate: ' + str(round(((truePositives/positives)*100), 2)) + '%')
    print('True Negatives Rate: ' + str(round(((trueNegatives/negatives)*100), 2)) + '%\n')
                        
def graphing(nhourlyhum, nhourlyVis, nhourlypress, hourlyhum, hourlyVis, hourlypress, centroids, newassignments):
    K = centroids.shape[0]

    fig = plt.figure(figsize = (8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.dist = 12 #viewing distance
    
    while (((np.median(nhourlyVis[newassignments == 0])) == 1) and (np.median(nhourlyVis[newassignments == 1]) == 1)):
        centroids = create_centroids(K)
        centroids, newassignments = iteration(centroids, nhourlyhum, nhourlypress, nhourlyVis)
        
    centx = centroids[:,0]
    centy = centroids[:,1]
    centz = centroids[:,2]
    
    for i in range(K):
        if (np.median(nhourlyVis[newassignments == i]) == 1):
            centlabel = 'No Rain Centroid' 
            labelname = 'No Rain'
            centcolor = 'maroon'
            valuecolor = 'orange'
        else:
            centlabel = 'Rain Centroid'
            labelname = 'Rain'
            centcolor = 'blue'
            valuecolor = 'teal'

        ax.scatter(centx[i], centy[i], centz[i], marker = '*', s = 300, color = centcolor, label = centlabel)  
        ax.scatter(hourlyhum[newassignments==i], hourlyVis[newassignments==i], hourlypress[newassignments==i], color = valuecolor, label = labelname) 
    
    # making headings and a legend for the graph
    ax.set_xlabel('\n\nRelative Humidity\n(%)', fontsize = 12)
    ax.set_ylabel('\n\nVisibility\n(miles)', fontsize = 12)
    ax.set_zlabel('\n\nPressure\n(inches of mercurcy)', fontsize = 12)
    ax.legend(bbox_to_anchor = (1.15, 1))
    ax.set_title('Pressure, Humidity, and Visibility\n Classified Using ' + str(K) + ' Centroids\n(Hourly Values Jan-April 2019)', fontsize = 14)
    plt.show