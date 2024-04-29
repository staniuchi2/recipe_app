from faker import Faker
from database_system.core import core_basic_write_dict
from database_system.structure import get_users_table


class DummyUser:
    def __init__(self, locale="en_US"):
        self.fake = Faker(locale)
        self.user_id = None
        self.user_name = None
        self.user_password = None
        self.populate_dummy_user()

    def populate_dummy_user(self):
        self.generate_dummy_user_name()
        self.generate_dummy_user_password()

    def generate_dummy_user_name(self):
        self.user_name = f"{self.fake.word().capitalize()} {self.fake.word().capitalize()}"

    def generate_dummy_user_password(self):
        self.user_password = f"{self.fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)}"

    def get_user_entry_dict(self):
        user_entry = {
            "user_name": self.user_name,
            "user_password": self.user_password
        }
        return user_entry

    def get_user_id(self):
        return self.user_id

    def print_user_details(self):
        to_print = self.get_user_entry_dict()
        print(f"user_id: {self.get_user_id()}")
        for key in to_print:
            value = to_print[key]
            print(f"{key}: {value}")

    def write_user_entry(self, conn):
        current_user_dict = self.get_user_entry_dict()
        user_structure = get_users_table()
        schema_name = user_structure["schema_name"]
        table_name = user_structure["table_name"]
        current_user_id = core_basic_write_dict(conn, schema_name, table_name, current_user_dict, return_id=True)
        self.user_id = current_user_id
        return self.user_id
