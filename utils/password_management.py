import bcrypt

def hash_password(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)
        

def match_passwords(plain, hashed):
        return bcrypt.checkpw(plain.encode('utf-8'), hashed.encode('utf-8'))