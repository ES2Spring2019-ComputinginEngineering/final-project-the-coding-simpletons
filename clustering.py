#Ben and Rónán
import numpy as np
import matplotlib.pyplot as plt

# clustering

def create_centroids(K):    
    return np.random.random((K,3))

def assign(centroids, humidity, pressure, visibility):
    K = 2
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
    K = 2
    
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
    centroids = newcentroids 
    maxdist = np.abs(np.amax(discent)) 
    count = 0
    while maxdist >= (1*(10**(-300))): 
        newassignments = assign(centroids, humidity, pressure, visibility) 
        newcentroids = updateCent(centroids, newassignments, humidity, pressure, visibility)         
        discent = centroids - newcentroids 
        centroids = newcentroids 
        assignments = newassignments
        maxdist = np.amax(np.abs(discent)) 
        count += 1         
    print('Centroids moved ' + str(count) + ' times')
    assignments = assign(centroids, humidity, pressure, visibility)
    
    return centroids, assignments 

def graphing(K, humidity, visibility, pressure, centroid, newassignments):   
    centx = centroid[:,0]
    centy = centroid[:,1]
    centz = centroid[:,2]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(K):
        if (np.median(visibility[newassignments == i]) == 1):
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

    
    # making headings and a legend for the graph
    ax.set_xlabel('Humidity')
    ax.set_ylabel('Visibility')
    ax.set_zlabel('Pressure')
    ax.set_title('Classified Data Using ' + str(K) + ' Centroids')
    plt.legend(bbox_to_anchor = (1.43, 1.025))
    plt.show