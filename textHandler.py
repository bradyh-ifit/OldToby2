import logging
import tkinter as tk


# create logger connected to the root logger
class TextHandler(logging.Handler):
    """Allows tkinter to log scrolltext"""

    def __init__(self, text):
        logging.Handler.__init__(self)
        self.text = text
    
    def emit(self, record):
        msg = self.format(record)


        #def append():
        self.text.insert(tk.END, f'{msg}\n')
        #Autoscroll to the bottom of text
        self.text.yview(tk.END)

        #self.text.after(0, append)
        #self.flush