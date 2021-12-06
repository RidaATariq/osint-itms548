# -*- coding: utf-8 -*-
"""
@authors: David Ngige & Rida Tariq

"""

from flask import Flask, render_template, request
from reddit_api import get_data, credentials, get_data

# Flask app
app = Flask(__name__)
app.config.from_pyfile("config.py")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("btn")
        data = get_data(query)
        if data:
            return render_template("index.html", data=data, banner="Here are your results")
        return render_template("index.html", banner="Could not find any related data")
    return render_template("index.html", banner="Search for your topic.")

@app.route("/twitter", methods = ["GET", "POST"])
def twitter_idx():
    if request.method == "POST":
        query = request.form.get("btn")
        data = get_data(query)
        if data:
            return render_template("twitter_idx.html", data=data, banner="Here are your results")
        return render_template("twitter_idx.html", banner="Could not find any related data")
    return render_template("twitter_idx.html", banner="Search for your topic.")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
