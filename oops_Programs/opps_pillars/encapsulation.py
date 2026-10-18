class Student:
    def __init__(self, name, roll_number):
        self.__name = name
        self.__roll_number = roll_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_roll_number(self):
        return self.__roll_number

    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    def print_student_details(self):
        return "Name : {}, Roll Number: {}".format(self.__name, self.__roll_number)


student = Student("Sathya", 101)
print(student.print_student_details())

# Modifying private attribute via public method
student.set_name("Raj")
student.set_roll_number(102)
print(student.print_student_details())
