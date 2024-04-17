import tkinter as tk
from tkinter import messagebox

vaib_ToDo = tk.Tk()
vaib_ToDo.geometry('850x650+700+330')
vaib_ToDo.title("Vaibhav's To Do List")
vaib_ToDo.config(bg='#FFA500')
vaib_ToDo.resizable(width=True, height=True)

def add_task():
    task = my_task_entry.get()
    if task != "":
        my_list.insert(tk.END, task)
        my_task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('There is no task, please enter some!')

def delete_task():
    if my_list.curselection():
        my_list.delete(tk.ANCHOR)
    else:
        messagebox.showwarning("Atleast select one to delete!")

disp_field = tk.Message( vaib_ToDo,font=('Arial', 20 ), width= 500 ,text='Enter Your Task Using Add Button',bg='#000000', fg='#FFFFFF')
disp_field.pack(pady=20)

box = tk.Frame(vaib_ToDo)
box.pack(pady=10)

display_list = tk.Listbox(box, width=1,height=1,font=('Arial', 20),bd=0,fg='#000000',selectbackground='#ff4122',activestyle="none")
display_list.pack(side=tk.LEFT, fill=tk.BOTH)

my_list = tk.Listbox(box, width=30,height=10,font=('Arial', 20),bd=0,fg='#000000',bg='#808080',selectbackground='#ff4122',activestyle="none")
my_list.pack(side=tk.LEFT, fill=tk.BOTH)

task_list = []
for item in task_list:
    my_list.insert(tk.END, item)

my_scrollbar = tk.Scrollbar(box)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview ,troughcolor='Black')

my_task_entry = tk.Entry( vaib_ToDo,font=('Arial', 24))
my_task_entry.pack(pady=20)

button_box = tk.Frame(vaib_ToDo)
button_box.pack(pady=20)

add_task_btn = tk.Button(button_box,text='Add',font=('Arial 14'),bg='#87CEEB',padx=20,pady=15,command=add_task)
add_task_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

del_task_btn = tk.Button(button_box,text='Delete',font=('Arial 14'),bg='#ff4122',padx=20,pady=10,command=delete_task)
del_task_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

vaib_ToDo.mainloop()