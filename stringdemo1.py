s = input("Enter a string: ")

al = 0
num = 0
sp = 0
uc = 0
lc = 0

for i in s:
    if i.isalpha():
        al = al+ 1
    elif i.isnumeric():
        num = num + 1
    elif i.isspace():
        sp = sp + 1
    if i.isupper():
        uc = uc + 1
    elif i.islower():
        lc = lc + 1

print("Total number of alphabet: ", al)
print("Total number of numeric: ", num)
print("Total number of space: ", sp)
print("Total number of upper case: ", uc)
print("Total number of lower case: ", lc)



