# Import dependencies
from flask import Flask, render_template, request, redirect, jsonify
import numpy as np 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt
import pandas as pd

# SET UP DATABASE
# ~~~~~~~~~~~~~~~~~~~~~~~

# Create enginge
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect database
Base = automap_base()

# Reflect tables
Base.prepare(engine, reflect=True)

# CREATE FLASK APP
# ~~~~~~~~~~~~~~~~~~~~~~~

# Create an instance 
app = Flask(__name__)

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
# Let's me see what tables are in there, access using .keys (base.classes.keys())
inspector = inspect(engine)
inspector.get_table_names()

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# CREATE FLASK ROUTES
# ~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/")
def home():
    return "<h1>Table of Contents</h1> <br> <ul><li>/api/v1.0/precipitation</li> <li>/api/v1.0/stations</li> <li><p href='/api/v1.0/tobs'>/api/v1.0/tobs</p></li> <li>/api/v1.0/<start></li> <li>/api/v1.0/<start>/<end></li></ul> "

@app.route("/api/v1.0/precipitation") 
def precipitation():
    
    # Create session
    session = Session(engine)

    # Find last date string 
    last_date_string = session.query(measurement.date).all()[-1][0]
    
    # Create variable for one year ago
    one_year_ago = dt.date(int(last_date_string[0:4])-1,int(last_date_string[5:7]), int(last_date_string[8:]))
    
    # Perform query to get data and precipitation data
    data_scores = session.query(measurement.date,measurement.prcp).filter(measurement.date>=one_year_ago).all()
    
    # Save query as dataframe
    precip_data = jsonify(pd.DataFrame(data_scores).sort_values('date').to_dict())
 
    # Close session
    session.close()

    return precip_data

@app.route("/api/v1.0/stations")
def stations():
    
    # Create session
    session = Session(engine)

    # Return list of stations from dataset
    active_stations = session.query(measurement.station, func.count(measurement.station)).\
                    group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
    
    # Close session
    session.close()

    # Return results
    return jsonify(active_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    
    # Create session
    session = Session(engine)

    # Query temperature observations
    observations = session.query(func.max(measurement.tobs), func.min(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.station =='USC00519281').all()

    # Close session
    session.close()

    # Return results
    return jsonify(observations)

@app.route("/api/v1.0/<start>")
def start(start="yyyy-mm-dd"):
    
    # Create session
    session = Session(engine)

    calculations = session.query(func.max(measurement.prcp),func.min(measurement.prcp), func.avg(measurement.prcp)).filter(measurement.date >=start).all()

    # Close session
    session.close()

    # Return results
    return jsonify(calculations)

@app.route("/api/v1.0/<start>/<end>")
def end(start="yyyy-mm-dd", end="yyyy-mm-dd"):
    
    # Create session
    session = Session(engine)

    calculations = session.query(func.max(measurement.prcp),func.min(measurement.prcp), func.avg(measurement.prcp)).filter((measurement.date >=start)&(measurement.date <=end)).all()

    # Close session
    session.close()

    # Return results
    return jsonify(calculations)

if __name__ == "__main__" : 
    app.run(debug=True)