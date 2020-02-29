from tkinter import *

class Calculator:
    

    def button_clear(self):
        self.e.delete(0, END)

    def button_add(self):
        self.first = self.e.get()
        self.math = "add"
        self.e.delete(0,END)
    def button_sub(self):
        self.first = self.e.get()
        self.math = "sub"
        self.e.delete(0,END)
    def button_mul(self):
        self.first = self.e.get()
        self.math = "mul"
        self.e.delete(0,END)
    def button_div(self):
        self.first = self.e.get()
        self.math = "div"
        self.e.delete(0,END)

    def button_equal(self):
        self.second = self.e.get()
        self.e.delete(0, END)

        if self.math == "add":
            self.sum = int(self.first) + int(self.second)
            self.e.insert(0, self.sum)
        if self.math == "sub":
            self.sum = int(self.first) - int(self.second)
            self.e.insert(0, self.sum)
        if self.math == "mul":
            self.sum = int(self.first) * int(self.second)
            self.e.insert(0, self.sum)
        if self.math == "div":
            self.sum = int(self.first) / int(self.second)
            self.e.insert(0, self.sum)
        
    def __init__(self,root):
        root.title("Calculator")
        self.e = Entry(root, width=38, borderwidth=5)
        self.e.grid(row=0,column=0, padx=40, pady=20, columnspan=3)

        button_1 = Button(root, text="1",padx =40, pady=20, command= lambda :self.button_click(1))
        button_2 = Button(root, text="2",padx =40, pady=20, command=lambda :self.button_click(2))
        button_3 = Button(root, text="3",padx =40, pady=20, command=lambda :self.button_click(3))
        button_4 = Button(root, text="4",padx =40, pady=20, command=lambda :self.button_click(4))
        button_5 = Button(root, text="5",padx =40, pady=20, command=lambda :self.button_click(5))
        button_6 = Button(root, text="6",padx =40, pady=20, command=lambda :self.button_click(6))
        button_7 = Button(root, text="7",padx =40, pady=20, command=lambda :self.button_click(7))
        button_8 = Button(root, text="8",padx =40, pady=20, command=lambda :self.button_click(8))
        button_9 = Button(root, text="9",padx =40, pady=20, command=lambda :self.button_click(9))
        button_0 = Button(root, text="0",padx =40, pady=20, command=lambda :self.button_click(0))
        button_add = Button(root, text="+",padx =39, pady=20, command=self.button_add)
        button_equal = Button(root, text="=",padx =91, pady=20, command=self.button_equal)
        button_clear = Button(root, text="Clear",padx =79, pady=20, command=self.button_clear)
        button_sub = Button(root, text="-",padx =40, pady=20, command=self.button_sub)
        button_mul = Button(root, text="*",padx =40, pady=20, command=self.button_mul)
        button_div = Button(root, text="/",padx =40, pady=20, command=self.button_div)
        
        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)

        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)

        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)

        button_0.grid(row=4, column=0)
        button_clear.grid(row=4, column=1,columnspan=2)
        button_add.grid(row=5, column=0)
        button_equal.grid(row=5, column=1, columnspan=2)

        button_sub.grid(row=6, column=0)
        button_mul.grid(row=6, column=1)
        button_div.grid(row=6, column=2)

    def button_click(self, number):
        self.a = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, str(self.a) + str(number))


root= Tk()
calc = Calculator(root)
root.mainloop()
