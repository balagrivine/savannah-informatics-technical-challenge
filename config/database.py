from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

class InitDB:
    """Initializes a postgresql database connection"""

    def __init__(self):
        """Initializes the InitDB class
        Attributes:
            None

        Methods:
            connect(): creates a connection to the database
        """
        self.db_name: str = os.getenv("DB_NAME", "savannah_ecommerce")
        self.db_user: str = os.getenv("DB_USER", "postgres")
        self.db_password: str = os.getenv("DB_PASSWORD", "postgres")
        self.db_port: int = os.getenv("DB_PORT", 5432)
        self.db_host: str = os.getenv("DB_HOST", "localhost")

    def connect(self):
        """This method makes a connection to the database"""
        try:
            connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                port=db_port,
                host=db_host
            )

            cursor = connection.cursor()
            return cursor
        except psycopg2.OperationalError as e:
            print("Failed to connect to the database")
            raise e
        finally:
            # Ensure db connection and cursor are closed to prevent
            # resource leaks
            if cursor:
                cursor.close()
            if connection:
                connection.close()
