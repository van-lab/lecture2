from flask import Flask, render_template, request, session
from flask_session import Session
#from flask_session.__init__ import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods=["GET", "POST"])
def noteindex():
  if session.get("notes") is None:
    session["notes"] = []
  if request.method == "POST":
    note = request.form.get("note")
    session["notes"].append(note)
  return render_template("noteindex.html", notes=session["notes"])

@app.route("/hello", methods=["GET", "POST"])
def hello():
  if request.method == "GET":
    return "Please submit the form."
  else:
    name = request.form.get("name")
    return render_template("hello.html", name=name)
