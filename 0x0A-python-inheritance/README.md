![Inheritance](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190501121513/inheritance.png)   
# Python
-----
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

Example:
---

```sh
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Ronald", "Aguirre")
x.printname()

```
## Output
```sh
$ Ronald Aguirre 
```


# Python - Inheritance
----
## Ronald Aguirre 