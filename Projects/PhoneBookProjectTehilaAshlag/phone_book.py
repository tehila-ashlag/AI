from contact import Contact
from compareable import Compareable


class PhoneBook(Compareable):
    def __init__(self,owner_name):
        self._contacts=[]
        self.__owner=owner_name

    @property
    def owner_name(self):
        return self.__owner

    @owner_name.setter
    def owner_name(self, value):
        self.__owner = value

    def add_contact(self, contact):
        if isinstance(contact, Contact):
            self._contacts.append(contact)
        else:
            raise TypeError("Contact must be an instance of Contact")
        
    def remove_contact(self, contact):
        if isinstance(contact, Contact):
            self._contacts.remove(contact)
        else:
            raise TypeError("Contact must be an instance of Contact")
    
    def get_contact(self, contact_name):
        for contact in self._contacts:
            if contact.compare_name(contact_name):
                return contact
        return None  
        
    def update_contact(self,new_property_val,property_name,contact_name):
        contact=self.get_contact(contact_name)
        if contact:
            if property_name=="mail":
                contact.mail=new_property_val
            elif property_name=="phone_number":
                contact.phone_number=new_property_val
            elif property_name=="name":
                contact.name=new_property_val
       
        
    def __str__(self):
        msg='''This is '''+self.__owner+'''s Phone Book:
              
              '''
        for contact in self._contacts:
            msg+=contact.__str__()+"\n"
        return msg
    
    def get_total_contact(self):
        return len(self._contacts)
    
    def __add__(self,other):
        if isinstance(other, PhoneBook):
            new_phone_book=PhoneBook()
            new_phone_book._contacts=self._contacts+other._contacts
            return new_phone_book
        else:
            raise TypeError("PhoneBook must be an instance of PhoneBook")
        
    def compare(self, unique_val):
        if isinstance(unique_val, str):
            return self.__owner_name == unique_val
        elif isinstance(unique_val, PhoneBook):
            return self.__owner_name == unique_val.owner_name
        else:
            return False
    

        
    
        

    

