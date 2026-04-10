import tkinter as tk
root=tk.Tk()
root.geometry("800x500")
b1=tk.Button(root,
             text="click here",
             font=("Arial",25),
             bg="black",
             fg="red")
b1.pack(pady=50)
root.mainloop()