# print("Hello world")
# print((2 + 3 )* 24 - 17 ** 2 / 14 //15 + 17  - 9)

# x = 10 
# y = 5
# my_full_name = "Michel"
# print (x*my_full_name)
# user_name = input("please enter your name:")
# print("Hello," + user_name)
# user_birth = input("please enter your birh year: ")
# user_age = 2022 - int(user_birth)
# print (user_age)
# print(user_name + "," + " your age is " + str(user_age))
# print(f"{user_name}, your age is {user_age}")
numbers = input("enter nums using comma:").split(",")
summ = 0
for z in numbers:
    summ = summ+ int(z)**3
print(summ)