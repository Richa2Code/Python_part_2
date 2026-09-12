# Shallow and deep copy 
import copy
#Normal copy 
original = [1, 3, 5, 7]
copy_one = original


copy_one.append(100)
print("\nNormal copy_one\n")
print(id(original))
print(id(copy_one))

print(original)
print(copy_one)

# Shallow copy 

print("\nShallow copy\n") 
o2 = [34, 56,[1, 2, 3], 37, 23]

# shallow = o2.copy() # First method 
shallow = copy.copy(o2)

shallow[2][0]=78 #This is problem where it changes in original also when there is another list insilde list this is where deep copy will come into the picture 

print(o2)
print(shallow)

print(id(o2))
print(id(shallow))

# Deep copy 

o3 = [12, 34, 56, [1, 2, 3, 4], 55]

print("\nDeep copy\n")
deep_copy = copy.deepcopy(o3)

deep_copy[3][1] = 22

print(o3)
print(deep_copy)

print(id(o3))
print(id(deep_copy))