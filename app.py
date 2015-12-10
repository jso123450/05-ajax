import urllib2, json
import pprint
import sys
import urllib
import pykemon
from flask import Flask, render_template, redirect
#pip install pykemon

app = Flask(__name__)
@app.route("/")
def home():
    return "home"

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
