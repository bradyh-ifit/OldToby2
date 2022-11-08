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
from adbConnect import device_list, ip_connect
from fullTest import reset_app


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

        #create a method that creates new tkinter window
        def new_window():
            #create new window
            new_window = tk.Toplevel(self.root)
            new_window.geometry('500x500')
            new_window.title('Add New Device')

            #create a title to add a new device
            new_device_label = Label(new_window, text='Add New Device')
            new_device_label.pack()
            #create a text box to add a new device
            new_ip = Text(new_window, height=1, width=20)
            new_ip.pack()


            #create a frame that shows all IP devices from device list
            device_frame = Frame(new_window, padx=10, pady=20)
            device_frame.pack()

            label_two = Label(device_frame, text='Devices Connected')
            label_two.configure(font=("Terminal", 12, "bold", "underline"))
            label_two.pack()

            for each in device_list:
                device_label = Label(device_frame, text=each)
                device_label.pack()

            device_frame_two = Frame(new_window, padx=10, pady=20)
            device_frame_two.pack()
            
            label_three = Label(device_frame_two, text='Devices To Connect')
            label_three.configure(font=("Terminal", 12, "bold", "underline"))
            label_three.pack()
            listbox = Listbox(device_frame_two, height=5, width=20)
            listbox.pack()

            def add_click():
                if new_ip.get('1.0', 'end-1c') == '':
                    messagebox.showerror('Error', 'Please enter an IP Address')
                else:
                    device_list.append(new_ip.get('1.0', 'end-1c'))
                    listbox.insert(0, new_ip.get('1.0', 'end-1c'))
                    new_ip.delete('1.0', 'end')
                    logging.info(device_list)
            

            #add a delete button to delete a device from the list
            def delete_click():
                try:
                    device_list.remove(listbox.get(listbox.curselection()))
                    listbox.delete(listbox.curselection())                   
                except:
                    messagebox.showerror('Error', 'Please select a device to delete')

            def connect_click():
                ip_connect()
                new_window.destroy()

            button_frame = Frame(new_window, padx=10, pady=10)
            button_frame.pack()

            #create an add button
            add_button = Button(button_frame, text='Add', command=add_click)
            add_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')

            #create a remove button
            remove_button = Button(button_frame, text='Remove', command=delete_click)
            remove_button.grid(row=0, column=1, padx=10, pady=10, sticky='w')

            #create a Connect button
            save_button = Button(button_frame, text='Connect', command=connect_click)
            save_button.grid(row = 0, column = 2, padx=10, pady=10)

            #create a button to close the window
            close_button = Button(button_frame, text='Close Window', command=new_window.destroy)
            close_button.grid(row = 0, column = 3, padx=10, pady=10, sticky='e')

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
                if radio_var.get() == 1:
                    threading.Thread(target = reset_app).start()

                else:

                    logging('Please select a test mode')
                    exit()

        #Button Selections
        button_one = Button(button_frame, text="Run Test", command=test_update)
        button_one.grid(row=1, column=1, padx=10, pady=10)

        def test_update_stop():
            global stop
            stop = False
            logging.info("Test Has Been Stopped")

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



