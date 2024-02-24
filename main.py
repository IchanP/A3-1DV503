from database import Database
from getpass import getpass
from mysql.connector import connect
from menu import print_header, print_option, get_choice
from employee import list_employee, add_employee
from dotenv import load_dotenv
from member import Member
import os
load_dotenv()
username = os.getenv("db_username")
password = os.getenv("db_password")

#Main menu
def main_menu(db:Database,options):
    while(True):
        #print header
        print_header("Welcome to the Online Book Store") 
        #print options
        print_option(options) 
        # get the users selection
        choice = get_choice(len(options))

        if choice == 1:
            #show employee menu
            print()
          #  employee_menu(db, ["List all employees", "Add new employee", "Delete employee", "Update employee", "Back to main menu"])
        elif choice == 2:
            member = Member()
            member.member_registration()
        else:
            quit()


def employee_menu(db:Database, options):
    while(True):
        #print header
        print_header("WELCOME TO EMPLOYEE MENU") # TODO  fix
        print_option(options)
        # get the users selection
        try:
            choice = get_choice(len(options))

            if choice == 1:
                #view employees
                list_employee(db, 5, 0)
            if choice == 2:
                #add employee
                add_employee(db)
            elif choice == 3:
                #edit employee
                print()
            elif choice == 4:
                #delete employee
                print()
            elif choice == 5:
                break
            employee_menu(db, options)
        except Exception as e:
            print("Invalid choice. Please try again")
            employee_menu(db, options)


db = Database(username, password)

main_menu(db, ["Member Login", "New Member Registration", "Quit"])
