from tkinter import *
import random
import time
import tkinter.font as tkFont

window = Tk()
window.title('Dice')
window.geometry('500x500')
ls = [1,2,3,4,5,6]
helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
lb_font= tkFont.Font(size=18,weight=tkFont.BOLD)
def but_click():
    global button0
    for i in range(0,15):
        button0.configure(text=random.choice(ls))
        window.update()
        time.sleep(0.1)
    lb.configure(text=button0['text'])

button0 = Button(window, text='1', height=5, width=10,bg= 'red',fg='white', command=but_click, relief=RAISED,font=helv36)
button0.pack(side=TOP)
lb = Label(window,text='click button to get a number',font=lb_font)
lb.pack(side=BOTTOM)
window.mainloop()
