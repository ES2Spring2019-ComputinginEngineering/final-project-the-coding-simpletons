# Weather Report 

  The program examines climatological data (accessed from a CSV file downloaded from NOAA's website) from the week of 02/08/19 - 02/14/19 to predict the weather for 02/15/19, 'tomorrow'. 
  
  Using weighted averages of the hourly values for humidity, pressure, visibility, temperature, and windspeed; a daily value for 'tomorrow' is predicted for each of these variables. Using the predicted values for humidity, pressure, and visibility; a new point is created for 'tomorrow' on a 3-dimensional graph including all the hourly values for humidity, pressure, and visibility from January to April of 2019. 
  
  Using K-nearest neighbor classification with the classification being precipitation (rain/no rain), the 'tomorrow' point is classified with a percent chance of rain determined from the classifications of the 10 nearest neighboring points. The predicted values, prediction classification (rain/no rain), and chance of rain can be accessed by the user from a tk button window. Clicking on different buttons returns data relevant to that button title (including a forecast image)
  
  Additionally, a K-means clustering alogorithm is generated to separate the hourly values for humidity, pressure, and visibility from January to April of 2019 into two clusters (rain/no rain). The accuracy of this clustering algorithm is determined by comparing the assigned classifications with the actual classifications accessed from the data. 

## Instructions

Running the code in the main class will produce an additional window on your screen with several buttons on it. Clicking the different buttons will produce data relevant to the button title in the environment you are running the code in (we used Spyder). This relevant data is the weather report. 

Pressing the 'Finished' button will discontinue the code, but may leave the window open with a color wheel of death. Not to worry, simply running the code once more allows one to use the weather report (although it will open a new window).

**Note**: The window does not always appear in an obvious location. It usually likes to hide to in the top left corner of the screen behind any other windows you may have open on your screen. You can also find it in your toolbar (if on a mac), by clicking on the white paper file named 'python'. 

## File List

Create a list of all of the files in your repository with one sentence descriptions

1. **weather.csv**  -->  CSV file with all of the climatological data from NOAA
2. **RAIN.jpg**  -->  Pic Art of a rainy cloud used as a forecast image
3. **SUN.png**  -->  Pic Art of a sun used as a forecast image
4. **main.py**  -->  Action of the program: variable assignment and produces weather report
5. **presentation.py**  -->  Tk button weather report functions and classes
6. **data.py**  -->  Data parsing, cleaning, and graphing
7. **clustering.py**  -->  Clustering, graphing of centroids with clusters, and accuracy of clusters
8. **prediction.py**  -->  Weighted averaging, weather value prediction, K-nearest neighbor classifcation, and accuracy of predicted values. 


## How to format your readme

In your readme, you can:
```
Give code examples
```

You can also include useful links, like this one with information about [formatting markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

You can 
- Also
- Make
- Lists
