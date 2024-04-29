from database_system.core import core_basic_write_dict, core_get_connection
from database_system.structure import get_recipes_table, get_users_table
data_insert_dict = {"user_id":1, "description":"Spinach pasta", "steps":"""1. Sason your meat with salt, pepper and ground nutmeg.
                    2. Brown and cook your meat till cooked through. 
                    3. Chop up your garlic and onions and add to the pan once the meat is done cooking.
                    4. Add the spinach and let it defrost, cook off the water that comes out the spinach as well.
                    5. Add in the double cream, taste and add more salt pepper and ground nutmeg as desired. """, "portions": 9}

recipe_table = get_recipes_table()
core_basic_write_dict(core_get_connection(), recipe_table["schema_name"], recipe_table["table_name"], data_insert_dict)
