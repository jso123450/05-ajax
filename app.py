import urllib2, json
import pprint
import sys
import urllib

from flask import Flask, render_template, redirect
#for google book api: pip install --upgrade google-api-python-client
#for goodreads api: http://www.goodreads.com/api/ (cannot find way to pull full list of random books)
#http://www.readbookonline.net/titles-a.htm nice sized list
app = Flask(__name__)
@app.route("/")
def home():
    return "home"

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
