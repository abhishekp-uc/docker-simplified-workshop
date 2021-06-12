# Import to send response as json data
import json
# Import to interact with database
from database_connector import DBManager
# Import to get news page as json
from data_extractor import get_news_page_as_json

# Imports to make flask work
from flask import Flask, url_for, redirect, render_template
from flask import request as flask_request


# Declare the server
server = Flask(__name__)


# Initially we will ask the user to turn on the database connection to the MySQL container
# This is done so that we can show that we are actually connecting to the database,
# MySQL Command to check who is logged in -
# SELECT user, host FROM mysql.user;
@server.route("/")
def landing_page():
    return render_template("index.html", db_manager_status=DBManager.is_connected)


# This function will toggle the database connection on and off
@server.route("/db_manager", methods=['GET'])
def db_manager():
    if not DBManager.is_connected:
        DBManager.connect()
    elif DBManager.is_connected:
        DBManager.disconnect()
    return redirect(url_for('landing_page'))


@server.route('/get_news', methods=['GET'])
def parse_news_page_html():
    # If database connection is created only then proceed otherwise redirect to landing page
    if DBManager.connection:
        # Get the parameter passed by the user in the url
        page_no = flask_request.args.get('page', default=0)
        news_page_json = get_news_page_as_json(page_no=page_no)
        return json.dumps(news_page_json)
    else:
        return redirect(url_for('landing_page'))


if __name__ == "__main__":
    try:
        server.run(debug=True, host='0.0.0.0', port=5000)
    finally:
        DBManager.disconnect()
