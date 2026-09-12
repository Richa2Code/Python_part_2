#pass by values 

def func(num):
  return num+num

def func2(lst):
  lst.append(100)
  return lst



num = 4 #integers are not mutable 
lst = [1, 2, 3] #list are mutable

value = func(num)
print(value)
print(num)
value2 = func2(lst)
print(value2)
print(lst)

# whatever antities are muatble that can be changed by function and immutable elements can not be changed