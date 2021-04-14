# Climate Analysis: Hawaii Weather

![Hawaii Skyline Weather Photo](https://github.com/ruthhinkle/sqlalchemy-challenge/blob/main/Images/hawaii.jpg)

## Part 1: Exploratory Analysis
Use Python and SQLAlchemy to do basic analysis on a climate database in a Jupyter Notebook file. 

### Precipitation Analysis

* Start by finding the most recent date in the data set.
* Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. Note you do not pass in the date as a variable to your query.
* Select only the date and prcp values.
* Load the query results into a Pandas DataFrame and set the index to the date column.
* Sort the DataFrame values by date.
* Plot the results using the DataFrame plot method.

### Station Analysis
* Design a query to calculate the total number of stations in the dataset.
* Design a query to find the most active stations (i.e. which stations have the most rows?).
    * List the stations and observation counts in descending order.
    * Which station id has the highest number of observations?
    * Using the most active station id, calculate the lowest, highest, and average temperature.
* Design a query to retrieve the last 12 months of temperature observation data (TOBS).
    * Filter by the station with the highest number of observations.
    * Query the last 12 months of temperature observation data for this station.
    * Plot the results as a histogram with bins=12.

## Part 2: Create Climate App
Design a Flask API based on the queries developed in the exploratory analysis from Part 1. 

Create Routes:
* /
    * Home page.
    * List all routes that are available.
* /api/v1.0/precipitation
    * Convert the query results to a dictionary using date as the key and prcp as the value.
    * Return the JSON representation of your dictionary.
* /api/v1.0/stations
    * Return a JSON list of stations from the dataset.
* /api/v1.0/tobs
    * Query the dates and temperature observations of the most active station for the last year of data.
    * Return a JSON list of temperature observations (TOBS) for the previous year.
* /api/v1.0/<start> and /api/v1.0/<start>/<end>
    * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    * When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    * When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.


