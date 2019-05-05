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
bestDateSet, time, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind = data.readDataFile()

dateRange = data.sliceOfInterest(bestDateSet, time)

btime, bhourlytemp, bhourlyprecip, bhourlyseapress, bhourlyhum, bhourlyVis, bhourlyPeakWind, bhourlyWind, bnhourlytemp, bnhourlyprecip, bnhourlyseapress, bnhourlyhum, bnhourlyVis, bnhourlyPeakWind, bnhourlyWind = data.dataOfInterest(dateRange, time, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind)

K = 2
centroids = clustering.create_centroids(K)
final_centroids, assignments = clustering.iteration(centroids, nhourlyhum, nhourlyseapress, nhourlyVis)

#COLLECTING PREDICTED VALUES
nexthumidity, nextpressure, nextvisibility, nexttemperature, nextwind, nextnhum, nextnpress, nextnvis = prediction.tomorrow(bestDateSet, btime, bhourlyhum, bhourlyseapress, bhourlyVis, bhourlytemp, bhourlyWind, bnhourlyhum, bnhourlyVis, bnhourlyseapress)

rain_value, rain_percent = prediction.kNearestNeighborClassifier(hourlyhum, hourlyseapress, hourlyVis, hourlyprecip, nextnhum, nextnpress, nextnvis)

#Uncommenting the below lines outputs information relevant to the report including the 
#range of dates we used to predict the weather and then measure our accuracy in those predictions,
#the graph of hourly values classified by precipitation (rain/no rain), the graph of hourly values 
#classified into two clusters (rain/no rain), and the accuracy of our K-means clustering alogrithim 
#on this particular data set
"""
print('The best set of days ranges from:\n' + str(bestDateSet[0]) + ' to ' + str(bestDateSet[len(bestDateSet)-1]))

data.graphData3D(nhourlyhum, nhourlyseapress, nhourlyVis, nhourlyprecip, nextnhum, nextnpress, nextnvis)

clustering.graphing(nhourlyhum, nhourlyVis, nhourlyseapress, final_centroids, assignments)

clustering.clusterAccuracy(nhourlyhum, nhourlyVis, nhourlyseapress, assignments, nhourlyprecip, final_centroids)
"""

#The below line of code is what produces and runs the interactive (buttons) weather report
#It may not pop up on your screen in an obvious location. For us the new window tends to pop up
#in the top left corner for the most part. 
#Pressing the 'Finished' button will discontinue the code, but may leave the window open with a 
#color wheel of death. Not to worry, simply running the code once more allows one to once again
#use the weather report.
presentation.report(bhourlyprecip, bhourlyhum, bhourlyseapress, bhourlyVis, bhourlytemp, bhourlyWind, nexthumidity, nextpressure, nextvisibility, nexttemperature, nextwind)