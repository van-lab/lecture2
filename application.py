# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:53:51 2020

@author: home990
"""

from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def index():
  headline = "Hello from headline variable."
  return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
  headline = "Goodbye from headline variable."
  return render_template("index.html", headline=headline)

@app.route("/newyear")
def newyear():
  now = datetime.now()
  new_year = now.month==1 and now.day == 1
  new_year = True
  return render_template("index.html", new_year=new_year)

@app.route("/david")
def david():
  return "Hello, David"

@app.route("/<string:name>")
def  hello(name):
  name = name.capitalize()
  return f"Hello, {name}"

@app.route("/names")
def names():
  names = ["alice", "bob", "charlie"]
  return render_template("index.html", names=names)

@app.route("/more")
def more():
  return render_template("more.html")

@app.route("/less")
def less():
  return render_template("less.html")

@app.route("/myindex")
def myindex():
  return render_template("/myindex.html")

@app.route("/mymore")
def mymore():
  return render_template("/mymore.html")
  