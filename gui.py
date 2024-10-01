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
vegOrFruit_label.grid(column=0, row=1, sticky="e", **options)

# vegOrFruit Radiobox
v = StringVar(root, "1")
radValues = {"Produkts ir dārzenis" : "vegetable",
             "Produkts ir auglis " : "fruit"}
for (text, value) in radValues.items():
    Radiobutton(root, text=text, variable=v, value = value).pack(fill = X, ipady= 5)






# start the loop
root.mainloop()

