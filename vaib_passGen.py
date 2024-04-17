import tkinter as Tk
from tkinter import *
import string
import random
import pyperclip


def passgen():
    sletter=string.ascii_lowercase
    cletter=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    sum=sletter+cletter+numbers+special_charecters
    passlen=int(spinboxlen.get())

    if complexitychoice.get()==1:
        passfield.insert(0,random.sample(sletter,passlen))

    if complexitychoice.get()==2:
        passfield.insert(0,random.sample(sletter+cletter,passlen))

    if complexitychoice.get()==3:
        passfield.insert(0,random.sample(sum,passlen))

def copy():
    randompass=passfield.get()
    pyperclip.copy(randompass)

vaib_passgen=Tk()
vaib_passgen.geometry('280x400+700+330')
vaib_passgen.config(bg='navy blue')
complexitychoice=IntVar()
passlabel=Label(vaib_passgen,text="Vaib's PassGen",font=('Arial',18,'bold'),bg='orange',fg='white')
passlabel.grid(pady=10)

complexity1=Radiobutton(vaib_passgen,text='Weak',value=1,variable=complexitychoice,font=("Arial" ,14))
complexity1.grid(pady=5)

complexity2=Radiobutton(vaib_passgen,text='Medium',value=2,variable=complexitychoice,font=("Arial" ,14))
complexity2.grid(pady=5)

complexity3=Radiobutton(vaib_passgen,text='Strong',value=3,variable=complexitychoice,font=("Arial" ,14))
complexity3.grid(pady=5)

passlen=Label(vaib_passgen,text='Maximum password length is 20',font =("Arial" ,14),bg='green',fg='white')
passlen.grid(pady=5)

spinboxlen=Spinbox(vaib_passgen,buttonbackground='black' ,background ='black',fg='white' ,from_=5,to_=20,width=5,font=("Arial" ,14))
spinboxlen.grid(pady=5)

generate=Button(vaib_passgen,text='Generate',font=("Arial" ,14),command=passgen)
generate.grid(pady=5)

passfield=Entry(vaib_passgen,width=25,bd=2,font=("Arial" ,14))
passfield.grid()

coppybtn=Button(vaib_passgen,text='Copy',font=("Arial" ,14),command=copy)
coppybtn.grid(pady=5)

vaib_passgen.mainloop()