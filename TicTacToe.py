from tkinter import *
import tkinter.messagebox
from random import choice

tk = Tk()
tk.title("TicTacToe")

btns = []
bclick = True
win_check = 0
flag=0

def win_check():
    if (btns[0]['text']==btns[1]['text']==btns[2]['text'] == 'X' or
        btns[3]['text']==btns[4]['text']==btns[5]['text'] == 'X' or
        btns[6]['text']==btns[7]['text']==btns[8]['text'] == 'X' or
        btns[0]['text']==btns[4]['text']==btns[8]['text'] == 'X' or
        btns[2]['text']==btns[4]['text']==btns[6]['text'] == 'X' or
        btns[0]['text']==btns[3]['text']==btns[6]['text'] == 'X' or
        btns[1]['text']==btns[4]['text']==btns[7]['text'] == 'X' or
        btns[2]['text']==btns[5]['text']==btns[8]['text'] == 'X'):
        tkinter.messagebox.showinfo("TicTacToe",'Player Wins')
        tk.destroy()
    elif (btns[0]['text']==btns[1]['text']==btns[2]['text'] == '0' or
        btns[3]['text']==btns[4]['text']==btns[5]['text'] == '0' or
        btns[6]['text']==btns[7]['text']==btns[8]['text'] == '0' or
        btns[0]['text']==btns[4]['text']==btns[8]['text'] == '0' or
        btns[2]['text']==btns[4]['text']==btns[6]['text'] == '0' or
        btns[0]['text']==btns[3]['text']==btns[6]['text'] == '0' or
        btns[1]['text']==btns[4]['text']==btns[7]['text'] == '0' or
        btns[2]['text']==btns[5]['text']==btns[8]['text'] == '0'):
        tkinter.messagebox.showinfo("TicTacToe",'Computer Wins')
        tk.destroy()
    elif flag == 9:
        tkinter.messagebox.showinfo("TicTacToe","It's a tie")
        tk.destroy()
def but_click(i):
    global bclick,flag
    if btns[i]['text'] =='' and bclick == True:
        btns[i].configure(text='X')
        bclick = False
        ls.remove(i)
        flag+=1
        win_check()
    if bclick == False:
        temp = choice([i for i in range(0,9) if i in ls])
        btns[temp].configure(text='0')
        bclick = True
        ls.remove(temp)
        flag+=1
        win_check()

for i in range(0,9):
    btns.append(Button(font=('Times 20 bold'), bg='white', text='',fg='black', height=2, width=4,command=lambda i=i: but_click(i)))
rows = 0
columns = 0
index = 1
ls = [0,1,2,3,4,5,6,7,8]
for i in btns:

    i.grid(row=rows, column=columns)
    columns += 1
    if index % 3 == 0:
        rows += 1
        columns = 0
    index += 1
tk.mainloop()
