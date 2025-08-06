import sys
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from UserLogic import User
from ClientLogic import Client

username = input('Enter Username')
password = input('Enter password')


CurrentUser = User(username,password)
    ClientInstance = Client(CurrentUser)

root = Tk()
root.title("Client")
root.geometry("600x800")


main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


message_display = scrolledtext.ScrolledText(main_frame, width=50, height=40, state='disabled')
message_display.pack(pady=10)

root.mainloop()
