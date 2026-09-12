# Shallow and deep copy 

#Normal copy 

original = [1, 3, 5, 7]
copy = original


copy.append(100)

print(id(original))
print(id(copy))

print(original)
print(copy)