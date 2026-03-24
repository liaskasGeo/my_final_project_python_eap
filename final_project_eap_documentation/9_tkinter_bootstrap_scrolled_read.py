# Read the input text from ScrolledText box
"""
    You can also read the text written inside the ScrolledText box and use it as a input entry box
    this helpful when you have to take in a large volume of text .

    The first part, '1.0' means that the input should be read from line one, character zero (ie: the very first character).
    END is an imported constant which is set to the string "end".
    The END part means to read until the end of the text box is reached.
    The only issue with this is that it actually adds a newline to our input. So, in order to fix it we should change END to end-1c.
    The -1c deletes 1 character, while -2c would mean delete two characters, and so on.
"""
from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap.widgets.scrolled import ScrolledText
import tkinter as tk


def button_1_handler():
    text = my_text.get('1.0', END)  # get all the text from the ScrolledText widget
    print(text)


root = ttkb.Window(themename='superhero')  # theme = superhero
root.geometry('800x500')
my_text = ScrolledText(root, height=10, width=100, wrap=WORD, autohide=True)
my_text.pack(pady=20)
# create button
button_1 = ttkb.Button(text='Read All Text', command=button_1_handler).pack(pady=20)
root.mainloop()