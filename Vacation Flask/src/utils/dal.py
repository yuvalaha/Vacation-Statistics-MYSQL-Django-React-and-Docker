from mysql.connector import connect
from .app_config import AppConfig


class Dal:
    # Constructor - creating new connection
    def __init__(self):
        self.connection = connect(
            host=AppConfig.mysql_host,
            user=AppConfig.mysql_user,
            password=AppConfig.mysql_password,
            database=AppConfig.mysql_database)

    # Get table
    def get_table(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()  # Get the table
            return table

    # Get one item
    def get_scalar(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            scalar = cursor.fetchone()  # Get the item
            return scalar

    # Insert row
    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()  # Save the database
            last_row_id = cursor.lastrowid  # Get the last row id
            return last_row_id

    # Update row
    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()  # Save the database
            row_count = cursor.rowcount  # How many rows we updated
            return row_count

    # Delete row
    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()  # Save the database
            row_count = cursor.rowcount  # How many rows we deleted
            return row_count

    # Executing stored procedure
    def execute_stored_procedure(self, procedure_name, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.callproc(procedure_name, params)
            result = next(cursor.stored_results(), None)
            table = result.fetchall()
            return table

    # Close resources
    def close(self):
        self.connection.close()
