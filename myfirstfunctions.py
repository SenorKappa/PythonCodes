def adding_number(num1, num2):
    print(num1+num2)

def subtracting_number(num1,num2):
    print(num1-num2)

def multiplying_number(num1,num2):
    print(num1*num2)

def dividing_number(num1,num2):
    print(num1/num2)

print("Enter your desired operation: (ADD, SUB, MUL, DIV) ")
op = str(input())
if op == "ADD":
    adding_number(num1=int(input()),num2=int(input()))
if op == "SUB":
    subtracting_number(num1=int(input()),num2=int(input()))
if op == "MUL":
    multiplying_number(num1=int(input()),num2=int(input()))
if op == "DIV":
    dividing_number(num1=int(input()),num2=int(input()))

elif op != "ADD" and op != "SUB" and op != "MUL" and op != "DIV":
        print("invalid operation")
        print("read instructions carefully")


