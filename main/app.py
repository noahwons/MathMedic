from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from sympy import *
from sympy.abc import x

app = Flask(__name__) 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=["GET", "POST"])    
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    
@app.route('/login', methods=["GET", "POST"])    
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return render_template("login.html")


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
    
    
if __name__ == "__main__":
    main()