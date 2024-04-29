from config import Config


def get_schema():
    config = Config()
    return config.db_name


def get_all_required_tables():
    all_tables = [
        get_ingredients_table(),
        get_users_table(),
        get_recipes_table(),
        get_middle_ingredients_recipes_table(),
        get_recipe_ratings()
    ]
    return all_tables


def get_ingredients_table():
    ingredients_table = {
        "schema_name": get_schema(),
        "table_name": "ingredients",
        "primary_key": "ingredient_id",
        "columns": {
            "ingredient_name": "TEXT"
        },
        "foreign_keys": None
    }
    return ingredients_table


def get_users_table():
    users_table = {
        "schema_name": get_schema(),
        "table_name": "users",
        "primary_key": "user_id",
        "columns": {
            "user_name": "TEXT",
            "user_password": "TEXT"
        },
        "foreign_keys": None
    }
    return users_table


def get_recipes_table():
    user_structure = get_users_table()
    recipes_table = {
        "schema_name": get_schema(),
        "table_name": "recipes",
        "primary_key": "recipe_id",
        "columns": {
            user_structure["primary_key"]: "INTEGER",
            "recipe_name": "TEXT",
            "description": "TEXT",
            "steps": "TEXT",
            "portions": "INTEGER"
        },
        "foreign_keys": [
            {
                "foreign_key_column": user_structure["primary_key"],
                "reference_schema": user_structure["schema_name"],
                "reference_table": user_structure["table_name"],
                "reference_column": user_structure["primary_key"],
                "is_nullable": False
            }
        ]
    }
    return recipes_table


def get_middle_ingredients_recipes_table():
    recipes_structure = get_recipes_table()
    ingredients_structure = get_ingredients_table()
    middle_ingredients_recipes_table = {
        "schema_name": get_schema(),
        "table_name": "middle_ingredients_recipes",
        "primary_key": "mir_id",
        "columns": {
            recipes_structure["primary_key"]: "INTEGER",
            ingredients_structure["primary_key"]: "INTEGER",
            "amount": "INTEGER",
            "unit": "TEXT"
        },
        "foreign_keys": [
            {
                "foreign_key_column": recipes_structure["primary_key"],
                "reference_schema": recipes_structure["schema_name"],
                "reference_table": recipes_structure["table_name"],
                "reference_column": recipes_structure["primary_key"],
                "is_nullable": False
            },
            {
                "foreign_key_column": ingredients_structure["primary_key"],
                "reference_schema": ingredients_structure["schema_name"],
                "reference_table": ingredients_structure["table_name"],
                "reference_column": ingredients_structure["primary_key"],
                "is_nullable": False
            }
        ]
    }
    return middle_ingredients_recipes_table


def get_recipe_ratings():
    recipes_structure = get_recipes_table()
    user_structure = get_users_table()
    recipe_ratings_table = {
        "schema_name": get_schema(),
        "table_name": "ratings",
        "primary_key": "rating_id",
        "columns": {
            recipes_structure["primary_key"]: "INTEGER",
            user_structure["primary_key"]: "INTEGER",
            "score": "INTEGER"
        },
        "foreign_keys": [
            {
                "foreign_key_column": recipes_structure["primary_key"],
                "reference_schema": recipes_structure["schema_name"],
                "reference_table": recipes_structure["table_name"],
                "reference_column": recipes_structure["primary_key"],
                "is_nullable": False
            },
            {
                "foreign_key_column": user_structure["primary_key"],
                "reference_schema": user_structure["schema_name"],
                "reference_table": user_structure["table_name"],
                "reference_column": user_structure["primary_key"],
                "is_nullable": False
            }
        ]
    }
    return recipe_ratings_table
