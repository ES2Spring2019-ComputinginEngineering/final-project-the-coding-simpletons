#Ben and Rónán
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3D clustering
def create_centroids(K):    
    return np.random.random((K,3))

def assign(centroids, nHourlyHum, nHourlyPress, nHourlyVis):
    K = centroids.shape[0]
    distances = np.zeros((K, nHourlyVis.size))
    
    for i in range(K):
        z = centroids[i,2]
        y = centroids[i,1] 
        x = centroids[i,0] 
        
        #fills each row with an array of the distances from each data point to the current centroid
        distances[i] = np.sqrt(((x-nHourlyHum)**2)+((y-nHourlyVis)**2)+((z-nHourlyPress)**2))
        
    #returns the index of the minimum distance from each point to the K centroids which is also the nearest centroid    
    assignments = np.argmin(distances, axis = 0)  
    
    #prevents assignments from failing and classifying all points into the same assignment
    check = True
    for i in range(K):
        if (i not in assignments):
            check = False
            
    if (check):
        return assignments
    else: #repeat process to return good assignments
        centroids = create_centroids(K)
        assignments = assign(centroids, nHourlyHum, nHourlyPress, nHourlyVis)
        return assignments
    
def updateCent(centroids, assignments, nHourlyHum, nHourlyPress, nHourlyVis):
    K = centroids.shape[0]
    newCentroids = np.zeros(centroids.shape)
    
     #for each centroid
    for i in range(K): 
        hum = [] 
        press = []
        vis = []
        
         #for every data point
        for j in range(assignments.size): 
            if assignments[j] == i: 
                hum.append(nHourlyHum[j])
                press.append(nHourlyPress[j])
                vis.append(nHourlyVis[j])
        
        #updates centroid locations        
        newCentroids[i,0] = np.mean(hum)
        newCentroids[i,1] = np.mean(vis)
        newCentroids[i,2] = np.mean(press)
        
    return newCentroids 

def iteration(centroids, nHourlyHum, nHourlyPress, nHourlyVis):
    pastCentroids = centroids    
    newAssignments = assign(centroids, nHourlyHum, nHourlyPress, nHourlyVis) 
    newcentroids = updateCent(centroids, newAssignments, nHourlyHum, nHourlyPress, nHourlyVis)
    
    disCent = pastCentroids - newcentroids  
    maxDist = np.abs(np.amax(disCent)) #arbitrary value to start the loop, just has to be greater than (10**-100)
    
    pastCentroids = newcentroids
    
    while (maxDist > (10**(-100))): 
        newAssignments = assign(pastCentroids, nHourlyHum, nHourlyPress, nHourlyVis) 
        newcentroids = updateCent(pastCentroids, newAssignments, nHourlyHum, nHourlyPress, nHourlyVis)
         
        disCent = pastCentroids - newcentroids 
        
        maxDist = np.amax(np.abs(disCent)) 
        
        pastCentroids = newcentroids 
    
    return pastCentroids, newAssignments 

def clusterAccuracy(nHourlyHum, nHourlyVis, nHourlyPress, assignments, nHourlyPrecip, finalCentroids):
    K = finalCentroids.shape[0]
    newCentroids = finalCentroids
    newAssignments = assignments
    falsePositives = 0
    falseNegatives = 0
    truePositives = 0
    trueNegatives = 0
    positives = 0 
    negatives = 0
      
    #this loop ensures that the clusters identified are rain/no rain clusters. It will not run if
    #both clusters are no rain clusters (when the median visibility of both clusters is a 1 (i.e. clear day))
    while (((np.median(nHourlyVis[newAssignments == 0])) == 1) and (np.median(nHourlyVis[newAssignments == 1]) == 1)):
        newCentroids = create_centroids(K)
        newCentroids, newAssignments = iteration(newCentroids, nHourlyHum, nHourlyPress, nHourlyVis)
        
    if (np.median(newAssignments) == 0): #no rain assignments are 0, since they make up the majority of the weather
        for i in range(newAssignments.size):
                if ((newAssignments[i] == 1) and (nHourlyPrecip[i] != 0)):
                    truePositives += 1
                    positives += 1
                elif((newAssignments[i] == 0) and (nHourlyPrecip[i] == 0)):
                    trueNegatives += 1
                    negatives += 1
                elif((newAssignments[i] == 1) and (nHourlyPrecip[i] == 0)):
                    falsePositives += 1
                    negatives += 1
                else:
                    falseNegatives += 1
                    positives += 1
    else: #no rain assignments are 1
        for i in range(newAssignments.size):
                if ((newAssignments[i] == 0) and (nHourlyPrecip[i] != 0)):
                    truePositives += 1
                    positives += 1
                elif((newAssignments[i] == 1) and (nHourlyPrecip[i] == 0)):
                    trueNegatives += 1
                    negatives += 1
                elif((newAssignments[i] == 0) and (nHourlyPrecip[i] == 0)):
                    falsePositives += 1
                    negatives += 1
                else:
                    falseNegatives += 1
                    positives += 1
    
    print('\nFalse Positives Rate: ' + str(round(((falsePositives/negatives)*100), 2)) + '%')
    print('False Negatives Rate: ' + str(round(((falseNegatives/positives)*100), 2)) + '%')
    print('True Positives Rate: ' + str(round(((truePositives/positives)*100), 2)) + '%')
    print('True Negatives Rate: ' + str(round(((trueNegatives/negatives)*100), 2)) + '%\n')

def denormalizeCent(centroids, hourlyHum, hourlyVis, hourlyPress):
    values = [hourlyHum, hourlyVis, hourlyPress]
    returnCentroids = np.zeros((centroids.shape[0], centroids.shape[1]))
    
    #populates returnCentroids with the denormalized values
    for i in range(centroids.shape[0]):
        for j in range(centroids.shape[1]):
            maximum = np.amax(values[j])
            minimum = np.amin(values[j])
            returnCentroids[i][j] = (centroids[i][j]*(maximum-minimum)) + minimum
            
    return returnCentroids
                     
def graphing(nHourlyHum, nHourlyVis, nHourlyPress, hourlyHum, hourlyVis, hourlyPress, centroids, newAssignments):
    K = centroids.shape[0]

    fig = plt.figure(figsize = (8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.dist = 12 #viewing distance
    
    #this loop ensures that the clusters identified are rain/no rain clusters. It will not run if
    #both clusters are no rain clusters (when the median visibility of both clusters is a 1 (i.e. clear day))
    while (((np.median(nHourlyVis[newAssignments == 0])) == 1) and (np.median(nHourlyVis[newAssignments == 1]) == 1)):
        centroids = create_centroids(K)
        centroids, newAssignments = iteration(centroids, nHourlyHum, nHourlyPress, nHourlyVis)
    
    newCentroids = denormalizeCent(centroids, hourlyHum, hourlyVis, hourlyPress)    
    centx = newCentroids[:,0]
    centy = newCentroids[:,1]
    centz = newCentroids[:,2]
    
    for i in range(K):
        if (np.median(nHourlyVis[newAssignments == i]) == 1):
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
        ax.scatter(hourlyHum[newAssignments==i], hourlyVis[newAssignments==i], hourlyPress[newAssignments==i], color = valuecolor, label = labelname) 
    
    ax.set_xlabel('\n\nRelative Humidity\n(%)', fontsize = 12)
    ax.set_ylabel('\n\nVisibility\n(miles)', fontsize = 12)
    ax.set_zlabel('\n\nPressure\n(inches of mercurcy)', fontsize = 12)
    ax.legend(bbox_to_anchor = (1.15, 1))
    ax.set_title('Pressure, Humidity, and Visibility\n Classified Using ' + str(K) + ' Centroids\n(Hourly Values Jan-April 2019)', fontsize = 14)
    plt.show