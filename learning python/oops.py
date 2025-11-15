#here we will learn about the oops in the python
# oops stands for object oriented programming system
# there are four main concepts in oops
# 1. class
# 2. object
# 3. inheritance
# 4. polymorphism
# 5. encapsulation
# 6. abstraction
# class is a blueprint of an object


#! creating a class
class Student:
    name ="nusrat jahan"

class Car:
    def __init__(self, color, model):  # color & model are parameters
        self.color = color
        self.model = model

# Create an object
my_car = Car("red", "Toyota")  # "red" & "Toyota" are arguments
print(my_car.color)  # Output: red

# we can also create the methods in the class 
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
    def get_age(self):
        return self.age
    

# we need create the class of a student that take the name marks of the three subjects 
# and return the average marks of the student
class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def average(self):
        return (self.marks1+self.marks2+self.marks3)/3  
    #static method
    @staticmethod #decorator which takes parameter as a function and return a function
    def info():
        print("This is a student class")


s1=Student("Nusrat", 85, 90, 95)
print(s1.average())
Student.info()

#pillars of the oops 
#1. abstraction: hiding the complexity and showing only the essential features of the object
#2. encapsulation: wrapping the data and the methods that operate on the data within one unit
#3. inheritance
#4. polymorphism

#1. lets understand the abstraction
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self._speed = 0  # private attribute

    def accelerate(self):
        self._speed += 5 # private method

    def brake(self):
        self._speed -= 5

    def get_speed(self):
        return self._speed # public method
# we can access the private attribute and method using the public method
my_car = Car("Toyota", 2020)
my_car.accelerate()
print(my_car.get_speed())  # Output: 5
my_car.brake()  
print(my_car.get_speed())  # Output: 0
#2. lets understand the encapsulation
# every thing we are doing in the class is encapsulated in the object 
# 
class Account:
    def __init__(self,balance,accountno):
        self.balance = balance  # we are giving the value to the attribute balance
        self.accountno = accountno
    def debit(self,balance):
        self.balance = self.balance - balance
        return self.balance
    def credit(self,balance):
        self.balance = self.balance + balance
        return self.balance
    def printBalance(self):
        print("The balance is:",self.balance)
    def getAccountNo(self):
        print("The account number is:",self.accountno)
a1=Account(1000,"12345")
a1.debit(200)
a1.printBalance()
a1.credit(500)
a1.printBalance()
a1.getAccountNo()
# we can delete any object or the method by using the del keyword
del a1
print(a1)  # this will give an error because the object is deleted

#public and private attribute 
class Person:
    def __init__(self, name, age):
        self.name = name  # public attribute
        self.__age = age  # private attribute

    def get_age(self):  # public method to access private attribute
        return self.__age

    def set_age(self, age):  # public method to modify private attribute
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age")

p1 = Person("Alice", 30)
print(p1.name)  # Output: Alice
print(p1.get_age())  # Output: 30            
print(p1.__age)  # This will give an error because __age is private

#private and public method
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # public attribute

    def deposit(self, amount):  # public method
        if amount > 0:
            self.__update_balance(amount)  # calling private method
        else:
            print("Please enter a valid amount")

    def withdraw(self, amount):  # public method
        if 0 < amount <= self.balance:
            self.__update_balance(-amount)  # calling private method
        else:
            print("Insufficient funds or invalid amount")

    def get_balance(self):  # public method
        return self.balance

    def __update_balance(self, amount):  # private method
        self.balance += amount