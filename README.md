# Rain or Shine? 

## Brief Description
Using climatological data from NOAA (National Oceanic and Atmospheric Administration) during the week of 02/08/19 - 02/14/19, the climatological data for the following day (02/15/19) is predicted using weighted averaging and a weather forecast of rain or no rain is made using K-nearest Neighbor classification. A K-means clustering algorithm is also applied to the climatological data to form rain/no rain clusters and its assignment accuracy is measured. 

## In-depth Description
  The program examines climatological data (accessed from a CSV file downloaded from NOAA's website) from the week of 02/08/19 - 02/14/19 to predict the weather for 02/15/19, 'tomorrow' in Boston, Massachusetts. 
  
  Using weighted averages of the hourly values for humidity, pressure, visibility, temperature, and windspeed; a daily value for 'tomorrow' is predicted for each of these variables. Using the predicted values for humidity, pressure, and visibility; a new point is created for 'tomorrow' on a 3-dimensional graph including all the hourly values for humidity, pressure, and visibility from January to April of 2019. 
  
  Using K-nearest neighbor classification with the classification being precipitation (rain/no rain), the 'tomorrow' point is classified with a percent chance of rain determined from the classifications of the 10 nearest neighboring points. The predicted values, prediction classification (rain/no rain), and chance of rain can be accessed by the user from a tk button window. Clicking on different buttons returns data relevant to that button title (including a forecast image)
  
  Additionally, a K-means clustering algorithm is generated to separate the hourly values for humidity, pressure, and visibility from January to April of 2019 into two clusters (rain/no rain). The accuracy of this clustering algorithm is determined by comparing the assigned classifications with the actual classifications accessed from the data. 

## Instructions

1. **Run the code in the main file.** This will produce an additional window on your screen with several buttons on it. 

2. **Click the different buttons to access different weather forecast data.** Each button produces data relevant to its title in the environment you are running the code in (we used Spyder).

3. **Press the 'Finished' button.** This will discontinue the code, but may leave the window open with a color wheel of death. Not to worry, simply running the code once more allows one to use the weather report (although it will open a new window).

4. To view the information relevant to the report you may uncomment the large block quote in the main file and comment out the presentation line. Make sure to comment out the presentation line, otherwise the code will continue to run while the tk window is open, preventing the clustering graph from being produced. 

**Note**: The window does not always appear in an obvious location. It should appear in the center of the screen and may hide behind any other windows you have open on your screen. You can also find it in your toolbar (if on a mac), by clicking on the white paper file named 'python'. 

## File List

**Note**: Meaing of different prefixes on variable names:

   - **b** : a value from the selected time period of the relevant 8 days of interest (02/08/19 - 02/15/19)
   
   - **n** : a normalized value
   
   - **next** : a predicted value

1. ***weather.csv***  -->  CSV file with all of the climatological data from NOAA
2. ***RAIN.jpg***  -->  Pic Art of a rainy cloud used as a forecast image
3. ***SUN.png***  -->  Pic Art of a sun used as a forecast image
4. ***main.py***  -->  Action of the program: variable assignment and produces weather report
5. ***presentation.py***  -->  tk button weather report
    *  *report(args)* : Opens a new tk window with buttons that return weather information when clicked.
        * parameters : bHourlyPrecip (1-D array), bHourlyHum (1-D array), bHourlyPress (1-D array), bHourlyVis (1-D array), bHourlyTemp (1-D array), bHourlyWind (1-D array), nextHum (float), nextPress (float), nextVis (float), nextTemp (float), nextWind (float)
        * returns : void
6. ***data.py***  -->  Data parsing, cleaning, and graphing
    *  *readDataFile()* : Reads in climatological data from the CSV file, cleans values, and produces normalized values as well.
        * parameters : void
        * returns : valuesOfInterest (a list of the climatological values we were interested in analyzing) : bestDateSet (1-D list of dates 02/08/19 - 02/16/19), time (1-D list of data collection times), hourlyTemp (1-D array), hourlyPrecip (precipitation)(1-D array), hourlyPress (pressure)(1-D array), hourlyHum (humidity)(1-D array), hourlyVis (visibility)(1-D array), hourlyPeakWind (peak wind speed)(1-D array), hourlyWind (average wind speed)(1-D array), nHourlyTemp (1-D array), nHourlyPrecip (1-D array), nHourlyPress (1-D array), nHourlyHum (1-D array), nHourlyVis (1-D array), nHourlyPeakWind (1-D array), nHourlyWind (1-D array)
    *  *sliceOfInterest(args)* : Using the identified set of dates and the list of data collection times, a indexing slice is identified which can be used to access the hourly values for climatological data during the period of interest. 
        * parameters : bestDateSet (1-D list), time (1-D list)
        * returns : [start (int), end (int)]
    *  *dataOfInterest(args)* : Using the slice of interest, the hourly values for climatological data during the period of interest are sliced and then returned. 
        * parameters : sliceRange ([start (int), end (int)]), time (1-D list), hourlyTemp (1-D array), hourlyPrecip (1-D array), hourlyPress (1-D array), hourlyHum (1-D array), hourlyVis (1-D array), hourlyPeakWind (1-D array), hourlyWind (1-D array), nHourlyTemp (1-D array), nHourlyPrecip (1-D array), nHourlyPress (1-D array), nHourlyHum (1-D array), nHourlyVis (1-D array), nHourlyPeakWind (1-D array), nHourlyWind (1-D array)
        * returns : bTime (1-D list), bHourlyTemp (1-D array), bHourlyPrecip (1-D array), bHourlyPress (1-D array), bHourlyHum (1-D array), bHourlyVis (1-D array), bHourlyPeakWind (1-D array), bHourlyWind (1-D array), bnHourlyTemp (1-D array), bnHourlyPrecip (1-D array), bnHourlyPress (1-D array), bnHourlyHum (1-D array), bnHourlyVis (1-D array), bnHourlyPeakWind (1-D array), bnHourlyWind (1-D array)
    *  *exploringGraphs(args)* : Produces 2-D graphs comparing all pairs of climatological variables, used to identify which variables are associated with precipitation. 
        * parameters : hourlyPress (1-D array), hourlyHum (1-D array), hourlyWind (1-D array), hourlyVis (1-D array), hourlyTemp (1-D array), hourlyPrecip (1-D array)
        * returns : void
    *  *graphData3d(args)* : Produces a 3-D graph (x = humidity, y = visibility, z = presure) classified by precipitation (rain/no rain)
        * parameters : hourlyHum (1-D array), hourlyPress (1-D array), hourlyVis (1-D array), hourlyPrecip (1-D array), nextHum (float), nextPress (float), nextVis (float)
        * returns : void
7. ***clustering.py***  -->  Clustering, graphing of centroids with clusters, and accuracy of clusters
   *  *create_centroids(args)* : Generates K random centroids 
        * parameters : K (int)
        * returns : array with shape (K, 3) and filled with random values for humidity, visibility, and pressure
   *  *assign(args)* : Assign each data point to a centroid
        * parameters : centroids (array with shape (K, 3)), nHourlyHum (1-D array), nHourlyPress (1-D array), nHourlyVis (1-D array)
        * returns : assignments (centroid assignments for each point (humidity, visibility, pressure))(1-D array)
   *  *updateCent(args)* : Updates the location of each centroid based on the mean of the values assigned to each one. 
        * parameters : centroids (array with shape (K, 3)), assignments (1-D array), nHourlyHum (1-D array), nHourlyPress (1-D array), nHourlyVis (1-D array)
        * returns : newCentroids (array with shape (K, 3))
   *  *iteration(args)* : Calls the assign and update functions until the centroids effectively stop moving 
        * parameters : centroids (array with shape (K, 3)), nHourlyHum (1-D array), nHourlyPress (1-D array), nHourlyVis (1-D array)
        * returns : centroids (final centroid points)(array with shape (K, 3)), assignments (final data assignments)(1-D array)
    *  *clusterAccuracy(args)* : Prints the rate of false positives, false negatives, true positives, and true negatives in assignment using the clustering algorithm
        * parameters : nHourlyHum (1-D array), nHourlyPress (1-D array), nHourlyVis (1-D array), assignments (1-D array), nHourlyPrecip (1-D array), centroids (array with shape (K, 3))
        * returns : void
    *  *denormalizeCent(args)* : Produces a denormalized centroid
        * parameters : centroids (array with shape (K, 3)), hourlyHum (1-D array), hourlyVis (1-D array), hourlyPress (1-D array)
        * returns : returnCentroids (array with shape (K, 3))
    *  *graphing(args)* : Produces a 3-D graph (x = humidity, y = visibility, z = presure) classified by clusters (rain/no rain)
        * parameters : nHourlyHum (1-D array), nHourlyVis (1-D array), nHourlyPress (1-D array), hourlyHum, hourlyVis, hourlyPress, centroids (array with shape (K, 3)), assignments (1-D array)
        * returns : void
8. ***prediction.py***  -->  Weighted averaging, weather value prediction, K-nearest neighbor classifcation, and accuracy of predicted values. 
    *  *weights(args)* : Makes a list of weights based upon the number of hourly values in the week of interest (02/08/19 - 02/14/19)
        * parameters : bestDateSet (1-D list), bTime (1-D list)
        * returns : weights (1-D list)
    *  *weightedValues(args)* : Takes in the hourly values from the week of interest for a specific variable, applies the weights, and returns a predicted value
        * parameters : bTime (1-D list), weights (1-D list), bHourlyData (1-D array)
        * returns : predictedValue (float)
    *  *tomorrow(args)* : Calls weightedValues to produce the predicted values of interest
        * parameters : bestDateSet (1-D list), bTime (1-D list), bHourlyHum (1-D array), bHourlyPress (1-D array), bHourlyVis (1-D array), bHourlyTemp (1-D array), bHourlyWind (1-D array), bnHourlyHum (1-D array), bnHourlyPress (1-D array), bnHourlyVis (1-D array)
        * returns : nextHum (float), nextPress (float), nextVis (float), nextTemp (float), nextWind (float), nextnHum (float), nextnPress (float), nextnVis (float)
    *  *predictedAccuracy(args)* : Calculates the percent error associated with a predicted value
        * parameters : data (float), nextData (float)
        * returns : percentError (float)
    *  *kNearestNeighborClassifier(args)* : Using K-nearest classification of the predicted data point compared to hourly values from Jan-April 2019, the predicted data point, 'tomorrow', is classified as rain or not rain and a percent chance of precipitation is given using the 10 closest neighbors. 
        * parameters : nHourlyHum (1-D array), nHourlyPress (1-D array), nHourlyVis (1-D array), nHourlyPrecip (1-D array), nextnHum (float), nextnPress (float), nextnVis (float)
        * returns : raining (float), likelihood (float)

## Features

### Libraries
1. Numpy  -->  numerical calculations
2. Matplotlib  -->  graphing
3. tkinter  -->  creating widgets (windows with buttons)
4. imageio  -->  importing and displaying images
5. csv  -->  accessing csv file 
