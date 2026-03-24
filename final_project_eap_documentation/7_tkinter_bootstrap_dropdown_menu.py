# Python tkinter/ttkbootstrap code for Creating and Using Drop Down Combo boxes
#Creating and Using Drop Down Combo boxes in tkinter/ttkbootstrap
import ttkbootstrap as ttkb

#1. Create a list of items that are used to populate the drop down menu.
options = ['Display 720p', 'Display 1024p', 'Display 2160p']  # create Dropdown options

def combobox_selected_handler(e):
    print(e)                                # prints the virtual event
    print(f'You selected {my_combo.get()}') # my_combo.get() get the selected value


root = ttkb.Window(themename='litera')
root.geometry('400x200')  # widthxheight
My_Label = ttkb.Label(text = "Monitors",bootstyle = 'primary',font = ('Helvetica',15)      )
My_Label.place(x=10,y=300)
My_Label.pack()

#Create Combobox You have to pass your drop down items list to the the keyword argument values
my_combo = ttkb.Combobox(values=options)
my_combo.pack(pady=50)
my_combo.current(2)  # set the default value on combobox
my_combo.bind('<<ComboboxSelected>>', combobox_selected_handler)  # bind the combobox
root.mainloop()
