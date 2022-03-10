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
    else:
        continue 
        