import urllib2, json
import pprint
import sys
import urllib
import pykemon
<<<<<<< HEAD

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
