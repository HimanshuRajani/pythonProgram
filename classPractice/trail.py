# class Dog:
#     def __init__(self, name):
#         self.name = name 
# my_dog = Dog("Buddy")

# print(my_dog.name)  # Output: Buddy

# class Car:
#     def __init__(self, make, model): 
#         self.make = make
#         self.model = model 
# my_car = Car("Toyota", "Corolla")

# print(my_car.make,my_car.model)

# class Person: 
#     def __init__(self, name):
#         self.name = name 
# p = Person("Alice")
# print(p.name) # Should print Alice

# class Calculator: 
#     def add(self, a, b):
#         return a + b 
# calc = Calculator() 
# print(calc.add(2,3)) # Should print 5 if the second argument is 3 

# class Circle:
#     pi = 3.14 #  pi is a class attribute
# print(Circle.pi) 

# class Book: 
#     def __init__(self, title):
#         self.title = title
# my_book = Book("1984") 
# print(my_book.title) # Should print 1984 

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self): 
#         return (self.height*self.width)
#     def perimeter(self): 
#         return (2*(self.height+self.width))
# rect = Rectangle(5, 10)
# print("Area:", rect.area())
# print("Perimeter:", rect.perimeter())

# class Animal:
#     def speak(self):
#         return "Animal sound" 
# class Dog(Animal):
#     def speak(self):
#         return "Bark"
# my_dog = Dog() 
# print(my_dog.speak()) # Should print "Bark" 

# class Cat: 
#     def speak(self):
#         return "Meow" 
# class Dog: 
#     def speak(self): 
#         return "Woof"
# def animal_sound(animal): 
#     print(animal.speak()) 
# my_cat = Cat() 
# my_dog = Dog() 
# animal_sound(my_cat) # Should print "Meow" 
# animal_sound(my_dog) # Should print "Woof" 

# class MathUtils:
#     def add(a, b):
#         return a + b 
# print(MathUtils.add(5, 10)) # Should print 15
