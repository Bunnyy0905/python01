from tkinter import *
root=Tk()
root.geometry("500x400")
mainmenu=Menu(root)

m1=Menu(mainmenu)
m1.add_command(label="Home")#add_command-->used to add options under the menus(i.e.adding submenus)
m1.add_command(label="New")
m1.add_command(label="Open")
m1.add_separator()#used to add line between the sub-menus
m1.add_command(label="Info")
m1.add_command(label="Save")
m1.add_command(label="Save As")
m1.add_command(label="Exit", command=root.quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)#add_cascade--> used to show the options(i.e.menus) horizontally

m2=Menu(mainmenu,tearoff=0) 
m2.add_command(label="Copy")
m2.add_command(label="Cut")
m2.add_command(label="Paste")
m2.add_separator()
m2.add_command(label="Format Painter")
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Home", menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Pictures")
m3.add_command(label="Shapes")
m3.add_command(label="Icons")
m3.add_command(label="Chart")
m3.add_command(label="ScreenShot")
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Insert", menu=m3)

root.mainloop()