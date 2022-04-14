import random
def generate_id(count): 
    rnd_id = 0
    for i in range(count):
        rnd_id = str(random.randint(0, 9)) + str(rnd_id)
    return rnd_id
generate_id(10)
# id = str(random.expovariate(8))


costomers = [{"id": "dcf124ed", "name": "Luke", "age": 43, "products": ["water", "fish"]}]
a = input("hello, do you wany buy: ")
while a == "Yes":
    id_costumers = input("hello, please, enter aacount: ")

    if   id_costumers == "Yes":
        b = input("Please eneter your id: ")
        for i in customers:
            if i["id"] == b:
                New_product = input("please, choice product ")
                i[products].append(New_product)
                print(costumers)
    elif id_costumers == "No":
        cust_new = {}
        cust_new["id"] = generate_id(8)
        cust_new["name"] = input("enter name: ")
        cust_new["age"] = input("enter age: ")
        cust_new["product"] = input("choice produc: t").split(", ")
        custumers.append(cust_new)
        print(customers)
    else:
        print( "please, enter only Yes or No")