import pandas as pd
from charge_util import charge_customer
import requests
from flask import jsonify

books_catalog=pd.DataFrame()
user_cart=[]

def refer_friend(mail,stars):
    try:
        response = requests.post('https://sharingGateway.com/referFriend', data={"mail":mail, "stars":stars})
        if response.status_code==200:
            return True
        else:
            return False
    except requests.exceptions.Timeout:
        return "Error: Request timed out."
    except requests.exceptions.RequestException as e:
         return "Error: {}".format(e)

def get_json_catalog():
    return books_catalog.to_json(orient='records')

def load_books():
    global books_catalog
    books_catalog = pd.read_csv("C:/Users/user/Documents/work/AICollege/Projects/APIBooksStoreProjectTehilaAshlag/books.csv")

def search_books(keyword):
    # Convert all relevant columns to lowercase for case-insensitive search
    books_catalog['Title'] = books_catalog['Title'].str.lower()
    books_catalog['Author'] = books_catalog['Author'].str.lower()
    books_catalog['Genre'] = books_catalog['Genre'].str.lower()

    # Search for the keyword in the title, author, or genre
    result_books_catalog = books_catalog[books_catalog['Title'].str.contains(keyword.lower()) |
                   books_catalog['Author'].str.contains(keyword.lower()) |
                   books_catalog['Genre'].str.contains(keyword.lower())]

    # Return the list of matching books
    matching_books = result_books_catalog.to_dict(orient='records')
    return matching_books

def add_to_cart(bookId):
    global user_cart
    added_to_cart=False
    if is_valid_book_id(bookId):
        user_cart.append(bookId)
        added_to_cart=True
    return added_to_cart


def is_valid_book_id(bookId):
    is_book_id_exist=False
    is_book_in_stock=False
    matching_valid_book=get_book_by_id(bookId)
    if not matching_valid_book.empty:
        is_book_id_exist=True
    if matching_valid_book['Availability'].values[0]=="In Stock":
        is_book_in_stock=True
    return is_book_id_exist and is_book_in_stock

def get_book_by_id(book_id):
    matching_valid_book=books_catalog[books_catalog['Id']==int(book_id)]
    return matching_valid_book  
    
def checkout():
    global user_cart
    total_price=0
    checkout_done=False
    for book_id in user_cart:
        book_details=get_book_by_id(book_id)
        total_price+=book_details['Price'].values[0]
    
    checkout_done=charge_customer(total_price)
    if checkout_done:
        user_cart=[]
    return checkout_done

def get_json_cart():
    if user_cart != [] and user_cart:
        books_in_cart = []
        for book_id in user_cart:
            book_details = get_book_by_id(book_id)
            if not book_details.empty:
                books_in_cart.append({"title": book_details["Title"].values[0], "price": book_details["Price"].values[0]})
    return jsonify(books_in_cart)