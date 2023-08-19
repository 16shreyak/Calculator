from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Beautiful Calculator")
        self.expression = StringVar()

        # Entry field to display the expression
        self.expression_field = Entry(root, textvariable=self.expression, font=('Arial', 24), bd=10,
                                      insertbackground='black')
        self.expression_field.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

        # Colors for buttons
        digit_color = '#d1d1d1'
        operator_color = '#ff8a65'
        equals_color = '#66bb6a'
        clear_color = '#ef5350'

        buttons = [
            ('7', 1, 0, digit_color), ('8', 1, 1, digit_color), ('9', 1, 2, digit_color), ('/', 1, 3, operator_color),
            ('4', 2, 0, digit_color), ('5', 2, 1, digit_color), ('6', 2, 2, digit_color), ('*', 2, 3, operator_color),
            ('1', 3, 0, digit_color), ('2', 3, 1, digit_color), ('3', 3, 2, digit_color), ('-', 3, 3, operator_color),
            ('0', 4, 0, digit_color), ('.', 4, 1, digit_color), ('C', 4, 2, clear_color), ('+', 4, 3, operator_color),
            ('=', 5, 0, equals_color),
        ]

        for button_text, row, col, color in buttons:
            self.create_button(button_text, row, col, color)

    def create_button(self, text, row, col, color):
        button = Button(self.root, text=text, font=('Arial', 20, 'bold'), padx=20, pady=20,
                        bg=color, command=lambda: self.button_click(text))
        button.grid(row=row, column=col, ipadx=10, ipady=10)

    def button_click(self, value):
        if value == '=':
            try:
                result = str(eval(self.expression.get()))
                self.expression.set(result)
            except:
                self.expression.set("Error")
        elif value == 'C':
            self.expression.set("")
        else:
            self.expression.set(self.expression.get() + str(value))

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    calculator = Calculator(root)
    root.mainloop()
