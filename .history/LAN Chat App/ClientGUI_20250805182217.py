import sys
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from UserLogic import User
from ClientLogic import Client

def main():
    username = input('Enter Username ')
    password = input('Enter Password ')
    CurrentUser = User(username, password)

    root = Tk()
    root.Title('Client')
    root.geometry('600x800')

    def showMessage(msg):
        message_display
