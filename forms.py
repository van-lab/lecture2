from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def myindex():
  return render_template("myindex.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
  if request.method == "GET":
    return "Please submit the form."
  else:
    name = request.form.get("name")
    return render_template("hello.html", name=name)
