class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
              return "Email is not set, please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None



skillf = Employee("Skill", "f")
# print(skillf.email)

o = "This is a string"
# print(dir(skillf))
# print(id("That That"))

import inspect
print(inspect.getmembers(skillf))