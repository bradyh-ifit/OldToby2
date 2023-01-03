import tkinter as tk
from tkinter import *
from tkinter import messagebox
import logging
import adbConnect
import adbConnectIp


device_list = []
device_ip = []

try:
    adbConnect.start_connect()
    #initializing wire connections
    for each in adbConnect.adb_sl:
        device_list.append(each)
except:
    pass

print(device_list)

def new_window(parent):

    #connect new_window to root
    new_window = tk.Toplevel(parent)
    new_window.geometry('500x500')
    new_window.title('Add New Device')

    #create a title to add a new device
    new_device_label = Label(new_window, text='Add New Device')
    new_device_label.pack()

    #create a text box to add a new device
    new_ip = Text(new_window, height=1, width=20)
    new_ip.pack()

############################################################################################################
#Devices Found/Connected Frame
############################################################################################################


    #create a frame that shows all IP devices from device list
    device_frame = Frame(new_window, padx=10, pady=20)
    device_frame.pack()

    label_two = Label(device_frame, text='Devices Connected')
    label_two.configure(font=("Terminal", 12, "bold", "underline"))
    label_two.pack()

    device_frame_two = Frame(new_window, padx=10, pady=20)
    device_frame_two.pack()

    listbox = Listbox(device_frame_two, height=5, width=20)
    listbox.pack()

    for each in device_list:
        device_label = Label(device_frame, text=each)
        device_label.pack()
        listbox.insert(END, each)
    
    for each in device_ip:
        #delete any duplicate IP addresses
        if each in device_list:
            device_list.remove(each)
        device_label = Label(device_frame, text=each)
        device_label.pack()
        listbox.insert(END, each)   

############################################################################################################
#Button Frame
############################################################################################################

    button_frame = Frame(new_window, padx=10, pady=10)
    button_frame.pack()

    #Save button function
    def save_click():
        if new_ip.get('1.0', 'end-1c') == '':
            messagebox.showerror('Error', 'Please enter an IP Address')
        else:
            device_ip.append(new_ip.get('1.0', 'end-1c'))
            print(device_ip)
            listbox.insert(END, new_ip.get('1.0', 'end-1c'))

        adbConnectIp.adb_connect_ip(new_ip.get('1.0', 'end-1c'))

        if adbConnectIp.adb_connect_ip(new_ip.get('1.0', 'end-1c')) == True:
            device_label = Label(device_frame, text=new_ip.get('1.0', 'end-1c'))
            device_label.pack()
            new_ip.delete('1.0', 'end')

    #create a save button
    save_button = Button(button_frame, text='Connect Device', command=save_click)
    save_button.grid(row = 0, column = 1, padx=10, pady=10)

    #add a delete button to delete a device from the list
    ############################################################################################################
    #curselection() returns the index of the selected item but does not seem to work. 

    def delete_click():
        try:  
            device_ip.remove(listbox.get(listbox.curselection()))
            listbox.delete(listbox.curselection())                 
        except:
            messagebox.showerror('Error', 'Please select a device to delete')


    #create a remove button
    remove_button = Button(button_frame, text='Disconnect Device', command=delete_click)
    remove_button.grid(row=0, column=2, padx=10, pady=10, sticky='w')


    def window_destroy():
        try:
            device_label.destroy()
        except:
            pass
        new_window.destroy()

    #create a button to close the window
    close_button = Button(button_frame, text='Close Window', command=window_destroy)
    close_button.grid(row = 0, column = 3, padx=10, pady=10, sticky='e')