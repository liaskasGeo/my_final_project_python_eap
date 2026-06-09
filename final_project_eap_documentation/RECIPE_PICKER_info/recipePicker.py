import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random


bg_colour = "#3d6466"
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def fetch_db(): #Fetch from database
    connection = sqlite3.connect("data/recipes.db") #establish connection with file
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    idx = random.randint(0, len(all_tables) - 1)  # random between all our tables

    #Fetch ingredients
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()
    return table_name, table_records

def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])


    ingredients = []

    #Ingredients
    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingredients.append(qty + " " + unit + " of " + name)

    return title, ingredients


def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise() #stacks one frame above the other
    frame1.pack_propagate(False)  # Prevents child element modifying the parent element.
    # logo widget
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")  # URL of image (load photo)
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)  # creates label in frame1 ,dispays image
    logo_widget.image = logo_img  # We need to specify that,otherwise image might not appear
    logo_widget.pack()  # displays and puts widget to GUI

    tk.Label(  # text inside
        frame1,
        text="ready for your random recipe?",
        bg=bg_colour,
        fg="white",
        font=("TkMenuFont", 14)
    ).pack()

    # button widget
    tk.Button(  # Button named SHUFFLE with interaction
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        # clear space between an element's actual content(pady) #pack organizing elements inside frame
        command=lambda: load_frame2()).pack(pady=20)  # function interaction

def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()#stacks one frame above the other
    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)

    # logo widget
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo_bottom.png")  # URL of image (load photo)
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)  # creates label in frame1 ,dispays image
    logo_widget.image = logo_img  # We need to specify that,otherwise image might not appear
    logo_widget.pack(pady=20)  # displays and puts widget to GUI

    tk.Label(  # text inside
        frame2,
        text=title,
        bg=bg_colour,
        fg="white",
        font=("TkHeadingFont", 20)
    ).pack(pady=25)

    for i in ingredients:
        tk.Label(  # text inside
            frame2,
            text=i,
            bg="#28393a",
            fg="white",
            font=("TkMenuFont", 14)
        ).pack(fill="both") #fills the bg colour right  / left

    tk.Button(  # Button named SHUFFLE with interaction
        frame2,
        text="BACK",
        font=("TkHeadingFont", 18),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        # clear space between an element's actual content(pady) #pack organizing elements inside frame
        command=lambda: load_frame1()
        ).pack(pady=20)  # function interaction

# initiallize app tkinter GUI
root = tk.Tk()
root.title("Recipe Picker") # Giving a titleto App
root.eval("tk::PlaceWindow . center") #places app at the center when launched

# create a frame widget
frame1 = tk.Frame(root,width=500,height=600,bg=bg_colour) #size and background color
frame2 = tk.Frame(root, bg=bg_colour)
frame1.grid(row=0,column=0) # Default values
frame2.grid(row=0,column=0)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0,sticky="nesw")  # Default values row = 0 , column = 0 , sticky = north east south west stick to all corners


load_frame1() #load function ,otherwise it doesnt show anything

# run app
root.mainloop() # runs until you press x to close