"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import data 
import clustering
import presentation
import prediction

#Variable assignments
bestDateSet, time, hourlyTemp, hourlyPrecip, hourlyPress, hourlyHum, hourlyVis, hourlyPeakWind, hourlyWind, nHourlyTemp, nHourlyPrecip, nHourlyPress, nHourlyHum, nHourlyVis, nHourlyPeakWind, nHourlyWind = data.readDataFile()

dateRange = data.sliceOfInterest(bestDateSet, time)

bTime, bHourlyTemp, bHourlyPrecip, bHourlyPress, bHourlyHum, bHourlyVis, bHourlyPeakWind, bHourlyWind, bnHourlyTemp, bnHourlyPrecip, bnHourlyPress, bnHourlyHum, bnHourlyVis, bnHourlyPeakWind, bnHourlyWind = data.dataOfInterest(dateRange, time, hourlyTemp, hourlyPrecip, hourlyPress, hourlyHum, hourlyVis, hourlyPeakWind, hourlyWind, nHourlyTemp, nHourlyPrecip, nHourlyPress, nHourlyHum, nHourlyVis, nHourlyPeakWind, nHourlyWind)


#Predicted Values
nextHum, nextPress, nextVis, nextTemp, nextWind, nextnHum, nextnPress, nextnVis = prediction.tomorrow(bestDateSet, bTime, bHourlyHum, bHourlyPress, bHourlyVis, bHourlyTemp, bHourlyWind, bnHourlyHum, bnHourlyPress, bnHourlyVis)

rainValue, rainPercent = prediction.kNearestNeighborClassifier(nHourlyHum, nHourlyPress, nHourlyVis, nHourlyPrecip, nextnHum, nextnPress, nextnVis)

#The line below was used at the beginning of the project to determine which climatological variables 
#should be compared to anticipate rain

#data.exploringGraphs(hourlyPress, hourlyHum, hourlyWind, hourlyVis, hourlyTemp, hourlyPrecip)

#Uncommenting the block quote below outputs information relevant to the report including the 
#range of dates we used to predict the weather and then measure our accuracy in those predictions,
#the graph of hourly values classified by precipitation (rain/no rain), the graph of hourly values 
#classified into two clusters (rain/no rain), and the accuracy of our K-means clustering alogrithim 
#on this particular data set
#UNCOMMENT ME
"""
K = 2
centroids = clustering.create_centroids(K)
finalCentroids, assignments = clustering.iteration(centroids, nHourlyHum, nHourlyPress, nHourlyVis)

print('The best set of days ranges from:\n' + str(bestDateSet[0]) + ' to ' + str(bestDateSet[len(bestDateSet)-1]))

data.graphData3D(hourlyHum, hourlyPress, hourlyVis, hourlyPrecip, nextHum, nextPress, nextVis)

clustering.graphing(nHourlyHum, nHourlyVis, nHourlyPress, hourlyHum, hourlyVis, hourlyPress, finalCentroids, assignments)

clustering.clusterAccuracy(nHourlyHum, nHourlyVis, nHourlyPress, assignments, nHourlyPrecip, finalCentroids)
"""

#The below line of code is what produces and runs the interactive (buttons) weather report
#It may not pop up on your screen in an obvious location. The new window should
#pop up in the middle of the screen.
#Pressing the 'Finished' button will discontinue the code, but may leave the window open with a 
#color wheel of death. Not to worry, simply running the code once more allows one to use the weather report.
presentation.report(bHourlyPrecip, bHourlyHum, bHourlyPress, bHourlyVis, bHourlyTemp, bHourlyWind, nextHum, nextPress, nextVis, nextTemp, nextWind, rainValue, rainPercent)