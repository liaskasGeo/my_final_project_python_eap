# Creating and Using Entry Box Widget in tkinter/ttkbootstrap
# ttkbootstrap Entry Widget
import ttkbootstrap as ttkb

def button_1_handler():
    print(f'You Typed in {My_Entry.get()}')

root = ttkb.Window(themename='superhero')  # theme = superhero
root.geometry('350x150')

# Create Entry Widget
My_Entry = ttkb.Entry()
My_Entry.insert(0, '')
My_Entry.pack(pady=20)

# Create Button
button_1 = ttkb.Button(text='Click Me', command=button_1_handler)
button_1.pack()
root.mainloop()





