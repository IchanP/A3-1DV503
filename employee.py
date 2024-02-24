from model.database import Database
from view.ui import ui

view = ui()

def list_employee(db:Database, limit, offset):

    query = f""" SELECT fname,lname,ssn from employee LIMIT {limit} OFFSET {offset} ; """
    employees = db.execute_and_fetchall(query)

    print_name_ssn(employees)
    
    options = ["Previous Page", "Next Page", "Back to Employee Menu"]
    view.print_options(options)
    choice = view.get_choice(len(options))

    handle_list_choice(db, limit, offset, choice, options)

def print_name_ssn(employees):
    print("List of employees: ")
    for employee in employees:
        print("-"*20)
        print(f"\t Name: {employee[0]} {employee[1]} \n\t SSN: {employee[2]}")

def handle_list_choice(db:Database, limit, offset, choice, options):
    if choice == 1:
        if offset-limit >= 0:
         list_employee(db, limit, offset-limit)
        else:
            print("No previous page")
            view.print_options(options)
            choice = view.get_choice(len(options))
            handle_list_choice(db, limit, offset, choice, options)
    elif choice == 2:
        list_employee(db, limit, offset+limit)
    elif choice == 3:
        return
    
def add_employee(db:Database):
    fname = input("First name:")
    lname = input("Last name:")
    ssn = input("SSN:")
    address = input("Address:")
    bdate = input("Birthdate:")
    sex = input("Gender:")
    salary = input("Salary:")
    dno = input("Department number:")

    try:
        insert_query = f""" INSERT INTO employee (fname, lname, ssn, bdate, address, sex, salary, dno) VALUES('{fname}', '{lname}', '{ssn}', '{bdate}', '{address}', '{sex}', {salary}, '{dno}'); """
        db.execute_with_commit(insert_query)
        print("Employee added successfully")
    except Exception as e:
        print("ADDING new employee failed")
        print(e)