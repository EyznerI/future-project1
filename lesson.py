import random
def generate_id(count): 
    rnd_id = 0
    for i in range(count):
        rnd_id = str(random.randint(0, 9)) + str(rnd_id)
    return rnd_id

# id = str(random.expovariate(8))


costomers = [{"id": "dcf124ed", "name": "Luke", "age": 43, "products": ["water", "fish"]}]
a = input("hello, do you wany buy: ")
while a == "Yes":
    id_costumers = input("do you have account?: ")

    if   id_costumers == "Yes":
        b = input("hello, please, enter id: ")
        for i in costomers:
            if i["id"] == b:
                New_product = input("please, choice product ")
                i["products"].append(New_product)
                print(costomers)
    elif id_costumers == "No":
        cust_new = {}
        cust_new["id"] = generate_id(8)
        cust_new["name"] = input("enter name: ")
        cust_new["age"] = input("enter age: ")
        cust_new["products"] = input("choice produc: t").split(", ")
        costomers.append(cust_new)
        print(costomers)
    else:
        print( "please, enter only Yes or No")
