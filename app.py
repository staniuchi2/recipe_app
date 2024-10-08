from flask import Flask, jsonify, request
from flask_cors import CORS
from app_helpers import *
from database_system.core import core_get_connection, core_basic_write_dict
from database_system.structure import get_recipes_table, get_schema
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


@app.route('/api/add_recipes', methods=['POST'])
def new_recipes():
    return_data = request.get_json()
    recipe_data = return_data['recipe_info']
    ingredients_data = return_data['ingredient_list']
    ingredient_name_dict = {'ingredient_name':ingredients_data[0]['ingredientName']}
    print(recipe_data)
    print(ingredient_name_dict)
    conn = core_get_connection()
    recipe_structure = get_recipes_table()
    core_basic_write_dict(conn, get_schema(), recipe_structure["table_name"], recipe_data)
 
 
    insert_ingredient_list(conn, get_schema(),ingredient_name_dict)
    conn.close()
    return jsonify(return_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=config.global_test_flag)
