import tkinter as tk
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *
import random

os.chdir('C:\\Users\\Naman\\Desktop\\Coding\\python\\Projects')


class Hangman:
    window = Tk()
    mainmenu = Menu(window)
    window.title('Hangman')
    window.geometry('200x200')

    def __init__(self):
        random_number = random.randint(0,853)
        __file = open('Hangman_Words.txt')
        read_word = __file.readlines()
        self.act_word = read_word[random_number].lower()
        self.ls_labels=[]
        for i in range(len(self.act_word)-1):
            li = Label(self.window,text = '_')
            li.grid(column=i,row=1)
            li.config(font= ("Helvetica",20))
            self.ls_labels.append(li)
        self.ls = list(self.act_word)
        self.score_label = Label(self.window, text=6,font=('Helvetica',20))
        self.score_label.grid(column = 1,row = 7)
        self.score = self.score_label['text']
        self.tot_score = 0

    def chk_win(self):
        if self.score == 0:
            c = "You have lost. The correct answer was: "+self.act_word
            tk.messagebox.showinfo("Hangman",c)
            res = tk.messagebox.askyesno('Hangman','Do you want to play again')
            if res == True:
                self.window.destroy()
                os.system('Hangman.py')
            elif res ==False:
                self.window.destroy()
        elif self.tot_score == len(self.ls)-1:
            tk.messagebox.showinfo("Hangman","You have won")
            res = tk.messagebox.askyesno('Hangman','Do you want to play again')
            if res == True:
                self.window.destroy()
                os.system('Hangman.py')
            elif res ==False:
                self.window.destroy()
    def keydown(self,e):
        temp = []
        if e.char in self.ls:
            for i in range(0,len(self.ls)):
                if  e.char == self.ls[i]:
                    temp.append(i)

            for i in range(0,len(temp)):
                self.ls_labels[temp[i]].config(text=e.char)
            self.tot_score += len(temp)
        else:
            self.score -= 1
            self.score_label.config(text=self.score)
        self.chk_win()

    def run(self):
        self.window.config(menu = self.mainmenu)
        self.window.bind("<KeyPress>",self.keydown)
        self.window.mainloop()


hm = Hangman()
hm.run()
