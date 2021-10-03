from tkinter import *

root = Tk()
root.title("Screen Resolution Detecter")
root.geometry('500x400')
root.resizable(width=False, height=False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

lbl1 = Label(text="Your screen resolution is: ", pady=100, padx=100).pack()

lbl2 = Label(text=str(screen_width) + " x " + str(screen_height), font=(90), borderwidth=1, relief='solid', padx=10, pady=10).pack() # format the integers into strings

root.mainloop()