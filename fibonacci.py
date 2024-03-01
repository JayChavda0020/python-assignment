# 0 1 1 2 3 5 8 13 21 34 ....
n = int(input("Enter n: "))
a,b = 0,1
print(a, end=" ")
while b<n:
    print(b, end=" ")
    a,b = b,a+b
