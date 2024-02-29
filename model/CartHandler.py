from model.database import Database
from mysql.connector import IntegrityError

class CartHandler:  
    
    def __init__(self, db: Database):
        self.db = db

    def add_book_to_cart(self, userid, isbn, quantity):
        query = """INSERT INTO cart VALUES(%s, %s, %s);"""
        values = (userid, isbn, quantity)

        return self._try_add_to_cart(query, values)

    def fetch_cart(self, email):
        query = """SELECT cart.isbn, title, price, qty, (books.price * cart.qty) AS total
                FROM cart
                JOIN books ON cart.isbn = books.isbn
                JOIN members ON cart.userid = members.userid
                WHERE members.email = %s;"""
        value = (email,)
        cart_tuple = self.db.execute_and_fetchall(query, value)

        return self._tuple_to_list(cart_tuple)

    def _tuple_to_list(self, tuple):
        list_of_cart_info = []
        for book in tuple:
            list_of_cart_info.append(self._cart_details_to_dictionary(book))
        return list_of_cart_info

    def _cart_details_to_dictionary(self, cart_info):
        keys = ['ISBN', 'Title','Price','Quantity', 'Total']
        return dict(zip(keys, cart_info))
    
    def _try_add_to_cart(self, query, value):
        try:
            self.db.execute_with_commit(query, value)
            return True
        except IntegrityError as e:
                print("This book is already in your cart!")
                return False