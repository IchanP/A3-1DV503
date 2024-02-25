from view.ui import ui
from model.MemberHandler import MemberHandler
from model.membervalidation import MemberValidation
from model.Exception.nomember import NoMember
from model.database import Database
from mysql.connector import IntegrityError

class AccountController:

    def __init__(self, db: Database, view: ui):
        self.db = db
        self.view = view

    def member_registration(self):
        self.view.print_header("New Member Registration")

        while True:
            [firstname, lastname, address, city, zip, phone, email] = self.view.get_inputs(["First Name: ", "Last Name: ", "Street address: ", "City: ", "Zip: ", "Phone: ", "Email: "])
            password = self.view.get_password()
            
            newMember = MemberHandler(self.db, firstname, lastname, address, city, zip, phone, email, password)
            
            member_validator = MemberValidation(newMember)
            if member_validator.is_there_errors() == False:
                break
            
            else:
                member_validator.print_errors()
                OPTION_RETURN = 2
                self.view.print_options(["Register Again", "Back to Main Menu"])
                choice = self.view.get_choice(2)
                if choice == OPTION_RETURN:
                    break

        self._try_add_member(newMember)


    def member_login(self):
        email = self.view.get_input("Enter your email: ")
        password = self.view.get_password()
        member = MemberHandler(self.db)
        try:
            if member.member_login("yennykinns@gmail.com", "yennykinns"):
                return email
            else:
                print("\nInvalid password")
                input("Press any key to continue")
        except Exception as e:
                if isinstance(e, NoMember):
                    print(e)
                else: 
                    print("An error occurred")
                    print(e)
                input("Press any key to continue")
                return None

    def _try_add_member(self, newMember: MemberHandler):
        try: 
            newMember.add_member()
            print("Member added successfully")
        except IntegrityError as e:
            if e.errno == 1062:
                duplicate = e.msg.split("'")[1]
                print(f"{duplicate} already exists please try again")
                self._handleIntegrityError()
    
    def _handleIntegrityError(self):
        self.view.print_options(["Register Again", "Back to Main Menu"])
        choice = self.view.get_choice(2)
        if choice == 1:
            self.member_registration()
