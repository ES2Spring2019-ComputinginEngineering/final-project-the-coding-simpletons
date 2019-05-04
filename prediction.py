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

def tomorrow(best, time, humidity, visibility, pressure, temp, wind, Nhumidity, Nvisibility, Npressure, Ntemp, Nwind):
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

def predictedAccuracy(humidity, visibility, pressure, temp, wind, nexthum, nextvis, nextpress, nexttemp, nextwind):
    actualValues = [humidity[57:], visibility[57:], pressure[57:], temp[57:], wind[57:]]
    predictedValues = [nexthum[57:], nextvis[57:], nextpress[57:], nexttemp[57:], nextwind[57:]]
    values = ['humidity', 'visibility', 'pressure', 'temperature', 'wind']
    for i in range(len(values)):
        percentError = ((predictedValues[i] - np.mean(actualValues[i]))/(np.mean(actualValues[i])))*100
        #uses the mean of the actual values because this gives an approximation of the daily value from the hourly values
        print('The percent error associated with the predicted ' + values[i] + ' value was ' + str(percentError) + '%')
        
"""
def tomorrow(best, time, humidity, visibility, pressure, temp, wind, Nhumidity, Nvisibility, Npressure, Ntemp, Nwind):
    weights=[(1/28), (2/28), (3/28), (4/28), (5/28), (6/28), (7/28)] #all add up to 1
    weighted=[]
    data = [humidity, visibility, pressure, temp, wind, Nhumidity, Nvisibility, Npressure, Ntemp, Nwind]
    arrData = np.asarray(data)
    
    for i in range(len(time)):
        if time[i][:10] == best[0]:
            weighted.append((arrData[:][i])*weights[0])
        elif time[i][:10]== best[1]:
            weighted.append((arrData[:][i])*weights[1])
        elif time[i][:10]== best[2]:
            weighted.append((arrData[:][i])*weights[2])
        elif time[i][:10]== best[3]:
            weighted.append((arrData[:][i])*weights[3])
        elif time[i][:10]== best[4]:
            weighted.append((arrData[:][i])*weights[4])
        elif time[i][:10]== best[5]:
            weighted.append((arrData[:][i])*weights[5])
        elif time[i][:10]== best[6]:
            weighted.append((arrData[:][i])*weights[6])
     
    return weighted
    #prediction = np.mean(weighted)
    #return nexthum, nextvis, nextpress, nexttemp, nextwind, Nnexthum, Nnextvis, Nnextpress, Nnexttemp, Nnextwind
"""
#SOMEHOW CHECK WHICH DAYS THESE HOURLY VALUES ARE ASSOCIATED WITH? DO WE HAVE ONE WEEK REPRESENTED?
        

def nearest_neighbor(type_1, type_2, type_3, percip, new_1, new_2, new_3):
    distance_arr = np.zeros(type_1.size)
    for i in range(type_1.size):
        distance_squared = (((type_1[i]-new_1)**2)+((type_2[i]-new_2)**2)+((type_3[i]-new_3)**2))
        distance = np.sqrt(distance_squared)
        distance_arr[i] = distance
    smallesti = np.argmin(distance_arr)
    raining = int(percip[smallesti])
    return raining


#Instead of Using Median we could use Percentage of nearest points that are rain to predict likelihood
def kNearestNeighborClassifier(type_1, type_2, type_3, percip, new_1, new_2, new_3):
    closest = np.zeros(5)
    distance_arr = np.zeros(type_1.size)
    for i in range(type_1.size):
        distance_squared = (((type_1[i]-new_1)**2)+((type_2[i]-new_2)**2)+((type_3[i]-new_3)**2))
        distance = np.sqrt(distance_squared)
        distance_arr[i] = distance
    indexes = np.argsort(distance_arr)
    for i in range(5):
        closest[i] = percip[indexes[i]] 
    raining = int(np.median(closest))
    rain = 0
    for i in range(closest.size):
        if closest[i] == 1:
            rain += 1
    percentage = rain / 5
    return raining, percentage

# Getting our predicted values in terms of actual numbers
def denormalize(normal, data_set):
    maximum = np.amax(data_set)
    minimum = np.amin(data_set)
    value = (normal*(maximum-minimum)) + minimum
    return value
    