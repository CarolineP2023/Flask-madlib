from flask import Flask, request , render_template
from stories import story


app = Flask(__name__)




@app.route("/")
def home_page():
    """ gives us inputs to add words for madlib"""
    return render_template("home.html")

@app.route("/story")
def get_story():
    """generates story from given words from home page"""
    generated_story = story.generate(request.args)

    return render_template("story.html", text=generated_story)