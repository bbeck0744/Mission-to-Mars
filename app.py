# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import mars_scrape
import os


# Hidden authetication file
#import config 

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def home(): 

    # Find data
    mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_info = mongo.db.mars_info
    mars_data = mars_scrape.mars_news()
    mars_data = mars_scrape.mars_image()
    mars_data = mars_scrape.mars_facts()
    mars_data = mars_scrape.mars_weather()
    mars_data = mars_scrape.mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)
