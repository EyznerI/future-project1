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
def sum_two(a,b):
    return a+b
c = sum_two(5,6)
print(c)


loop = [15,17,19, 41]
def sum_loop(loop):
    summ = 0
    for m in loop:
        summ = summ+m  
    return summ
m = sum_loop(loop)
print(m)    