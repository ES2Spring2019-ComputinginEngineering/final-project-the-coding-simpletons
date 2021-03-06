#Ben and Rónán

import numpy as np

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
    
    for i in range(len(time[:-(len(time) - len(weights))])): #weights each value in the past week
       weighted.append((data[i])*weights[i])
            
    prediction = np.sum(weighted)
    
    return prediction


def tomorrow(bestDateSet, bTime, bHourlyHum, bHourlyPress, bHourlyVis, bHourlyTemp, bHourlyWind, bnHourlyHum, bnHourlyPress, bnHourlyVis):
    worth = weights(bestDateSet, bTime)
    
    #non-normalized values to be returned in the weather report
    nextHum= weightedValues(bTime, worth, bHourlyHum)
    nextPress= weightedValues(bTime, worth, bHourlyPress)
    nextVis= weightedValues(bTime, worth, bHourlyVis)
    nextTemp = weightedValues(bTime, worth, bHourlyTemp)
    nextWind = weightedValues(bTime, worth, bHourlyWind)
    
    #normalized values used to predict if it's raining the next day
    nextnHum= weightedValues(bTime, worth, bnHourlyHum)
    nextnPress= weightedValues(bTime, worth, bnHourlyPress)
    nextnVis= weightedValues(bTime, worth, bnHourlyVis)
    
    return nextHum, nextPress, nextVis, nextTemp, nextWind, nextnHum, nextnPress, nextnVis

def predictedAccuracy(data, nextData):
    actual = data[57:]
    percentError = np.abs(((nextData - np.mean(actual))/(np.mean(actual)))*100)
    #uses the mean of the actual values because this gives an approximation of the daily value from the hourly values
    
    return percentError

#In addition to using the median we could use the percentage of nearest points that are rain to predict likelihood
def kNearestNeighborClassifier(nHourlyHum, nHourlyPress, nHourlyVis, nHourlyPrecip, nextnHum, nextnPress, nextnVis):
    closest = np.zeros(10)
    distance_arr = np.zeros(len(nHourlyHum))
    
    for i in range(nHourlyHum.size):
        distance_squared = (((nHourlyHum[i]-nextnHum)**2)+((nHourlyPress[i]-nextnPress)**2)+((nHourlyVis[i]-nextnVis)**2))
        distance = np.sqrt(distance_squared)
        distance_arr[i] = distance
        
    indexes = np.argsort(distance_arr)
    
    for i in range(10):
        closest[i] = nHourlyPrecip[indexes[i]]  
    raining = int(np.median(closest)) # overall rain calssification
    
    # calculating chance of rain
    rain = 0
    for i in range(closest.size):
        if (closest[i] > 0): 
            rain += 1
    likelihood = (rain/10)*100
    
    return raining, likelihood

