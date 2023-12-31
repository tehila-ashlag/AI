from contact import Contact

class BusinessContact (Contact):
    def __init__ (self,name, phone_number, mail,business_name):
        super().__init__(name, phone_number,mail)
        self.business_name = business_name

    @property
    def business_name(self):
        return self._business_name

    @business_name.setter
    def business_name(self, value):
        self._business_name = value

    def __str__(self):
        return f"{super().__str__()}\n Business: {self.business_name}\n"
    
    def compare_name(self, queriedName):
        return super().compare_name(queriedName)