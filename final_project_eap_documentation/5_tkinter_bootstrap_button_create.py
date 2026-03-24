import ttkbootstrap
import ttkbootstrap as ttkb

def button_1_handler():
   print('You Clicked Me')

root = ttkb.Window(themename = 'litera')
root.geometry('400x200')                # widthxheight

#Create Button
button_1 = ttkb.Button(text = 'Click Me',command = button_1_handler)
button_1.place(x=20,y=20)
root.mainloop()


