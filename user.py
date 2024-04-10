#User module for Question 1
import random
class User:
    def __init__ (self, login):
        self.__user_registration= random.randint(1000, 9999) #Four digit random number as their new user registration.
        self._login_=login
        
    def get_user_registration(self):
        return self.__user_registration    
    
    def get_login(self):
        print(self._login_)
    
    def set_login(self, new_login):
        self._login_ = new_login

    def display_account_information(self):
        print(f"Your user registration is {self.__user_registration} and your login is {self._login_}.")
    
    