from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from jinja2 import Template
import scrape_mars


app = Flask(__name__)
#  template_folder='../pages/templates')

# app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_data"
# mongo = PyMongo(app)
mongo=PyMongo(app, uri="mongodb://localhost:27017/mars_data")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    Mars= mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", Mars=Mars)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)

