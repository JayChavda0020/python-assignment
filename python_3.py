a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a > b:
    if a > c:
        print(a, "is greater")
    else:
        print(c, "is greater")
elif b > c:
    print(b, "is greater")
else:
    print(b, "is greater")
