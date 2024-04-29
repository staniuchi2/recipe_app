from faker import Faker
from database_system.core import core_basic_write_dict
from database_system.structure import get_ingredients_table


class DummyIngredient:
    def __init__(self):
        self.fake = Faker()
        self.ingredient_name = None

    def populate_dummy_ingredient(self):
        self.ingredient_name = self.fake.word().capitalize()

    def get_ingredient_entry_dict(self):
        return {"ingredient_name": self.ingredient_name}

    def write_ingredient_entry(self, conn):
        ingredient_dict = self.get_ingredient_entry_dict()
        ingredient_structure = get_ingredients_table()
        ingredient_id = core_basic_write_dict(conn, ingredient_structure["schema_name"], ingredient_structure["table_name"], ingredient_dict, return_id=True)
        return ingredient_id
