import tkinter as tk
import math

main = tk.Tk()


class CalculatorGUI:

    def __init__(self):
        self.entry = tk.Entry(main, bg="#b1e8ee", bd=5, relief="sunken")
        self.entry.grid(row=0, column=0, columnspan=6, sticky="we")
        self.init_buttons()
        main.configure(background='light blue')
        main.mainloop()

    def init_buttons(self):
        tk.Button(main, text="x2", width=7, command=self.square, bg="light green").grid(row=1, column=0)
        tk.Button(main, text="root", width=7, command=self.sqroot, bg="light green").grid(row=1, column=1)
        tk.Button(main, text="%", width=7, command=self.percentage, bg="light green").grid(row=1, column=2)
        tk.Button(main, text="1/x", width=7, command=self.kehrwert, bg="light green").grid(row=1, column=3)
        tk.Button(main, text="(", width=7, command=lambda: self.writetoentry("(")).grid(row=1, column=4)
        tk.Button(main, text=")", width=7, command=lambda: self.writetoentry(")")).grid(row=1, column=5)
        tk.Button(main, text="+", width=7, command=lambda: self.writetoentry("+")).grid(row=2, column=3)
        tk.Button(main, text="1", width=7, command=lambda: self.writetoentry("1")).grid(row=2, column=0)
        tk.Button(main, text="2", width=7, command=lambda: self.writetoentry("2")).grid(row=2, column=1)
        tk.Button(main, text="3", width=7, command=lambda: self.writetoentry("3")).grid(row=2, column=2)
        tk.Button(main, text="-", width=7, command=lambda: self.writetoentry("-")).grid(row=3, column=3)
        tk.Button(main, text="4", width=7, command=lambda: self.writetoentry("4")).grid(row=3, column=0)
        tk.Button(main, text="5", width=7, command=lambda: self.writetoentry("5")).grid(row=3, column=1)
        tk.Button(main, text="6", width=7, command=lambda: self.writetoentry("6")).grid(row=3, column=2)
        tk.Button(main, text="*", width=7, command=lambda: self.writetoentry("*")).grid(row=4, column=3)
        tk.Button(main, text="7", width=7, command=lambda: self.writetoentry("7")).grid(row=4, column=0)
        tk.Button(main, text="8", width=7, command=lambda: self.writetoentry("8")).grid(row=4, column=1)
        tk.Button(main, text="9", width=7, command=lambda: self.writetoentry("9")).grid(row=4, column=2)
        tk.Button(main, text="/", width=7, command=lambda: self.writetoentry("/")).grid(row=5, column=3)
        tk.Button(main, text=".", width=7, command=lambda: self.writetoentry(".")).grid(row=5, column=0)
        tk.Button(main, text="clear", width=7, command=self.clear, bg="grey").grid(row=5, column=1)
        tk.Button(main, text="0", width=7, command=lambda: self.writetoentry("0")).grid(row=5, column=2)
        tk.Button(main, text="ce", width=7, command=self.clearelement, bg="grey").grid(row=5, column=4)
        tk.Button(main, text="=", width=7, command=self.calculatetext, bg="grey").grid(row=5, column=5)

    def clear(self):
        self.entry.delete(0, tk.END)

    def clearelement(self):
        self.entry.delete(self.entry.index(tk.END) - 1)

    def writetoentry(self, text):
        self.entry.insert(tk.END, text)
        return

    def calculatetext(self):
        result = self.entry.get()
        self.entry.delete(0, tk.END)
        try:
            self.entry.insert(0, eval(result))
        except SyntaxError:
            self.entry.insert(0, "Wrong Syntax, please us a correct mathematical notation")

    def square(self):
        number = self.entry.get()
        numberconverted = float(number)
        self.entry.delete(0, tk.END)
        squareresult = numberconverted * numberconverted
        self.entry.insert(0, str(squareresult))

    def sqroot(self):
        number = self.entry.get()
        numconverted = float(number)
        self.entry.delete(0, tk.END)
        sqr = math.sqrt(numconverted)
        self.entry.insert(0, str(sqr))

    def kehrwert(self):
        number = self.entry.get()
        numconverted = float(number)
        self.entry.delete(0, tk.END)
        kehrwert = 1 / numconverted
        self.entry.insert(0, str(kehrwert))

    def percentage(self):
        numbers = self.entry.get()
        numarray = numbers.split(" ")
        num1 = float(numarray[0])
        num2 = float(numarray[1])

        self.entry.delete(0, tk.END)
        percentage = (num1 / num2) * 100
        self.entry.insert(0, str(percentage) + "%")


if __name__ == "__main__":
    calc = CalculatorGUI()
