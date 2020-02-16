class Student:
    school = 'ABA TECH'
    def __init__(self):
        self.name = 'Ramit'
        self.age = 12

    def update(self):
        self.age = 15

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
    
    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        return "this is static method in this module"
        
s1 = Student()
s2 = Student()


s2.name = 'Vishnu'
s2.age = 15
# if s1.compare(s2):
#     print('They are same')
# else:
#     print('They are different')
# print(s1.age)
# print(s1.name,s1.age,s1.school)
# print(s2.name,s2.age,s2.school)
print(s1.info())