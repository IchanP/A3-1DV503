from mysql.connector import connect

class Database:

    # establish connection to the db
    # THis __init__ method is called when the class is instantiated
    def __init__(self, username, password) -> None:
        try:
         self.connection = connect(host="localhost", user=username, password=password, database="book_store")
        except Exception as e:
            print(e)
            print("Connection to database failed, check your enviorment variables and try again.")

    #get the cursor
    def get_cursor(self):
        return self.connection.cursor()
    
    def execute_and_fetchone(self, query, tuple = None):
        with self.get_cursor() as cursor:
            cursor.execute(query, tuple)
            return cursor.fetchone()
        

    def execute_and_fetchall(self, query, tuple = None):
        with self.get_cursor() as cursor: # Using with statement to automatically close the cursor
            cursor.execute(query, tuple)
            return cursor.fetchall()
    
    #execute with commit
    def execute_with_commit(self, query, tuple = None):
        with self.get_cursor() as cursor: # Using with statement to automatically close the cursor
            cursor.execute(query, tuple)
            self.connection.commit()
    
    def execute_with_commit_and_get_last_row(self, query, tuple = None):
        with self.get_cursor() as cursor: # Using with statement to automatically close the cursor
            cursor.execute(query, tuple)
            self.connection.commit()
            return cursor._last_insert_id