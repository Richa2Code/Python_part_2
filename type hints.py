def fun(a: int, b: int) -> int:
  return a//b

num1 = 3
num2 = 4
print(fun(num1, num2))

# same for function also 

def greet() -> None:
  print("Hello, user i am here to help you.")

def add(a) -> int:
  return a+a

def for_lst(lst: list[int | str]):
  lst.append(100)
  print(lst)

greet()
print(add(4.00))

# same for the list also 

lst1 = [1, 2, 3, 4, "richa"]
for_lst(lst1)
