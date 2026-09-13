# class and object explanation 

# Class is the blueprint and based on that we can create multiple classes which have same characteristics.

# class creation
class Student:

  # Method : The functions which present inside the class called as the method with self always 

  # Constructor
  def __init__(self, roll:int, name:str, gender:str, age:int):
    print("\nCONSTRUCTOR CALLED\n")
    self.roll_no = roll
    self.name = name
    self.gender = gender
    self.age = age


  # method1 
  # def set_details(self, r:int, n:str, g:str, age:int):
  #   self.roll_no = r
  #   self.name = n
  #   self.gender= g
  #   self.age = age

  # def set_details(self):
  #   self.roll_no = int(input("Enter roll number : "))
  #   self.name = input("Enter your name : ")
  #   self.gender= input("Enter gender : ")
  #   self.age = int(input("Enter your age : "))

  # method2
  def show_details(self):
    print(f"Name : {self.name}")
    print(f"Roll.NO : {self.roll_no}")
    print(f"age : {self.age}")
    print(f"gender : {self.gender}")


# Object creation

# object1
student1 = Student(1121, "Makwana Richa", "Female", 18)
# student1.set_details(1121, "Makwana Richa", "Female", 18)
student1.show_details()
print("\n----------------------\n")
# object1
student2 = Student(1122, "Patel Richi", "Female", 18)
# student2.set_details(1122, "Patel Richi", "Female", 18)
student2.show_details()


