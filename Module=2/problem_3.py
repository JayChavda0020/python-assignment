n = int(input("Enter N: "))
n2 = int(input("Enter N2: "))
sum = 0

while n2 >= n:
    sum = sum + n2
    n2 -= 1
print("Fibonacci is: ", sum)
