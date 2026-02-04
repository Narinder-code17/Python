from tkinter import *

# ---- Window ----
root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# ---- Display ----
expression = StringVar()

display = Entry(root, textvariable=expression, font=("Arial", 22),
                bd=5, relief=SUNKEN, justify="right")
display.pack(fill=X, padx=10, pady=10, ipady=10)


# ---- Button click handler ----
def button_click(value):
    current = expression.get()
    expression.set(current + value)


def clear_display():
    expression.set("")


def delete_last():
    current = expression.get()
    expression.set(current[:-1])


def calculate():
    try:
        result = eval(expression.get())
        expression.set(str(result))
    except:
        expression.set("Error")


# ---- Button layout ----
btn_frame = Frame(root)
btn_frame.pack()

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
]

for (text, row, col) in buttons:
    cmd = (lambda x=text: calculate() if x == '=' else button_click(x))
    Button(btn_frame, text=text, width=6, height=2,
           font=("Arial", 14),
           command=cmd).grid(row=row, column=col, padx=5, pady=5)

# Extra controls
Button(btn_frame, text="C", width=6, height=2,
       font=("Arial", 14), command=clear_display).grid(row=5, column=0, padx=5, pady=5)

Button(btn_frame, text="DEL", width=6, height=2,
       font=("Arial", 14), command=delete_last).grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
