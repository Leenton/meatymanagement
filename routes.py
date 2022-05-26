from flask import Flask, render_template, url_for, redirect, request, session, jsonify, json
import os
import random
UPLOAD_FOLDER = "./static/uploads"
app = Flask(__name__)

app.config['SECRET_KEY'] = "684a2c31fa1f159e791fbd0d01e4214c58b1ba170543bd7085dd61c722617f9f"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/",  methods=["GET"])
def home():
    return render_template("home.html") 

@app.route("/anison",  methods=['GET'])
def anison():
    return render_template("assets.html")

@app.route("/tournament",  methods=['GET'])
def tournament():
    return render_template("tournament.html")

@app.route("/art",  methods=['GET'])
def art():
    Memes = os.listdir(".//static//MeatyMemes")
    Meme = Memes[random.randint(0,(len(Memes)) - 1)]
    return render_template("art.html", Meme=Meme)

@app.route("/privacy",  methods=['GET'])
def privacy():
    return "We steal all your data so we can sell it to the Meaty Mafia"

if __name__ == "__main__":
    app.run(use_reloader=False, host= '0.0.0.0', debug=True)