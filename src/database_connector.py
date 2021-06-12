# Imported used to connect to MySQL
import mysql.connector
# Import to get the environmental keys
import os


# The database connector which connects to the MySQL database
class DBManager:
    # Declare global variables
    connection = None
    cursor = None
    is_connected = False

    # Define method to connect to the MySQL container
    @classmethod
    def connect(cls, database=None, host="workshop-mysql-db", user="root"):
        # Connect to database if already not connected
        if not cls.connection:
            cls.connection = mysql.connector.connect(
                user=user,
                password=os.environ['MYSQL_ROOT_PASSWORD'],
                host=host,  # Name of the MySQL DB container as set in the docker-compose.yml file
                database=database if database else os.environ['MYSQL_DATABASE'],
                auth_plugin='mysql_native_password'
            ) # FYI this uses the default port i.e if you had changed the port then you would need to update this code
            cls.cursor = cls.connection.cursor(dictionary=True)
            cls.is_connected = True

    # Define method to disconnect to the MySQL container
    @classmethod
    def disconnect(cls):
        # DisConnect to database if only connected
        if cls.connection:
            # Close the connection
            cls.connection.close()
            # Reset the database manager variables
            cls.connection = None
            cls.cursor = None
            cls.is_connected = False

    # Define method to insert all title, description from news page into database in one query
    @classmethod
    def insert_all_title_description_into_db(cls, title_description_tuple_list, page_no):
        if cls.cursor:
            insert_title_description_query = f"INSERT INTO news_articles (title, description, page_no) VALUES (%s, %s, {page_no})"
            cls.cursor.executemany(insert_title_description_query, title_description_tuple_list)
            cls.connection.commit()
            return len(title_description_tuple_list)

    # Define method to get the title, description for a particular page from database as dictionary
    @classmethod
    def get_entries_from_db_for_page_no(cls, page_no):
        if cls.cursor:
            select_title_description_for_page_no_query = f"SELECT title, description FROM news_articles WHERE page_no = {page_no}"
            cls.cursor.execute(select_title_description_for_page_no_query)
            return cls.cursor.fetchall()
        return None
