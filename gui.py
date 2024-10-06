from apples import Harvest, Apple
import tkinter as tk
from tkinter import ttk, END
from tkinter import *

allHarvests = []

# Program appearance
root = tk.Tk()
root.title("Auglu un darzenu skaititajs")
root.geometry("800x800")

# Create the frame
frame = ttk.Frame(root)
frame.pack()

# Field options
options = {'padx': 5, 'pady': 5}

# vegOrFruit label
vegOrFruit_label = ttk.Label(frame, text="Objekts ir Dārzenis vai Auglis?")
vegOrFruit_label.grid(column=0, row=0, sticky="E", **options)

# vegOrFruit Radiobox entry
def sel():
    return str(VegOrFruit.get())

VegOrFruit = tk.StringVar()
VegOrFruitRadiobox1 = ttk.Radiobutton(frame, text="Auglis", variable=VegOrFruit, value="Fruit", command=sel())
VegOrFruitRadiobox2 = ttk.Radiobutton(frame, text="Dārzenis", variable=VegOrFruit, value="vegetable", command=sel())

VegOrFruitRadiobox1.grid(column=0, row=1, sticky="E", **options)
VegOrFruitRadiobox2.grid(column=0, row=2, sticky="E", **options)

# howMuch label
howMuchLabel = ttk.Label(frame, text="Cik daudz ir prece(kilogramos)?")
howMuchLabel.grid(column=1, row=0, sticky="E", **options)

#howMuch entry
howMuch=tk.StringVar()
howMuchEntry = ttk.Entry(frame, textvariable=howMuch)
howMuchEntry.grid(column=1, row=1, **options)
howMuchEntry.focus()

#name label
nameLabel = ttk.Label(frame, text="Kāds ražas nosaukums?")
nameLabel.grid(column=2, row=0, sticky="E", **options)

# name entry
name = tk.StringVar()
nameEntry = ttk.Entry(frame, textvariable=name)
nameEntry.grid(column=2, row=1, **options)

# breed label
breedLabel = ttk.Label(frame, text="Kāda ir sķirne?(ja ābols)")
breedLabel.grid(column=3, row=0, sticky="E", **options)

# breed entry
breed = tk.StringVar()
breedEntry = ttk.Entry(frame, textvariable=breed)
breedEntry.grid(column=3, row=1, **options)

# create Object button
def createHarvestButton():
    daudzums = howMuch.get()
    whatType = VegOrFruit.get()
    whatName = name.get()


# Start the loop
root.mainloop()