from database_system.core import core_get_connection
from database_system.setup import setup_database


def main():
    conn = core_get_connection()
    setup_database(conn)
    conn.close()


if __name__ == '__main__':
    main()
