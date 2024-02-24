from model.database import Database
from getpass import getpass
from mysql.connector import connect
from view.ui import ui
from employee import list_employee, add_employee
from dotenv import load_dotenv
from model.member import Member
from model.membervalidation import MemberValidation
from model.Exception.nomember import NoMember
import os

load_dotenv()
username = os.getenv("db_username")
password = os.getenv("db_password")

view = ui()

#Main menu
def main_menu(db:Database,options):
    while(True):
        
        #print header
        view.print_header("Welcome to the Online Book Store") 
        #print options
        view.print_options(options) 
        # get the users selection
        choice = view.get_choice(len(options))

        if choice == 1:
            #show employee menu
            member_login()
        elif choice == 2:
            member_registration()
        else:
            quit()

def member_menu():
    view.print_header("Member Menu")
    view.print_options(["Browse by Subject", "Search by Author/Title", "Check out", "Logout"])

def member_registration():
    view.print_header("New Member Registration")

    while True:
        [firstname, lastname, address, city, zip, phone, email] = view.get_inputs(["First Name: ", "Last Name: ", "Street address: ", "City: ", "Zip: ", "Phone: ", "Email: "])
        password = view.get_password()
        newMember = Member(firstname, lastname, address, city, zip, phone, email, password)
        member_validator = MemberValidation(newMember)
        if member_validator.is_there_errors() == False:
            break
        member_validator.print_errors()
        view.print_options(["Register Again", "Back to Main Menu"])
        choice = view.get_choice(2)
        if choice == 2:
            break
    try_add_member(newMember)

 


def member_login():
    [email] = view.get_inputs(["Enter your email: "])
    password = view.get_password()
    member = Member()
    try:
        if member.member_login(db, email, password):
            member_menu()
        else:
            print("\nInvalid password")
            input("Press any key to continue")
    except Exception as e:
            if isinstance(e, NoMember):
                print(e)
            else: 
                print("An error occurred")
            input("Press any key to continue")

def try_add_member(newMember: Member):
    try: 
        newMember.add_member(db)
        print("Member added successfully")
        input("Press any key to continue")
    except Exception as e:
     if e.errno == 1062:
        duplicate = e.msg.split("'")[1]
        print(f"{duplicate} already exists please try again")
        view.print_options(["Register Again", "Back to Main Menu"])
        choice = view.get_choice(2)
        if choice == 1:
            member_registration()


db = Database(username, password)

main_menu(db, ["Member Login", "New Member Registration", "Quit"])
