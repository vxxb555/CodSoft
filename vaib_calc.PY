import tkinter as tk

calc = ""

def add_to_calc(symbol):
    global calc
    calc += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calc)

def evaluate_calc():
    global calc
    try:
        if "+" in calc:
            result = str(eval(calc))
            calc = ""
            text_result.delete(1.0, "end")
            text_result.insert(1.0, result)
        elif "-" in calc:
            result = str(eval(calc))
            calc = ""
            text_result.delete(1.0, "end")
            text_result.insert(1.0, result)
        elif "*" in calc:
            result = str(eval(calc))
            calc = ""
            text_result.delete(1.0, "end")
            text_result.insert(1.0, result)
        elif "/" in calc:
            result = str(eval(calc))
            calc = ""
            text_result.delete(1.0, "end")
            text_result.insert(1.0, result)
        else:
            result = str(eval(calc))
            calc = ""
            text_result.delete(1.0, "end")
            text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "error")

def clear_field():
    global calc
    calc = ""
    text_result.delete(1.0, "end")

vaib_calc = tk.Tk()
vaib_calc.geometry("300x300")
vaib_calc.title("Vaibhav's Calculator")
vaib_calc.resizable(width=True, height=True)

text_result = tk.Text(vaib_calc, height=2, width=16, font=("Arial",25),bg='gray',fg='black')
text_result.grid(columnspan=5, pady=5)

btn_1 = tk.Button(vaib_calc , text="1", command=lambda: add_to_calc(1), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(vaib_calc , text="2", command=lambda: add_to_calc(2), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(vaib_calc , text="3", command=lambda: add_to_calc(3), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(vaib_calc , text="4", command=lambda: add_to_calc(4), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(vaib_calc , text="5", command=lambda: add_to_calc(5), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(vaib_calc , text="6", command=lambda: add_to_calc(6), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(vaib_calc , text="7", command=lambda: add_to_calc(7), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(vaib_calc , text="8", command=lambda: add_to_calc(8), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(vaib_calc , text="9", command=lambda: add_to_calc(9), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(vaib_calc , text="0", command=lambda: add_to_calc(0), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(vaib_calc , text="+", command=lambda: add_to_calc("+"), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(vaib_calc , text="-", command=lambda: add_to_calc("-"), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_minus.grid(row=3, column=4)
btn_multiply = tk.Button(vaib_calc , text="*", command=lambda: add_to_calc("*"), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_multiply.grid(row=4, column=4)
btn_divide = tk.Button(vaib_calc , text="/", command=lambda: add_to_calc("/"), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_divide.grid(row=5, column=4)
btn_bracOpen = tk.Button(vaib_calc , text="(", command=lambda: add_to_calc("("), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_bracOpen.grid(row=5, column=1)
btn_bracClose = tk.Button(vaib_calc , text=")", command=lambda: add_to_calc(")"), width=5,font=("Arial" ,14),bg='black',fg='white')
btn_bracClose.grid(row=5, column=3)
btn_equal = tk.Button(vaib_calc , text="=", command=evaluate_calc , width=11,font=("Arial" ,14),bg='black',fg='white')
btn_equal.grid(row=6, column=1, columnspan=2)
btn_clr = tk.Button(vaib_calc , text="Clear", command=clear_field , width=11,font=("Arial" ,14),bg='black',fg='white')
btn_clr.grid(row=6, column=3, columnspan=2)

vaib_calc.mainloop()