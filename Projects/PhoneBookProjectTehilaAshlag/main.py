from contact import Contact
from business_contact import BusinessContact
from phone_book import PhoneBook

phone_books=[]

def display_menu():
    print('''1. create new Phone Book
             2. Add Contact
             3. Add Business Contact
             4. Remove Contact
             5. Update Contact
             6. View Phone Book
             7. Display Contact
             8. Total Contact         
             9. Exist''')
    return input("Enter your choice: ")

def get_phone_book(phone_book_owner_name):
    for phone_book in phone_books:
        if phone_book.owner_name==phone_book_owner_name:
            return phone_book
    return None

def main():
    global phone_books
    while True:
        choise=display_menu()
        if choise=="1":
            owner_name=input("Enter your name: ")
            phone_book=PhoneBook(owner_name)
            phone_books.append(phone_book)
            print("Your Phone Book Created")
            continue
        elif choise=="2":
            owner_name=input("Enter your name:")
            phone_book=get_phone_book(owner_name)
            input_name=input("Enter the new contact name: ")
            input_phone_number=input("Enter the new contact phone number: ")
            input_mail=input("Enter the new contact mail: ")
            contact=Contact(input_name,input_phone_number,input_mail)
            phone_book.add_contact(contact)
            print("Contact Added")
            continue
        elif choise=="3":
            owner_name=input("Enter your name:")
            phone_book=get_phone_book(owner_name)
            input_name=input("Enter the new contact name: ")
            input_phone_number=input("Enter the new contact phone number: ")
            input_mail=input("Enter the new contact mail: ")
            input_business_name=input("Enter the new contact business name: ")
            contact=BusinessContact(input_name,input_phone_number,input_mail,input_business_name)
            phone_book.add_contact(contact)
            print("Business Contact Added")
            continue
        elif choise=="4":
            owner_name=input("Enter your name:")
            phone_book=get_phone_book(owner_name)
            contact_name_to_remove=input("Enter the name of the contact you want to remove: ")
            contact=phone_book.get_contact(contact_name_to_remove)
            if contact:
                phone_book.remove_contact(contact)
                print("Contact Removed")
                continue            
        elif choise=="5":
             owner_name=input("Enter your name:")
             phone_book=get_phone_book(owner_name)
             contact_name_to_update=input("Enter the name of the contact you want to update: ")
             prop_to_update=input("what do u want to change? type one of these choises mail/phone_number/name: ")
             new_value=input("what do u want to change it to? ")
             phone_book.update_contact(new_value,prop_to_update,contact_name_to_update)
             print("Contact Updated")      
            
        elif choise=="6":
            owner_name=input("Enter your name:")
            phone_book=get_phone_book(owner_name)
            print(phone_book)
            continue
        elif choise=="7":
            owner_name=input("Enter your name:")
            phone_book=get_phone_book(owner_name)
            contact_name=input("Enter the name of the contact you want to view: ")
            contact=phone_book.get_contact(contact_name)
            if contact:
                print(contact)
            else:
                print("Contact does not exist")
            continue
        elif choise=="8":
            owner_name=input("Enter your name:")
            phone_book=get_phone_book(owner_name)
            print(phone_book.get_total_contact())
            continue


if __name__ == '__main__':
    main()
    
