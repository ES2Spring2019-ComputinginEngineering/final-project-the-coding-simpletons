#Ben and Rónán

import numpy as np

#figure out how to make this take in any best date set and still work
def weights(bestDateSet, time):
    weights = []
    weekEndIndex = 0
    dates = []
    
    for i in range(len(time)):
        
        if (time[i][:10] in bestDateSet):
            
            if (time[i][:10] not in dates):
                dates.append(time[i][:10])
                
            if (len(dates) == (len(bestDateSet) - 1)): 
                weekEndIndex = i #the index of the first hourly value for the 8th day in the bestDateSet
                break #so as to avoid using the index of future hourly values on the 8th day
                
    weightSum = ((weekEndIndex)*(weekEndIndex + 1))/2 #the sum of the numbers from 1 to 57 using the formula n(n+1)/2
                                                      
    for i in range(1, (weekEndIndex+1)): #57 hourly values from the week prior to the 8th day
        weights.append(i/weightSum)
    
    return weights

def weightedValues(time, weights, data):
    weighted = []        
    
    for i in range(len(time[:-(len(time) - len(weights))])): #for each value in the past week
       weighted.append((data[i])*weights[i])
            
    prediction = np.sum(weighted)
    
    return prediction

def tomorrow(bestDateSet, time, humidity, pressure, visibility, temp, wind, Nhumidity, Npressure, Nvisibility):
    worth = weights(bestDateSet, time)
    
    #non-normalized values to be returned in the weather report
    nexthum= weightedValues(time, worth, humidity)
    nextpress= weightedValues(time, worth, pressure)
    nextvis= weightedValues(time, worth, visibility)
    nexttemp = weightedValues(time, worth, temp)
    nextwind = weightedValues(time, worth, wind)
    
    #normalized values used to predict if it's raining the next day
    Nnexthum= weightedValues(time, worth, Nhumidity)
    Nnextpress= weightedValues(time, worth, Npressure)
    Nnextvis= weightedValues(time, worth, Nvisibility)
    
    return nexthum, nextpress, nextvis, nexttemp, nextwind, Nnexthum, Nnextpress, Nnextvis


def predictedAccuracy(data, nextdata):
    actual = data[57:]
    percentError = np.abs(((nextdata - np.mean(actual))/(np.mean(actual)))*100)
    #uses the mean of the actual values because this gives an approximation of the daily value from the hourly values
    return percentError

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
    