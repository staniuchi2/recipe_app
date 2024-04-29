from flask import Flask, render_template, request
from config import Config
from database_system.core import core_get_connection, core_basic_lookup
from database_system.structure import get_recipes_table

app = Flask(__name__)


def get_all_recipes(conn):
    config = Config()
    recipe_structure = get_recipes_table()
    query = (f"SELECT "
             f"recipe_id, recipe_name "
             f"FROM "
             f"{config.db_name}.{recipe_structure['table_name']};")
    result = core_basic_lookup(conn, query)
    return result


@app.route('/', methods=['GET'])
def index():
    conn = core_get_connection()
    recipe_list = get_all_recipes(conn)
    conn.close()
    return render_template('index.html', recipes=recipe_list)


@app.route("/recipes/<recipe_id>", methods=['GET', 'POST'])
def recipes(recipe_id):
    return render_template("recipes.html", recipe=recipe_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
