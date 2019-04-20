#Ben and Rónán 

import csv
import numpy as np

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
    
    """
    dailyTemp = np.zeros(numDays)  # Daily dry bulb
    dailyHum = np.zeros(numDays)  # Daily humidity
    dailySeaPress = np.zeros(numDays)  # Daily sea pressure
    dailyDiffNormTemp = np.zeros(numDays)  # Daily difference from normal temp
    dailyMaxTemp = np.zeros(numDays)  # Daily dry bulb
    dailyMinTemp = np.zeros(numDays) # Daily dry bulb
    dailyWindDirec = np.zeros(numDays) # Daily sustained wind direction
    dailyPeakWind = np.zeros(numDays)  # Daily gusting speeds
    dailyPrecip = np.zeros(numDays)  # Daily precipitation
    dailyWindSpeed = np.zeros(numDays)  # Daily sustained wind speeds
    """
    
    dates = []
    dailyTemp = []
    dailyHum = []
    dailySeaPress = []
    dailyDiffNormTemp = []
    dailyMaxTemp = []
    dailyMinTemp = []
    dailyWindDirec = []
    dailyPeakWind = []
    dailyPrecip = []
    dailyWindSpeed = []
    
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
        else:
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
    
    valuesOfInterest.append(dates)
    valuesOfInterest.append(dailyTemp)
    valuesOfInterest.append(dailyHum)
    valuesOfInterest.append(dailySeaPress)
    valuesOfInterest.append(dailyDiffNormTemp)
    valuesOfInterest.append(dailyMaxTemp)
    valuesOfInterest.append(dailyMinTemp)
    valuesOfInterest.append(dailyWindDirec)
    valuesOfInterest.append(dailyPeakWind)
    valuesOfInterest.append(dailyPrecip)
    valuesOfInterest.append(dailyWindSpeed)
    
    """
    hourlytemp = np.zeros(numRows-1) # Hourly dry bulb temps
    hourlypercip = np.zeros(numRows-1) # Hourly percipitation
    hourlyseapress = np.zeros(numRows-1) # Hourly sea level pressure
    hourlyhum = np.zeros(numRows-1) # Hourly relative humidity
    hourlyVis = np.zeros(numRows-1)  # Hourly visibility
    hourlyPeakWind = np.zeros(numRows-1) # Hourly peak wind speed
    hourlyWind = np.zeros(numRows-1) # Hourly sustained wind speed
    """
    
    hours = []
    hourlytemp = []
    hourlyprecip = []
    hourlyseapress = []
    hourlyhum = []
    hourlyVis = []
    hourlyPeakWind = []
    hourlyWind = []
            
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
        else:
            hours.append(data[i][1][11:])
            hourlytemp.append(float(data[i][43]))
            hourlyprecip.append(float(data[i][44]))
            hourlyseapress.append(float(data[i][49]))
            hourlyhum.append(float(data[i][48]))
            hourlyVis.append(float(data[i][52]))
            hourlyPeakWind.append(float(data[i][55]))
            hourlyWind.append(float(data[i][56]))
            
    print(str(badCounter2) + ' hourly values did not contain useable data')
    
    valuesOfInterest.append(hours)
    valuesOfInterest.append(hourlytemp)
    valuesOfInterest.append(hourlyprecip)
    valuesOfInterest.append(hourlyseapress)
    valuesOfInterest.append(hourlyhum)
    valuesOfInterest.append(hourlyVis)
    valuesOfInterest.append(hourlyPeakWind)
    valuesOfInterest.append(hourlyWind)
            
    #SOME NORMALIZATION STEP WILL BE NECESSARY
    """
    for i in range(numRows - 1):
        nGlucose[i] = (glucose[i] - np.amin(glucose))/(np.amax(glucose)- np.amin(glucose))
        nHemoglobin[i] = (hemoglobin[i] - np.amin(hemoglobin))/(np.amax(hemoglobin)- np.amin(hemoglobin))
    """
    
    return valuesOfInterest


dates, dailyTemp, dailyHum, dailySeaPress, dailyDiffNormTemp, dailyMaxTemp, dailyMinTemp, dailyWindDirec, dailyPeakWind, dailyPrecip, dailyWinds, hours, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind = readDataFile()
