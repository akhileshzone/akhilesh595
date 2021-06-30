# scientific calculator
import math

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def exp(a):
    return a ** 2


def sqrt(a):
    print(math.sqrt(a))


def sin(x):
    print(math.sin(x))


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


# select the operation want to perform

print("""
1.Addition
2.Substraction
3.Multiplication
4.Division
5.Exponent
6.Square root
7.Sin
8.Cos
9.Tan
""")
# Select an operation
op = int(input("Enter the operation="))

while op < 10:
    if op == 1:
        print("Enter the parameters=")
        x1 = int(input("Enter x="))
        y1 = int(input("Enter y="))
        res = add(x1, y1)
        print("Addition=", res)
    elif op == 2:
        print("Enter the parameters=")
        x2 = int(input("Enter x="))
        y2 = int(input("Enter y="))
        res = sub(x2, y2)
        print("Substraction=", res)
    elif op == 3:
        print("Enter the parameters=")
        x3 = int(input("Enter x="))
        y3 = int(input("Enter y="))
        res = mul(x3, y3)
        print("Multiplication=", res)
    elif op == 4:
        print("Enter the parameters=")
        x4 = int(input("Enter x="))
        y4 = int(input("Enter y="))
        res = div(x4, y4)
        print("Division=", res)
    elif op == 5:
        print("Enter the parameters=")
        x5 = int(input("Enter x="))
        res = exp(x5)
        print("Exponent=", res)
    elif op == 6:
        print("Enter the parameters=")
        x6 = int(input("Enter x="))
        res = sqrt(x6)
        print("Square root=", res)
    elif op == 7:
        print("Enter the parameters=")
        x7 = int(input("Enter x="))
        res = sin(x7)
        print("Sin=", res)
    elif op == 8:
        print("Enter the parameters=")
        x8 = int(input("Enter x="))
        res = cos(x8)
        print("Cos=", res)
    elif op == 9:
        print("Enter the parameters=")
        x9 = int(input("Enter x="))
        res = tan(x9)
        print("Tan=", res)

    else:
        print("Choose an operation!")

    New = int(input("Do you want to continue-(Yes-1),(No-0)"))
    if New==1:
        op=int(input("Enter the operation="))
    elif New==0:
        print("Thankyou for using the calculator!")
        break
    else:
        print("Entered an invaild key.")
        break
