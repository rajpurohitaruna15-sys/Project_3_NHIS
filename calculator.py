from tkinter import *

# window
root = Tk()
root.title("Basic Calculator")
root.geometry("300x400")

# display
entry = Entry(root, font=("Arial", 20), bd=5, relief=RIDGE, justify="right")
entry.pack(fill=X, padx=10, pady=10)

# functions
def press(val):
    entry.insert(END, val)

def clear():
    entry.delete(0, END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# buttons frame
frame = Frame(root)
frame.pack()

# buttons list
buttons = [
    ('7', press), ('8', press), ('9', press), ('/', press),
    ('4', press), ('5', press), ('6', press), ('*', press),
    ('1', press), ('2', press), ('3', press), ('-', press),
    ('0', press), ('C', clear), ('=', equal), ('+', press)
]

row = 0
col = 0

for (text, func) in buttons:
    if text == '=':
        Button(frame, text=text, width=5, height=2, command=func).grid(row=row, column=col)
    elif text == 'C':
        Button(frame, text=text, width=5, height=2, command=func).grid(row=row, column=col)
    else:
        Button(frame, text=text, width=5, height=2,
               command=lambda t=text: func(t)).grid(row=row, column=col)

    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()

Button(root, text=".", width=5, height=2,
       command=lambda: click(".")).place(x=50, y=230)

Button(root, text="%", width=5, height=2,
       command=lambda: click("%")).place(x=120, y=230)


def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current[:-1])

Button(root, text="⌫", width=5, height=2,
       command=backspace).place(x=190, y=230)

entry = Entry(root, width=16, font=("Arial", 20),
              borderwidth=5, justify="right")