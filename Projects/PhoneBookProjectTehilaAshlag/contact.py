from searchable import Compareable
from util import is_valid_email

class Contact(Compareable):
  def __init__(self,name, phone_number,mail) :
    self.__name = name
    self.__phone_number = phone_number
    self.__mail = mail

  @property
  def name(self):
      return self.__name

  @property
  def phone_number(self):
      return self.__phone_number

  @property
  def mail(self):
      return self.__mail  
  
  @name.setter
  def name(self, value):
      if not isinstance(value, str):
          raise ValueError("Name must be a string")
      self.__name = value

  @phone_number.setter
  def phone_number(self, value):
      if not isinstance(value, str):
          raise ValueError("Phone number must be a string")
      self.__phone_number = value

  @mail.setter
  def mail(self, value):
      if not isinstance(value, str):
          raise ValueError("Mail must be a string")
      elif not is_valid_email(value):
          raise ValueError("Provided mail is not a valid")
      self.__mail = value

  def __str__(self):
      return f"Name: {self.__name}\n Email: {self.__mail}\n Phone Number: {self.__phone_number}\n"

  def compare_name(self, queriedName):
      return self.__name.lower() == queriedName.lower()