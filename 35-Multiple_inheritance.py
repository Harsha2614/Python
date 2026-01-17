class Animal:

    def __init__(self,name):
         self.name=name             #this method is directly called
          
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
    pass

class predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
    pass

class rabbit(prey):
    pass

class Hawk(predator):
    pass
class fish(prey,predator):
    pass

rabbit=rabbit('nemo')
Hawk=Hawk('tony')
fish=fish('bugs')

rabbit.sleep()
