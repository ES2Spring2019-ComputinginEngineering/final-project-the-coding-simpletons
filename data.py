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
                
def graphData3D(pressure, humidity, windspeed, visibility, temperature, precipitation, newx, newz, newy):
    #matplotlib.use('MacOSX')
    #print(matplotlib.is_interactive())
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
