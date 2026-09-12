# Annoattion is specifying which kind of data type it's taking and returning 

# example one 
def calculate(a: int , b: int) -> int:
  return a + b

x = calculate(3,  5)
print(x)

# Example 2
def max_mark(marks: list) -> int:
  return max(marks)

mark = [20, 18, 19, 100]
max = max_mark(mark)
print(f"Maximum mark is {max}")

# above example we send a list and function returns the maximum number or marks from it which is int type 