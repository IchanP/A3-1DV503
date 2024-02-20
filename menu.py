from database import Database

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

def employees_menu(db:Database, options):
    #print header
    print_header("WELCOME TO EMPLOYEE MENU")
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


def print_header(title):
    print("************************************************")
    print("***                                          ***")
    print("***          " + title + "        ***")
    print("***                                          ***")
    print("************************************************")

def print_option(options):
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")

def get_choice(maxOptions):
    selectedOption = None
    while (selectedOption is None):
        choice = input("Enter Choice:")
        try:
            if int(choice) in [x for x in range(1,maxOptions+1)]:
                selectedOption = int(choice)
            else:
                print("Invalid choice. Please selected from the available options.")
                selectedOption = None
        except Exception as e:
            print("Invalid choice. Please try again")
            selectedOption = None

    return selectedOption