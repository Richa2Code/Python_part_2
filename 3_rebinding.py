# rebinding 

def rebind(x):
  x = [100, 12, 33]
  # in above line we gmade another variable called x so basically it will not affect the original one which called as rebindind 
  print(f"Inside the function = {x}")

nums = [1, 2, 3, 4]
rebind(nums)
print(f"Outside the function = {nums}")
