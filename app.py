from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = "potatoesRlife"

debug = DebugToolbarExtension(app)


@app.route("/")
def madlib_create():
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)

@app.route("/story.html")
def madlib_story():
    # prompts = story.prompts
    text = story.generate(request.args)
    return render_template("story.html", text = text)