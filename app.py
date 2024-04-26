from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')


@app.route("/recipes/<recipe_id>")
def recipes(recipe_id):
    return render_template("recipes.html")