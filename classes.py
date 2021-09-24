from optiontal_func import *


class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def subject_output(self):
        print(self.subject_name)

    def save_file(self, file_name):
        data = self.subject_name+"\n"
        file_name.write(data)


class Group:
    def __init__(self, group_number):
        self.group_number = group_number

    def group_output(self):
        print(self.group_number)

    def save_file(self, file_name):
        data = str(self.group_number)+"\n"
        file_name.write(data)


class Student(Human, Group):
    def __init__(self, name, surname, age, group_number, education_plan):
        super().__init__(name, surname, age)
        self.group_number = group_number
        self.education_plan = education_plan

    def output_info(self):
        print("first name: " + self.name)
        print("surname: " + self.surname)
        print("age: " + str(self.age))
        print("group number: " + str(self.group_number))
        print("education plan: " + self.education_plan)

    def save_file(self, file_name):
        data = self.name+":"+self.surname+":"+str(self.age)+":"+str(self.group_number)+":"+self.education_plan+"\n"
        file_name.write(data)


class Teacher(Human, Subject):
    def __init__(self, name, surname, age, salary, subject_name):
        super().__init__(name, surname, age)
        self.subject_name = subject_name
        self.salary = salary

    def output_info(self):
        print("first name: " + self.name)
        print("surname: " + self.surname)
        print("age: " + str(self.age))
        print("salary: " + str(self.salary) + " BYN")
        print("subject: " + self.subject_name)

    def save_file(self, file_name):
        data = self.name + ":" + self.surname + ":" + str(self.age) + ":" + str(self.salary) + ":" + self.subject_name+"\n"
        file_name.write(data)