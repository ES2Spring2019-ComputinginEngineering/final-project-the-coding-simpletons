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
from data import *
from PIL import Image

sunny = Image.open('SUN.png') 

rainy = Image.open('RAIN.jpg') 

rain_value, rain_percent = kNearestNeighborClassifier(hourlyhum, hourlyseapress, hourlyprecip, next_hum, next_press)

ave_temp = 'interpolated ave'

high_temp = 'interpolated high'

low_temp = 'interpolated low'

temp = 'interpolated ave' + '(high_temp/low_temp)'

winds = 'interpolated speed' + 'direction'

humidity = 'interpolated humidity'

pressure = 'interpolated pressure'

visibility = 'interpolated visibility'

sunny.show()
