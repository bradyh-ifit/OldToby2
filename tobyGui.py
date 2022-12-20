from asyncio.log import logger
from cgitb import enable
from curses.ascii import EM
from multiprocessing import parent_process
from multiprocessing.resource_sharer import stop
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from typing import List
from tobyList import *
import logging
import threading
from threading import Thread
from testMethods import reset_app
import deviceWindow


class MyGui(tk.Frame):
    log_window = None
    msg_one = None

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.build_gui()

    def build_gui(self):
        #size window and set title

        self.root.geometry('1000x1000')
        self.root.title("Old Toby 2")

        top_frame = Frame(self.root, padx=10, pady=10)
        top_frame.pack()
        my_label = Label(top_frame, text='Old Toby 2 Automation')
        my_label.configure(font=("Terminal", 25, "bold"))
        my_label.pack()

        #Drop Down Menu Frame
        drop_frame = Frame(self.root, padx=10, pady=10)
        drop_frame.pack()
        
        def new_window():
            deviceWindow.new_window(self.root)

        #create a button to add a new device
        add_device_button = Button(drop_frame, text="Add Device", command=new_window)
        add_device_button.grid(row=0, column=2, padx=10, pady=10)

        #Radio Button Menu Frame
        radio_frame = Frame(self.root, padx=10, pady=15)
        radio_frame.pack()

        #Scrolling Text (SHELL) Frame
        text_frame = Frame(self.root, padx=10, pady=15)
        text_frame.pack()

        #Button Selection Frame
        button_frame = Frame(self.root, padx=50, pady=15)
        button_frame.pack()

        #Drop Down Menu Selections
        drop_label = Label(drop_frame, text='Select update versions')
        drop_label.configure(font=("Terminal", 14, "bold", "underline"))
        drop_label.grid(row=1, column=2, pady=25)

        clicked_user = StringVar()
        clicked_user.set("Choose User")

        drop_user = OptionMenu(drop_frame, clicked_user, *options_user)
        drop_user.grid(row=2, column=1, sticky=W, padx=15, pady=10)

        clicked_tablet = StringVar()
        clicked_tablet.set("Choose Tablet")

        drop_tablet = OptionMenu(drop_frame, clicked_tablet, *options_tablet)
        drop_tablet.grid(row=2, column=2, padx=15, pady=10)

        clicked_admin = StringVar()
        clicked_admin.set("Choose Admin")

        drop_admin = OptionMenu(drop_frame, clicked_admin, *options_admin)
        drop_admin.grid(row=2, column=3, sticky=E, padx=15, pady=10)

        clicked_wolf = StringVar()
        clicked_wolf.set("Choose Wolf")

        drop_wolf = OptionMenu(drop_frame, clicked_admin, *options_wolf)
        drop_wolf.grid(row=3, column=1, sticky=W, padx=15, pady=10)

        clicked_launch = StringVar()
        clicked_launch.set("Choose Launcher")

        drop_launch = OptionMenu(drop_frame, clicked_admin, *options_launcher)
        drop_launch.grid(row=3, column=2, padx=15, pady=10)

        clicked_web= StringVar()
        clicked_web.set("Choose Webview")

        drop_web = OptionMenu(drop_frame, clicked_admin, *options_webview)
        drop_web.grid(row=3, column=3, sticky=E, padx=15, pady=10)

        #radio button selections
        radio_label = Label(radio_frame, text='Select Testing Mode')
        radio_label.configure(font=("Terminal", 14, "bold", "underline"))
        radio_label.grid(row=1, column=2, pady=25)

        def check_boxes():
            
            if radio_var.get() != 3:
                check_one.configure(state='disabled')
                check_two.configure(state='disabled')
                check_three.configure(state='disabled')
                check_four.configure(state='disabled')
                check_five.configure(state='disabled')
                check_six.configure(state='disabled')
            else:
                check_one.configure(state='normal')
                check_two.configure(state='normal')
                check_three.configure(state='normal')
                check_four.configure(state='normal')
                check_five.configure(state='normal')
                check_six.configure(state='normal')

        #create a graphical user interface for the radio buttons using tkinter

        radio_var = IntVar()
        radio_var.set(0)

        radio_var1 =IntVar()
        radio_var1.set(1)

        radio_var2 =IntVar()
        radio_var2.set(1)

        radio_var3 =IntVar()
        radio_var3.set(1)

        radio_var4 =IntVar()
        radio_var4.set(1)

        radio_var5 =IntVar()
        radio_var5.set(1)

        radio_var6 =IntVar()
        radio_var6.set(1)

        radio_one = Radiobutton(radio_frame, text="Full Test", variable=radio_var, value=1, command=check_boxes)
        radio_one.grid(row=2, column=1, sticky=W, padx=15, pady=10)

        radio_two = Radiobutton(radio_frame, text="Quick Test", variable=radio_var, value=2, command=check_boxes)
        radio_two.grid(row=2, column=2, padx=15, pady=10)

        radio_three = Radiobutton(radio_frame, text="Custom Test", variable=radio_var, value=3, command=check_boxes)
        radio_three.grid(row=2, column=3, sticky=E, padx=15, pady=10)

        #create check buttons for the custom test
        check_one = Checkbutton(radio_frame, text="Wolf", variable=radio_var1)
        check_one.grid(row=3, column=1, sticky=W, padx=15, pady=10)

        check_two = Checkbutton(radio_frame, text="Admin", variable=radio_var2)
        check_two.grid(row=3, column=2, padx=15, pady=10)

        check_three = Checkbutton(radio_frame, text="Launcher", variable=radio_var3)
        check_three.grid(row=3, column=3, sticky=E, padx=15, pady=10)

        check_four = Checkbutton(radio_frame, text="Webview", variable=radio_var4)
        check_four.grid(row=4, column=1, sticky=W, padx=15, pady=10)

        check_five = Checkbutton(radio_frame, text="Brainboard", variable=radio_var5)
        check_five.grid(row=4, column=2, padx=15, pady=10)

        check_six = Checkbutton(radio_frame, text="OS", variable=radio_var6)
        check_six.grid(row=4, column=3, sticky=E, padx=15, pady=10)

        # #Scrolling Text (SHELL) Window for logging
        text_label = Label(text_frame, text='Log Output')
        text_label.configure(font=("Terminal", 14, "bold", "underline"))
        text_label.grid(row=1, column=1, pady=25)
        self.log_window = tk.Text(text_frame, height=20, width=100)
        self.log_window.grid(row=2, column=1, padx=10, pady=10)

        def test_update():
            global stop
            stop = True
            if stop == True:
                if radio_var.get() == 1 or adb_devices == True:
                    reset_app()

                else:

                    logging.info('Please select a test mode')
                    return

        #Button Selections
        button_one = Button(button_frame, text="Run Test", command=test_update)
        button_one.grid(row=1, column=1, padx=10, pady=10)

        def test_update_stop():
            #create a function to stop the test and reset_thread
            global stop
            stop = False
            logging.info('Test Stopped')
            return

        #create a button to stop the test_update function
        button_five = Button(button_frame, text="Stop Test", command=test_update_stop)
        button_five.grid(row=1, column=2, padx=10, pady=10)


        #clear log button will clear the log_window
        def clear_test_window():
            self.log_window.configure(state='normal')
            self.log_window.delete('1.0', tk.END)

        button_two = Button(button_frame, text="Clear Log", command=clear_test_window)
        button_two.grid(row=1, column=3, padx=10, pady=10)

        button_three = Button(button_frame, text="Exit", command=self.root.destroy)
        button_three.grid(row=1, column=5, padx=10, pady=10)

        #Button to write log to file
        button_four = Button(button_frame, text="Write Log", command='')
        button_four.grid(row=1, column=4, padx=10, pady=10)


        self.log_window.configure(state='normal')



