import base64
from config import Config
from database_system.core import core_basic_lookup, core_basic_write_dict
from database_system.structure import get_recipes_table, get_middle_ingredients_recipes_table, get_ingredients_table
from mysql.connector import Error



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

def get_recipe_info_by_id(conn, recipe_id):
    config = Config()
    recipe_structure = get_recipes_table()
    ingredients_structure = get_ingredients_table()
    mid_ingredients_structure = get_middle_ingredients_recipes_table()
    query = (f"SELECT * "
             f"FROM "
             f"{config.db_name}.{ingredients_structure['table_name']} "
             f"INNER JOIN {config.db_name}.{mid_ingredients_structure['table_name']} "
             f"ON "
             f"{config.db_name}.{mid_ingredients_structure['table_name']}.ingredient_id = {config.db_name}.{ingredients_structure['table_name']}.ingredient_id "
             f"WHERE {config.db_name}.{mid_ingredients_structure['table_name']}.recipe_id = %s;")
    result  = core_basic_lookup(conn, query, values=recipe_id)
    return result


def insert_ingredient_list(conn, schema_name, data_dict, return_id=False):
    columns = ', '.join(data_dict.keys())
   
    placeholders = ', '.join(['%s'] * len(data_dict))  # Using %s as placeholder for MySQL
  
    ingredient_name = data_dict['ingredient_name']

    # Prepare the INSERT statement
    query = f"""INSERT INTO `{schema_name}`.ingredients ({columns}) VALUES ({placeholders});"
              WHERE NOT EXISTS (SELECT *
              FROM `{schema_name}`.ingredients
              WHERE `{schema_name}`.ingredients.ingredient_name = `{ingredient_name}`)"""

    id_query = "SELECT LAST_INSERT_ID();"  # Query to fetch the last inserted ID   

    # Execute the query with data values
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, list(data_dict.values()))
            conn.commit()  # Ensure to commit since autocommit might be False

            if return_id:
                cursor.execute(id_query)
                last_id = cursor.fetchone()[0]  # Fetch the last ID inserted
                return last_id

            print("Data inserted successfully.")
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()  # Rollback in case of error
        return None  # Return None in case of an error
