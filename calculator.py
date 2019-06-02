from tkinter import *
import tkinter as tk
from tkinter import messagebox
mainWindow=tk.Tk()
mainWindow.geometry("600x700+0+0")
mainWindow.title("Calculator")
heading_label=tk.Label(mainWindow,font=("arial",20,'bold'),text="enter first number" ,pady=(10),padx=(20))
heading_label.pack()
name_field=tk.Entry(mainWindow,font=("arial",20,'bold'))
name_field.pack()
heading_label2=tk.Label(mainWindow,font=("arial",20,'bold'),text="enter second number",pady=(10),padx=(20))
heading_label2.pack()
name_field2=tk.Entry(mainWindow,font=("arial",20,'bold'))
name_field2.pack()
button=tk.Button(mainWindow,font=("arial",20,'bold'),text="Add",command=lambda: addition())
button.pack()
button=tk.Button(mainWindow,font=("arial",20,'bold'),text="Subtract",command=lambda: subtraction())
button.pack()
button=tk.Button(mainWindow,font=("arial",20,'bold'),text="Multiply",command=lambda: multiplication())
button.pack()
button=tk.Button(mainWindow,font=("arial",20,'bold'),text="Division",command=lambda: division())
button.pack()
button=tk.Button(mainWindow,font=("arial",20,'bold'),text="Reset",command=lambda: clear())
button.pack()
result_label=tk.Label(mainWindow,font=("arial",20,'bold'),text="operation result is:",padx=(20),pady=(10))
result_label.pack()
def clear():
    name_field.delete(0,END)
    name_field2.delete(0, END)
def addition():
    first=int(name_field.get())
    second=int(name_field2.get())
    result=first+second
    print("result is:",result)
    result_label.config(text="operation is:"+ str(result))
def subtraction():
    first=int(name_field.get())
    second=int(name_field2.get())
    result=first-second

    print("result is:",result)
    result_label.config(text="operation is:"+ str(result))
def multiplication():
    first=int(name_field.get())
    second=int(name_field2.get())
    result=first*second
    print("result is:",result)
    result_label.config(text="operation is:"+ str(result))
def division():
    first=int(name_field.get())
    second=int(name_field2.get())
    # result=first/second
    # print("result is:",result)
    # result_label.config(text="operation is:"+ str(result))
    try:
        result = first / second
        print('division result is:', result)
        result_label.config(text="operation is:" + str(result))
    except ZeroDivisionError:

        messagebox.showerror(ZeroDivisionError,"division by zero")

mainWindow.mainloop()