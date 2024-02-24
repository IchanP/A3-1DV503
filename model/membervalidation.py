import re

class MemberValidation:

    def __init__(self, member):
        self.errorMessages = []
        self.is_name_valid(member.firstname)
        self.is_name_valid(member.lastname)
        self.is_address_valid(member.address)
        self.is_city_valid(member.city)
        self.is_zip_valid(member.zip)
        self.is_phone_valid(member.phone)
        self.is_email_valid(member.email)
        self.is_password_valid(member.password)


    def is_name_valid(self, name):
     #Can't put numbers in your name
      if True != bool(re.match("^[A-Za-z ]{1,50}$", name)):
            self.errorMessages.append("Your  name is not valid, it must be between 1 and 50 characters and contain only letters and spaces.")      

    def is_address_valid(self, address):
        #Can't put special symbols in your address requires at least one letter
        if True != bool(re.match("^(?=.*[A-Za-z])[A-Za-z0-9 .,]{1,50}$", address)):
            self.errorMessages.append("Your address is not valid, it must be between 1 and 50 characters and contain only letters, numbers, spaces, periods, and commas.")
    
    def is_city_valid(self, city):
        #Can't put numbers or special symbols in city 
        if True != bool(re.match("^[A-Za-z ]{1,30}$", city)):
            self.errorMessages.append("Your city is not valid, it must be between 1 and 30 characters and contain only letters and spaces.")
    
    def is_zip_valid(self, zip):
        if True != bool(re.match("^\d{5,10}$", zip) and int(zip) > 0):
            self.errorMessages.append("Your zip is not valid, it must be a positive number and contain only numbers.")
    
    def is_phone_valid(self, phone):
        #Phone number maximum of 15 characters, allows for +, -, (, ), and numbers but not letters
        if True != bool(re.match("^[0-9+()\- ]{1,15}$", phone)):
            self.errorMessages.append("Your phone number is not valid, it must be between 1 and 15 characters and contain only numbers, +, -, (, and ).")

    def is_email_valid(self, email):
        # Must contain @ and . and be between 3 and 40 characters
        if True != bool(re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,40}$", email)):
            self.errorMessages.append("Your email is not valid, it must be between 3 and 40 characters and contain only letters, numbers, periods, and @ symbols.")

    
    def is_password_valid(self, password):
        #Password must be between 8 and 200 characters no special symbols REQUIRED
        if True != bool(re.match("^[A-Za-z0-9!@#$%^&*()_+]{8,200}$", password)):
            self.errorMessages.append("Your password is not valid, it must be between 8 and 200 characters")

    def is_there_errors(self):
        if len(self.errorMessages) > 0:
            return True
        return False

    def print_errors(self):
        print("\nError: ")
        for message in self.errorMessages:
            print(message)
        return