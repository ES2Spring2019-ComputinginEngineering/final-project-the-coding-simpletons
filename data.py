#Ben and Rónán 

import csv

def readDataFile():
    csv_file = open('weather.csv')

    numRows = sum(1 for row in csv_file)
    
    csv_file.seek(0)
    
    csv_reader = csv.reader(csv_file, delimiter = ',')

    glucose = np.zeros(numRows-1) #true blood glucose 
    hemoglobin = np.zeros(numRows-1) #true hemoglobin
    classification = np.zeros(numRows-1) #class
    nGlucose = np.zeros(numRows-1) #normalized blood glucose values
    nHemoglobin = np.zeros(numRows-1) #normalized hemoglobin values

    count = 0
    index = 0
    for row in csv_reader:
        if (count == 0):
            count += 1
        else:
            glucose[index] = float(row[0])
            hemoglobin[index] = float(row[1])
            classification[index] = int(row[2])
            index += 1
            
    for i in range(numRows - 1):
        nGlucose[i] = (glucose[i] - np.amin(glucose))/(np.amax(glucose)- np.amin(glucose))
        nHemoglobin[i] = (hemoglobin[i] - np.amin(hemoglobin))/(np.amax(hemoglobin)- np.amin(hemoglobin))
        
    return nGlucose, nHemoglobin, classification
