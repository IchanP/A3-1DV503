import unittest
from model.MemberHandler import MemberHandler
from model.database import Database
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("db_username")
password = os.getenv("db_password")


class TestMemberValidation(unittest.TestCase):

    def __init__(self, methodName='AddMember'):
        super().__init__(methodName)
        self.member = MemberHandler()
        self.member.firstname = "John"
        self.member.lastname = "Doe"
        self.member.address = "; DROP TABLE members; --"
        self.member.city = "Anytown"
        self.member.zip = "12345"
        self.member.phone = "555-1234"
        self.member.email = "john@example.com"
        self.member.password = "PASSWORD123"
        self.db = Database(username, password)

    def test_add_member_sql(self):
        self.member.add_member(self.db)
        # TODO make a query after