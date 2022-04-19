import tkinter as tk

main = tk.Tk()


class CalculatorGUI:

    def __init__(self):
        self.entry = tk.Entry(main, bg="#FFFFFF", bd=5, relief="sunken")
        self.entry.grid(row=0, column=0, columnspan=6, sticky="we")
        self.init_buttons()
        main.mainloop()

    def init_buttons(self):
        tk.Button(main, text="x2", width=7).grid(row=1, column=0)
        tk.Button(main, text="root", width=7).grid(row=1, column=1)
        tk.Button(main, text="%", width=7).grid(row=1, column=2)
        tk.Button(main, text="1/x", width=7).grid(row=1, column=3)
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
        tk.Button(main, text="clear", width=7, command=self.clear).grid(row=5, column=1)
        tk.Button(main, text="0", width=7, command=lambda: self.writetoentry("0")).grid(row=5, column=2)
        tk.Button(main, text="ce", width=7, command=self.clearelement).grid(row=5, column=4)
        tk.Button(main, text="=", width=7, command=self.calculatetext).grid(row=5, column=5)

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
        self.entry.insert(0, eval(result))
        return


if __name__ == "__main__":
    calc = CalculatorGUI()





