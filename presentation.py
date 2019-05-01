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
from prediction import *
from data import *
from clustering import *
import tkinter as tk
import imageio
import matplotlib.pyplot as plt
import numpy as np

#rain_value, rain_percent = kNearestNeighborClassifier(hourlyhum, hourlyseapress, hourlyprecip, next_hum, next_press)

ave_temp = 'interpolated ave'

high_temp = 'interpolated high'

low_temp = 'interpolated low'

temp = 'interpolated ave' + '(high_temp/low_temp)'

winds = 'interpolated speed' + 'direction'

humidity = 'interpolated humidity'

pressure = 'interpolated pressure'

visibility = 'interpolated visibility'


class interface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack() 
        self.create_widgets()

    def create_widgets(self):
        tk.Button(root,text="Rain",command=self.rain).pack(side="top")
        tk.Button(root,text="Temperature (High/Low)",command=self.temp).pack(side="top")      
        tk.Button(root,text="Humidity",command=self.hum).pack(side="top")        
        tk.Button(root,text="Wind Speed",command=self.wind).pack(side="top")
        tk.Button(root,text="Pressure",command=self.press).pack(side="top")
        tk.Button(root,text="Visibility",command=self.vis).pack(side="top")

    def rain(self):
        if rain_value == 1:
            im = np.array(imageio.imread('SUN.png', as_gray=False), dtype = "int64")
        else:
            print("Chance of Rain: " + str(rain_percent) + "\n")
            im = np.array(imageio.imread('RAIN.jpg', as_gray=False), dtype = "int64")
        plt.figure()
        plt.imshow(im)
        plt.axis('off')
        plt.show()
        
    def temp(self):
        print("Temperature: " + str(ave_temp) + "F\n High: " + str(high_temp) + "F\n Low:  " + str(low_temp) +  "F\n")
        
    def hum(self):
        print("Humidity: " + str(humidity) + "%\n")
        
    def wind(self):
        print("Wind: " + str(winds) + "mph\n")
        
    def press(self):
        print("Pressure: " + str(pressure) + "Pa\n")
    
    def vis(self):
        if visibility == 1:
            print("Visibility: Clear Skies\n")
        else:
            print("Visibility: " + str(visibility) + "\n")

root = tk.Tk()