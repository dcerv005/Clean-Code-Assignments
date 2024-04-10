#Cart module for Question 1
class ShoppingCart:
    def __init__(self):
        self.cart={}

    def view_cart(self):
        print(self.cart)

    def add_to_cart(self, item):
        if item.stock_status == 'Available':
            self.cart[item.title]= {}
            self.cart[item.title]= {'Author': item.author, 'Price': item.price}
            item.stock_status = 'Unavailable'
        else:
            print(f"Item '{item.title}' is not available.")
    def remove_item(self, item):
        del self.cart[item.title]
        item.stock_status = 'Available'
        print(f"{item.title} was deleted from the cart.")
    
    def check_out(self,user):
        total=0
        total = sum(item['Price'] for item in self.cart.values())
        print(f"{user._login_}: Your total was ${total}.")
        self.cart={}

