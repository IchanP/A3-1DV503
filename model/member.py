from view.menu import print_header, print_option, get_choice
from model.membervalidation import MemberValidation
from getpass import getpass
from utils.password_management import hash_password
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
        hashed_password = hash_password(self.password)
        try:
            query = """INSERT INTO members (fname, lname, address, city, zip, phone, email, password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
            tuple = (self.firstname, self.lastname, self.address, self.city, self.zip, self.phone, self.email, hashed_password)
            db.execute_with_commit(query, tuple)
        except Exception as e:
            if e.errno == 1062:
                duplicate = e.msg.split("'")[1]
                print(f"{duplicate} already exists please try again")

    def validate_member_input(self):
        member_validation = MemberValidation(self)


        if member_validation.is_there_errors():
            member_validation.print_errors()
            self.member_registration()
    