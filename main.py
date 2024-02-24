from model.database import Database
from getpass import getpass
from mysql.connector import connect
from view.ui import ui
from employee import list_employee, add_employee
from dotenv import load_dotenv
from model.member import Member
from model.membervalidation import MemberValidation
from model.Exception.nomember import NoMember
from controller.accountcontroller import AccountController
import os

load_dotenv()
username = os.getenv("db_username")
password = os.getenv("db_password")

db = Database(username, password)
view = ui()
acc_controller = AccountController(db, view)

#Main menu
def main_menu(options):
    while(True):
        
        #print header
        view.print_header("Welcome to the Online Book Store") 
        #print options
        view.print_options(options) 
        # get the users selection
        choice = view.get_choice(len(options))

        if choice == 1:
           if acc_controller.member_login():
                member_menu()
        elif choice == 2:
            acc_controller.member_registration()
        else:
            quit()

def member_menu():
    view.print_header("Member Menu")
    view.print_options(["Browse by Subject", "Search by Author/Title", "Check out", "Logout"])

main_menu(["Member Login", "New Member Registration", "Quit"])
