d = {
    "Name" : "Jay",
    "DOB" : "21-22001",
    "DOB" : "21-02-2001",
    "Mobile" : 91235463211,
    "Lang" : ["Python","HTML","JS"]
}

print(d["Name"])
print("*"*50)

print(d.get("DOB"))
print("*"*50)

k = d.keys()
print(k)
print("*"*50)

d["country"] = "India"
print(d)
print("*"*50)
print(k)
print("*"*50)

d1 = d.values()
print(d1)
print("*"*50)
d["college"] = "indus"
print(d1)
print("*"*50)

x = d.items()
print(x)
print("*"*50)
d["email"] = "jay@gmail.com"
print(x)
print("*"*50)

print("college" in d)
print("*"*50)

d["email"] = "jay123"
print(d)
print("*"*50)

d.update({"email":"jay34","mobile":854621165546})
print(d)
print("*"*50)

d.pop("Lang")
print(d)
print("*"*50)

d.popitem()
print(d)
print("*"*50)

del d["email"]
print(d)
print("*"*50)

# del d ----> deletes the dictionary completely
d.clear() # ----> empties the dictionary
print(d)

