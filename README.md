# Rain or Shine? 

## Brief Description
Using climatological data from NOAA (National Oceanic and Atmospheric Administration) during the week of 02/08/19 - 02/14/19, the climatological data for the following day (02/15/19) is predicted using weighted averaging and a weather forecast of rain or no rain is made using K-nearest Neighbor classification. A K-means clustering algorithm is also applied to the climatological data to form rain/no rain clusters and its assignment accuracy is measured. 

## In-depth Description
  The program examines climatological data (accessed from a CSV file downloaded from NOAA's website) from the week of 02/08/19 - 02/14/19 to predict the weather for 02/15/19, 'tomorrow' in Boston, Massachusetts. 
  
  Using weighted averages of the hourly values for humidity, pressure, visibility, temperature, and windspeed; a daily value for 'tomorrow' is predicted for each of these variables. Using the predicted values for humidity, pressure, and visibility; a new point is created for 'tomorrow' on a 3-dimensional graph including all the hourly values for humidity, pressure, and visibility from January to April of 2019. 
  
  Using K-nearest neighbor classification with the classification being precipitation (rain/no rain), the 'tomorrow' point is classified with a percent chance of rain determined from the classifications of the 10 nearest neighboring points. The predicted values, prediction classification (rain/no rain), and chance of rain can be accessed by the user from a tk button window. Clicking on different buttons returns data relevant to that button title (including a forecast image)
  
  Additionally, a K-means clustering algorithm is generated to separate the hourly values for humidity, pressure, and visibility from January to April of 2019 into two clusters (rain/no rain). The accuracy of this clustering algorithm is determined by comparing the assigned classifications with the actual classifications accessed from the data. 

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
    *  *report(args)* : Opens a new tk window with buttons that return weather information when clicked.
        * parameters : bhourlyprecip (1-D list), bhourlyhum (1-D list), bhourlyseapress (1-D list), bhourlyVis (1-D list), bhourlytemp (1-D list), bhourlyWind (1-D list), nexthum (float), nextpress (float), nextvis (float), nexttemp (float), nextwind (float)
        * returns : void
6. ***data.py***  -->  Data parsing, cleaning, and graphing
    *  *readDataFile()* : Reads in climatological data from the CSV file, cleans values, and produces normalized values as well.
        * parameters : void
        * returns : valuesOfInterest (a list of the climatological values we were interested in analyzing) : bestDateSet (list of dates 02/08/19 - 02/16/19), time (list of data collection times), hourlytemp (1-D list), hourlyprecip (precipitation)(1-D list), hourlyseapress (pressure)(1-D list), hourlyhum (humidity)(1-D list), hourlyVis (visibility)(1-D list), hourlyPeakWind (peak wind speed)(1-D list), hourlyWind (average wind speed)(1-D list), nhourlytemp (1-D array), nhourlyprecip (1-D array), nhourlyseapress (1-D array), nhourlyhum (1-D array), nhourlyVis (1-D array), nhourlyPeakWind (1-D array), nhourlyWind (1-D array)
    *  *sliceOfInterest(args)* : Using the identified set of dates and the list of data collection times, a indexing slice is identified which can be used to access the hourly values for climatological data during the period of interest. 
        * parameters : bestDateSet (1-D list), time (1-D list)
        * returns : [start (int), end (int)]
    *  *dataOfInterest(args)* : Using the slice of interest, the hourly values for climatological data during the period of interest are sliced and then returned. 
        * parameters : sliceRange ([start (int), end (int)]), time (1-D list), hourlytemp (1-D list), hourlyprecip (1-D list), (1-D list), hourlyVis (1-D list), hourlyPeakWind (1-D list), hourlyWind (1-D list), nhourlytemp (1-D array), nhourlyprecip (1-D array), nhourlyseapress (1-D array), nhourlyhum (1-D array), nhourlyVis (1-D array), nhourlyPeakWind (1-D array), nhourlyWind (1-D array)
        * returns : btime (1-D list), bhourlytemp (1-D list), bhourlyprecip (1-D list), bhourlyseapress (1-D list), bhourlyhum (1-D list), bhourlyVis (1-D list), bhourlyPeakWind (1-D list), bhourlyWind (1-D list), bnhourlytemp (1-D array), bnhourlyprecip (1-D array), bnhourlyseapress (1-D array), bnhourlyhum (1-D array), bnhourlyVis (1-D array), bnhourlyPeakWind (1-D array), bnhourlyWind (1-D array)
    *  *exploringGraphs(args)* : Produces 2-D graphs comparing all pairs of climatological variables, used to identify which variables are associated with precipitation. 
        * parameters : hourlypress (1-D list), hourlyhum (1-D list), hourlyWind (1-D list), hourlyVis (1-D list), hourlytemp (1-D list), hourlyprecip (1-D list)
        * returns : void
    *  *graphData3d(args)* : Produces a 3-D graph (x = humidity, y = visibility, z = presure) classified by precipitation (rain/no rain)
        * parameters : nhourlyhum (1-D array), nhourlypress (1-D array), nhourlyVis (1-D array), nhourlyprecip (1-D array), nextnhum (float), nextnpress (float), nextnvis (float)
        * returns : void
7. ***clustering.py***  -->  Clustering, graphing of centroids with clusters, and accuracy of clusters
   *  *create_centroids(args)* : Generates K random centroids 
        * parameters : K (int)
        * returns : array with shape (K, 3) and filled with random values for humidity, visibility, and pressure
   *  *assign(args)* : Assign each data point to a centroid
        * parameters : centroids (array with shape (K, 3)), nhourlyhum (1-D array), nhourlypress (1-D array), nhourlyVis (1-D array)
        * returns : assignments (centroid assignments for each point (humidity, visibility, pressure))(1-D array)
   *  *updateCent(args)* : Updates the location of each centroid based on the mean of the values assigned to each one. 
        * parameters : centroids (array with shape (K, 3)), assignments (1-D array), nhourlyhum (1-D array), nhourlypress (1-D array), nhourlyVis (1-D array)
        * returns : newCentroids (array with shape (K, 3))
   *  *iteration(args)* : Calls the assign and update functions until the centroids effectively stop moving 
        * parameters : centroids (array with shape (K, 3)), nhourlyhum (1-D array), nhourlypress (1-D array), nhourlyVis (1-D array)
        * returns : centroids (final centroid points)(array with shape (K, 3)), assignments (final data assignments)(1-D array)
    *  *clusterAccuracy(args)* : Prints the rate of false positives, false negatives, true positives, and true negatives in assignment using the clustering algorithm
        * parameters : nhourlyhum (1-D array), nhourlypress (1-D array), nhourlyVis (1-D array), assignments (1-D array), nhourlyprecip (1-D array), centroids (array with shape (K, 3))
        * returns : void
    *  *graphing(args)* : Produces a 3-D graph (x = humidity, y = visibility, z = presure) classified by clusters (rain/no rain)
        * parameters : nhourlyhum (1-D array), nhourlypress (1-D array), nhourlyVis (1-D array), centroids (array with shape (K, 3)), assignments (1-D array)
        * returns : void
8. ***prediction.py***  -->  Weighted averaging, weather value prediction, K-nearest neighbor classifcation, and accuracy of predicted values. 
    *  test

**Note**: Meaing of different prefixes on variable names:

   - **b** : a value from the selected time period of the relevant 8 days of interest (02/08/19 - 02/15/19)
   
   - **n** : a normalized value
   
   - **next** : a predicted value
