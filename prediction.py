#Ben and Rónán

import numpy as np

def weights(best, time, data):
    #1653 is 1 the sum of through 57
    weights = []
    for i in range(1, 58): #57 hourly values from the week prior to the 8th day
        weights.append(i/1653)
        
    weighted=[]
    for i in range(len(time[:-2])):
       weighted.append((data[i])*weights[i])
            
    prediction = np.sum(weighted)
    
    return prediction

def tomorrow(best, time, humidity, pressure, visibility, temp, wind, Nhumidity, Nvisibility, Npressure, Ntemp, Nwind):
    Nnexthum= weights(best, time, Nhumidity)
    Nnextvis= weights(best, time, Nvisibility)
    Nnextpress= weights(best, time, Npressure)
    Nnexttemp = weights(best, time, Ntemp)
    Nnextwind = weights(best, time, Nwind)
    
    nexthum= weights(best, time, humidity)
    nextvis= weights(best, time, visibility)
    nextpress= weights(best, time, pressure)
    nexttemp = weights(best, time, temp)
    nextwind = weights(best, time, wind)
    
    return nexthum, nextvis, nextpress, nexttemp, nextwind, Nnexthum, Nnextvis, Nnextpress, Nnexttemp, Nnextwind

def predictedAccuracy(humidity, pressure, visibility, temp, wind, nexthum, nextvis, nextpress, nexttemp, nextwind):
    actualValues = [humidity[57:], visibility[57:], pressure[57:], temp[57:], wind[57:]]
    predictedValues = [nexthum, nextvis, nextpress, nexttemp, nextwind]
    values = ['humidity', 'visibility', 'pressure', 'temperature', 'wind']
    
    for i in range(len(values)):
        percentError = np.abs(((predictedValues[i] - np.mean(actualValues[i]))/(np.mean(actualValues[i])))*100)
        #uses the mean of the actual values because this gives an approximation of the daily value from the hourly values
        print('The percent error associated with the predicted ' + values[i] + ' value was:\n' + str(percentError) + '%')
        

def nearest_neighbor(humidity, pressure, visibility, precip, nhumidity, npressure, nvisibility):
    distance_arr = np.zeros(humidity.size)
    
    for i in range(humidity.size):
        distance_squared = (((humidity[i]-nhumidity)**2)+((pressure[i]-npressure)**2)+((visibility[i]-nvisibility)**2))
        distance = np.sqrt(distance_squared)
        distance_arr[i] = distance
        
    smallesti = np.argmin(distance_arr)
    raining = int(precip[smallesti])
    
    return raining


#In addition to using the median we could use the percentage of nearest points that are rain to predict likelihood
def kNearestNeighborClassifier(humidity, pressure, visibility, precip, nhumidity, npressure, nvisibility):
    closest = np.zeros(10)
    distance_arr = np.zeros(len(humidity))
    
    for i in range(len(humidity)):
        distance_squared = (((humidity[i]-nhumidity)**2)+((pressure[i]-npressure)**2)+((visibility[i]-nvisibility)**2))
        distance = np.sqrt(distance_squared)
        distance_arr[i] = distance
        
    indexes = np.argsort(distance_arr)
    
    for i in range(10):
        closest[i] = precip[indexes[i]] 
        
    raining = int(np.median(closest))
    
    rain = 0
    
    for i in range(closest.size):
        if (closest[i] > 0): 
            rain += 1
            
    likelihood = (rain/10)*100
    
    return raining, likelihood

# Getting our predicted values in terms of actual numbers
def denormalize(normal, data_set):
    maximum = np.amax(data_set)
    minimum = np.amin(data_set)
    value = (normal*(maximum-minimum)) + minimum
    return value
    