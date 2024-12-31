import requests
import sqlite3    
from bs4 import BeautifulSoup

#python -m pip install requests
#=> get data from web (html,json,xml)
#python -m pip install beautifulsoup4
#=>parse html
#git config --global user.name "Ashishverma66"
#git config --global user.email "ashishvermadev66@gmail.com"
#git status #file ma k k  change xa
#git diff  #file vitra k k change cha
#git add . #file track garcha
#git commit -m "message" #k kam gareko xa

#Todays work
#install git
#create repository in github
#go to git bash
#git config --global user.name "Ashishverma66"
#git config --global user.email "ashishvermadev66@gmail.com"

#git init
#git status => if you want to check what are the status of files
#git diff => if you want to check what are the changes
#git add .
#git commit -m "Your message"
#copy past git code from github



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




