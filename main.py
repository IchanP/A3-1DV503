from database import Database
from getpass import getpass
from mysql.connector import connect
from menu import print_header, print_option, get_choice

#Main menu
def main_menu(db:Database,options):
    #print header
    print_header("Welcome to the company database") # TODO Change to db.name ?
    #print options
    print_option(options) 
    # get the users selection
    choice = get_choice(len(options))

    if choice == 1:
        #show employee menu
        employees_menu(db, ["List all employees", "Add new employee", "Delete employee", "Update employee", "Back to main menu"])
    else:
        quit()


def employee_menu(db:Database, options):
    #print header
    print_header("WELCOME TO EMPLOYEE MENU") # TODO  fix
    print_option(options)
    # get the users selection
    choice = get_choice(len(options))
    if choice == 1:
        #view employees
        view_employees(db)
    if choice == 2:
        #add employee
        add_employee(db)
    elif choice == 3:
        #edit employee
        delete_employee(db)
    elif choice == 4:
        #delete employee
        update_employee(db)
    elif choice == 5:
        #view employees
        main_menu(db)



# check DB credentials
def check_db_credentials(username, password):
    try:
        connect(host="localhost", user=username, password=password, database="company") # TODO fix the database name
        return True
    except Exception as e:
        print(e)
        return False

valid_connection = False
username, password = (None, None)

while(not valid_connection):
    username = input("Enter your SQL username:")
    password = getpass("Enter your SQL Password:")
    if(check_db_credentials(username, password)):
        valid_connection = True
    else:
        print("Invalid credentials. Please try again") # TODO change this to a nicer message

db = Database(username, password) 
main_menu(db, ["Employees", "Exit"]) # TODO change this to a nicer message
