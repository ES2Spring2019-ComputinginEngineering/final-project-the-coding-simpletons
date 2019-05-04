"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import data 
import clustering
import prediction
import presentation


# DEMONSTRATION CODE

bestDateSet, time, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind = data.readDataFile()

dateRange = data.sliceOfInterest(bestDateSet, time)

btime, bhourlytemp, bhourlyprecip, bhourlyseapress, bhourlyhum, bhourlyVis, bhourlyPeakWind, bhourlyWind, bnhourlytemp, bnhourlyprecip, bnhourlyseapress, bnhourlyhum, bnhourlyVis, bnhourlyPeakWind, bnhourlyWind = data.dataOfInterest(dateRange, time, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind)

nexthum, nextpress, nextvis, nexttemp, nextwind, Nnexthum, Nnextpress, Nnextvis = prediction.tomorrow(bestDateSet, btime, bhourlyhum, bhourlyseapress, bhourlyVis, bhourlytemp, bhourlyWind, bnhourlyhum, bnhourlyseapress, bnhourlyVis)

<<<<<<< HEAD
data.graphData3D(nhourlyhum, nhourlyseapress, nhourlyVis, nhourlyprecip, Nnexthum, Nnextvis, Nnextpress)
=======
prediction.predictedAccuracy(bhourlyhum, bhourlyseapress, bhourlyVis, bhourlytemp, bhourlyWind, nexthum, nextpress, nextvis, nexttemp, nextwind)


#data.graphData3D(nhourlyseapress, nhourlyhum, nhourlyWind, nhourlyVis, nhourlytemp, nhourlyprecip, Nnexthum, Nnextvis, Nnextpress)
>>>>>>> 314d0b2114d7e60ab57eedf8452e95715d130ba8

"""
K=2
centroids = clustering.create_centroids(K)

final_centroids, assignments = clustering.iteration(centroids, hourlyhum, hourlyseapress, hourlyVis)

clustering.graphing(K, hourlyhum, hourlyVis, hourlyseapress, final_centroids, assignments)
"""

# This files should not contain any function defitions


# IMPORT STATEMENTS




# DEMONSTRATION CODE


data.graphData3D(nhourlyhum, nhourlyseapress, nhourlyVis, nhourlyprecip, Nnexthum, Nnextpress, Nnextvis)

K=2
centroids = clustering.create_centroids(K)

final_centroids, assignments = clustering.iteration(centroids, nhourlyhum, nhourlyseapress, nhourlyVis)

clustering.graphing(nhourlyhum, nhourlyVis, nhourlyseapress, final_centroids, assignments)

"""
import presentation
import tkinter as tk

root = tk.Tk()
presentation.interface(master=root).mainloop()
"""

