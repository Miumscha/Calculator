import tkinter as tk

main = tk.Tk()


class CalculatorGUI():

    def __init__(self):
        self.lb = tk.Entry(main, bg="#FFFFFF", bd=5, relief="sunken")
        self.lb.grid(row=0, column=0, columnspan=4, sticky="we")
        self.init_buttons()
        main.mainloop()

    def init_buttons(self):
        tk.Button(main, text="x2", width=7).grid(row=1, column=0)
        tk.Button(main, text="root", width=7).grid(row=1, column=1)
        tk.Button(main, text="%", width=7).grid(row=1, column=2)
        tk.Button(main, text="1/x", width=7).grid(row=1, column=3)
        tk.Button(main, text="+", width=7).grid(row=2, column=3)
        tk.Button(main, text="1", width=7).grid(row=2, column=0)
        tk.Button(main, text="2", width=7).grid(row=2, column=1)
        tk.Button(main, text="3", width=7).grid(row=2, column=2)
        tk.Button(main, text="-", width=7).grid(row=3, column=3)
        tk.Button(main, text="4", width=7).grid(row=3, column=0)
        tk.Button(main, text="5", width=7).grid(row=3, column=1)
        tk.Button(main, text="6", width=7).grid(row=3, column=2)
        tk.Button(main, text="*", width=7).grid(row=4, column=3)
        tk.Button(main, text="7", width=7).grid(row=4, column=0)
        tk.Button(main, text="8", width=7).grid(row=4, column=1)
        tk.Button(main, text="9", width=7).grid(row=4, column=2)
        tk.Button(main, text="/", width=7).grid(row=5, column=3)
        tk.Button(main, text=".", width=7).grid(row=5, column=0)
        tk.Button(main, text="clear", width=7, command=self.clear).grid(row=5, column=1)
        tk.Button(main, text="0", width=7).grid(row=5, column=2)




    def clear(self):
        self.lb.delete(0, "end")






if __name__ == "__main__":
    calc = CalculatorGUI()





