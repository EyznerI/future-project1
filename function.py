# def shop(c,age):
#     print(f"hello, {c}, {age}")
# shop("Anna",33)

# def age():
#     age = input("enter your age: ")
#     if age>= "18":
#         print("you are adult")
#     else:
#         print("you are not adult")
# age()
# def sum_two(a,b):
#     return a+b
# c = sum_two(5,6)
# print(c)


# loop = [15,17,19, 41]
# def sum_loop(loop):
#     summ = 0
#     for m in loop:
#         summ = summ+m  
#     return summ
# m = sum_loop(loop)
# print(m)    
def age():
    b = input("enter your age: ")
    if int(b) >= 18:
        print("ok, please take your cigarets")
    else:
        print("please, get out of here")


while True:
    choice = input("Do you wanna choose coffe or cigarets? please enter: if coffe = 1, if  cigarets = 0 ")
    if choice == "0":
        age()
    elif choice == "1":
        print("please, take your coffe")
    else:
        continue
    term = input("terminate (t) or continue(c)? ")
    if term == "t":
        break
    elif term == "c":
        print("terminate (t) or continue(c)? ")
    else:
        continue 
        