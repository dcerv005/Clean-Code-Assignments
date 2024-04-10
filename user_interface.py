class UserInterface:
    def get_detail(self):
        return input("Do you want a detailed forecast? (yes/no): ").lower()
    
    def get_city(self):
        return input("Enter the city to get the weather forecast or enter exit to end session. ").title()