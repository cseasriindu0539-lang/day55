import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator
root=tk.Tk()
root.geometry("650x500")
root.title("language translatoor")
lang={
    "telugu":"te",
    "hindi":"hi",
    "tamil":"ta",
    "kannada":"ka",
    "malayalam":"ml"
}
l1=tk.Label(root,text="LANGUAGE TRANSLATOR",font=("Arial",35,"bold"))
l1.pack(pady=30)
l2=tk.Label(root,text="Enter text to convert !",font=("Arial",15))
l2.pack()
input_text=tk.Text(root,height=6,width=60)
input_text.pack(pady=10)
l3=tk.Label(root,text="select target language to convert",font=("Arial",15))
l3.pack(pady=13)
combo=ttk.Combobox(root,values=list(lang.keys()),width=25)
combo.pack(pady=8)
def translator():
    text=input_text.get("1.0",tk.END)
    dst=combo.get()
    gt=GoogleTranslator(source="auto",target=lang[dst])
    result=gt.translate(text)
    output.delete("1.0",tk.END)
    output.insert(tk.END,result)
btn=tk.Button(root,text="translate",
              font=("Arial",13,"bold"),
              bg="green",fg="white",command=translator)
btn.pack(pady=10)
output=tk.Text(root,height=5,width=60)
output.pack()
root.mainloop()