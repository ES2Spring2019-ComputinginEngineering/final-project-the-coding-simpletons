# Ben and Rónán
import prediction
import tkinter as tk
import imageio
import matplotlib.pyplot as plt
import numpy as np

def report(bHourlyPrecip, bHourlyHum, bHourlyPress, bHourlyVis, bHourlyTemp, bHourlyWind, nextHum, nextPress, nextVis, nextTemp, nextWind, rainValue, rainPercent):
    bC = 'navy' #background color on window
    # ROUNDING VALUES FOR PRESENTATION
    rainPercent = round(rainPercent, 1)
    
    humidity = round(nextHum, 1)
    
    pressure = round(nextPress, 1)
    
    visibility = round(nextVis, 1)
    
    temperature = round(nextTemp, 1)
    
    winds = round(nextWind, 1)
    
    root = tk.Tk()
    root.geometry("200x200+550+350") #dimensions of window and centering window on screen
    root.configure(background=bC) #adding background color
    root.title('Weather Report')
    
    #The interface class is effectively the window being opened with each function
    #contained within being a unqiue button with the exception of __init__() and creat_widgets()
    class interface(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack() 
            self.create_widgets()
    
        def create_widgets(self):
            tk.Label(text = 'test')
            tk.Button(root, text="Location", command=self.location, highlightbackground=bC).pack(side="top")
            tk.Button(root, text="Tomorrow's Date", command=self.tomorrow, highlightbackground=bC).pack(side="top")
            tk.Button(root, text="Tomorrow's Weather", command=self.weather, highlightbackground=bC).pack(side="top")
            tk.Button(root, text="Average Temperature", command=self.temp, highlightbackground=bC).pack(side="top")      
            tk.Button(root, text="Humidity", command=self.hum, highlightbackground=bC).pack(side="top")        
            tk.Button(root, text="Wind Speed", command=self.wind, highlightbackground=bC).pack(side="top")
            tk.Button(root, text="Pressure", command=self.press, highlightbackground=bC).pack(side="top")
            tk.Button(root, text="Visibility", command=self.vis, highlightbackground=bC).pack(side="top")
            tk.Button(root, text="Finished", command=root.destroy, highlightbackground=bC).pack(side="top")
        
        def location(self):
            print('This report returns the weather in Boston, Massachussetts\n')
            
        def tomorrow(self):
            print('Tomorrow is February 15, 2019\n')
            
        def weather(self):
            print("Chance of Rain: " + str(rainPercent) + "%\n")
            if rainValue == 0:
                im = np.array(imageio.imread('SUN.png', as_gray=False), dtype = "int64")
            else:
                im = np.array(imageio.imread('RAIN.jpg', as_gray=False), dtype = "int64")
            plt.figure()
            plt.imshow(im)
            plt.axis('off')
            plt.show()
            
        def temp(self):
            accuracy = round(prediction.predictedAccuracy(bHourlyTemp, temperature),1)
            print("Average Temperature for Tomorrow is " + str(temperature) + " F, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
            
        def hum(self):
            accuracy = round(prediction.predictedAccuracy(bHourlyHum, humidity),1)
            print("Relative Humidity for Tomorrow is " + str(humidity) + "%, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
            
        def wind(self):
            accuracy = round(prediction.predictedAccuracy(bHourlyWind, winds),1)
            print("Average Wind Speed for tomorrow is " + str(winds) + " mph, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
            
        def press(self):
            accuracy = round(prediction.predictedAccuracy(bHourlyPress, pressure),1)
            print("Pressure for Tomorrow is " + str(pressure) + " inches of mercury, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
        
        def vis(self):
            accuracy = round(prediction.predictedAccuracy(bHourlyVis, visibility),1)
            if visibility > 9.7:
                print("Clear Skies Tomorrow with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
            else:
                print("Visibility for Tomorrow is " + str(visibility) + " miles, with a Reported Accuracy of " + str(100.0-accuracy) + "%\n")
    
    interface(master=root).mainloop()
