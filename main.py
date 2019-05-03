"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import data 
import clustering
import prediction



# DEMONSTRATION CODE

#dates, dailyTemp, dailyHum, dailySeaPress, dailyDiffNormTemp, dailyMaxTemp, dailyMinTemp, dailyWindDirec, dailyPeakWind, dailyPrecip, dailyWinds, 
bestDateSet, time, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind = data.readDataFile()

dateRange = data.sliceOfInterest(bestDateSet, time)

#indexRange = dataOfInterest()

nexthum, nextvis, nextpress, nexttemp, nextwind, Nnexthum, Nnextvis, Nnextpress, Nnexttemp, Nnextwind = prediction.tomorrow(bestDateSet, time, hourlyhum, hourlyVis, hourlyseapress, hourlytemp, hourlyWind, nhourlyhum, nhourlyVis, nhourlyseapress, nhourlytemp, nhourlyWind)
#next_hum = trending(hourlyhum)
#next_press = trending(hourlyseapress)
#next_vis = trending(hourlyVis)


#will_it_rain = prediction.nearest_neighbor(hourlyhum, hourlyseapress, hourlyprecip, next_hum, next_press)
#is_it_raining, rain_percent = prediction.kNearestNeighborClassifier(hourlyhum, hourlyseapress, hourlyprecip, next_hum, next_press)

#data.graphData3D(hourlyseapress, hourlyhum, hourlyWind, hourlyVis, hourlytemp, hourlyprecip, next_hum, 0.95, next_press)

"""
K=2
centroids = clustering.create_centroids(K)

final_centroids, assignments = clustering.iteration(centroids, hourlyhum, hourlyseapress, hourlyVis)

clustering.graphing(K, hourlyhum, hourlyVis, hourlyseapress, final_centroids, assignments)
"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import data 
import clustering
import prediction



# DEMONSTRATION CODE

#dates, hours, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind = data.readDataFile()

#next_hum = trending(hourlyhum)
#next_press = trending(hourlyseapress)
#next_vis = trending(hourlyVis)


#will_it_rain = prediction.nearest_neighbor(hourlyhum, hourlyseapress, hourlyprecip, next_hum, next_press)
#is_it_raining, rain_percent = prediction.kNearestNeighborClassifier(hourlyhum, hourlyseapress, hourlyprecip, next_hum, next_press)

#data.graphData3D(hourlyseapress, hourlyhum, hourlyWind, hourlyVis, hourlytemp, hourlyprecip, next_hum, 0.95, next_press)

K=2
centroids = clustering.create_centroids(K)

#final_centroids, assignments = clustering.iteration(centroids, hourlyhum, hourlyseapress, hourlyVis)

#clustering.graphing(K, hourlyhum, hourlyVis, hourlyseapress, final_centroids, assignments)


import presentation as pressi
import tkinter as tk

root = tk.Tk()
face = pressi.interface(master=root)
face.mainloop()
