# Perfect example of class and object 

class Student:

  def __init__(self, name:str, age: int, marks: list[int]):
    self.name = name
    self.age = age
    self.marks = marks

  def total(self):
    print(f"Total marks : {sum(self.marks)}")
    return sum(self.marks)

  def avg(self):
    print(f"Average is {self.total() / len(self.marks)}")
    return self.total()/len(self.marks)

  def grade(self):
    avg = self.avg() * 100
    if avg>=90:
      print(f"Grade : A")
    elif avg>=50 and avg<=89:
      print("Grade : B")
    elif avg<50:
      print("Grade : C")


Student1 = Student("Richa Makwana", 18, [20, 19, 19, 18, 18])
Student1.grade()