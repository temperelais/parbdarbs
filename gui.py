from apples import Harvest, Apple
import tkinter as tk
from tkinter import ttk, END
from tkinter import *

# programas izskats

root = tk.Tk()
root.title("Auglu un darzenu skaititajs")
root.geometry("500x300")

frame = ttk.Frame(root)

# field options

options = {'padx':5,'pady': 5}

# vegOrFruit label
vegOrFruit_label = ttk.Label(frame, text="Dārzenis vai Auglis?")
vegOrFruit_label.grid(column=2, row=2, sticky="e", **options)

# vegOrFruit Radiobox

var = tk.StringVar()
def resultOfRadBox():
    print(var.get())

theRadButtons =(tk.Radiobutton(root, text="Produkts ir auglis", variable=var, value="fruit", command=resultOfRadBox),
                tk.Radiobutton(root, text="Produkts ir dārzenis", variable=var, value="vegetable", command=resultOfRadBox))
count =1
for i in theRadButtons:
    i.grid(column=1,row=count,**options)
    count+=1

# 







# start the loop
root.mainloop()

