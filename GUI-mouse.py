# GUI-mouse.py
from tkinter import * # Lip: TK Interface
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title('โปรแกรมสั่งกดปฎิทินมั่ง')
GUI.geometry('500x300')

def Calendar():
    pg.click(1500,900)


B1 = Button(GUI,text='Calendar1',command=Calendar)
B1.pack(ipadx=20, ipady=10 )

B2 = ttk.Button(GUI,text='Calendar2',command=Calendar)
B2.pack(ipadx=20, ipady=10 )

def Google():
    webbrowser.open('http://www.google.com')


B3 = ttk.Button(GUI,text='Google.com',command=Google)
B3.pack(ipadx=20, ipady=10)

GUI.mainloop()

