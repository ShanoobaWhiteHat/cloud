#import flask library along with flask render template, request and requests

#initialize flask
from flask import Flask, render_template, request
import requests
app= Flask(__name__)
@app.route("/")
#Define visitor function to check how many visitor are there
def visitors():

    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    visitors_count = visitors_count + 1

    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()
    return render_template("index.html", count= visitors_count)
@app.route("/", methods= ["POST"])


def weather_stats():
    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    #Get latitude and longitude from the from
    latitude= request.form["Latitude"]
    longitude= request.form["Longitude"]
    api_url= 'https://weather-l6tl.onrender.com/api/getCurrentWeather/'+latitude+'/'+longitude
    response= requests.get(api_url)
    weather_data= response.json()
    return render_template("index.html", weather= weather_data, count= visitors_count)

#add code for executing flask
if __name__ == "__main__":
    app.run()
