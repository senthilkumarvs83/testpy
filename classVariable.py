class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        # self.lap = Laptop()
    
    def getAverage(self):
        return (self.m1+self.m2+self.m3)/3
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.ram = 8
    
obj1 = Student(34,56,67)
# obj2 = Student(94,66,77)
obj2 = obj1.Laptop()
print(obj2.brand, obj2.ram)



