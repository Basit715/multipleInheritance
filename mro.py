"""Explaining method resolution order(mro)
Suppose we have a scenario of multiple inheritance like
"""

# class Father:
#      def showF(self):
#           print("Father class method")
          
# class Mother:
#      def showM(self):
#           print("Mother class method")
          
# class Son(Father, Mother):
#      def showS(self):
#           print("son class method") 
     
     
# s = Son()
# s.showS()
# s.showF()
# s.showM()

"""Until now everything looks fine  but the work gets tricky when we have constructrs coming into play as 
lets copy the above classes and comment out above code and lets add constructors one by one
"""

# class Father:
#      def showF(self):
#           print("Father class method")
          
# class Mother:
#      def showM(self):
#           print("Mother class method")
          
# class Son(Father, Mother):
#      def __init__(self):
#           print("son constructor called")
#      def showS(self):
#           print("son class method") 

"""first lets create the son class constructor
When object of son class be created, the constructor will be called for son class as;

"""

# s = Son()  # son constructor will be called


"""Now if we add the constructor in father class also 
then if we create the object of son class, the constructor for son class will be prefferd and will get executed and 
father class constructor will not be executed
"""

# class Father:
#      def __init__(self):
#           print("father class constructor called")
#      def showF(self):
#           print("Father class method")
          
# class Mother:
#      def showM(self):
#           print("Mother class method")
          
# class Son(Father, Mother):
#      def __init__(self):
#           print("son constructor called")
#      def showS(self):
#           print("son class method") 
          
# s = Son()  # only son construtor will be still called


"""now if we want to call the father constructor also we need to use the super() keyword in son constructor as"""
# class Father:
#      def __init__(self):
#           print("father class constructor called")
#      def showF(self):
#           print("Father class method")
          
# class Mother:
#      def __init__(self):
#           print("mother class constructor called")
#      def showM(self):
#           print("Mother class method")
          
# class Son(Father, Mother):
#      def __init__(self):
#           super().__init__()
#           print("son constructor called")
#      def showS(self):
#           print("son class method") 
          
# S = Son()   # now first the father constructor will be called and then the son constructor will be called

"""But still the mother class constructor does not get called
The solution to this problem is adding super() method in all the parent classes and thats where mro comes into play
"""
class Father:
     def __init__(self):
          super().__init__()
          print("father class constructor called")
     def showF(self):
          print("Father class method")
          
class Mother:
     def __init__(self):
          super().__init__()
          print("mother class constructor called")
     def showM(self):
          print("Mother class method")
          
class Son(Father, Mother):
     def __init__(self):
          super().__init__()
          print("son constructor called")
     def showS(self):
          print("son class method") 
          
s = Son()


"""
output:
mother class constructor called
father class constructor called
son constructor called

But how!
lets understand mro

In the multiple inheritance scenario members of class are searched first in the current class(say Son). If not found there, the search continues into parent class in depth-first, left to right(say father, mother here) without searching the same class twice

we have the scenario here as

object->(father, mother)->son ie father and mother class are derived from object class and son class is derived from father and mother classes

s = Son()
1.The search will start from the Son. As the object of Son class is created, the constructor of son is called.
Now the son constructor is visited once it will not be visited again
2. Son has super().__init__() inside its constructor so its parent class, the one in the left side i;e father classe's constructor is called
3.Fther class has also super().__init__() inside its constructor so its parent object class constructor is called.
4. object class does not have any constructor so the search will continue to the right hand side class(Mother) of object class so Mother class constructor is called
5.As mother class has also super().__init__() so its parent class 'object' constructor is called but as it has already been visited once so it will not get called and it will move to next line in mother class constructor and print
(mother class constructor called)
then control will be returned to father class constructor and moving to next line it will print
(father class constructor called)
and at the end son class constructor called will be prited 


"""