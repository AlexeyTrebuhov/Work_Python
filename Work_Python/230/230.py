from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0" # исходное значение на табло
        self.lbl = Label(text=self.formula, font=(
            "https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Roboto:ital,wght@1,100&family=Secular+One&display=swap" , 21, "bold"), bg="#72cced", foreground="#0b0514")
        self.lbl.place(x=2, y=10)

        btns = [
            "%", "CE", "C", "⌫",
            "1/x", "x²", "√x", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "2", "+",
            "+/-", "0", ".", "="
        ]

        x = 3 # отступ блока кнопок слева
        y = 70 # отступ блока кнопок сверху
        for bt in btns:
            def com(x=bt): return self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Roboto:ital,wght@1,100&family=Secular+One&display=swap", 10),
                   command=com).place(x=x, y=y,
                                      width=35, # ширина клавиш
                                      height=35) # высота клавиш
            x += 36   # расстояние от начала первой кнопки до начала следующей
            if x > 144: # условие отступа при достижении правого поля
                x = 3  # отступ справа ( для нового ряда)
                y += 36  # отступ сверху ( для нового ряда)

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "⌫":
            self.formula = self.formula[0:-1]
        elif operation == "x²":
            self.formula = str((eval(self.formula))**2)
        elif operation == "1/x":
            self.formula = str(eval(1/(self.formula)))




        elif operation == "=":
            self.formula = str(eval(self.formula))
      





        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#72cced" # Цвет фона
    root.geometry("148x287-50-100") # Размер внешний и место появления программы на мониторе
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
