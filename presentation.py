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
humidity, pressure, visibility, temperature, winds, Nhumidity, Nvisibility, Npressure, Ntemperature, Nwinds= prediction.tomorrow(bestDateSet, btime, bhourlyhum, bhourlyseapress, bhourlyVis, bhourlytemp, bhourlyWind, bnhourlyhum, bnhourlyVis, bnhourlyseapress, bnhourlytemp, bnhourlyWind)
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
        print("Average Temperature: " + str(temperature) + " F\n")
        
    def hum(self):
        print("Humidity: " + str(humidity) + "%\n")
        
    def wind(self):
        print("Wind: " + str(winds) + " mph\n")
        
    def press(self):
        print("Pressure: " + str(pressure) + "Pa\n")
    
    def vis(self):
        if visibility > .98:
            print("Visibility: Clear Skies\n")
        else:
            print("Visibility: " + str(visibility) + "\n")

