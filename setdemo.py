set1 = {1,2,3,"python","programminig",True,False,10.10}
print(set1)  # Duplicates are not allowed.
print("*"*50)
print(len(set1))
print("*"*50)
print(type(set1))
print("*"*50)

for s in set1:
    print(s)
print("*"*50)

print("python" in set1)
print("*"*50)

set1.add(5.5)
print(set1)                         # add item to the set
print("*"*50)

set2 = {"tops", "technologies"}
set1.update(set2)                   # add two sets
print(set1)
print("*"*50)

list1 = ["React","Javascript"]
set1.update(list1)
print(set1)                         # object in update method can be of any type
print("*"*50)

set1.remove(5.5)
set1.discard("Javascript")          # Removes item from set
print(set1)                         # if item does not exist remove will raise error while discard does not
print("*"*50)

set1.pop()
print(set1)                         # removes random item from set
print("*"*50)

set1.clear()
print(set1)                         # empties the set                                                     
print("*"*50)

# del set1
# print(set1)                       # completely deletes the set
