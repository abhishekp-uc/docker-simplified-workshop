# Import to make requests to get the news from website
import requests
# Import to parse the HTML
from bs4 import BeautifulSoup
# Import to interact with database
from database_connector import DBManager


# Define a function to parse the news page website and get title and description
def get_title_and_description_tuple_list(page=0):
    # Challenge: You can make this data extraction faster & consume less resource by other means, way way faster
    # Hint: Regex
    # Declare the news page url
    news_page_url = "https://www.indiatoday.in/india?page={page_number}"
    # Hit the news page site and get the HTML
    html = requests.get(news_page_url.format(page_number=page))
    # Create a beautiful soup object
    soup = BeautifulSoup(html.text, 'html.parser')
    # Parse the HTML and create a list of title and description
    title_description_tuple_list = []
    for details_div in soup.find_all('div', {'class': 'detail'}):
        title_description_tuple_list.append((details_div.h2.text, details_div.p.text))
    return title_description_tuple_list


# Define a function to get the news page as json from db if it already exists else parse it from the website
def get_news_page_as_json(page_no=0):
    # Check if the specific page number has already been extracted
    result_dict = DBManager.get_entries_from_db_for_page_no(page_no=page_no)
    if not result_dict:
        # Get all the title, description and page_no
        title_description_tuple_list = get_title_and_description_tuple_list(page=page_no)
        no_of_rows_inserted = DBManager.insert_all_title_description_into_db(title_description_tuple_list, page_no=page_no)
    result_dict = DBManager.get_entries_from_db_for_page_no(page_no=page_no)
    return result_dict
