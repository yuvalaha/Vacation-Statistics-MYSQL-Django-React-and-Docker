from hashlib import sha512 # SHA - Secure Hashing Algorithm - sha512 is a powerful hashing algorithm
from utils.app_config import AppConfig
class Cyber:
    
    # The function receive plain password and return hashed password with salting
    @staticmethod
    def hash_func(plain_text):
        encoded_text = plain_text.encode("UTF-8") + AppConfig.passwords_salt.encode("UTF-8")
        hashed_text = sha512(encoded_text).hexdigest()
        return hashed_text
        
        
        