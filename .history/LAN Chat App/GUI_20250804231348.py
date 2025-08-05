import sys
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from Server Logic import Server

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
root.geometry("800x500")

if __name__ == "__main__":
    ServerInstance = Server()

main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

message_display = scrolledtext.ScrolledText(main_frame, width=50, height=15, state='disabled')
message_display.pack(pady=10)

sys.stdout = RedirectConsolToGUI(message_display)
sys.stderr = RedirectConsolToGUI(message_display)

def onStart():
    ServerInstance.initiateMultiThreading()
    message_display.config(state='normal')
    message_display.delete(1.0, 'end')
    message_display.insert('end', 'Server started...\n')
    message_display.config(state='disabled')

startButton = ttk.Button(main_frame, text="Start Server", command=onStart)
startButton.pack()

root.mainloop()
