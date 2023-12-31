import pandas as pd
from charge_util import chargeCustomer
import requests

def referFriend(mail,stars):
    try:
        response = requests.post('https://sharingGateway.com/referFriend', data={"mail":mail, "stars":stars})
        if response.status_code==200:
            return True
        else:
            return False
    except requests.exceptions.Timeout:
        print("Timeout")
    except requests.exceptions.RequestException:
        print("RequestException")


def main():
    booksCatalog=loadCatalog()
    menu(booksCatalog)


def freindlyInput(msg):
    return input('''
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
          
          '''+msg+" - ") 


def printMsg(msg):
    print('''
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
          
          '''+msg+
'''

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

          ''') 

def loadCatalog():
    booksCatalog = pd.read_csv("C:/Users/user/Documents/work/AICollege/Projects/BooksStore/books.csv")
    return booksCatalog

def searchBooks(booksCatalog,keyword):
    # Convert all relevant columns to lowercase for case-insensitive search
    booksCatalog['Title'] = booksCatalog['Title'].str.lower()
    booksCatalog['Author'] = booksCatalog['Author'].str.lower()
    booksCatalog['Genre'] = booksCatalog['Genre'].str.lower()

    # Search for the keyword in the title, author, or genre
    result_booksCatalog = booksCatalog[booksCatalog['Title'].str.contains(keyword.lower()) |
                   booksCatalog['Author'].str.contains(keyword.lower()) |
                   booksCatalog['Genre'].str.contains(keyword.lower())]

    # Return the list of matching books
    matching_books = result_booksCatalog.to_dict(orient='records')
    return matching_books

def addToCart(booksCatalog,bookId,userCart):
    if isValidBookId(booksCatalog,bookId):
        userCart.append(bookId)
    return userCart

def isValidBookId(booksCatalog,bookId):
    isBookIdExist=False
    isBookInStock=False
    matching_valid_book=getBookById(booksCatalog,bookId)
    if not matching_valid_book.empty:
        isBookIdExist=True
    if matching_valid_book['Availability'].values[0]=="In Stock":
        isBookInStock=True
    return isBookIdExist and isBookInStock

def getBookById(booksCatalog,bookId):
    matching_valid_book=booksCatalog[booksCatalog['Id']==int(bookId)]
    return matching_valid_book  
    
def checkout(booksCatalog,userCart):
    totalPrice=0
    checkoutDone=False
    for index, bookId in enumerate(userCart):
        bookDetails=getBookById(booksCatalog,bookId)
        totalPrice+=bookDetails['Price'].values[0]

    # sum(float(getBookById(booksCatalog,bookId)['Price'].values[0]) for bookId in userCart)
    
    checkoutDone=chargeCustomer(totalPrice)

    return checkoutDone

def viewCart(booksCatalog,userCart):
    if userCart!=None and userCart:
        msg='''
Books in cart with their prices:
'''
        for index,bookId in enumerate(userCart):
            bookDetails=getBookById(booksCatalog,bookId)
            msg+='"'+str(bookDetails['Title'].values[0])+'"'+" : "+str(bookDetails['Price'].values[0])+"$"+"\n"
    else:
        msg="Your Cart is Empty! U can start Shopping now :-) Enjoy"
 
    printMsg(msg+'''
             
                      ___
                     //
____________________//
\_\_\__\_|_/_/_/_/_/ 
 \_\_\_\_|_/_/_/_/
  \_\_\_\_/_/_/_/
     \_______/ 
      \_|_|_/
       O   O
''')
        

    
     

def menu(booksCatalog):
    userCart=[]
    applicationExitMode=False
    printMsg("Wellcome to Tehilas Book Store!")
    while not applicationExitMode:
        choise=input('''how can I help you today? please type the number of the option that you want.
            1. search for books
            2. view cart
            3. add to cart
            4. checkout
            5. refer a friend to our store with recommendation!
            6. Exit 
            ''')
        
        applicationExitMode=int(choise)==6
        if applicationExitMode==False:
            if int(choise)==1:
                keyword=freindlyInput("What keyword would you like to search for?")
                matching_books=searchBooks(booksCatalog,keyword)
                printMsg(str(matching_books))
            elif int(choise)==2:
                viewCart(booksCatalog,userCart)
            elif int(choise)==3:
                bookId=freindlyInput("What book do you want to add? enter book Id pls")
                userCart=addToCart(booksCatalog,bookId,userCart)
                printMsg("book added to cart!")
            elif int(choise)==4:
                if checkout(booksCatalog,userCart):
                    userCart=None
                    printMsg("Hooray! Transaction Confirmed Enjoy your new books!")
                else:
                    printMsg("Sorry. Customer billing not approved )-: pls try again")
            elif int(choise)==5:
                mail=freindlyInput("enter your friend mail:")
                stars=freindlyInput('''Share with your friend what is the star rating of our store to your opinion?
                                    answer using * char.
                                    e.g.:
                                    *****''')
                if referFriend(mail,stars):
                    printMsg("Hooray! Friend refered and invited to our Store Thank You!")
                else:
                    printMsg("Very Bad. we did not succeeded to invite your friend)-: pls try again later")

main()