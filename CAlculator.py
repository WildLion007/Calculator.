def addition() :
    num1 = input("Enter a number")
    num2 = input ("Enter a number to add")
    ans_add = float(num1) + float(num2)
    print(ans_add)
def subtraction() :
    num3 = input("Enter a number")
    num4 = input ( "Enter another numbe to subtract")
    ans_subtract = float(num3) - float(num4)
    print(ans_subtract)
def multiplication ():
    num5 = input("Enter a number")
    num6 = input("Enter another number to multiply")
    ans_multiply = float(num5) *float(num6)
    print(ans_multiply)
def division ():
    num7 = input("Enter a number")
    num8 = input("Enter another number to divide")
    ans_divide = float(num7) / float(num8)
    print(ans_divide)
def exponents () :
    num9 = input("Enter a number")
    num10 = input("Enter another number as the exponentyesadd")
    ans_expo = float(num9) ** float(num10)
    print(ans_expo)
Question = input("Do u want to add, subtract, divide, multiply or find powers?")
if Question == "add":
    addition()
elif Question =="subtract":
    subtraction()
elif Question =="multiply":
    multiplication()
elif Question == "divide":
    division()
else:
    exponents()






