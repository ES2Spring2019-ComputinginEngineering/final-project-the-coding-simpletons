#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:19:20 2019

@author: benpradko
"""
import tkinter as tk
import imageio
import matplotlib.pyplot as plt
import numpy as np

rain = 0
percentage = 20
temp = 3
hi = 5
lo = 1
wind = 45
hum = 86

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

    def rain(self):
        if rain == 1:
            im = np.array(imageio.imread('SUN.png', as_gray=False), dtype = "int64")
        else:
            print("Chance of Rain: " + str(percentage) + "\n")
            im = np.array(imageio.imread('RAIN.jpg', as_gray=False), dtype = "int64")
        plt.figure()
        plt.imshow(im)
        plt.axis('off')
        plt.show()
        
    def temp(self):
        print("Temperature: " + str(temp) + "F\n High: " + str(hi) + "F\n Low:  " + str(lo) +  "F\n")
        
    def hum(self):
        print("Humidity: " + str(hum) + "\n")
        
    def wind(self):
        print("Wind: " + str(wind) + "\n")

root = tk.Tk()
face = interface(master=root)
face.mainloop()