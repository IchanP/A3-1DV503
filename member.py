from menu import print_header, print_option, get_choice
from membervalidation import MemberValidation
from getpass import getpass

class Member:

    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.address = None
        self.city = None
        self.zip = None
        self.phone = None
        self.email = None
        self.password = None
        return


    def member_registration(self):
        print_header("New Member Registration")
        # TODO validation
        self.firstname = input("First Name: ") # varchar(50)
        self.lastname = input("Last Name: ") #varchar(50)
        self.address = input("Street address: ") #varchar(50)
        self.city = input("City: ") #varchar(30)
        self.zip = input("Zip: ") #int unsigned
        self.phone = input("Phone: ") #varchar(15)
        self.email = input("Email: ") #varchar(40)
        self.password = getpass("Password: ") #varchar(200) 
        self.validate_member_input()
        


    def add_member(self, db):
        x = "y"

    def validate_member_input(self):
        member_validation = MemberValidation()
        member_validation.is_name_valid(self.firstname)
        member_validation.is_name_valid(self.lastname)
        member_validation.is_address_valid(self.address)
        member_validation.is_city_valid(self.city)
        member_validation.is_zip_valid(self.zip)
        member_validation.is_phone_valid(self.phone)
        member_validation.is_email_valid(self.email)
        member_validation.is_password_valid(self.password)

        if member_validation.is_there_errors():
            member_validation.print_errors()
            self.member_registration()
    