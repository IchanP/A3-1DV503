from model.database import Database
from view.ui import ui
from dotenv import load_dotenv
from controller.accountcontroller import AccountController
from controller.subjectcontroller import SubjectController
import os

load_dotenv()
username = os.getenv("db_username")
password = os.getenv("db_password")

db = Database(username, password)
view = ui()
acc_controller = AccountController(db, view)
subj_controller = SubjectController(db, view)

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
      #     if acc_controller.member_login():
                member_menu()
        elif choice == 2:
            acc_controller.member_registration()
        else:
            quit()

def member_menu():
    while(True):
        view.print_header("Member Menu")
        options = ["Browse by Subject", "Search by Author/Title", "Check out", "Logout"]
        view.print_options(options)
        choice = view.get_choice(len(options))

        if choice == 1:
            subj_controller.subject_menu()
        elif choice == 2:
            print()
        elif choice == 3:
            print()
        elif choice == 4:
            break

main_menu(["Member Login", "New Member Registration", "Quit"])
