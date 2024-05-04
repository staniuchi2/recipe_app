from config import Config
from database_system.core import core_basic_lookup
from database_system.structure import get_recipes_table


def get_all_recipes(conn):
    config = Config()
    recipe_structure = get_recipes_table()
    query = (f"SELECT "
             f"recipe_id, recipe_name "
             f"FROM "
             f"{config.db_name}.{recipe_structure['table_name']};")
    result = core_basic_lookup(conn, query)
    return result


def get_recipe_by_id(conn, recipe_id):
    config = Config()
    recipe_structure = get_recipes_table()
    query = (f"SELECT "
             f"recipe_id, recipe_name "
             f"FROM "
             f"{config.db_name}.{recipe_structure['table_name']} "
             f"WHERE "
             f"recipe_id = %s;")
    result = core_basic_lookup(conn, query, values=recipe_id)
    if result:
        return result[0]
    return result
