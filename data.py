#Ben and Rónán 

import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def readDataFile():
    valuesOfInterest = []
    
    data = []
    index = 0
    dayIndices = []
    
    csv_file = open('weather.csv')

    numRows = sum(1 for row in csv_file)
    
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file, delimiter = ',')
    
    for row in csv_reader:
        data.append(row)
        if ('SOD' in row[2]):
            dayIndices.append(index)
        index += 1
        
    numDays = len(dayIndices)
    
    #Initializing daily values
    
    dates = [] 
    dailyTemp = [] # Daily dry bulb
    dailyHum = [] # Daily humidity
    dailySeaPress = [] # Daily sea pressure
    dailyDiffNormTemp = [] # Daily difference from normal temp
    dailyMaxTemp = [] # Daily dry bulb
    dailyMinTemp = [] # Daily dry bulb
    dailyWindDirec = [] # Daily sustained wind direction
    dailyPeakWind = [] # Daily gusting speeds
    dailyPrecip = [] # Daily precipitation
    dailyWindSpeed = [] # Daily sustained wind speeds
    
    badCounter = 0
    for i in range(numDays):
        try:
            data[dayIndices[i]][1][:10]
            float(data[dayIndices[i]][19])
            float(data[dayIndices[i]][20])
            float(data[dayIndices[i]][21])
            float(data[dayIndices[i]][26])
            float(data[dayIndices[i]][28])
            float(data[dayIndices[i]][29])
            float(data[dayIndices[i]][35])
            float(data[dayIndices[i]][31])
            float(data[dayIndices[i]][32])
            float(data[dayIndices[i]][36])
        except:
            badCounter += 1
        else: #completed for days when all values can be converted to floats (cells not empty or letters)
            dates.append(data[dayIndices[i]][1][:10])
            dailyTemp.append(float(data[dayIndices[i]][19]))
            dailyHum.append(float(data[dayIndices[i]][20]))
            dailySeaPress.append(float(data[dayIndices[i]][21]))
            dailyDiffNormTemp.append(float(data[dayIndices[i]][26]))
            dailyMaxTemp.append(float(data[dayIndices[i]][28]))
            dailyMinTemp.append(float(data[dayIndices[i]][29]))
            dailyWindDirec.append(float(data[dayIndices[i]][35]))
            dailyPeakWind.append(float(data[dayIndices[i]][31]))
            dailyPrecip.append(float(data[dayIndices[i]][32]))
            dailyWindSpeed.append(float(data[dayIndices[i]][36]))
            
    print(str(badCounter) + ' daily values did not contain useable data')
    
    #Initializing hourly values
   
    hours = [] # Time values, by the hour-ish
    hourlyTemp = [] # Hourly dry bulb temps
    hourlyPrecip = [] # Hourly precipitation
    hourlySeaPress = [] # Hourly sea level pressure
    hourlyHum = [] # Hourly relative humidity
    hourlyVis = [] # Hourly visibility
    hourlyPeakWind = [] # Hourly peak wind speed
    hourlyWindSpeed = [] # Hourly sustained wind speed
            
    badCounter2 = 0
    for i in range(numRows):
        try:
            data[i][1][11:]
            float(data[i][43])
            float(data[i][44])
            float(data[i][49])
            float(data[i][48])
            float(data[i][52])
            float(data[i][55])
            float(data[i][56])
        except:
            badCounter2 += 1
        else: #completed for hours when all values can be converted to floats (cells not empty or letters)
            hours.append(data[i][1][11:])
            hourlyTemp.append(float(data[i][43]))
            hourlyPrecip.append(float(data[i][44]))
            hourlySeaPress.append(float(data[i][49]))
            hourlyHum.append(float(data[i][48]))
            hourlyVis.append(float(data[i][52]))
            hourlyPeakWind.append(float(data[i][55]))
            hourlyWindSpeed.append(float(data[i][56]))
            
    print(str(badCounter2) + ' hourly values did not contain useable data')
            
    #Normalization and array conversion
    
    ndailyTemp = np.zeros(len(dailyTemp))
    ndailyHum = np.zeros(len(dailyHum))
    ndailySeaPress = np.zeros(len(dailySeaPress))
    ndailyDiffNormTemp = np.zeros(len(dailyDiffNormTemp))
    ndailyMaxTemp = np.zeros(len(dailyMaxTemp))
    ndailyMinTemp = np.zeros(len(dailyMinTemp))
    ndailyWindDirec = np.zeros(len(dailyWindDirec))
    ndailyPeakWind = np.zeros(len(dailyPeakWind))
    ndailyPrecip = np.zeros(len(dailyPrecip))
    ndailyWindSpeed = np.zeros(len(dailyWindSpeed))
    
    nhourlyTemp = np.zeros(len(hourlyTemp))
    nhourlyPrecip = np.zeros(len(hourlyPrecip))
    nhourlySeaPress = np.zeros(len(hourlySeaPress))
    nhourlyHum = np.zeros(len(hourlyHum))
    nhourlyVis = np.zeros(len(hourlyVis))
    nhourlyPeakWind = np.zeros(len(hourlyPeakWind))
    nhourlyWindSpeed = np.zeros(len(hourlyWindSpeed))
    

    for i in range(len(dates)):
        ndailyTemp[i] = (dailyTemp[i] - np.amin(dailyTemp))/(np.amax(dailyTemp)- np.amin(dailyTemp))
        ndailyHum[i] = (dailyHum[i] - np.amin(dailyHum))/(np.amax(dailyHum)- np.amin(dailyHum))
        ndailySeaPress[i] = (dailySeaPress[i] - np.amin(dailySeaPress))/(np.amax(dailySeaPress)- np.amin(dailySeaPress))
        ndailyDiffNormTemp[i] = (dailyDiffNormTemp[i] - np.amin(dailyDiffNormTemp))/(np.amax(dailyDiffNormTemp)- np.amin(dailyDiffNormTemp))
        ndailyMaxTemp[i] = (dailyMaxTemp[i] - np.amin(dailyMaxTemp))/(np.amax(dailyMaxTemp)- np.amin(dailyMaxTemp))
        ndailyMinTemp[i] = (dailyMinTemp[i] - np.amin(dailyMinTemp))/(np.amax(dailyMinTemp)- np.amin(dailyMinTemp))
        ndailyWindDirec[i] = (dailyWindDirec[i] - np.amin(dailyWindDirec))/(np.amax(dailyWindDirec)- np.amin(dailyWindDirec))
        ndailyPeakWind[i] = (dailyPeakWind[i] - np.amin(dailyPeakWind))/(np.amax(dailyPeakWind)- np.amin(dailyPeakWind))
        ndailyPrecip[i] = (dailyPrecip[i] - np.amin(dailyPrecip))/(np.amax(dailyPrecip)- np.amin(dailyPrecip))
        ndailyWindSpeed[i] = (dailyWindSpeed[i] - np.amin(dailyWindSpeed))/(np.amax(dailyWindSpeed)- np.amin(dailyWindSpeed))
   
    for i in range(len(hours)):
        nhourlyTemp[i] = (hourlyTemp[i] - np.amin(hourlyTemp))/(np.amax(hourlyTemp)- np.amin(hourlyTemp))
        nhourlyPrecip[i] = (hourlyPrecip[i] - np.amin(hourlyPrecip))/(np.amax(hourlyPrecip)- np.amin(hourlyPrecip))
        nhourlySeaPress[i] = (hourlySeaPress[i] - np.amin(hourlySeaPress))/(np.amax(hourlySeaPress)- np.amin(hourlySeaPress))
        nhourlyHum[i] = (hourlyHum[i] - np.amin(hourlyHum))/(np.amax(hourlyHum)- np.amin(hourlyHum))
        nhourlyVis[i] = (hourlyVis[i] - np.amin(hourlyVis))/(np.amax(hourlyVis)- np.amin(hourlyVis))
        nhourlyPeakWind[i] = (hourlyPeakWind[i] - np.amin(hourlyPeakWind))/(np.amax(hourlyPeakWind)- np.amin(hourlyPeakWind))
        nhourlyWindSpeed[i] = (hourlyWindSpeed[i] - np.amin(hourlyWindSpeed))/(np.amax(hourlyWindSpeed)- np.amin(hourlyWindSpeed))

    
    valuesOfInterest.append(dates)
    valuesOfInterest.append(ndailyTemp)
    valuesOfInterest.append(ndailyHum)
    valuesOfInterest.append(ndailySeaPress)
    valuesOfInterest.append(ndailyDiffNormTemp)
    valuesOfInterest.append(ndailyMaxTemp)
    valuesOfInterest.append(ndailyMinTemp)
    valuesOfInterest.append(ndailyWindDirec)
    valuesOfInterest.append(ndailyPeakWind)
    valuesOfInterest.append(ndailyPrecip)
    valuesOfInterest.append(ndailyWindSpeed)
    
        
    valuesOfInterest.append(hours)
    valuesOfInterest.append(nhourlyTemp)
    valuesOfInterest.append(nhourlyPrecip)
    valuesOfInterest.append(nhourlySeaPress)
    valuesOfInterest.append(nhourlyHum)
    valuesOfInterest.append(nhourlyVis)
    valuesOfInterest.append(nhourlyPeakWind)
    valuesOfInterest.append(nhourlyWindSpeed)
    
    return valuesOfInterest

def Class_rain(percip):
    class_rain = np.zeros(percip.size)
    for i in range(percip.size):
        if percip[i] == 0:  #yo why doesn't this work?
            class_rain[i] = 0
        else:
            class_rain[i] = 1
    print(class_rain)
    return class_rain


def trending(values):
    change = []
    length = values.size
    final_day = values[length - 1]
    for i in range(length - 2):
        delta = (values[i+1] - values[i])
        change.append(delta)
    avechange = np.mean(change)
    next_day = final_day + avechange
    return next_day

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
    return raining

def graphData(pressure, humidity, windspeed, visibility, temperature, precipitation, newx, newy, newz):
    # graphing our parsed, and normalized data 
    sevenday= precipitation[0:169]
    plt.plot(pressure[0:169] ,humidity[0:169] ,'b.',label='Rain')
    plt.plot(pressure[0:169][sevenday==0],humidity[0:169][sevenday==0],'r.',label ='No rain')
    plt.plot(newx, newy, 'g*', label='Tomorrow')
    plt.xlabel('Pressure')
    plt.ylabel('Humidity')
    plt.legend(loc = 3)
    plt.title('7 Day Hourly Pressure and Humidity with Prediction')
    plt.show()
    
    # graphing our parsed, and normalized data 
    plt.plot(pressure[precipitation!=0],humidity[precipitation!=0],'b.',label='Rain')
    plt.plot(pressure[precipitation==0],humidity[precipitation==0],'r.',label ='No rain')
    plt.plot(newx, newy, 'g*', label='Tomorrow')
    plt.xlabel('Pressure')
    plt.ylabel('Humidity')
    plt.legend(loc = 3)
    plt.title('All Pressure and Humidity with Prediction')
    plt.show()
    
    # graphing our parsed, and normalized data with color intensitites for amount of rain
    plt.scatter(pressure, humidity, c = precipitation, cmap=cm.Blues)
    plt.plot(newx, newy, 'g*', label='Tomorrow')
    plt.colorbar(label='Precipitation')
    plt.xlabel('Pressure')
    plt.ylabel('Humidity')
    plt.legend(loc = 3)
    plt.title('All Pressure and Humidity with Prediction')
    plt.show()
    
    # graphing our parsed, and normalized data 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(elev=50, azim=200)
    ax.scatter(humidity[precipitation!=0], visibility[precipitation!=0], pressure[precipitation!=0], label='Rain')
    ax.scatter(humidity[precipitation==0], visibility[precipitation==0], pressure[precipitation==0], label ='No rain')
    ax.scatter(newx, newy, newz, color = 'black', label='Tomorrow')
    ax.set_xlabel('Humidity')
    ax.set_ylabel('Visibility')
    ax.set_zlabel('Pressure')
    ax.legend(loc = 3)
    ax.set_title('Pressure, Humidity, and Visibility Classified by Precipitationn\n', fontsize = 14)
    plt.show()
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(humidity[precipitation!=0], visibility[precipitation!=0], pressure[precipitation!=0], label='Rain')
    ax.scatter(humidity[precipitation==0], visibility[precipitation==0], pressure[precipitation==0], label ='No rain')
    ax.scatter(newx, newy, newz, color = 'black', label='Tomorrow')
    ax.set_xlabel('Humidity')
    ax.set_ylabel('Visibility')
    ax.set_zlabel('Pressure')
    ax.legend(loc = 3)
    ax.set_title('Pressure, Humidity, and Visibility Classified by Precipitationn\n', fontsize = 14)
    plt.show()
    """
    #graphs every unqiue pair of the selected hourly variables
    selectValues = [pressure, humidity, windspeed, visibility, temperature]
    selectLabels = ['pressure', 'humidity', 'windspeed', 'visibility', 'temperature']
    for i in range(len(selectValues)):
        for j in range(len(selectValues)):
            if (j > i):
                # graphing our parsed, and normalized data 
                plt.plot(selectValues[i][precipitation!=0],selectValues[j][precipitation!=0],'b.',label='Rain')
                plt.plot(selectValues[i][precipitation==0],selectValues[j][precipitation==0],'r.',label ='No rain')
                plt.xlabel(selectLabels[i])
                plt.ylabel(selectLabels[j])
                plt.legend(loc = 3)
                plt.title(selectLabels[j] + ' vs. ' + selectLabels[i])
                plt.show()
    """
    
# clustering

def create_centroids(K):    
    return np.random.random((K,3))

def assign(centroids, humidity, pressure, visibility):
    K = 3
    distances = np.zeros((K, len(visibility)))
    
    for i in range(K):
        z = centroids[i,2]
        y = centroids[i,1] 
        x = centroids[i,0] 
        
        distances[i] = np.sqrt(((x-humidity)**2)+((y-visibility)**2)+((z-pressure)**2))
        
    assignments = np.argmin(distances, axis = 0)  
          
    return assignments

def updateCent(centroids, assignments, humidity, pressure, visibility):
    K = 3
    
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
        
    return newcentroids # returns the array of new centroids

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
    print('Centroids moved ' + str(count) + ' times') # to check that the function ran
    assignments = assign(centroids, humidity, pressure, visibility)
    
    return centroids, assignments 

#graphing centroids
    
def graphing(K, humidity, visibility, pressure, centroid, newassignments):    #seperating the centroid array so that it can be cycled through in the loop
    centx = centroid[:,0]
    centy = centroid[:,1]
    centz = centroid[:,2]
    
    for i in range(K):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        centlabel = 'Case ' + str(i) 
        ax.scatter(centx[i], centy[i], centz[i], label = centlabel) 
        labelname = 'Case ' + str(i) 
        ax.scatter(humidity[newassignments==i],visibility[newassignments==i], visibility[newassignments==i],label = labelname) 
        
    '''
    # making headings and a legend for the graph
    plt.xlabel('Hemoglobin')
    plt.ylabel('Glucose')
    plt.title('Classified Data Using ' + str(K) + ' Centroids')
    plt.legend(bbox_to_anchor = (1.25, 1.025)) # positioning the legend so that it does not interfere with the data points
    '''
    plt.show()


#def interpolationPredictions: (use daily values, interpolate last week or so)
dates, dailyTemp, dailyHum, dailySeaPress, dailyDiffNormTemp, dailyMaxTemp, dailyMinTemp, dailyWindDirec, dailyPeakWind, dailyPrecip, dailyWinds, hours, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind = readDataFile()

next_hum = trending(hourlyhum)
next_press = trending(hourlyseapress)

#class_rain = Class_rain(hourlyprecip)

will_it_rain = nearest_neighbor(hourlyhum, hourlyseapress, hourlyprecip, next_hum, next_press)
is_it_raining = kNearestNeighborClassifier(hourlyhum, hourlyseapress, hourlyprecip, next_hum, next_press)

#graphData(hourlyseapress, hourlyhum, hourlyWind, hourlyVis, hourlytemp, hourlyprecip, next_hum, 0.5, next_press)

K=3
centroids = create_centroids(K)

final_centroids, assignments = iteration(centroids, hourlyhum, hourlyseapress, hourlyVis)

graphing(K, hourlyhum, hourlyVis, hourlyseapress, final_centroids, assignments)