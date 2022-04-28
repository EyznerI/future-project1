class Customer:
    def __init__(self, n, a,):
        self.name = n
        self.age = a
        self.products = []
    
    def __str__(self):
        return(f"this is instanse of a Class with name {self.name} and age {self.age}")

    def add_product(self, title):
        self.products.append(title)

customers = []
user2 = Customer("Kate", 36)
user1 = Customer("MOnika", 63)
customers.append(user1)
customers.append(user2)

print(customers[0].name)

for c in customers:
    print(c.name, c.age)

 user1 = Customer("Petya", 25)
# user1.add_product("oil")
# user2 = Customer("Kate", 36)
# user2.add_product("sosigise")
# print(user1.products, user1.name)
# print(user2.products, user2.name)