import tkinter as tk

#fonction d'execution.
def solve():
    var=tk.StringVar()
    label=tk.Label(root, textvariable=var, relief='raised')
    var.set('hello tkinter univers!')
    label.pack(padx=10, pady=10)


root=tk.Tk()
button=tk.Button(root, text='press',command=solve)
button.pack()

root.mainloop()