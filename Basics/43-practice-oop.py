class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __add__(obj1,obj2):
        return obj1.marks+obj2.marks
        pass


s1=Student('Harsha',90)
s2=Student('Vardhan',91)

print(s1+s2) #type error


