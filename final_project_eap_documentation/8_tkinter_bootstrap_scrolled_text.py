import ttkbootstrap as ttkb
from tkinter import *
from ttkbootstrap.widgets.scrolled import ScrolledText

root = ttkb.Window(themename = 'litera')
root.geometry('400x200')                # widthxheight

# Define the font family and font size
font_family = 'Comic Sans MS'
font_size = 25
my_text = ScrolledText(root,height = 10,width = 100,wrap = WORD,autohide = True,font=(font_family, font_size))
my_text.insert(END,f'Type after this in Comic Sans font: \n')# add text
my_text.pack(pady = 20,padx =20)

root.mainloop()

