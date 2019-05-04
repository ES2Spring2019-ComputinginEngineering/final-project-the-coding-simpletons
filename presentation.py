# Ben and Rónán
'''
date
image
rain/percipitation  (give percentages from k nearest neighbor)
temp (high/low)
winds
humidity
pressure
visibility
'''
import prediction
import data
from clustering import *
import tkinter as tk
import imageio
import matplotlib.pyplot as plt
import numpy as np

#VALUES REQUIRED TO OBTAIN PREDICTIONS
bestDateSet, time, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind = data.readDataFile()
dateRange = data.sliceOfInterest(bestDateSet, time)
btime, bhourlytemp, bhourlyprecip, bhourlyseapress, bhourlyhum, bhourlyVis, bhourlyPeakWind, bhourlyWind, bnhourlytemp, bnhourlyprecip, bnhourlyseapress, bnhourlyhum, bnhourlyVis, bnhourlyPeakWind, bnhourlyWind = data.dataOfInterest(dateRange, time, hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind)


#COLLECTING PREDICTED VALUES
humidity, pressure, visibility, temperature, winds, Nhumidity, Nvisibility, Npressure = prediction.tomorrow(bestDateSet, btime, bhourlyhum, bhourlyseapress, bhourlyVis, bhourlytemp, bhourlyWind, bnhourlyhum, bnhourlyVis, bnhourlyseapress)
rain_value, rain_percent = prediction.kNearestNeighborClassifier(hourlyhum, hourlyseapress, hourlyVis, hourlyprecip, Nhumidity, Npressure, Nvisibility)

# ROUNDING VALUES FOR PRESENTATION
rain_percent = round(rain_percent)

humidity = round(humidity)

pressure = round(pressure)

visibility = round(visibility)

temperature = round(temperature)

winds = round(winds)

root = tk.Tk()

class interface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack() 
        self.create_widgets()

    def create_widgets(self):
        tk.Button(root,text="Rain",command=self.rain).pack(side="top")
        tk.Button(root,text="Average Temperature",command=self.temp).pack(side="top")      
        tk.Button(root,text="Humidity",command=self.hum).pack(side="top")        
        tk.Button(root,text="Wind Speed",command=self.wind).pack(side="top")
        tk.Button(root,text="Pressure",command=self.press).pack(side="top")
        tk.Button(root,text="Visibility",command=self.vis).pack(side="top")
        tk.Button(root,text="All Done.", command=root.destroy).pack(side="top")

    def rain(self):
        if rain_value == 0:
            im = np.array(imageio.imread('SUN.png', as_gray=False), dtype = "int64")
        else:
            print("Chance of Rain: " + str(rain_percent) + "%\n")
            im = np.array(imageio.imread('RAIN.jpg', as_gray=False), dtype = "int64")
        plt.figure()
        plt.imshow(im)
        plt.axis('off')
        plt.show()
        
    def temp(self):
        accuracy = round(prediction.predictedAccuracy(bhourlytemp, temperature))
        print("Average Temperature for Tomorrow is " + str(temperature) + " F, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
        
    def hum(self):
        accuracy = round(prediction.predictedAccuracy(bhourlyhum, humidity))
        print("Humidity for Tomorrow is " + str(humidity) + "%, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
        
    def wind(self):
        accuracy = round(prediction.predictedAccuracy(bhourlyWind, winds))
        print("Average Wind for tomorrow is " + str(winds) + " mph, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
        
    def press(self):
        accuracy = round(prediction.predictedAccuracy(bhourlyseapress, pressure))
        print("Pressure for Tomorrow is " + str(pressure) + "Pa, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
    
    def vis(self):
        accuracy = round(prediction.predictedAccuracy(bhourlyVis, visibility))
        if visibility > 9.7:
            print("Clear Skies Tomorrow with " + str(100.0-accuracy) + "% Accuracy\n")
        else:
            print("Visibility for Tomorrow is " + str(visibility) + "with" + str(100.0-accuracy) + "% Accuracy\n")

