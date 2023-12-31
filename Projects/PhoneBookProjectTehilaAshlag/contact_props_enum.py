from enum import Enum

class ContactProperties(Enum):
    NAME = 1
    PHONE = 2
    EMAIL = 3

class BusinessContactProperties(ContactProperties):
    BUSINESS = 4