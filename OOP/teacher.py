class Person:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    

class Student(Person):
    
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade
        
    def get_grade(self):
        return self.__grade
    
    
# TODO
# Make a Teacher class that inherits Person and add salary attribute with it getter and setters.
# Override get_name to make Mr/{name}.
class Teacher(Person):
    
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.set_salary(salary)

    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
             print("Enter right salary")


    def get_name(self):
        return ("Mr/"+super().get_name())

    def get_salary(self):
        return self.__salary

# Should print teacher name, age and salary.
# Although I don't know the implementation of the teacher.
# I can make the program and this is one of the advantage of oop.
if __name__ == "__main__":
    teacher = Teacher("Abdullah", 21, 2000)
    print("Name: " + teacher.get_name() + "\nAge: " +  str(teacher.get_age()) + "\nSalary: " +  str(teacher.get_salary())) 
    
# Expected Output:
# Name: Mr/Abdullah
# Age: 21
# Salary: 2000
