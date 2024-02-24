from view.ui import ui
from model.member import Member
from model.membervalidation import MemberValidation
from model.Exception.nomember import NoMember
from model.database import Database

class AccountController:

    def __init__(self, db: Database, view: ui):
        self.db = db
        self.view = view

    def member_registration(self):
        self.view.print_header("New Member Registration")

        while True:
            [firstname, lastname, address, city, zip, phone, email] = self.view.get_inputs(["First Name: ", "Last Name: ", "Street address: ", "City: ", "Zip: ", "Phone: ", "Email: "])
            password = self.view.get_password()
            newMember = Member(firstname, lastname, address, city, zip, phone, email, password)
            member_validator = MemberValidation(newMember)
            if member_validator.is_there_errors() == False:
                break
            member_validator.print_errors()
            self.view.print_options(["Register Again", "Back to Main Menu"])
            choice = self.view.get_choice(2)
            if choice == 2:
                break
        self.try_add_member(newMember)


    def member_login(self):
        [email] = self.view.get_inputs(["Enter your email: "])
        password = self.view.get_password()
        member = Member()
        try:
            if member.member_login(self.db, email, password):
                return True
            else:
                print("\nInvalid password")
                input("Press any key to continue")
                return False
        except Exception as e:
                if isinstance(e, NoMember):
                    print(e)
                else: 
                    print("An error occurred")
                input("Press any key to continue")
                return False

    def try_add_member(self, newMember: Member):
        try: 
            newMember.add_member(self.db)
            print("Member added successfully")
            input("Press any key to continue")
        except Exception as e:
            if e.errno == 1062:
                duplicate = e.msg.split("'")[1]
                print(f"{duplicate} already exists please try again")
                self.view.print_options(["Register Again", "Back to Main Menu"])
                choice = self.view.get_choice(2)
                if choice == 1:
                    self.member_registration()