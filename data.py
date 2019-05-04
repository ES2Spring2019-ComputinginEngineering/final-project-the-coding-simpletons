#Ben and Rónán 

import csv
import numpy as np
import matplotlib.pyplot as plt

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
        
    #Initializing hourly values
   
    time = [] # Time values, by the hour-ish
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
            time.append(data[i][1][:])
            hourlyTemp.append(float(data[i][43]))
            hourlyPrecip.append(float(data[i][44]))
            hourlySeaPress.append(float(data[i][49]))
            hourlyHum.append(float(data[i][48]))
            hourlyVis.append(float(data[i][52]))
            hourlyPeakWind.append(float(data[i][55]))
            hourlyWindSpeed.append(float(data[i][56]))
            
    #print(str(badCounter2) + ' hourly values did not contain useable data\n')
    
    
    #Makes a list of the dates with hourly values associated with them
    dates = []
    for i in time:
        if (i[:10] not in dates):
            dates.append(i[:10])
    
    
    #Measures the number of hourly associated with each day and removes the hourly values
    #from the list if two or less hourly values are associated with that day
    newTime = []              
    for i in range(len(dates)):
        
        counter = 1
        lowerIndex = 0
        upperIndex = 0
        
        for j in range(len(time) - 1):
            if (dates[i] in time[j]):
                if (counter == 1):
                    lowerIndex = j
                counter += 1 
                if ((time[j+1][:10] != dates[i]) or ((j+1) == (len(time) - 1))):
                   upperIndex = j+1
                   break
        if (counter > 2):
            newTime = newTime + time[lowerIndex:upperIndex]
            
    time = newTime
    
    
    #Removes the dates from the dates list that have two or less hourly values
    #associated with that day
    newDates = []
    for i in dates:
        for j in time:
            if (i in j):
                newDates.append(i)
                break
    dates = newDates
    
    
    dateRanges = [] #list of all the differents groupings of consecutive days
    cDateRange = [] #current date ranges, individual groupings of consecutive days
    pastIndex = 0
    for i in range(1, len(dates)):
        
        if (len(cDateRange) == 0):
            cDateRange.append(pastIndex)
            
        newIndex = i
        
        if (int(dates[newIndex][8:]) == (int(dates[pastIndex][8:]) + 1)):
            cDateRange.append(newIndex)
        else:
            dateRanges.append(cDateRange)
            cDateRange = []
            
        pastIndex = newIndex
      
    
    maxDays = 0 #maximum number of days grouped together
    maxIndices = [] #indices at which these maximum number of days are grouped in dateRanges
    for i in range(len(dateRanges)):
        if (len(dateRanges[i]) > maxDays):
            maxDays = len(dateRanges[i])
            maxIndices = [i]
        elif (len(dateRanges[i]) == maxDays):
            maxIndices.append(i)
    
    bestDateSet = [] #the longest group of dates
    for i in maxIndices:
        for j in dateRanges[i]:
            bestDateSet.append(dates[j])
    #print('The best set of days ranges from:\n' + str(bestDateSet[0]) + ' to ' + str(bestDateSet[maxDays - 1]))
    
    #Normalization and array conversion
    nhourlyTemp = np.zeros(len(hourlyTemp))
    nhourlyPrecip = np.zeros(len(hourlyPrecip))
    nhourlySeaPress = np.zeros(len(hourlySeaPress))
    nhourlyHum = np.zeros(len(hourlyHum))
    nhourlyVis = np.zeros(len(hourlyVis))
    nhourlyPeakWind = np.zeros(len(hourlyPeakWind))
    nhourlyWindSpeed = np.zeros(len(hourlyWindSpeed))
    
    for i in range(len(hourlyTemp)):
        nhourlyTemp[i] = (hourlyTemp[i] - np.amin(hourlyTemp))/(np.amax(hourlyTemp)- np.amin(hourlyTemp))
        nhourlyPrecip[i] = (hourlyPrecip[i] - np.amin(hourlyPrecip))/(np.amax(hourlyPrecip)- np.amin(hourlyPrecip))
        nhourlySeaPress[i] = (hourlySeaPress[i] - np.amin(hourlySeaPress))/(np.amax(hourlySeaPress)- np.amin(hourlySeaPress))
        nhourlyHum[i] = (hourlyHum[i] - np.amin(hourlyHum))/(np.amax(hourlyHum)- np.amin(hourlyHum))
        nhourlyVis[i] = (hourlyVis[i] - np.amin(hourlyVis))/(np.amax(hourlyVis)- np.amin(hourlyVis))
        nhourlyPeakWind[i] = (hourlyPeakWind[i] - np.amin(hourlyPeakWind))/(np.amax(hourlyPeakWind)- np.amin(hourlyPeakWind))
        nhourlyWindSpeed[i] = (hourlyWindSpeed[i] - np.amin(hourlyWindSpeed))/(np.amax(hourlyWindSpeed)- np.amin(hourlyWindSpeed))

    #adds these values to a list to be returned
    valuesOfInterest.append(bestDateSet)
    valuesOfInterest.append(time)
    valuesOfInterest.append(hourlyTemp)
    valuesOfInterest.append(hourlyPrecip)
    valuesOfInterest.append(hourlySeaPress)
    valuesOfInterest.append(hourlyHum)
    valuesOfInterest.append(hourlyVis)
    valuesOfInterest.append(hourlyPeakWind)
    valuesOfInterest.append(hourlyWindSpeed)
    valuesOfInterest.append(nhourlyTemp)
    valuesOfInterest.append(nhourlyPrecip)
    valuesOfInterest.append(nhourlySeaPress)
    valuesOfInterest.append(nhourlyHum)
    valuesOfInterest.append(nhourlyVis)
    valuesOfInterest.append(nhourlyPeakWind)
    valuesOfInterest.append(nhourlyWindSpeed)

    return valuesOfInterest

def sliceOfInterest(bestDateSet, time): #2/8/19 to 2/15/19 7 days to pull data from, 1 day to compare with predictions 
    start = 0 #start of the slice
    end = 0 #end of the slice
    dates = [] #used as a form of counter in this case so to know what dates have already been looked at
    for i in range(len(time)):
        
        if (time[i][:10] in bestDateSet):
            if (time[i][:10] not in dates):
                dates.append(time[i][:10])
            
            if (start == 0):
                start = i #the index of the first hourly value for the 1st day in the bestDateSet
                
            elif (len(dates) == len(bestDateSet)): 
                end = i #the index of the first hourly value for the 9th day in the bestDateSet
                break #to save time, ends the loop once the ending index has been found
    
    return [start, end]

def dataOfInterest(sliceRange, time, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind):
    returnValues = []
    a = sliceRange[0] #start of the slice
    b = sliceRange[1] #end of the slice
    
    returnValues.append(time[a:b])
    returnValues.append(hourlytemp[a:b])
    returnValues.append(hourlyprecip[a:b])
    returnValues.append(hourlyseapress[a:b])
    returnValues.append(hourlyhum[a:b])
    returnValues.append(hourlyVis[a:b])
    returnValues.append(hourlyPeakWind[a:b])
    returnValues.append(hourlyWind[a:b])
    returnValues.append(nhourlytemp[a:b])
    returnValues.append(nhourlyprecip[a:b])
    returnValues.append(nhourlyseapress[a:b])
    returnValues.append(nhourlyhum[a:b])
    returnValues.append(nhourlyVis[a:b])
    returnValues.append(nhourlyPeakWind[a:b])
    returnValues.append(nhourlyWind[a:b])
    
    return returnValues
    
def exploringGraphs(pressure, humidity, windspeed, visibility, temperature, precipitation):
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
                
def graphData3D(humidity, pressure, visibility, precipitation, nhum, npress, nvis):
    #matplotlib.use('MacOSX')
    #print(matplotlib.is_interactive())
    # graphing our parsed, and normalized data 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(elev=50, azim=200)
    ax.scatter(humidity[precipitation!=0], visibility[precipitation!=0], pressure[precipitation!=0], label='Rain')
    ax.scatter(humidity[precipitation==0], visibility[precipitation==0], pressure[precipitation==0], label ='No rain')
    ax.scatter(nhum, nvis, npress, color = 'black', label='Tomorrow')
    ax.set_xlabel('Humidity')
    ax.set_ylabel('Visibility')
    ax.set_zlabel('Pressure')
    ax.legend(bbox_to_anchor = (1.43, 1.025))
    ax.set_title('Pressure, Humidity, and Visibility Classified by Precipitationn\n', fontsize = 14)
    plt.show()
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(humidity[precipitation!=0], visibility[precipitation!=0], pressure[precipitation!=0], label='Rain')
    ax.scatter(humidity[precipitation==0], visibility[precipitation==0], pressure[precipitation==0], label ='No rain')
    ax.scatter(nhum, nvis, npress, color = 'black', label='Tomorrow')
    ax.set_xlabel('Humidity')
    ax.set_ylabel('Visibility')
    ax.set_zlabel('Pressure')
    ax.legend(bbox_to_anchor = (1.43, 1.025))
    ax.set_title('Pressure, Humidity, and Visibility Classified by Precipitationn\n', fontsize = 14)
    plt.show()
