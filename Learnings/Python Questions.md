Python questions
-------------------------------------------------

[1)What are different types of oops concept in python?](#question-1)  
[2)?](#question-2)  
[3)?](#question-3)  
[4)?](#question-4)  
[5)?](#question-5)  
[6)?](#question-6)  
[7)?](#question-7)  
[8)?](#question-8)  
[9)?](#question-9)  
[10)?](#question-10)  


## Question 1  
What are different types of oops concept in python?  
A)  
In Python, the main Object-Oriented Programming (OOP) concepts are:

1. **Class and Object**:
   - **Class** is a blueprint for creating objects (instances). It defines a set of attributes and methods.
   - **Object** is an instance of a class.

   Example:
   ```python
   class Car:
       def __init__(self, brand, model):
           self.brand = brand
           self.model = model

   my_car = Car("Toyota", "Corolla")
   print(my_car.brand)  # Output: Toyota
   ```

2. **Inheritance**:
   - Allows one class (child) to inherit properties and methods from another class (parent), enabling code reusability.

   Example:
   ```python
   class Animal:
       def speak(self):
           return "Animal speaks"

   class Dog(Animal):
       def speak(self):
           return "Dog barks"

   my_dog = Dog()
   print(my_dog.speak())  # Output: Dog barks
   ```

3. **Encapsulation**:
   - Wrapping up of variables and methods into a single unit. 
   It has access specifiers like public, private and protected.

   Example:
   ```python
   class Person:
       def __init__(self, name):
           self.__name = name  # private attribute

       def get_name(self):
           return self.__name

   person = Person("Alice")
   print(person.get_name())  # Output: Alice
   ```

4. **Polymorphism**:
   - Allows objects of different classes to be treated as instances of the same class through method overriding or using functions that can work with different types.

   Example:
   ```python
   class Cat:
       def sound(self):
           return "Meow"

   class Dog:
       def sound(self):
           return "Bark"

   def animal_sound(animal):
       print(animal.sound())

   cat = Cat()
   dog = Dog()
   animal_sound(cat)  # Output: Meow
   animal_sound(dog)  # Output: Bark
   ```

5. **Abstraction**:
   - Hides the complex implementation details and shows only the necessary features. It can be achieved using abstract classes (through `abc` module).

   Example:
   ```python
   from abc import ABC, abstractmethod

   class Shape(ABC):
       @abstractmethod
       def area(self):
           pass

   class Square(Shape):
       def __init__(self, side):
           self.side = side

       def area(self):
           return self.side * self.side

   square = Square(4)
   print(square.area())  # Output: 16
   ```


## Question 2  
## Question 3  
## Question 4  
## Question 5  
## Question 6  
## Question 7  
## Question 8  
## Question 9  
## Question 10  