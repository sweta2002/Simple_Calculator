def addition(number_1, number_2):
    add = number_1 + number_2
    print("sum is ",add)

def subtraction(number_1, number_2):
    sub = number_1 - number_2
    print("difference is ",sub)

def multiplication(number_1, number_2):
    mul = number_1 * number_2
    print("product is ",mul)

def division(number_1, number_2):
    div = number_1 // number_2
    print("quotient is ",div)

number_1 = int(input("enter the first number"))
number_2 = int(input("enter the second number"))
print("1 - addition\t 2 - subtraction\t 3 - multiplication\t 4 - division")
a = int(input("enter the option"))
if(a == 1):
    addition(number_1,number_2)
elif(a == 2):
    subtraction(number_1,number_2)
elif(a == 3):
    multiplication(number_1,number_2)
elif(a == 4):
    division(number_1,number_2)
else:
    print("invalid option")

