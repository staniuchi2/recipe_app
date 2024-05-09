import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        true_key_words = ["true", "1", "t", "y", "yes"]
        false_key_words = ["false", "0", "f", "n", "no"]

        # Check and convert the testing flag to a boolean for use
        global_test_flag = os.getenv("TEST_FLAG", "true").lower()
        if global_test_flag in true_key_words:
            self.__global_test_flag = True
        elif global_test_flag in false_key_words:
            self.__global_test_flag = False
        else:
            print(f"Warning!\nThe provided TEST_FLAG does not look valid, defaulting to True!")
            self.__global_test_flag = True

        # Automatically select which database to use based on the flag
        db_key_prefix = "TEST" if self.__global_test_flag else "PROD"
        self.__db_host = os.getenv(f"{db_key_prefix}_DB_HOST")
        self.__db_name = os.getenv(f"{db_key_prefix}_DB_NAME")
        self.__db_user = os.getenv(f"{db_key_prefix}_DB_USER")
        self.__db_root_user = os.getenv(f"{db_key_prefix}_DB_ROOT_USER")
        self.__db_port = os.getenv(f"{db_key_prefix}_DB_PORT")
        self.__db_password = os.getenv(f"{db_key_prefix}_DB_PASSWORD")
        self.__db_root_password = os.getenv(f"{db_key_prefix}_DB_ROOT_PASSWORD")
        self.__jwt_secret_key = os.getenv("JWT_SECRET_KEY")
        self.__jwt_expiry_delta = os.getenv("JWT_EXPIRY_DELTA")

    @property
    def global_test_flag(self):
        return self.__global_test_flag

    @property
    def db_host(self):
        return self.__db_host

    @property
    def db_name(self):
        return self.__db_name

    @property
    def db_user(self):
        return self.__db_user

    @property
    def db_root_user(self):
        return self.__db_root_user

    @property
    def db_port(self):
        return self.__db_port

    @property
    def db_password(self):
        return self.__db_password

    @property
    def db_root_password(self):
        return self.__db_root_password

    @property
    def jwt_secret_key(self):
        return self.__jwt_secret_key

    @property
    def jwt_expiry_delta(self):
        return self.__jwt_expiry_delta
