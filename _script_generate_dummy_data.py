from database_system.core import core_get_connection
from dummy_data_factory.dummy_users import DummyUser


def main():
    user_id_list = []
    users_to_create = 5
    min_recipes_per_user = 5
    min_ingredients_per_recipe = 5
    min_reviews_per_recipe = 5
    max_recipes_per_user = 5
    max_ingredients_per_recipe = 5
    max_reviews_per_recipe = 5
    # Start by generating_users
    conn = core_get_connection()
    current_dummy_user = DummyUser()
    for user_count in range(users_to_create):
        current_dummy_user.populate_dummy_user()
        current_dummy_user.write_user_entry(conn)
        print(f"\nCreated fake user:")
        current_dummy_user.print_user_details()
    conn.close()


if __name__ == '__main__':
    main()
