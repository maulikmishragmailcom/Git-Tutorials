from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename 
import os
from django.contrib.sessions.backends import file
def newfile():
    global file
    root.title('Untitled - Notepad')
    file = None
    TextArea.delete(1.0, END)
def openfile():
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if file=='':
        file=None
    else:
        root.title(os.path.basename(file) + '- Notepad')
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),                             ("Text Documents", "*.txt")])
        if file=="":
            file=None
        else:
            #Save as a new file
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename((file) + '- Notepad'))
            tmsg.showinfo('File', 'File Saved Successfuly')
    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
     TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    tmsg.showinfo('About - Notepad', 'This Notepad is by Maulik Mishra')
if __name__ == '__main__':
    root = Tk()
    root.title('Unitled - Notepad')
    # root.wm_iconbitmap('notepad.ico')
    root.geometry('788x644')
    #Add textarea
    TextArea = Text(root, font='lucida 13')
    file = None
    TextArea.pack(expand=True,fill=BOTH)
    

    #Lets Create a Menubar
    MenuBar = Menu(root)
    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    #To open new file
    FileMenu.add_command(label='New', command=newfile)

    #To open  already existing file
    FileMenu.add_command(label='Open', command=openfile)
    
    #To save the current file
    FileMenu.add_command(label='Save', command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label='Exit', command=quitApp)
    MenuBar.add_cascade(label='File', menu=FileMenu)
    #File Menu Ends
    

    #Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label='Cut', command=cut)
    EditMenu.add_command(label='Copy', command=copy)
    EditMenu.add_command(label='Paste', command=paste)

    MenuBar.add_cascade(label='Edit', menu=EditMenu)
    # EditMenu.config(menu=MenuBar)
    #Edit Menu Ends

    #Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label='About Notepad', command=about)
    MenuBar.add_cascade(label='Help', menu=HelpMenu)
    
    root.config(menu=MenuBar)

    #Help Menu Ends

    #Adding Scrollbar using rules from Tkinter lecture 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()
