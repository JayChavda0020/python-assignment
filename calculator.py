import tkinter as tk

def button_click(symbol):
    current = display_var.get()
    if symbol == '=':
        try:
            result = eval(current)
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif symbol == 'C':
        display_var.set("")
    else:
        display_var.set(current + symbol)

root = tk.Tk()
root.title("Simple Calculator")

display_var = tk.StringVar()

display = tk.Entry(root, textvariable=display_var, font=('Arial', 18), bd=10, insertwidth=4, width=14, justify='right')
display.grid(row=0, column=0, columnspan=4)

def key_press(event):
    key = event.char
    if key.isdigit() or key == '.':
        button_click(key)
    elif key == '+':
        button_click('+')
    elif key == '-':
        button_click('-')
    elif key == '*':
        button_click('*')
    elif key == '/':
        button_click('/')
    elif key == '\r':
        button_click('=')
    elif key == '\x08':
        button_click('C')

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, font=('Arial', 14), padx=20, pady=20, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col)

root.bind('<Key>', key_press)

root.mainloop()
