# Ben and Rónán
import prediction
import tkinter as tk
import imageio
import main
import matplotlib.pyplot as plt
import numpy as np


# ROUNDING VALUES FOR PRESENTATION
rain_percentage = round((main.rain_percent))

humidity = round((main.humidity), 1)

pressure = round((main.pressure), 1)

visibility = round((main.visibility), 1)

temperature = round((main.temperature), 1)

winds = round((main.winds), 1)

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
        if main.rain_value == 0:
            im = np.array(imageio.imread('SUN.png', as_gray=False), dtype = "int64")
        else:
            print("Chance of Rain: " + str(rain_percent) + "%\n")
            im = np.array(imageio.imread('RAIN.jpg', as_gray=False), dtype = "int64")
        plt.figure()
        plt.imshow(im)
        plt.axis('off')
        plt.show()
        
    def temp(self):
        accuracy = round(prediction.predictedAccuracy(main.bhourlytemp, temperature),1)
        print("Average Temperature for Tomorrow is " + str(temperature) + " F, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
        
    def hum(self):
        accuracy = round(prediction.predictedAccuracy(main.bhourlyhum, humidity),1)
        print("Humidity for Tomorrow is " + str(humidity) + "%, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
        
    def wind(self):
        accuracy = round(prediction.predictedAccuracy(main.bhourlyWind, winds),1)
        print("Average Wind for tomorrow is " + str(winds) + " mph, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
        
    def press(self):
        accuracy = round(prediction.predictedAccuracy(main.bhourlyseapress, pressure),1)
        print("Pressure for Tomorrow is " + str(pressure) + "Pa, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
    
    def vis(self):
        accuracy = round(prediction.predictedAccuracy(main.bhourlyVis, visibility),1)
        if visibility > 9.7:
            print("Clear Skies Tomorrow with " + str(100.0-accuracy) + "% Accuracy\n")
        else:
            print("Visibility for Tomorrow is " + str(visibility) + "with" + str(100.0-accuracy) + "% Accuracy\n")

interface(master=root).mainloop()