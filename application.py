from flask import Flask, render_template, session, url_for, redirect
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SEESION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
    elif session["turn"] == "X" :
        ## Check if Y has won
        for i in range(3):
            # Row test
            if session["board"][i] == ["Y", "Y", "Y"]:
                return " Y has won"
            # Column test
            elif  session["board"][0][i] == "Y" and session["board"][1][i] == "Y" and session["board"][2][i] == "Y":
                return "Y has won"
       ## Diagonal tests
        if session["board"][0][0] == "Y" and session["board"][1][1] == "Y" and session["board"][2][2] == "Y":
            return "Y has won"
        elif session["board"][0][2] == "Y" and session["board"][1][1] == "Y" and session["board"][2][0] == "Y":
            return "Y has won"
    elif session["turn"] == "Y":
        ## Check if X has won
        for i in range(3):
            # Row test
            if session["board"][i] == ["X", "X", "X"]:
                return "X has won" 
            # Column test
            elif session["board"][0][i] == "X" and session["board"][1][i] == "X" and session["board"][2][i] == "X":
                return "X has won"
        ## Diagonal tests
        if session["board"][0][0] == "X" and session["board"][1][1] == "X" and session["board"][2][2] == "X":
            return "X has won"
        elif session["board"][0][2] == "X" and session["board"][1][1] == "X" and session["board"][2][0] == "X":
            return "X has won"

    return render_template("game.html", game = session["board"],turn = session["turn"])  

@app.route("/play/<int:row>/<int:col>")
def play(row,col):
    if session["turn"] == "X":
        session["board"][row][col] = "X"
        session["turn"] = "Y"
    else:
        session["board"][row][col] = "Y"
        session["turn"] = "X"

    return redirect(url_for("index"))