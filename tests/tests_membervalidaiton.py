import unittest
from model.membervalidation import MemberValidation

# Mocking a simple member object since MemberValidation expects one
class MockMember:
    def __init__(self, firstname, lastname, address, city, zip, phone, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.city = city
        self.zip = zip
        self.phone = phone
        self.email = email
        self.password = password

class TestMemberValidation(unittest.TestCase):

    def __init__(self, methodName='MemberValidation'):
        super().__init__(methodName)

    def test_does_validation_work(self):
        member = MockMember("Pontus", "Grandin", "123 Main St.", "Anywhere Anytime", "1234567", "+123-456-7890", "pontus.grandin@gmail.com", "password")
        member_validation = MemberValidation(member)
        self.assertEqual(member_validation.is_there_errors(), False)

    def test_invalid_name(self):
        member = MockMember("John123", "Doe", "123 Main St.", "Anytown", "12345", "555-1234", "john@example.com", "Password123!")
        validator = MemberValidation(member)
        self.assertEqual(validator.is_there_errors(), True)

    def test_invalid_address(self):
        member = MockMember("John", "Doe", "123 Main St.!", "Anytown", "12345", "555-1234", "john@example.com", "Password123!")
        validator = MemberValidation(member)
        self.assertEqual(validator.is_there_errors(), True)

    def test_invalid_city(self):
        member = MockMember("John", "Doe", "123 Main St.", "Anytown123", "12345", "555-1234", "john@example.com", "Password123!")
        validator = MemberValidation(member)
        self.assertEqual(validator.is_there_errors(), True)

    def test_invalid_zip(self):
        member = MockMember("John", "Doe", "123 Main St.", "Anytown", "ABCDE", "555-1234", "john@example.com", "Password123!")
        validator = MemberValidation(member)
        self.assertEqual(validator.is_there_errors(), True)

    def test_invalid_phone(self):
        member = MockMember("John", "Doe", "123 Main St.", "Anytown", "12345", "ABC-555-1234", "john@example.com", "Password123!")
        validator = MemberValidation(member)
        self.assertEqual(validator.is_there_errors(), True)

    def test_invalid_email(self):
        member = MockMember("John", "Doe", "123 Main St.", "Anytown", "12345", "555-1234", "johnexample.com", "Password123!")
        validator = MemberValidation(member)
        self.assertEqual(validator.is_there_errors(), True)

    def test_invalid_password(self):
        member = MockMember("John", "Doe", "123 Main St.", "Anytown", "12345", "555-1234", "john@example.com", "short")
        validator = MemberValidation(member)
        self.assertEqual(validator.is_there_errors(), True)
    
    def test_safe_from_injections(self):
        member = MockMember("John", "Doe", "; DROP TABLE members; --", "Anytown", "12345", "555-1234", "john@example.com", "PASSWORD123!")
        

if __name__ == '__main__':
    unittest.main()
