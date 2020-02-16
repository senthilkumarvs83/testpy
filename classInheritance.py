class Employee:
    raise_amt = 1.05
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def displaydet(self):
        return (self.name, self.age, self.salary)
    
    def calcSalary(self):
        self.salary = int(self.salary * self.raise_amt)

    # def __repr__(self):
    #     return self.name, self.age, self.salary

a1 = Employee('vignesh',27,90000)
# a2 = Developer('vignesh',27,90000,'python')
print(a1)

