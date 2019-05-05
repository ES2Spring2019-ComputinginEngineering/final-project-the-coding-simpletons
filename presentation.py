# Ben and Rónán
import prediction
import tkinter as tk
import imageio
import matplotlib.pyplot as plt
import numpy as np

def report(bhourlyprecip, bhourlyhum, bhourlyseapress, bhourlyVis, bhourlytemp, bhourlyWind, nexthum, nextpress, nextvis, nexttemp, nextwind):
    bC = 'navy' #background color on window
    rain_value, rain_percent = prediction.kNearestNeighborClassifier(bhourlyhum, bhourlyseapress, bhourlyVis, bhourlyprecip, nexthum, nextpress, nextvis)
    # ROUNDING VALUES FOR PRESENTATION
    rain_percent = round(rain_percent, 1)
    
    humidity = round(nexthum, 1)
    
    pressure = round(nextpress, 1)
    
    visibility = round(nextvis, 1)
    
    temperature = round(nexttemp, 1)
    
    winds = round(nextwind, 1)
    
    root = tk.Tk()
    root.geometry("200x180")
    root.configure(background=bC)
    root.title('Weather Report')

    class interface(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack() 
            self.create_widgets()
    
        def create_widgets(self):
            tk.Label(text = 'test')
            tk.Button(root, text="Tomorrow's Date", command=self.tomorrow, highlightbackground=bC).pack(side="top")
            tk.Button(root, text="Tomorrow's Weather", command=self.weather, highlightbackground=bC).pack(side="top")
            tk.Button(root, text="Average Temperature", command=self.temp, highlightbackground=bC).pack(side="top")      
            tk.Button(root, text="Humidity", command=self.hum, highlightbackground=bC).pack(side="top")        
            tk.Button(root, text="Wind Speed", command=self.wind, highlightbackground=bC).pack(side="top")
            tk.Button(root, text="Pressure", command=self.press, highlightbackground=bC).pack(side="top")
            tk.Button(root, text="Visibility", command=self.vis, highlightbackground=bC).pack(side="top")
            tk.Button(root, text="Finished", command=root.destroy, highlightbackground=bC).pack(side="top")
    
        def tomorrow(self):
            print('Tomorrow is February 15, 2019\n')
            
        def weather(self):
            print("Chance of Rain: " + str(rain_percent) + "%\n")
            if rain_value == 0:
                im = np.array(imageio.imread('SUN.png', as_gray=False), dtype = "int64")
            else:
                im = np.array(imageio.imread('RAIN.jpg', as_gray=False), dtype = "int64")
            plt.figure()
            plt.imshow(im)
            plt.axis('off')
            plt.show()
            
        def temp(self):
            accuracy = round(prediction.predictedAccuracy(bhourlytemp, temperature),1)
            print("Average Temperature for Tomorrow is " + str(temperature) + " F, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
            
        def hum(self):
            accuracy = round(prediction.predictedAccuracy(bhourlyhum, humidity),1)
            print("Humidity for Tomorrow is " + str(humidity) + "%, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
            
        def wind(self):
            accuracy = round(prediction.predictedAccuracy(bhourlyWind, winds),1)
            print("Average Wind for tomorrow is " + str(winds) + " mph, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
            
        def press(self):
            accuracy = round(prediction.predictedAccuracy(bhourlyseapress, pressure),1)
            print("Pressure for Tomorrow is " + str(pressure) + " Pa, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
        
        def vis(self):
            accuracy = round(prediction.predictedAccuracy(bhourlyVis, visibility),1)
            if visibility > 9.7:
                print("Clear Skies Tomorrow with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
            else:
                print("Visibility for Tomorrow is " + str(visibility) + " with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
    
    interface(master=root).mainloop()
