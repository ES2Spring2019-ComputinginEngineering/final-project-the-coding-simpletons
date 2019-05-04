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

btime, bhourlytemp, bhourlyprecip, bhourlyseapress, bhourlyhum, bhourlyVis, bhourlyPeakWind, bhourlyWind, bnhourlytemp, bnhourlyprecip, bnhourlyseapress, bnhourlyhum, bnhourlyVis, bnhourlyPeakWind, bnhourlyWind = data.dataOfInterest(dateRange, time, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind)
#indexRange = dataOfInterest()

nexthum, nextpress, nextvis, nexttemp, nextwind, Nnexthum, Nnextpress, Nnextvis = prediction.tomorrow(bestDateSet, btime, bhourlyhum, bhourlyseapress, bhourlyVis, bhourlytemp, bhourlyWind, bnhourlyhum, bnhourlyseapress, bnhourlyVis)

prediction.predictedAccuracy(bhourlyhum, bhourlyseapress, bhourlyVis, bhourlytemp, bhourlyWind, nexthum, nextpress, nextvis, nexttemp, nextwind)



#will_it_rain = prediction.nearest_neighbor(hourlyhum, hourlyseapress, hourlyprecip, next_hum, next_press)
#is_it_raining, rain_percent = prediction.kNearestNeighborClassifier(hourlyhum, hourlyseapress, hourlyVis, hourlyprecip, next_hum, next_press, next_vis)

#data.graphData3D(hourlyseapress, hourlyhum, hourlyWind, hourlyVis, hourlytemp, hourlyprecip, next_hum, 0.95, next_press)

"""
K=2
centroids = clustering.create_centroids(K)

final_centroids, assignments = clustering.iteration(centroids, hourlyhum, hourlyseapress, hourlyVis)

clustering.graphing(K, hourlyhum, hourlyVis, hourlyseapress, final_centroids, assignments)
"""

# This files should not contain any function defitions


# IMPORT STATEMENTS




# DEMONSTRATION CODE


#data.graphData3D(hourlyseapress, hourlyhum, hourlyWind, hourlyVis, hourlytemp, hourlyprecip, next_hum, 0.95, next_press)

K=2
centroids = clustering.create_centroids(K)

#final_centroids, assignments = clustering.iteration(centroids, hourlyhum, hourlyseapress, hourlyVis)

#clustering.graphing(K, hourlyhum, hourlyVis, hourlyseapress, final_centroids, assignments)

"""
import presentation
import tkinter as tk

root = tk.Tk()
presentation.interface(master=root).mainloop()
"""

