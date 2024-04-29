from faker import Faker
from database_system.core import core_basic_write_dict
from database_system.structure import get_recipe_ratings


class DummyRating:
    def __init__(self):
        self.fake = Faker()
        self.rating_id = None
        self.user_id = None
        self.recipe_id = None
        self.score = None

    def populate_dummy_rating(self, user_id, recipe_id):
        self.user_id = user_id
        self.recipe_id = recipe_id
        self.score = self.fake.random_int(min=1, max=5)

    def get_rating_entry_dict(self):
        return {
            "user_id": self.user_id,
            "recipe_id": self.recipe_id,
            "score": self.score
        }

    def write_rating_entry(self, conn):
        rating_dict = self.get_rating_entry_dict()
        rating_structure = get_recipe_ratings()
        rating_id = core_basic_write_dict(conn, rating_structure["schema_name"], rating_structure["table_name"], rating_dict, return_id=True)
        self.rating_id = rating_id
        return self.rating_id
