class Computer:
    counter = 0
    def __init__(self,brand,ram):
        self.brand = brand
        self.ram = ram
        counter = counter+1

    def Config(self):
        print('Ram 16g, 1 TB')

    @classmethod
    def display(cls):
        return cls.counter

    @staticmethod
    def info():
        print('In info block')
    
    class Laptop:
        def __init__(self):
            self.com = 'HP'
            self.ram = '8 gb'

c1 = Computer('HP', '16GB')
# print(c1.brand, c1.ram)
# print(c1.lap.ram)
c2 = Computer('lenovo', '16GB')
print(Computer.counter)
