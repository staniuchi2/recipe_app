from flask import Flask, jsonify
from flask_cors import CORS
from app_helpers import get_all_recipes, get_recipe_by_id, get_recipe_info_by_id
from database_system.core import core_get_connection
from config import Config
app = Flask(__name__)
CORS(app)
config = Config()

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    conn = core_get_connection()
    all_recipes = get_all_recipes(conn)
    conn.close()
    return jsonify(all_recipes)


@app.route("/api/recipes/<recipe_id>", methods=['GET', 'POST'])
def recipes(recipe_id):
    conn = core_get_connection()
    current_recipe = get_recipe_by_id(conn, recipe_id)
    ingredient_list = get_recipe_info_by_id(conn, recipe_id)
    recipe_info = {"recipe":current_recipe, "ingredients":ingredient_list}
    print(ingredient_list)
    conn.close()
    return jsonify(recipe_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=config.global_test_flag)
