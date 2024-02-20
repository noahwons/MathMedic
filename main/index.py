from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__) 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=["GET", "POST"])    
def index():
    if request.method == "GET":
        # do sum shit
        pass
    else:
        return render_template("index.html")

    
if __main__ == "__name__":
    main()