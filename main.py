from tobyGui import *
import logging 
import logging.handlers
from adbConnect import adb_devices
from textHandler import TextHandler

def main():

    root = tk.Tk()
    gui = MyGui(root)


    #create a logger that will be used by all modules using TextHandler
    text_handler = TextHandler(gui.log_window)
    text_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    text_handler.setLevel(logging.INFO)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(text_handler)

    logger.info('Starting Old Toby 2')


    gui.build_gui()

    adb_devices()

    root.mainloop()


main()
