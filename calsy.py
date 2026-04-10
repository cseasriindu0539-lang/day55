import tkinter as tk
root=tk.Tk()
root.geometry("800x500")

num1=tk.Label(root,text="enter first number")
l1=tk.Entry(root)
num1.place(x=50,y=50)
l1.place(x=250,y=50)


num2=tk.Label(root,text="enter first number")
num2.place(x=50,y=100)
l2=tk.Entry(root)
l2.place(x=250,y=100)


def add():
    a=float(l1.get())
    b=float(l2.get())
    sum=a+b
    anss.config(text=sum)


b1=tk.Button(root,text="add",command=add)
b1.place(x=180,y=150)
anss=tk.Label(root,text="ans")
anss.place(x=180,y=200)
root.mainloop()