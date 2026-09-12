# muatating 

def rebind(x):
  x.append(100)
  # here i am changing something within the taken variable so it will change both as it muatble. so it's called as mutating
  print(f"Inside the function = {x}")

nums = [1, 2, 3, 4]
rebind(nums)
print(f"Outside the function = {nums}")
print(f"Outside the function = {nums}")
