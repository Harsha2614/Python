#class
class Car:
    def __init__(self,car,year,color,for_sale):
        self.car=car
        self.year=year
        self.color=color
        self.for_sale=for_sale
#methods
    def drive(self):
        print(f"You drive the {self.color} {self.car}")
    def stop(self):
        print(f"You stop the {self.color} {self.car}")
    def desc(self):
        print(f" {self.year} {self.color} {self.car}")



obj1=Car("Mustang",2023,"red",True)

print(obj1.car)

obj1.drive()
obj1.stop()
obj1.desc() 




