from tkinter import *
import tkinter.messagebox as tmsg

def b1function():
    tmsg.showinfo('Setup Wizard','The installation was sucsessfull !')
def b2function():
    tmsg.showerror('Setup Wizard','The installation process was cancled.')
root = Tk()
root.geometry('550x400')
root.minsize(550,400)
root.maxsize(550,400)
root.title('THE GAMING PROJECT SETUP WIZARD')
img = PhotoImage(file='i2.png')
root.iconphoto(False,img)
#Variabels
texts = 'WELCOME TO THE INSTALLATION SETUP WIZARD\nPLEASE GO THROUGH TO OUR PRIVACY\nPOLICY,AND THEN INSTALL.TO INSTALL\nPLEASE CLICK ON THE "Install" Button.'
logo = PhotoImage(file='i2.png')
#Labels
title = Label(text='WELCOME TO THE SETUP WIZARD',bg='black',fg='white',width=100,font=('bold',10),height=4)
title.pack()
f1 = Frame(root,padx=30,pady=100)
f1.pack(side=LEFT,anchor=NW)
main_text = Label(f1,text=texts,font=('bold',10))
main_text.pack()
logoimg = Label(image=logo,bg='black',borderwidth=5,relief=SUNKEN)
logoimg.pack(pady=100)
btn1 = Button(text='Install',width=10,command=b1function)
btn1.pack(side=LEFT,anchor=SE)
btn2 = Button(text='Cancle',width=10,command=b2function)
btn2.pack(side=RIGHT,anchor=SE,)
yourmenu = Menu(root)
m1 = Menu(yourmenu)
m1.add_command(label='GTA V')
m1.add_command(label='FORTNITE')
m1.add_command(label='PUBG')
yourmenu.add_cascade(label='Help',menu=m1)
yourmenu.add_cascade(label='About-us',menu=m1)
root.config(menu=yourmenu)
root.mainloop()