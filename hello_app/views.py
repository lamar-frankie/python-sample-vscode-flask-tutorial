from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("convert_temp/<temp>")
def convert_temp(temp):
    input_temp = float(temp)
    #conversion
    f_to_c = ((input_temp - 32) * (5.0 /9.0))
    
    return "{:.1f}".format(input_temp) + " degrees F is " + "{:.1f}".format(f_to_c) + " degrees C"
