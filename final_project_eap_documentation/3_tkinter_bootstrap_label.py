import ttkbootstrap as ttkb
root = ttkb.Window(themename = 'litera')
root.geometry('400x400')
My_Label = ttkb.Label(text = "Hello World")
My_Label.place(x=10,y=300)
My_Label.pack()
root.mainloop()