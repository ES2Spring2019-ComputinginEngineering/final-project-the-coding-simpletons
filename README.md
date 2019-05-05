# Weather Report 

  The program examines climatological data (accessed from a CSV file downloaded from NOAA's website) from the week of 02/08/19 - 02/14/19 to predict the weather for 02/15/19, 'tomorrow'. 
  Using weighted averages of the hourly values for humidity, pressure, visibility, temperature, and windspeed; a daily value for 'tomorrow' is predicted for each of these variables. Using the predicted values for humidity, pressure, and visibility; a new point is created for 'tomorrow' on a 3-dimensional graph including all the hourly values for humidity, pressure, and visibility from January to April of 2019. Using K-nearest neighbor classification with the classification being precipitation (rain/no rain), the 'tomorrow' point is classified with a percent chance of rain determined from the classifications of the 10 nearest neighboring points. The predicted values, prediction classification (rain/no rain), and chance of rain can be accessed by the user from a tk button window. Clicking on different buttons returns data relevant to that button title (including a forecast image)
  Additionally, a K-means clustering alogorithm is generated to separate the hourly values for humidity, pressure, and visibility from January to April of 2019 into two clusters (rain/no rain). The accuracy of this clustering algorithm is determined by comparing the assigned classifications with the actual classifications accessed from the data. 

## Instructions

Describe how the users(instructors) should run your code to see an ***easy to run example of the functionality***. This should all be in a *main.py* "driver" script.

## File List

Create a list of all of the files in your repository with one sentence descriptions 

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
