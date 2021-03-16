from tkinter import *
import time
from random import randint
#window
tkWindow = Tk()  
tkWindow.geometry('1150x700')  
tkWindow.title('Cake shop customer page')
#welcome to cake shop
usernameLabel = Label(tkWindow, text="CAKE SHOP",font ="times 18 bold").grid(row=3, column=8)
