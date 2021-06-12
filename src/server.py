import requests
import os
import mysql.connector

from flask import Flask, redirect
from flask import request as flask_request
from bs4 import BeautifulSoup
server = Flask(__name__)


class DBManager:
    def __init__(self, database, host="workshop-mysql-db", user="root"):
        self.connection = mysql.connector.connect(
            user=user,
            password=os.environ['MYSQL_ROOT_PASSWORD'],
            host=host,  # Name of the MySQL DB container as set in the docker-compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()


# Declare the server
server = Flask(__name__)
database_connection = None


@server.route("/")
def landing_page():
    global database_connection
    database_connection_status = "OFF"
    landing_page_html = "<h1>Welcome, Database Connection: {db_conn_status}</h1>"
    if database_connection:
        database_connection_status = "ON"
    landing_page_html.format(db_conn_status=database_connection_status)


# @server.route("/create_db_conn", methods=['GET'])
# def landing_page():
#     global database_connection
#     # Database connection if not created then create
#     if not database_connection:
#         database_connection = DBManager(database=os.environ['MYSQL_DATABASE'])
#     redirect("/")
#
#
# @server.route('/get_news', methods=['GET'])
# def parse_news_page_html():
#     global database_connection
#     # If database connection is created only then proceed otherwise redirect to landing page
#     if database_connection:
#         # Declare the news page url
#         news_page_url = "https://www.indiatoday.in/india?page={page_number}"
#         # Get the parameter passed by the user
#         page = flask_request.args.get('page')
#         # Hit the news page site and get the HTML
#         html = requests.get(news_page_url.format(page_number=page))
#         # Create a beautiful soup object
#         soup = BeautifulSoup(html)
#         # Parse the HTML and create a list of title and description
#         title_description_tuple_list = []
#         for details_div in soup.find_all('div', {'class': 'detail'}):
#             title_description_tuple_list.serverend((details_div.h2.text, details_div.p.text))
#         # Insert into database
#     else:
#         redirect("/")


if __name__ == "__main__":
    server.run(debug=True, host='0.0.0.0', port=5000)
