# Nested dictionaries
print("*"*50)

family = {
    "father" : {
        "name" : "Merambhai",
        "age" : 60
    },
    "mother" : {
        "name" : "Bhavnaben",
        "age" : 57
    },
    "son" : {
        "name" : "Jay",
        "age" : 23
    }
}   

print(family)

print("*"*50)

child1 = {
    "name" : "john",
    "age" : 20
}
child2 = {
    "name" : "Leo",
    "age" : 25
}
child3 = {
    "name" : "sean",
    "age" : 30
}

family1 = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(family1)
print("*"*50)
print(family["father"]["name"])
print("*"*50)
print(family1["child2"]["name"])