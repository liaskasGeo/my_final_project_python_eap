#Python code for Detect and Handle Window Close Button Event in tkinter/ttkbootstrap
import ttkbootstrap as ttkb
def custom_exit_handler():
    print ('You Clicked Exit Button')
    #add custom code here
    root.destroy()
root = ttkb.Window(themename = 'litera')
root.geometry('400x900')                # widthxheight
root.title('My ttkbootstrap Window')
root.protocol("WM_DELETE_WINDOW", custom_exit_handler)
root.mainloop()