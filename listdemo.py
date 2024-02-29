# list is a group of different type of data

l = [1, 2, 3, 1.1, 2.2 , "Tops", 10, True, 1, 2, False, "python"]

print(l)
l.append(100)
print(l)
l1 = l.copy()
print(l1)
print(l.count(1))
l2 = [1000, 2000, 3000]
l.extend(l2)
print(l)
print(l.index(10))
l.insert(5, 101)
print(l)
l.pop()
print(l)
l.pop(5)
print(l)
l.remove(3)
print(l)
l.clear()
print(l)
