# class is the blueprint and based on that class we can make multiple instances from the class which is called as object.

class student:
  def __init__(self, name, age):
    print("Hello, your assistant is here to help you !")
    self.name = name
    self.age = age

  def info(self):
    print(f"Your name is {self.name}. You are {self.age} years old.")
    print("Thank you !")


obj = student("Vraj", 22)
obj.info()