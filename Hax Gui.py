from tkinter import *
import sys
import os
try:
    import keyboard
except ImportError:
    print ("ayo imma try get the keyboard ting dw fam")
    os.system("python -m pip install keyboard")

import tkinter as tk
import keyboard
import time

def rick():
    keyboard.press_and_release('win + r')
    time.sleep(1)
    keyboard.write('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    keyboard.press_and_release('enter')
    time.sleep(2)
    keyboard.press_and_release('f')

def dog():
    keyboard.press_and_release('win + r')
    time.sleep(1)
    keyboard.write('https://www.youtube.com/watch?v=LG713y9_E08')
    keyboard.press_and_release('enter')
    time.sleep(2)
    keyboard.press_and_release('f')

def shutdown():
    keyboard.press_and_release('win + r')
    time.sleep(1)
    keyboard.write('shutdown -s -c "Night!" -t 120')
    keyboard.press_and_release('enter')

def abortShutdown():
    keyboard.press_and_release('win + r')
    time.sleep(1)
    keyboard.write('shutdown -a')
    keyboard.press_and_release('enter')

def fakeUpdate():
    keyboard.press_and_release('win + r')
    time.sleep(1)
    keyboard.write('http://fakeupdate.net/win10/index.html')
    keyboard.press_and_release('enter')
    time.sleep(1)
    keyboard.press_and_release('F11')

def hotdog():
    keyboard.press_and_release('win + r')
    keyboard.write('http://s3.amazonaws.com/rapgenius/hotdog.jpg')

def Cancel():
    window.destroy()

def command1(event):
    if entry1.get() == 'admin' and entry2.get() == 'p4ssword' or entry1.get() == 'NewUser' and entry2.get() == 'NewPass':
        window.deiconify()
        top.destroy()

def command2():
    top.destroy()
    window.destroy()
    sys.exit()

window = Tk()
top = Toplevel()

top.geometry('300x260')
top.attributes("-alpha",0.75)
top.title('LOGIN SCREEN')
top.configure(background='black')
lbl0 = Label(top, text="Hobbson's Hax",bg='black',fg='lime',font=('Comic Sans MS',30))
lbl1 = Label(top, text='Username:',bg='black',fg='lime',font=('Helvetica',10))
entry1 = Entry(top,bg='black',fg='lime',)
lbl2 = Label(top, text='Password:',bg='black',fg='lime',font=('Helvetica',10))
entry2 = Entry(top,show="*",bg='black',fg='lime')
button2 = Button(top, text='Cancel',bg='black',fg='lime',command=lambda:command2())
entry1.config(insertbackground="white")
entry2.config(insertbackground="white")
lbl3 = Label(top, text="Copyright Hobbson's Hax 2021",bg='black',fg='lime', font=('Arial',7))

entry2.bind('<Return>',command1)


lbl0.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()
lbl3.pack()

window.configure(bg="black")
window.title("Hax Gui")
window.attributes("-alpha",0.75)
window.attributes('-topmost', 1)
#topstuff-----------------------------------------------------
hello = tk.Label(text="wagwan my drilla", fg="Cyan",bg="black",width=30,height=5)
hello.grid(row=0, column=1)
rickroll = tk.Button(text="clikqe for rikque",width=20,height=5,fg="lime",bg="black",command=rick)
rickroll.grid(row=1, column=0)
shutyDownBoi = tk.Button(text="clikqe for Shutdown(2 mins)",width=20,height=5,fg="lime",bg="black",command=shutdown)
shutyDownBoi.grid(row=2, column=0)
antiShutyDownBoi = tk.Button(text="clikqe for AntiShutdown",width=20,height=5,fg="lime",bg="black",command=abortShutdown)
antiShutyDownBoi.grid(row=2, column=1)
fakeyUpdateBoi = tk.Button(text="clikqe for fakeUpdate.exe",width=20,height=5,fg="lime",bg="black",command=fakeUpdate)
fakeyUpdateBoi.grid(row=1, column=1)
dogEahhh = tk.Button(text="clikqe EAHHGg",width=20,height=5,fg="lime",bg="black",command=dog)
dogEahhh.grid(row=1,column=2)
cancel = tk.Button(text="Exit",width=20,height=5,fg="Crimson",bg="black",command=Cancel)
cancel.grid(row=2,column=2)
#end stuff----------------------------------------------------
window.withdraw()
window.mainloop()