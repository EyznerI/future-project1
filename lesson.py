# f = open("text.txt", "w")
# f.write("Hello\n")
# f.write("world")

# f = open("text.txt", "a")
# f.write("name\n")
# f.write("age")

# f.close()
# import random

# def generate_num(count):
#     rnd_id = ""
#     for i in range(count):
#         rnd_id = str(random.randint(0, 9)) + str(rnd_id)
#     return rnd_id

# f = open("text.txt", "w")
# for n in range(10):
#     f.write(f"{generate_num(8)}\n")

# f.close()

# import random
# print(random.randint(0, 9))


# customers = [{"name": "Luke", "age": "43", "products": ["water", "fish"]},
#             {"name": "Mike", "age": "43", "products": ["water", "fish"]},
#             {"name": "Pablo", "age": "43", "products": ["water", "fish"]}]
            
# with open("text.txt", "r+") as f:
#     for customer in customers:
#         f.write(f"{customer}\n")
customers = []

with open ("text.txt", 'r+') as f:
    data = f.readlines()
    for line in data:
        user = line.split(",")
        customer = {}
        customer["name"] = user[0]
        customer["age"] = int(user[1].split("\n")[0])
        customer["products"] = user[2].split(";")
        
        customers.append(customer)
print(customers)