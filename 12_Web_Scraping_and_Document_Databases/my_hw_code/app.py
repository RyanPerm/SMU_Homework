from flask import Flask, render_template, redirect
import pymongo
from scrape import scrape_info

app = Flask(__name__)
scrapeMars = Scrape_info()

#mongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_app

@app.route("/")
def home():

    mars_data = db.mars_data.find_one()

    return render_template("index.html", mars-mars_data)

@app.route("/scrape")
def scrape():
    scraped_data = scrapeMars.scrape_info()
    db.mars_data.update({}, scraped_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)