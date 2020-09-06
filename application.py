from flask import Flask, render_template, session, redirect, url_for
#from flask_session import Session
#from tempfile import mkdtemp

app = Flask(__name__)

#app.config["SESSION_FILE_DIR"] = mkdtemp()
#app.config["SEESION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)
@app.route("/")
def index():
    return render_template("index.html")