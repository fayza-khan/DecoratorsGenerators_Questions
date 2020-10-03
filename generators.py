def item(n):
    for items in range(n):
        yield items


i = item(8)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print("*******")
for id in item(10):
    print(id)

# convert a string into an iterator
g = "Fayza"
str_iterator = iter(g)
print(next(str_iterator))
print(next(str_iterator))
print(next(str_iterator))

