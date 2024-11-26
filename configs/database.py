from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

class InitDB:
    """Initializes a postgresql database connection"""

    db_name: str = os.getenv("DB_NAME", "savannah_ecommerce")
    db_user: str = os.getenv("DB_USER", "postgres")
    db_password: str = os.getenv("DB_PASSWORD", "postgres")
    db_port: int = os.getenv("DB_PORT", 5432)
    db_host: str = os.getenv("DB_HOST", "localhost")

    def connect(self):
        """This method makes a connection to the database"""
        try:
            # Use as context manager to close the connection
            # automatically afterwards
            with psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                port=self.db_port,
                host=self.db_host
            ) as conn:
                return conn
        except psycopg2.OperationalError as e:
            print("Failed to connect to the database")
            raise e