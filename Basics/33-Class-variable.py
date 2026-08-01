class Student:

    class_variable=2024
    Student_num=0

    def __init__(self,name,year):
        self.name=name
        self.year=year
        Student.Student_num+=1

obj3=Student("Harsha",2004)
obj4=Student("Vardhan",200)
obj5=Student("narayana",20)

# print(obj3.name)
# print(obj3.year)
# print(Student.class_variable) #best way to call class variable instead of using instance i.e., obj3.class_variable
print(f"My class Has {Student.Student_num} Students")

print(obj3.name)
print(obj4.name)
print(obj5.name)