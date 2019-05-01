#Ben and Rónán

import numpy as np

def tomorrow(dailyHum, hourlyVis, hours, dailyPress, dailyTemp):
    dayIndices = [0] #Indices that mark the start of a new day in the hourly values
    dailyVis = []
    for i in range(len(hours) - 1):
        if (int(hours[i][11:13]) > int(hours[i+1][11:13])):
            dayIndices.append(i + 1)
    
    for i in range(len(dayIndices)):
        if (i == (len(dayIndices) - 1)):
            dailyVis.append(np.average(hourlyVis[dayIndices[i:]]))
        else:
            dailyVis.append(np.average(hourlyVis[dayIndices[i]:dayIndices[i+1]]))
        
    return dailyVis

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