# Rain or Shine? 

## Brief Description
Using climatological data from NOAA (National Oceanic and Atmospheric Administration) during the week of 02/08/19 - 02/14/19, the climatological data for the following day (02/15/19) is predicted using weighted averaging and a weather forecast of rain or no rain is made using K-nearest Neighbor classification. A K-means clustering algorithm is also applied to the climatological data to form rain/no rain clusters and its assignment accuracy is measured. 

## In-depth Description
  The program examines climatological data (accessed from a CSV file downloaded from NOAA's website) from the week of 02/08/19 - 02/14/19 to predict the weather for 02/15/19, 'tomorrow' in Boston, Massachusetts. 
  
  Using weighted averages of the hourly values for humidity, pressure, visibility, temperature, and windspeed; a daily value for 'tomorrow' is predicted for each of these variables. Using the predicted values for humidity, pressure, and visibility; a new point is created for 'tomorrow' on a 3-dimensional graph including all the hourly values for humidity, pressure, and visibility from January to April of 2019. 
  
  Using K-nearest neighbor classification with the classification being precipitation (rain/no rain), the 'tomorrow' point is classified with a percent chance of rain determined from the classifications of the 10 nearest neighboring points. The predicted values, prediction classification (rain/no rain), and chance of rain can be accessed by the user from a tk button window. Clicking on different buttons returns data relevant to that button title (including a forecast image)
  
  Additionally, a K-means clustering alogorithm is generated to separate the hourly values for humidity, pressure, and visibility from January to April of 2019 into two clusters (rain/no rain). The accuracy of this clustering algorithm is determined by comparing the assigned classifications with the actual classifications accessed from the data. 

## Instructions

Running the code in the main file will produce an additional window on your screen with several buttons on it. Clicking the different buttons will produce data relevant to the button title in the environment you are running the code in (we used Spyder). This relevant data is the weather report. 

Pressing the 'Finished' button will discontinue the code, but may leave the window open with a color wheel of death. Not to worry, simply running the code once more allows one to use the weather report (although it will open a new window).

**Note**: The window does not always appear in an obvious location. It should appear in the center of the screen and may hide behind any other windows you have open on your screen. You can also find it in your toolbar (if on a mac), by clicking on the white paper file named 'python'. 

## File List

Create a list of all of the files in your repository with one sentence descriptions

1. ***weather.csv***  -->  CSV file with all of the climatological data from NOAA
2. ***RAIN.jpg***  -->  Pic Art of a rainy cloud used as a forecast image
3. ***SUN.png***  -->  Pic Art of a sun used as a forecast image
4. ***main.py***  -->  Action of the program: variable assignment and produces weather report
5. ***presentation.py***  -->  tk button weather report
    *  **report(args)** : when called opens a new tk window with buttons that return weather information when clicked
        * parameters : bhourlyprecip, bhourlyhum, bhourlyseapress, bhourlyVis, bhourlytemp, bhourlyWind, nexthum, nextpress, nextvis, nexttemp, nextwind
        * returns : void
6. ***data.py***  -->  Data parsing, cleaning, and graphing
    *  **readDataFile()** : reads in climatological data from the CSV file, cleans values, and produces normalized values as well
        * parameters : void
        * returns : valuesOfInterest (a list of the climatological values we were interested in analyzing) : bestDateSet (list of dates 02/08/19 - 02/16/19), time (list of data collection times), hourlytemp, hourlyprecip, hourlyseapress, hourlyhum, hourlyVis, hourlyPeakWind, hourlyWind, nhourlytemp, nhourlyprecip, nhourlyseapress, nhourlyhum, nhourlyVis, nhourlyPeakWind, nhourlyWind
7. ***clustering.py***  -->  Clustering, graphing of centroids with clusters, and accuracy of clusters
    *  test
8. ***prediction.py***  -->  Weighted averaging, weather value prediction, K-nearest neighbor classifcation, and accuracy of predicted values. 
    *  test

**Note**: Meaing of different prefixes on variable names:

   - **b** : a value from the selected time period of the relevant 8 days of interest (02/08/19 - 02/15/19)
   
   - **n** : a normalized value
   
   - **next** : a predicted value
