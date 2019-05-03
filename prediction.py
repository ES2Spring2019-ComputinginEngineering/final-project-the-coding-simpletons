#Ben and Rónán

import numpy as np

def weights(best, time, data):
    weights=[1, ((np.e)**(1/2)),np.e,((np.e)**(3/2)), ((np.e)**(2)),((np.e)**(5/2)),((np.e)**(3))]
    weighted=[]
    for i in range(len(time)):
        if time[i][:10] == best[0]:
            weighted.append((data[i])*weights[0])
        elif time[i][:10]== best[1]:
            weighted.append((data[i])*weights[1])
        elif time[i][:10]== best[2]:
            weighted.append((data[i])*weights[2])
        elif time[i][:10]== best[3]:
            weighted.append((data[i])*weights[3])
        elif time[i][:10]== best[4]:
            weighted.append((data[i])*weights[4])
        elif time[i][:10]== best[5]:
            weighted.append((data[i])*weights[5])
        elif time[i][:10]== best[6]:
            weighted.append((data[i])*weights[6])
    prediction = np.mean(weighted)
    return prediction

def tomorrow(best, dates, humidity, visibility, pressure, temp, wind, Nhumidity, Nvisibility, Npressure, Ntemp, Nwind):
    Nnexthum= weights(best, dates, Nhumidity)
    Nnextvis= weights(best, dates, Nvisibility)
    Nnextpress= weights(best, dates, Npressure)
    Nnexttemp = weights(best, dates, Ntemp)
    Nnextwind = weights(best, dates, Nwind)
    nexthum= weights(best, dates, humidity)
    nextvis= weights(best, dates, visibility)
    nextpress= weights(best, dates, pressure)
    nexttemp = weights(best, dates, temp)
    nextwind = weights(best, dates, wind)
    
    return nexthum, nextvis, nextpress, nexttemp, nextwind, Nnexthum, Nnextvis, Nnextpress, Nnexttemp, Nnextwind
        

#SOMEHOW CHECK WHICH DAYS THESE HOURLY VALUES ARE ASSOCIATED WITH? DO WE HAVE ONE WEEK REPRESENTED?
        

def nearest_neighbor(type_1, type_2, percip, new_1, new_2):
    distance_arr = np.zeros(type_1.size)
    for i in range(type_1.size):
        distance_squared = (((type_1[i]-new_1)**2)+(type_2[i]-new_2)**2)
        distance = np.sqrt(distance_squared)
        distance_arr[i] = distance
    smallesti = np.argmin(distance_arr)
    raining = int(percip[smallesti])
    return raining


#Instead of Using Median we could use Percentage of nearest points that are rain to predict likelihood
def kNearestNeighborClassifier(type_1, type_2, percip, new_1, new_2):
    closest = np.zeros(5)
    distance_arr = np.zeros(type_1.size)
    for i in range(type_1.size):
        distance_squared = (((type_1[i]-new_1)**2)+(type_2[i]-new_2)**2)
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
    