# Function with no argument and no return value 

def printLine():
    print("*" * 50)

printLine()
print("Welcome to user defined function in python")
printLine()

# Function with argument but no return value

def add(a,b):
    print("Addition: ",a+b)

printLine()
x = int(input("Enter Value: "))
y = int(input("Enter Value: "))
add(x,y)
printLine()

# Function with argument and return value

def sub(a,b):
    return a-b

printLine()
x = int(input("Enter Value: "))
y = int(input("Enter Value: "))
ans = sub(x,y)
# print("Subtraction: ", ans)  
print("Subtraction: ", sub(x,y))
printLine()