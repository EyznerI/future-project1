import random
# points = []
# lines = ["Petya", 12, 43, 0]
# print(len(lines))
# lines.append("Kolya")

# print(lines[0])

# dict = {"name": "Anna",  "age": 32, "wifes": ["katya", "natasha"]}
# print(dict["wifes"])
# dict["status"] = "single"
# dict['name'] = 'yura'
# print(dict)

# for k, v in dict.items():
#     print(k, v)

def generate_id(count):
    rnd_id = ""
    for i in range(count):
        rnd_id = str(random.randint(0, 9)) + str(rnd_id)
    return rnd_id
generate_id(10)

# id = str(random.expovariate(8))


costomers = [{"id": "dcf124ed", "name": "Luke", "age": 43, "products": ["water", "fish"]}]
a = input("hello,  do you want buy smth.?: ")
while a == "yes":
    # id_costumers = input(" please, enter your account: ")
    id_costumers = input("Do you have account?: ")

    if   id_costumers == "yes":
        b = input("Please eneter your id: ")
        # for i in customers:
        #     b = input("hello, please, enter id: ")
        for i in costomers:
            if i["id"] == b:
                new_product = input("please, choice product: ")
                # i["products"].append(New_product)
                # print(costomers)
                i["products"].append(new_product)
                print(costomers)
                break
    elif id_costumers == "no":
        cust_new = {}
        cust_new["id"] = generate_id(8)
        cust_new["name"] = input("enter name: ")
        cust_new["age"] = input("enter age: ")
        # cust_new["product"] = input("choice produc: ").split(", ")
        costomers.append(cust_new)
        print(costomers)
        cust_new["products"] = input("choice product: ").split(", ")
        costomers.append(cust_new)
        print(costomers)
    else:
        print( "please, enter only yes or no")
    ex = input(" if you want finish programm, enter <exit> ")
    if ex == "exit":
        break
