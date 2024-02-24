from model.membervalidation import MemberValidation
from view.ui import ui
from getpass import getpass
from utils.password_management import hash_password, match_passwords
from model.database import Database
from model.Exception.nomember import NoMember
class MemberHandler:

    def __init__(self, db: Database, firstname=None, lastname=None, address=None, city=None, 
                 zip=None, phone=None, email=None, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.city = city
        self.zip = zip
        self.phone = phone
        self.email = email
        self.password = password
        self.db = db

    
    def member_login(self, email, password):
        foundMember = self._get_full_member_by_email(email)
        if foundMember == None:
            raise NoMember("No member found with that email")

        return match_passwords(password, foundMember[8])       
        

    def add_member(self, ):
        hashed_password = hash_password(self.password)

        addMemberQuery = """INSERT INTO members (fname, lname, address, city, zip, phone, email, password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
        addMemberValues = (self.firstname, self.lastname, self.address, self.city, self.zip, self.phone, self.email, hashed_password)
        self.db.execute_with_commit(addMemberQuery, addMemberValues)

    def get_id_by_email(self, email):
       query =  """SELECT userid FROM members WHERE email = %s"""
       value = (email,)
       fullTuple = self._try_exec_and_fetchone(query, value)
       return fullTuple[0]

    def _get_full_member_by_email(self, email):
        query = """SELECT * FROM members WHERE email = %s""" 
        getByEmailValue = (email,)
        return self._try_exec_and_fetchone(query, getByEmailValue)
    
    def _try_exec_and_fetchone(self, query, value):
        try:
          fetchedTuple = self.db.execute_and_fetchone(query, value)

          if fetchedTuple == None:
            raise NoMember("No member found with that email")
          return fetchedTuple
        except Exception as e: 
            if isinstance(e, NoMember):
                print(e)
            else:
                print("An error occurred")
                print(e)
            