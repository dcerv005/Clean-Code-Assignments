#Question 1
from book import Book
from user import User
from cart import ShoppingCart

cart = ShoppingCart()
#The only two books in the book store lol.
item1 = Book("The Alchemist", "Paulo Coelho", 29.99, "Available")
item2 = Book("The Hobbit", "JRRT", 39.99, "Available")

user_login = input("Welcome to the Book Store! Please enter your new login to register: ")
user1= User(user_login)
#print(user1.get_user_registration())

while True:

    try:
        
        
        
               
        user_choice = int(input("Please choose an option:\n0. Add item 1 to cart\n1. Add item 2 to cart\n2. Remove from cart\n3. View Cart\n4. Check Out\n5. Login Change\n6. Exit\n"))
        if user_choice not in [0, 1, 2, 3, 4, 5, 6]:
            raise ValueError("Please choose a valid input.")
        if user_choice == 0:
            cart.add_to_cart(item1)
        elif user_choice == 1:
            cart.add_to_cart(item2)
        elif user_choice == 2:
            if cart.cart:
                item = int(input("Please identify which item to remove:(1 or 2) "))
                if item == 1:
                    cart.remove_item(item1)
                elif item == 2:
                    cart.remove_item(item2)
                else:
                    raise ValueError("Item not found.")
            else:                
                print("Cart is empty")
        elif user_choice == 3:
            cart.view_cart()
        elif user_choice == 4:
            cart.check_out(user1)
        elif user_choice == 5:
            change_login = input("Please select a new login that is different from the previous login. ")
            if user_login.lower() == change_login.lower():
                raise ValueError("Please pick a new login")
            else:
                user1.set_login(change_login)
                user1.display_account_information()
        elif user_choice == 6:
            print ("\n\tThank you for coming to the BookStore!")
            break
    except Exception as e:
        print(e)








