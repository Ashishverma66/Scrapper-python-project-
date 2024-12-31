#python -m pip install requests
#=> get data from web (html,json,xml)
#python -m pip install beautifulsoup4
#=>parse html

import requests    
from bs4 import BeautifulSoup

URL="http://books.toscrape.com/"

def scrape_book(url):
    response=requests.get(url)
    if response.status_code!=200:
        print(f'Failed to fetch the page, sttus code: {response.status_code}')
        return
    
    response.encoding=response.apparent_encoding
    

    
    soup=BeautifulSoup(response.text, "html.parser")
    books=soup.find_all("article", class_="product_pod")
    for book in books:
        title=book.h3.a['title']
        price_text=book.find("p", class_="price_color").text
    
        currency=price_text[0]
        price=price_text[1:]
        insert_book(title, currency, price)
    


import sqlite3

def create_connection():
     try:
         con=sqlite3.connect('books.sqlite3')
         return con
     except Exception as e:
         print(e)
         
def create_table(con):
    CREATE_BOOKS_TABLE_QUERY="""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title CHAR(255) NOT NULL,
            Currency CHAR(255) NOT NULL,
            Price CHAR(255) NOT NULL
        );
    """

    
    
    cur=con.cursor()
    cur.execute(CREATE_BOOKS_TABLE_QUERY)
    print("Books table was created successfully.")
    
def insert_book(Title, Currency, Price):
    con=sqlite3.connect("books.sqlite3")
    cursor=con.cursor()
    cursor.execute(
        "INSERT INTO books(Title,Currency,Price) VALUES (?,?,?)",
        (Title, Currency, Price)
    )
    
    con.commit()
    con.close()


    
con=create_connection()
    
create_table(con)
   
scrape_book(URL)




