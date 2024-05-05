import base64
from config import Config
from database_system.core import core_basic_lookup
from database_system.structure import get_recipes_table


def convert_image_to_base64(image):
    return base64.b64encode(image).decode('utf-8') if image else None


def get_all_recipes(conn):
    config = Config()
    recipe_structure = get_recipes_table()
    query = (f"SELECT * "
             f"FROM "
             f"{config.db_name}.{recipe_structure['table_name']};")
    recipes = core_basic_lookup(conn, query)
    for recipe in recipes:
        if recipe['recipe_image']:
            recipe['recipe_image'] = convert_image_to_base64(recipe['recipe_image'])
    return recipes


def get_recipe_by_id(conn, recipe_id):
    config = Config()
    recipe_structure = get_recipes_table()
    query = (f"SELECT * "
             f"FROM "
             f"{config.db_name}.{recipe_structure['table_name']} "
             f"WHERE "
             f"recipe_id = %s;")
    result = core_basic_lookup(conn, query, values=recipe_id)
    if result:
        recipe = result[0]
        if recipe['recipe_image']:
            recipe['recipe_image'] = convert_image_to_base64(recipe['recipe_image'])
        return recipe
    return result

