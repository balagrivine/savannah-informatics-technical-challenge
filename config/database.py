from dotenv import load_dotenv
import os
import psycopg3

load_dotenv()

def init_db():
    """Initializes a postgresql database connection"""

    db_url = os.getenv("DB_URL")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_port = os.getenv("DB_PORT")
    db_host = os.getenv("DB_HOST")

    connection = psycopg3.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        port=db_post,
        host=db_host
    )

    cursor = connection.cursor()
    return cursor
