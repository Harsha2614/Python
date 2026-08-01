class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def run(self):
        print(f"{self.name} is running")

class Dog(Animal):
    def sound(self):
        print("Bark")

    pass

class Cat(Animal):
    def sound(self):
        print("meow")
    pass

class Mouse(Animal):
    def sound(self):
        print("sqeew")
    pass

d1=Dog("Mickey")
c1=Cat("mouse")
m1=Mouse("jerry")  #calling the Animal parent class

d1.eat()  #calling the method in animal class
c1.sound() #calling the method created in cat class
m1.sleep() #calling the method in animal class


