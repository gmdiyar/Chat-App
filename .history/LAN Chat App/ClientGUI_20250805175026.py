import sys
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from ServerLogic import Server

class RedirectConsolToGUI:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        def append():
            self.text_widget.config(state='normal')
            self.text_widget.insert('end', string)
            self.text_widget.see('end')
            self.text_widget.config(state='disabled')
        self.text_widget.after(0, append)

    def flush(self):
        pass

root = Tk()
root.title("Server")
root.geometry("600x800")

if __name__ == "__main__":
    ServerInstance = Server()

main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


message_display = scrolledtext.ScrolledText(main_frame, width=50, height=40, state='disabled')
message_display.pack(pady=10)

root.mainloop()
