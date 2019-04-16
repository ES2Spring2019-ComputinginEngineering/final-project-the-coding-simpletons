#Ben and Rónán 

import csv
import numpy as np

def readDataFile():
    csv_file = open('weather.csv')

    numRows = sum(1 for row in csv_file)
    
    csv_file.seek(0)
    
    csv_reader = csv.reader(csv_file, delimiter = ',')
    

    Dates = []
    report_types = []
    
    counter = 0
    
    for row in csv_reader:
        report_types.append(row[2])
        if (row[2] == 'SOD'):
            counter += 1
    return counter, report_types
        
    '''
    dailytemp = np.zeros(numRows-1)  # Daily dry bulb
    dailyhum = np.zeros(numRows-1)  # Daily humidity
    dailyseapress = np.zeros(numRows-1)  # Daily sea pressure
    dailyDiffNormTemp = np.zeros(numRows-1)  # Daily difference from normal temp
    dailyMaxTemp = np.zeros(numRows-1)  # Daily dry bulb
    dailyMinTemp = np.zeros(numRows-1) # Daily dry bulb
    dailyWindDirec = np.zeros(numRows-1) # Daily sustained wind direction
    dailyPeakWind = np.zeros(numRows-1)  # Daily gusting speeds
    dailyPercip = np.zeros(numRows-1)  # Daily percipitation
    dailyWind = np.zeros(numRows-1)  # Daily sustained winds
    
    hourlytemp = np.zeros(numRows-1) # Hourly dry bulb temps
    hourlypercip = np.zeros(numRows-1) # Hourly percipitation
    hourlyseapress = np.zeros(numRows-1) # Hourly sea level pressure
    hourlyhum = np.zeros(numRows-1) # Hourly relative humidity
    hourlyVis = np.zeros(numRows-1)  # Hourly visibility
    hourlyPeakWind = np.zeros(numRows-1) # Hourly peak wind speed
    hourlyWind = np.zeros(numRows-1) # Hourly sustained wind speed

    count = 0
    index = 0
    for row in csv_reader:
        if (count == 0):
            count += 1
        elif:
            dailytemp[index] = float(row[0])
            dailyhum[index] = float(row[1])
            dailyseapress[index] = int(row[2])
            dailyDiffNormTemp
            dailyMaxTemp
            dailyMinTemp
            dailyWindDirec
            dailyPeakWind
            dailyPercip
            dailyWind
        elif:
            hourlytemp
            hourlypercip
            hourlyseapress
            hourlyhum
            hourlyVis
            hourlyPeakWind
            hourlyWind
        index += 1
            
    for i in range(numRows - 1):
        nGlucose[i] = (glucose[i] - np.amin(glucose))/(np.amax(glucose)- np.amin(glucose))
        nHemoglobin[i] = (hemoglobin[i] - np.amin(hemoglobin))/(np.amax(hemoglobin)- np.amin(hemoglobin))
        
    return nGlucose, nHemoglobin, classification
    '''
counter, report_types = readDataFile()
