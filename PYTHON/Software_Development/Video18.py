from tkinter import *
root = Tk()
root.geometry('655x444')
root.title('CodeWithHarry - Title Of my GUI')
# root.wm_iconbitmap('.ico_file')
root.config(background='light blue')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f'{width}x{height}')
Button(text='Close', command=root.destroy).pack()
root.mainloop()