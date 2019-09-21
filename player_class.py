#Testing classes

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.head = self.Head()

class Head:
    def __init__(self, size):
        self.size = size
        
        
p1 = Person("John", 36, ('Big', 4))
p2 = Person("James", 18)

pint(p1)