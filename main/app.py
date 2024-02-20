from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__) 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=["GET", "POST"])    
def index():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return render_template("login.html")

    
if __name__ == "__main__":
    main()