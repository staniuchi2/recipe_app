from config import Config
import mysql.connector
from mysql.connector import Error


def core_get_connection():
    # ProgrammePilotConfig will automatically pick which database to connect to
    config = Config()
    connection = mysql.connector.connect(
        database=config.db_name,
        user=config.db_root_user,
        password=config.db_root_password,
        host=config.db_host,
        port=config.db_port,
        autocommit=True
    )
    return connection


def core_basic_lookup(conn, query, values=False, show_query=False):
    try:
        with conn.cursor(dictionary=True) as cursor:  # Use dictionary=True to get results as dictionaries
            if values:
                cursor.execute(query, (values,))  # Ensure values are passed as a tuple
            else:
                cursor.execute(query)
            result = cursor.fetchall()  # Fetch all results
            if show_query:
                print(cursor.statement)  # cursor.query is not valid in mysql.connector; use cursor.statement
        if not result:
            return None
        return result
    except Exception as error:
        print(f"An error occurred: {error}")
        return None


def core_basic_write_dict(conn, schema_name, table_name, data_dict):
    # Prepare column names and placeholders for the insert statement
    columns = ', '.join(data_dict.keys())
    placeholders = ', '.join(['%s'] * len(data_dict))  # Using %s as placeholder for MySQL

    # Prepare the INSERT statement
    query = f"INSERT INTO `{schema_name}`.`{table_name}` ({columns}) VALUES ({placeholders});"

    # Execute the query with data values
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, list(data_dict.values()))
            conn.commit()  # Ensure to commit since autocommit might be False
            print("Data inserted successfully.")
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()  # Rollback in case of error


def core_create_schema(conn, schema_name):
    create_schema_query = "CREATE DATABASE IF NOT EXISTS `{}`"
    formatted_query = create_schema_query.format(schema_name)
    try:
        with conn.cursor() as cursor:
            cursor.execute(formatted_query)
            conn.commit()  # Commit the transaction
            print(f"Database '{schema_name}' has been created or already exists.")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")



def core_create_minimal_table(conn, schema_name, table_name, primary_key_column_name):
    create_table_query = (
        "CREATE TABLE IF NOT EXISTS `{0}`.`{1}` (`{2}` INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (`{2}`))"
    ).format(schema_name, table_name, primary_key_column_name)
    try:
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)
            conn.commit()  # Commit the transaction
            print(f"Table '{table_name}' created in database '{schema_name}' with primary key '{primary_key_column_name}'.")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")


def core_add_columns_to_table(conn, schema_name, table_name, columns):
    # Query to check if a column exists
    check_column_exists_query = """
    SELECT EXISTS (
        SELECT 1 
        FROM information_schema.columns 
        WHERE table_schema = %s AND table_name = %s AND column_name = %s
    );
    """

    # Prepare and execute queries for each column
    try:
        with conn.cursor() as cursor:
            for column, data_type in columns.items():
                # Check if the column already exists
                cursor.execute(check_column_exists_query, (schema_name, table_name, column))
                exists = cursor.fetchone()[0]

                if not exists:
                    # Construct and execute the ADD COLUMN query
                    add_column_query = f"ALTER TABLE `{schema_name}`.`{table_name}` ADD COLUMN `{column}` {data_type};"
                    cursor.execute(add_column_query)
                    conn.commit()  # Commit after each column addition
                    print(f"Added column '{column}' to '{table_name}' in database '{schema_name}'.")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
        conn.rollback()  # Rollback if an error occurs


def core_add_foreign_keys_to_table(conn, schema_name, table_name, foreign_keys):
    if not foreign_keys:
        return

    with conn.cursor() as cursor:
        for foreign_key in foreign_keys:
            foreign_key_column = foreign_key['foreign_key_column']
            reference_schema = foreign_key['reference_schema']
            reference_table = foreign_key['reference_table']
            reference_column = foreign_key['reference_column']
            is_nullable = foreign_key['is_nullable']

            # Fetch column data type dynamically
            cursor.execute(f"""
                SELECT DATA_TYPE 
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s AND COLUMN_NAME = %s;
            """, (schema_name, table_name, foreign_key_column))
            result = cursor.fetchone()
            if result:
                data_type = result[0]

                # Modify column nullability based on 'is_nullable' flag
                if not is_nullable:
                    alter_column_query = f"ALTER TABLE `{schema_name}`.`{table_name}` MODIFY `{foreign_key_column}` {data_type} NOT NULL;"
                    cursor.execute(alter_column_query)

                # Add the foreign key constraint
                add_foreign_key_query = f"""
                ALTER TABLE `{schema_name}`.`{table_name}`
                ADD CONSTRAINT `fk_{table_name}_{foreign_key_column}_{reference_table}` FOREIGN KEY (`{foreign_key_column}`)
                REFERENCES `{reference_schema}`.`{reference_table}` (`{reference_column}`);
                """
                cursor.execute(add_foreign_key_query)
                print(f"Foreign key added to '{table_name}' referencing '{reference_table}'. Nullable: {is_nullable}")
            else:
                print(f"Data type for '{foreign_key_column}' in '{table_name}' could not be found.")

        conn.commit()





