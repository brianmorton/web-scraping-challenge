#app.py
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_dict = mongo.db.mars_dict.find_one()
    print(mars_dict)
    return render_template("index.html",  mars_dict=mars_dict)


@app.route("/scrape")
def scraper():
    mars_dict = mongo.db.mars_dict
    print("before scrape")
    mars_dict_data = scrape_mars.scrape()
    print("after scrape")
    mars_dict.update({}, mars_dict_data, upsert=True)
    return redirect("/", code=302)




#end
if __name__ == "__main__":
    app.run(debug=True)
