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
# frame.pack()

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

# listbox update
def changeListbox():
    listbox.delete(0,END)
    for Harvest in allHarvests:
        listbox.insert("end","{},{},{}".format(Harvest.name,Harvest.howMuch,Harvest.VegOrFruit))
    for i in allHarvests:
        if type(i) is Harvest:
            listbox.insert(("end","{},{},{}".format(Harvest.name, Harvest.howMuch, Harvest.VegOrFruit),"nav ābols"))
        if type(i) is Apple:
            listbox.insert(("end","{},{},{}".format(Apple.name, Apple.howMuch, Apple.appleBreed),"ābols"))


# create Object button
def createHarvestClicked():
    daudzums = howMuch.get()
    whatType = VegOrFruit.get()
    whatName = name.get()
    whatBreed = breed.get()
    if whatBreed != "":
        allHarvests.append(Apple(whatName,daudzums,whatBreed))
    else:
        allHarvests.append(Harvest(whatType, whatName, daudzums))
    
    changeListbox()

harvestButton = ttk.Button(frame, text="Izveidot ražu")
harvestButton.grid(column=4, row=0, sticky="E", **options)
harvestButton.configure(command=createHarvestClicked)

listOfHarvests = tk.Variable(value=tuple(allHarvests))

listbox = tk.Listbox(
    root,
    listvariable=listOfHarvests,
    height=6,
    selectmode=tk.EXTENDED
)

listbox.grid(row=4, columnspan=3, **options)


# add padding to the frame and show it
frame.grid(padx=10, pady=10)

def on_select(event):
    selected_indices = listbox.curselection()
    if len(selected_indices) == 2:
        selected_items = [listbox.get(index) for index in selected_indices]
        global merge_button
        merge_button["state"] = "normal"  # Enable the merge button
    
def on_merge():
    selected_indices = listbox.curselection()
    if len(selected_indices) == 2:
        selected_items = [listbox.get(index) for index in selected_indices]
        new_item = " ".join(selected_items)
        listbox.delete(*selected_indices)
        listbox.insert(("ievārījums"))
        merge_button["state"] = "disabled"  # Disable the merge button

listbox.bind("<<ListboxSelect>>", on_select)

# Create the merge button
merge_button = tk.Button(root, text="savienot divus itemus listboksā", command=on_merge, state="disabled")
merge_button.grid()
    
    

# Start the loop
root.mainloop()