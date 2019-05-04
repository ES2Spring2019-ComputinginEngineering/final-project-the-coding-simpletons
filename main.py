"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import data 
import clustering
from presentation import *
import tkinter as tk


# DEMONSTRATION CODE

print('The best set of days ranges from:\n' + str(bestDateSet[0]) + ' to ' + str(bestDateSet[len(bestDateSet)-1]))

data.graphData3D(nhourlyhum, nhourlyseapress, nhourlyVis, nhourlyprecip, Nnexthum, Nnextvis, Nnextpress)

K=2
centroids = clustering.create_centroids(K)

final_centroids, assignments = clustering.iteration(centroids, nhourlyhum, nhourlyseapress, nhourlyVis)

clustering.graphing(nhourlyhum, nhourlyVis, nhourlyseapress, final_centroids, assignments)

"""
root = tk.Tk()
presentation.interface(master=root).mainloop()
"""
