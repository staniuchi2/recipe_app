from faker import Faker
import random
from database_system.core import core_basic_write_dict
from database_system.structure import get_recipes_table


class DummyRecipe:
    def __init__(self, locale="en_US"):
        self.fake = Faker(locale)
        self.recipe_id = None
        self.user_id = None
        self.recipe_name = None
        self.description = None
        self.steps = None
        self.portions = None

    def populate_dummy_recipe(self, user_id):
        self.user_id = user_id
        self.recipe_name = self.fake.sentence(nb_words=5)
        self.description = self.fake.text(max_nb_chars=200)
        self.steps = "\n".join(self.fake.sentences(nb=5))
        self.portions = random.randint(1, 12)

    def get_recipe_entry_dict(self):
        return {
            "user_id": self.user_id,
            "recipe_name": self.recipe_name,
            "description": self.description,
            "steps": self.steps,
            "portions": self.portions
        }

    def write_recipe_entry(self, conn):
        recipe_dict = self.get_recipe_entry_dict()
        recipe_structure = get_recipes_table()
        self.recipe_id = core_basic_write_dict(conn, recipe_structure["schema_name"], recipe_structure["table_name"], recipe_dict, return_id=True)
        return self.recipe_id
