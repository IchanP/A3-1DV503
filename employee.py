from database import Database

def list_employee(db:Database, limit, offset):
    query = f""" SELECT fname,lname,ssn from employee LIMIT {limit} OFFSET {offset} ; """
    employees = db.execute_and_fetchall(query)
    print("List of employees: ")

    for employee in employees:
        print("-"*20)
        print(f"\t Name: {employee[0]} {employee[1]} \n\t SSN: {employee[2]}")