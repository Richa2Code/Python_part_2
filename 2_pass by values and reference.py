# call by value 
import copy
def function(x):
  x+=1
  print(f"Inside the function = {x}")

num = 12 #num is immutable so only it's valuewill goes to the function not the adderess itself 
print(f"Outside the function = {num}")
function(num)

# call by reference

def fun2(num):
  num = copy.deepcopy(num)
  num.append(100)
  print(f"Inside the function = {num}")


element = [1, 2, 3] # element is mutable type so here it's address will go to the function 
fun2(element)
print(f"Outside the function = {element}")