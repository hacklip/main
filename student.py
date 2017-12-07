from module import *
from moduleElement import *

class Student(object):

    modules = []
    grades = {}

    def __init__(self, name):
        self.name = name

    def add_module(self,title):
        self.modules.append(title)
        self.grades[title] = title.get_grade()

    def get_list_modules(self):
        print("Modules of Student {}:".format(self.name))#this line was nowhere mentioned in the exercises, but apparently you expect this output so here we go...
        for mod in self.modules:
            print(mod.get_title())

    def get_grades(self):
        print("Grades of Student {}:".format(self.name))#same for this line...
        for i in self.grades.keys():
            print("{}: {}".format(i.get_title(), self.grades[i]))


## test cases ###
me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
# 	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
# 	Info 1: 6
