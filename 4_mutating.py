# muatating 

def rebind(x):
  x.append(100)
  print(f"Inside the function = {x}")

nums = [1, 2, 3, 4]
rebind(nums)
print(f"Outside the function = {nums}")
