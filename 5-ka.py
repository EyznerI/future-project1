choice = input("Do you wanna choose coffe or cigarets? please enter: if coffe = 1, if  cigarets = 0 ")
if choice == "0":
    age = input("enter your age:")
    if age > "18":
        print("ok, take your cigarets")
    else:
     print("please, get out of here and come back, when your age will be more 18") 
else:
    print("please, take your coffe")