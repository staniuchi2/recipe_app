import random
from database_system.core import core_get_connection
from dummy_data_factory.dummy_users import DummyUser
from dummy_data_factory.dummy_recipes import DummyRecipe
from dummy_data_factory.dummy_ingredients import DummyIngredient
from dummy_data_factory.dummy_middle_ingredients_recipes import DummyMiddleIngredientsRecipes
from dummy_data_factory.dummy_ratings import DummyRating

global_ingredients = {}


def create_user(conn):
    dummy_user = DummyUser()
    dummy_user.populate_dummy_user()
    user_id = dummy_user.write_user_entry(conn)
    print(f"\nCreated fake user: ID = {user_id}")
    dummy_user.print_user_details()
    return user_id


def create_recipes_for_user(conn, user_id, min_recipes, max_recipes):
    num_recipes = random.randint(min_recipes, max_recipes)
    print(f"Generating {num_recipes} recipes for user ID {user_id}")
    for _ in range(num_recipes):
        recipe_id = create_recipe(conn, user_id)
        create_ingredients_and_links(conn, recipe_id)
        create_reviews_for_recipe(conn, recipe_id, user_id)


def create_recipe(conn, user_id):
    dummy_recipe = DummyRecipe()
    dummy_recipe.populate_dummy_recipe(user_id)
    recipe_id = dummy_recipe.write_recipe_entry(conn)
    print(f"Recipe created: ID = {recipe_id}")
    return recipe_id


def create_or_get_ingredient(conn, used_ingredients):
    dummy_ingredient = DummyIngredient()
    dummy_ingredient.populate_dummy_ingredient()

    # 20% chance to reuse an existing ingredient if available and not used in this recipe
    if random.random() < 0.20 and global_ingredients and any(name not in used_ingredients for name in global_ingredients):
        possible_reuse = [name for name in global_ingredients if name not in used_ingredients]
        if possible_reuse:
            chosen_ingredient = random.choice(possible_reuse)
            ingredient_id = global_ingredients[chosen_ingredient]
            print(f"Force reusing existing ingredient by chance: ID = {ingredient_id}, Name = {chosen_ingredient}")
            used_ingredients.add(chosen_ingredient)
            return ingredient_id

    # Avoid using the same ingredient in one recipe
    while dummy_ingredient.ingredient_name in used_ingredients:
        dummy_ingredient.populate_dummy_ingredient()

    # Check if the ingredient already exists globally
    if dummy_ingredient.ingredient_name in global_ingredients:
        ingredient_id = global_ingredients[dummy_ingredient.ingredient_name]
        print(f"Reusing existing ingredient: ID = {ingredient_id}, Name = {dummy_ingredient.ingredient_name}")
    else:
        ingredient_id = dummy_ingredient.write_ingredient_entry(conn)
        global_ingredients[dummy_ingredient.ingredient_name] = ingredient_id
        print(f"Ingredient added: ID = {ingredient_id}, Name = {dummy_ingredient.ingredient_name}")

    # Add to used ingredients to prevent reuse in the same recipe
    used_ingredients.add(dummy_ingredient.ingredient_name)
    return ingredient_id


def create_ingredients_and_links(conn, recipe_id):
    min_ingredients, max_ingredients = 3, 7
    num_ingredients = random.randint(min_ingredients, max_ingredients)
    used_ingredients = set()  # Track ingredients used in this recipe
    print(f"Adding {num_ingredients} ingredients to recipe ID {recipe_id}")
    for _ in range(num_ingredients):
        ingredient_id = create_or_get_ingredient(conn, used_ingredients)
        link_ingredient_to_recipe(conn, recipe_id, ingredient_id)


def create_ingredient(conn):
    dummy_ingredient = DummyIngredient()
    dummy_ingredient.populate_dummy_ingredient()
    ingredient_id = dummy_ingredient.write_ingredient_entry(conn)
    print(f"Ingredient added: ID = {ingredient_id}")
    return ingredient_id


def link_ingredient_to_recipe(conn, recipe_id, ingredient_id):
    middle = DummyMiddleIngredientsRecipes()
    middle.write_middle_ingredient_recipe_entry(conn, recipe_id, ingredient_id)
    print(f"Linked recipe ID {recipe_id} with ingredient ID {ingredient_id}")


def create_reviews_for_recipe(conn, recipe_id, user_id):
    min_reviews, max_reviews = 1, 3
    num_reviews = random.randint(min_reviews, max_reviews)
    print(f"Creating {num_reviews} reviews for recipe ID {recipe_id}")
    for _ in range(num_reviews):
        create_review(conn, recipe_id, user_id)


def create_review(conn, recipe_id, user_id):
    dummy_rating = DummyRating()
    dummy_rating.populate_dummy_rating(user_id, recipe_id)
    rating_id = dummy_rating.write_rating_entry(conn)
    print(f"Review created: Rating ID = {rating_id}")


def main():
    conn = core_get_connection()
    print("Database connection established.")
    users_to_create = 5
    min_recipes_per_user, max_recipes_per_user = 5, 10
    try:
        for _ in range(users_to_create):
            user_id = create_user(conn)
            create_recipes_for_user(conn, user_id, min_recipes_per_user, max_recipes_per_user)
    finally:
        conn.close()
        print("Database connection closed.")


if __name__ == '__main__':
    main()
