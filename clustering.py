#Ben and Rónán
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# clustering

def create_centroids(K):    
    return np.random.random((K,3))

def assign(centroids, humidity, pressure, visibility):
    K = centroids.shape[0]
    distances = np.zeros((K, len(visibility)))
    
    for i in range(K):
        z = centroids[i,2]
        y = centroids[i,1] 
        x = centroids[i,0] 
        
        distances[i] = np.sqrt(((x-humidity)**2)+((y-visibility)**2)+((z-pressure)**2))
        
    assignments = np.argmin(distances, axis = 0)  
    
    if (0 in assignments) and (1 in assignments):# and (2 in assignments):
        return assignments
    else:
        centroids = create_centroids(K)
        assignments = assign(centroids, humidity, pressure, visibility)
        return assignments
    
def updateCent(centroids, assignments, humidity, pressure, visibility):
    K = centroids.shape[0]
    
    newcentroids = np.zeros(centroids.shape)
    
    for i in range(K): 
        hum = [] 
        press = []
        vis = []
        for j in range(assignments.size): 
            if assignments[j] == i: 
                hum.append(humidity[j])
                press.append(pressure[j])
                vis.append(visibility[j])
        newcentroids[i,0] = np.mean(hum)
        newcentroids[i,1] = np.mean(vis)
        newcentroids[i,2] = np.mean(press)
        
    return newcentroids 

def iteration(centroids, humidity, pressure, visibility):    
    assignments = assign(centroids, humidity, pressure, visibility) 
    newcentroids = updateCent(centroids, assignments, humidity, pressure, visibility)
    
    discent = centroids - newcentroids  
    maxdist = np.abs(np.amax(discent))
    
    centroids = newcentroids
    
    count = 0
    
    while (maxdist >= (10**(-100))): 
        newassignments = assign(centroids, humidity, pressure, visibility) 
        newcentroids = updateCent(centroids, newassignments, humidity, pressure, visibility)
         
        discent = centroids - newcentroids 
        
        maxdist = np.amax(np.abs(discent)) 
        count += 1         
        
        centroids = newcentroids 
        assignments = newassignments
        
    print('\nCentroids moved ' + str(count) + ' times\n')
    assignments = assign(centroids, humidity, pressure, visibility)
    
    return centroids, assignments 

def clusterAccuracy(predClassification, dataClassification, finalCentroids, visibility):
    
    falsePositives = 0
    falseNegatives = 0
    truePositives = 0
    trueNegatives = 0
    positives = 0 
    negatives = 0
    
    #if (np.median(visibility[predClassification == i]) == 1): #If visibilities are mostly 1, this is the non-rain cluster
    """
    for i in range(predClassification.size):
            if(predClassification[i] == dataClassification[i]):
                if(predClassification[i] == 1):
                    truePositives += 1
                    positives += 1
                else:
                    trueNegatives += 1
                    negatives += 1
            else:
                if(predClassification[i] == 0):
                    falsePositives += 1
                    positives += 1
                else:
                    falseNegatives += 1
                    negatives += 1
    """
    print('False Positives Rate: ' + str((falsePositives/positives)*100))
    print('False Negatives Rate: ' + str((falseNegatives/negatives)*100))
    print('True Positives Rate: ' + str((truePositives/positives)*100))
    print('True Negatives Rate: ' + str((trueNegatives/negatives)*100))
    print('(Values given in percent)')
                        
def graphing(humidity, visibility, pressure, centroids, newassignments):
    K = centroids.shape[0]
    centx = centroids[:,0]
    centy = centroids[:,1]
    centz = centroids[:,2]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for i in range(K):
        ax.scatter(centx[i], centy[i], centz[i], marker = '*', s = 300, label = 'Centroid ' + str(i))  
        ax.scatter(humidity[newassignments==i],visibility[newassignments==i], pressure[newassignments==i], label = 'Cluster ' + str(i))
        """
        centlabel = 'Centroid NA' 
        labelname = 'NA'
        centcolor = 'magenta'
        valuecolor = 'chartreuse'
        if (np.mean(visibility[newassignments == i]) == 1):
            centlabel = 'Centroid No Rain' 
            labelname = 'No Rain'
            centcolor = 'maroon'
            valuecolor = 'orange'
        else:
            centlabel = 'Centroid Rain'
            labelname = 'Rain'
            centcolor = 'blue'
            valuecolor = 'teal'

        ax.scatter(centx[i], centy[i], centz[i], marker = '*', s = 300, color = centcolor, label = centlabel)  
        ax.scatter(humidity[newassignments==i],visibility[newassignments==i], pressure[newassignments==i], color = valuecolor, label = labelname) 
        """
    
    # making headings and a legend for the graph
    ax.set_xlabel('Humidity')
    ax.set_ylabel('Visibility')
    ax.set_zlabel('Pressure')
    ax.set_title('Classified Data Using ' + str(K) + ' Centroids', fontsize = 14)
    plt.legend(bbox_to_anchor = (1.43, 1.025))
    plt.show