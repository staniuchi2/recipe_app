from database_system.core import core_create_minimal_table, core_add_columns_to_table, core_add_foreign_keys_to_table
from database_system.structure import get_all_required_tables


def setup_database(conn):
    all_tables = get_all_required_tables()
    for table in all_tables:
        print(f"Creating {table['table_name']}")
        core_create_minimal_table(conn, table["schema_name"], table["table_name"], table["primary_key"])
        # Add additional columns
        if table["columns"]:
            print(f"Adding columns to table {table['table_name']} in schema {table['schema_name']}.")
            core_add_columns_to_table(conn, table["schema_name"], table["table_name"],
                                      table["columns"])

        # Add foreign key constraints if any
        if table.get("foreign_keys"):
            print(f"Adding foreign keys to table {table['table_name']} in schema {table['schema_name']}.")
            core_add_foreign_keys_to_table(conn, table["schema_name"], table["table_name"],
                                           table["foreign_keys"])
        