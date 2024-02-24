from model.database import Database

class CartHandler:  
    

    def add_book_to_cart(self, db: Database, userid, isbn, quantity):
        query = """INSERT INTO cart VALUES(%s, %s, %s);"""
        values = (userid, isbn, quantity)
        db.execute_with_commit(query, values)
        