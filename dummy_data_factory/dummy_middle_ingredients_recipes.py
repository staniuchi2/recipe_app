from database_system.core import core_basic_write_dict
from database_system.structure import get_middle_ingredients_recipes_table
from faker import Faker


class DummyMiddleIngredientsRecipes:
    def __init__(self):
        self.fake = Faker()

    def write_middle_ingredient_recipe_entry(self, conn, recipe_id, ingredient_id):
        middle_ingredients_recipes_table = get_middle_ingredients_recipes_table()
        entry_dict = {
            "recipe_id": recipe_id,
            "ingredient_id": ingredient_id,
            "amount": self.fake.random_int(min=1, max=500),
            "unit": self.fake.random_element(elements=("grams", "ml", "cups", "tablespoons", "teaspoons"))
        }
        core_basic_write_dict(conn, middle_ingredients_recipes_table["schema_name"], middle_ingredients_recipes_table["table_name"], entry_dict)
