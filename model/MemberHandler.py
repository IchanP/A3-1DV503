from model.membervalidation import MemberValidation
from view.ui import ui
from getpass import getpass
from utils.password_management import hash_password, match_passwords
from model.database import Database
from model.Exception.nomember import NoMember
class MemberHandler:

    def __init__(self, firstname=None, lastname=None, address=None, city=None, 
                 zip=None, phone=None, email=None, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.city = city
        self.zip = zip
        self.phone = phone
        self.email = email
        self.password = password

    
    def member_login(self, db, email, password):
        foundMember = self._get_one_by_email(db, email)

        if foundMember == None:
            raise NoMember("No member found with that email")

        return match_passwords(password, foundMember[8])       
        

    def add_member(self, db: Database):
        hashed_password = hash_password(self.password)

        addMemberQuery = """INSERT INTO members (fname, lname, address, city, zip, phone, email, password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
        addMemberValues = (self.firstname, self.lastname, self.address, self.city, self.zip, self.phone, self.email, hashed_password)
        db.execute_with_commit(addMemberQuery, addMemberValues)



    def _get_one_by_email(self, db: Database, email):
        query = """SELECT * FROM members WHERE email = %s""" 
        getByEmailValue = (email,)
        member = db.execute_and_fetchone(query, getByEmailValue)
        return member
    
