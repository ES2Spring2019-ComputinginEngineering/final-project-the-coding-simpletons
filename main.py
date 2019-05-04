"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import data 
import clustering
import prediction
import presentation
import tkinter as tk


# DEMONSTRATION CODE

bestDateSet, time, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind = data.readDataFile()

print('The best set of days ranges from:\n' + str(bestDateSet[0]) + ' to ' + str(bestDateSet[len(bestDateSet)-1]))

dateRange = data.sliceOfInterest(bestDateSet, time)

btime, bhourlytemp, bhourlyprecip, bhourlyseapress, bhourlyhum, bhourlyVis, bhourlyPeakWind, bhourlyWind, bnhourlytemp, bnhourlyprecip, bnhourlyseapress, bnhourlyhum, bnhourlyVis, bnhourlyPeakWind, bnhourlyWind = data.dataOfInterest(dateRange, time, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind)

nexthum, nextpress, nextvis, nexttemp, nextwind, Nnexthum, Nnextpress, Nnextvis = prediction.tomorrow(bestDateSet, btime, bhourlyhum, bhourlyseapress, bhourlyVis, bhourlytemp, bhourlyWind, bnhourlyhum, bnhourlyseapress, bnhourlyVis)

data.graphData3D(nhourlyhum, nhourlyseapress, nhourlyVis, nhourlyprecip, Nnexthum, Nnextvis, Nnextpress)

K=2
centroids = clustering.create_centroids(K)

final_centroids, assignments = clustering.iteration(centroids, nhourlyhum, nhourlyseapress, nhourlyVis)

clustering.graphing(nhourlyhum, nhourlyVis, nhourlyseapress, final_centroids, assignments)

"""
root = tk.Tk()
presentation.interface(master=root).mainloop()
"""

