from tkinter import *

welcome_w = Tk() #instatiate an instance of a window

photo = PhotoImage(file='bread.png')
welcome_w.geometry("420x420")
welcome_w.title("Geo-San Bakery")
icon = PhotoImage(file='bread.png')
welcome_w.iconphoto(True, icon)
welcome_w.config(background="#dec787")


label = Label(master=welcome_w,
              text="Hello!",
              font=('Times New Roman', 40, 'bold'),
              fg='#b56c36',
              bg='white',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack(fill=BOTH, expand=True)
#label.place(x=10, y=10)

welcome_w.mainloop() #place window on computer screen, listen for events

