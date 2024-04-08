from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from sympy import *
from sympy.abc import x
import numpy as np
from werkzeug.security import check_password_hash, generate_password_hash
import plotly.graph_objects as go
from cs50 import SQL



app = Flask(__name__) 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///users.db")


@app.route('/', methods=["GET", "POST"])    
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Forget user id
        session.clear()

        if not request.form.get("username"):
            return render_template("failure.html", message="Please enter a username")

        elif not request.form.get("password"):
            return render_template("failure.html", message="Please enter a password")

        rows = db.execute("SELECT * FROM users WHERE username = ?;", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("failure.html", message="Invalid username or password")

        if request.form.get("username") in rows[0]["username"]:

            session["user_id"] = rows[0]["id"]

            return redirect("/")

    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        usernames = db.execute("SELECT username FROM users;")

        if usernames:
            if request.form.get("username") in usernames[0]["username"]:
                return render_template("failure.html", message="Username taken")

        if request.form.get("confirm") != request.form.get("password"):
            return render_template("failure.html", message="Passwords do not match")

        hash = generate_password_hash(request.form.get("password"))

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?);", request.form.get("username"), hash)

        id = db.execute("SELECT id FROM users WHERE hash = ?;", hash)

        session["user_id"] = id[0]["id"]

        return redirect("/")
    else:
        return render_template("register.html")


@app.route('/calculate', methods=["GET", "POST"])        
def calculate():
    if request.method == "GET":
        return render_template("calculate.html")
    else:
        expression = request.form.get("expression")
        return render_template("calculate.html", expression=sympify(expression, evaluate=True))
    
    
@app.route('/simplify', methods=["GET", "POST"])        
def simplify():
    #TODO: Does not yet work as intended
    if request.method == "GET":
        return render_template("simplify.html")
    else:
        x = symbols('x')
        expression = simplify(sympify(request.form.get("expression")))
        
        return render_template("simplify.html", expression=expression)
    
@app.route('/graph', methods=["GET", "POST"])        
def graph():
    #TODO: Does not yet work as intended
    if request.method == "GET":
        return render_template("graph.html")
    else:
        x = symbols('x')
        expression = simplify(sympify(request.form.get("expression")))
        
        return render_template("graph.html", expression=expression)
    
@app.route("/failure")
def failure():
    return render_template("failure.html")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")
    
    
if __name__ == "__main__":
    main()