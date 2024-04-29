from flask import Flask, render_template, request
from database_system.core import core_get_connection
from mysql.connector import connect, Error

app = Flask(__name__)

conn = core_get_connection()
cursor = conn.cursor()

def refresh_recipe_list():
    query = """SELECT recipe_id, recipe_name
            FROM test_db_name.recipes"""
    cursor.execute(query)
    result = cursor.fetchall()
    return result


@app.route('/', methods = ['GET'])
def index():
    recipe_list = refresh_recipe_list()
    return render_template('index.html', recipes = recipe_list)


@app.route("/recipes/<recipe_id>", methods = ['GET','POST'])
def recipes(recipe_id):

    return render_template("recipes.html", recipe = recipe_id)