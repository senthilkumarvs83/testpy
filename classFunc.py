class Student:
    def method(self):
        return 'In instance method' , self
    
    @classmethod
    def class_method(cls):
        return 'In class method', cls
    
    @staticmethod
    def static_method():
        return 'In static method'

a = Student()
print(a.method())
print(a.class_method())
print(a.static_method())