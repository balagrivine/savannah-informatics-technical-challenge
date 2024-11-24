import psycopg2
from psycopg2.extras import DictCursor
from fastapi import HTTPException
from typing import Optional

from configs.database import InitDB


class CustomerRepository(InitDB):
    """This class handles data manipulation in the customers database"""

    def __init__(self):
        """Initializes the CustomerRepository class"""

        # Call the connect method of the base class to create db connection
        self.conn = self.connect()

    def create_customer(
            self,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
            shipping_address: Optional[str]=None
        ):
        """Creates a new customer in the database"""
        
        sql_context = """
        INSERT INTO
            customers (first_name, last_name, email, password, shipping_address)
        VALUES
            (%s, %s, %s, %s, %s);
        """
        data = (first_name, last_name, email, password, shipping_address)
        
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql_context, data)

            self.conn.commit()
        except psycopg2.DataError as e:
            self.conn.rollback()
            raise HTTPException(
                status_code=400, detail=f"Data error occured, possibly due to invalid data: {e}"
            )
        except psycopg2.IntegrityError as e:
            self.conn.rollback()
            raise HTTPException(
                status_code=409, detail="User with the same email already exists"
            )

    def get_customer_by_id(self, customer_id: int):
        """Gets a single user from the database with the specified id"""

        sql_context = """
        SELECT
            id, first_name, last_name, email, shipping_address
        FROM
            customer
        WHERE
            id=%s;
        """
        data = (customer_id,)

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql_context, data)
                customer = cursor.fetchone()

            return customer
        except psycopg2.DataError:
            self.conn.rollback()
            raise HTTPException(
                status_code=400,
                detail="Data error occured, possibly due to invalid data"
            )
    def get_customer_by_email(self, email: str):
        """Gets a single customer from the database with with the specified email"""

        sql_context = """
        SELECT
            id, email, password
        FROM
            customers
        WHERE
            email=%s;
        """
        data = (email,)

        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(sql_context, data)
                customer = cursor.fetchone()

            self.conn.commit()
            return customer
        except psycopg2.Error as e:
            pass
