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
        message_display.configure(state='normal')
        message_display.insert(END, msg + '\n')
        message_display.configure(state='disabled')
        message_display.yview(END)

    client = Client(CurrentUser, message_callback=show_message)

    main_frame = ttk.Frame(root, padding="3 3 12 12")
    main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    global message_display 
    message_display = scrolledtext.ScrolledText(main_frame, width=60, height=30),
    message_display.grid(row=1, column=0, padx=10, pady=5, sticky=W)

    def send_