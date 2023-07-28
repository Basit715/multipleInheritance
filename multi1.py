# The situation of multiple inheritance when two base classes are not designed for multiple inheritanc and are unrelated to each other

"""Class person is first class that has an attribute name and is not related to Employee class"""
class Person:
     def __init__(self, name):
          self.name = name
        

"""Class Employee is another class that has an attribute salary and is not related to Person class"""  
class Employee:
     def __init__(self, salary):
          self.salary = salary
          

"""Now we create a programmer class that inherits from class Person and class Employee """
"""Now we have two ways and both will be explained
1. without use of super keyword
2. With use of super keyword 
"""

"""Without use of super keyword"""

# class Programmer(Person, Employee):
#      def __init__(self, name = 'name', salary = 'salarry', language = 'language'):
#           Person.__init__(self, name)
#           Employee.__init__(self, salary)
#           self.language = language
          
#      def show(self):
#           print(f"The name of programmer is {self.name}")
#           print(f"The salary of programmer is {self.salary}")
#           print(f"The langauge used by the progammer is {self.language}")


"""with use of super keyword"""
class Programmer(Person, Employee):
     def __init__(self, name='name', salary='salary', lang='language'):
          super().__init__(name)
          super(Person, self).__init__(salary)
          self.language = lang
     def show(self):
           print(f"The name of programmer is {self.name}")
           print(f"The salary of programmer is {self.salary}")
           print(f"The langauge used by the progammer is {self.language}") 
     
          
          
"""creating the object of class Programmer""" 
p1 = Programmer("Basit", 120000, "python")
p1.show()    