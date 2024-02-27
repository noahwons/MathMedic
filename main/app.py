from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

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
        for char in expression:
            if char == '+':
                result =  int(expression[0]) + int(expression[2])
        return render_template("calculate.html", expression=result)
    
    
if __name__ == "__main__":
    main()