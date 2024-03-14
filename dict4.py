# loop through a dictionary

d = {
    "name":"Jay",
    "age":23,
    "country":"India"
}

for x in d:
    print(x)
print("*"*50)

for x in d:
    print(d[x])
print("*"*50)

for x in d.values():
    print(x)
print("*"*50)

for x in d.keys():
    print(x)
print("*"*50)

for x,y in d.items():
    print(x,y)