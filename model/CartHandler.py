from model.database import Database
from mysql.connector import IntegrityError

class CartHandler:  
    
    def __init__(self, db: Database):
        self.db = db

    def add_book_to_cart(self, userid, isbn, quantity):
        query = """INSERT INTO cart VALUES(%s, %s, %s);"""
        values = (userid, isbn, quantity)

        return self._try_add_to_cart(query, values)


    def _try_add_to_cart(self, query, value):
        try:
            self.db.execute_with_commit(query, value)
            return True
        except IntegrityError as e:
                print("This book is already in your cart!")
                return False