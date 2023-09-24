import tkinter as tk
import math 

# Evaluate
def calculate():
    expression = result_label.get()
    try:
        result = eval(expression)
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, result)
    except Exception as e:
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, "Error")

def button_click(text):
    current = result_label.get()
    if text == "=":
        calculate()
    elif text == "C":
        result_label.delete(0, tk.END)
    elif text == "DEL":
        result_label.delete(len(current) - 1)
    else:
        result_label.insert(tk.END, text)

# Square root function
def square_root():
    current = result_label.get()
    try:
        result = math.sqrt(float(current))
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, result)
    except ValueError:
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, "Error")

# Cube root function
def cube_root():
    current = result_label.get()
    try:
        result = float(current) ** (1/3)
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, result)
    except ValueError:
        result_label.delete(0, tk.END)
        result_label.insert(tk.END, "Error")

# 
calc = tk.Tk()
calc.title("Calculator")
# calc.iconbitmap('calc.ico')
calc.configure(borderwidth=2)
calc.geometry("500x550")
calc.resizable(False, False)


result_label = tk.Entry(calc, font=("Arial", 24), justify="right", bg="#7c83a3", bd=8)
result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10, sticky="nsew")
label = tk.Label(calc, text="Purva Athnere", pady=5, font=("Arial", 10,"italic", "bold"))
label.grid(row=1, column=0)

buttons = [
    'C', 'DEL', '√', '³√',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'  
]

row_val = 2
col_val = 0

button_width = 6
button_height = 2
button_font_size = 16
button_padx = 5
button_pady = 5

for button_text in buttons:
    if button_text == '√': 
        tk.Button(
            calc,
            text=button_text,
            width=button_width,
            height=button_height,
            font=("Arial", button_font_size),
            bg="#4e4e52",
            command=square_root,            
            bd=8,
            padx=button_padx,
            pady=button_pady
        ).grid(row=row_val, column=col_val, padx=0, pady=0, ipadx=0, ipady=0, sticky="nsew")
    elif button_text == '³√':  
        tk.Button(
            calc,
            text=button_text,
            width=button_width,
            height=button_height,
            font=("Arial", button_font_size),
            bg="#4e4e52",
            bd=8,
            command=cube_root,
            padx=button_padx,
            pady=button_pady
        ).grid(row=row_val, column=col_val, padx=0, pady=0, ipadx=0, ipady=0, sticky="nsew")
    elif button_text == 'C' or button_text == 'DEL':
        tk.Button(
            calc,
            text=button_text,
            width=button_width,
            height=button_height,
            font=("Arial", button_font_size),
            bg="red",bd=8,
            command=lambda text=button_text: button_click(text),
            padx=button_padx,
            pady=button_pady
        ).grid(row=row_val, column=col_val, padx=0, pady=0, ipadx=0, ipady=0, sticky="nsew")
    elif button_text == '=':
        tk.Button(
            calc,
            text=button_text,
            width=button_width,
            height=button_height,
            font=("Arial", button_font_size),
            bg="green", bd=8,
            command=lambda text=button_text: button_click(text),
            padx=button_padx,
            pady=button_pady
        ).grid(row=row_val, column=col_val, padx=0, pady=0, ipadx=0, ipady=0, sticky="nsew")
    elif button_text == '+' or button_text == '-' or button_text == '/' or button_text == '*':
        tk.Button(
            calc,
            text=button_text,
            width=button_width,
            height=button_height,
            font=("Arial", button_font_size),
            bg="#4e4e52",bd=8,
            command=lambda text=button_text: button_click(text),
            padx=button_padx,
            pady=button_pady
        ).grid(row=row_val, column=col_val, padx=0, pady=0, ipadx=0, ipady=0, sticky="nsew")
    else:
        tk.Button(
            calc,
            text=button_text,
            width=button_width,
            height=button_height,
            font=("Arial", button_font_size),
            bg="#807f7e",
            command=lambda text=button_text: button_click(text),
            bd=8,
            padx=button_padx,
            pady=button_pady
        ).grid(row=row_val, column=col_val, padx=0, pady=0, ipadx=0, ipady=0, sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
        
for i in range(4):
    calc.grid_rowconfigure(i, weight=1)
    calc.grid_columnconfigure(i, weight=1)

calc.mainloop()
