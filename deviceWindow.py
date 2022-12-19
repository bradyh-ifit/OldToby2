import tkinter as tk
from tkinter import *
from tkinter import messagebox
import logging
import adbConnect
import adbConnectIp


device_list = []
device_ip = []

for each in adbConnect.adb_sl:
    device_list.append(each)


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
            device_ip.append(new_ip.get('1.0', 'end-1c'))
            listbox.insert(0, new_ip.get('1.0', 'end-1c'))
            new_ip.delete('1.0', 'end')
            
    

    #add a delete button to delete a device from the list
    def delete_click():
        try:
            device_ip.remove(listbox.get(listbox.curselection()))
            listbox.delete(listbox.curselection())                   
        except:
            messagebox.showerror('Error', 'Please select a device to delete')

    def save_click():
        for each in device_ip:
            adbConnectIp.adb_connect_ip(each)
        
        

    button_frame = Frame(new_window, padx=10, pady=10)
    button_frame.pack()

    #create an add button
    add_button = Button(button_frame, text='Add', command=add_click)
    add_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    #create a remove button
    remove_button = Button(button_frame, text='Remove', command=delete_click)
    remove_button.grid(row=0, column=1, padx=10, pady=10, sticky='w')

    #create a save button
    save_button = Button(button_frame, text='Connect Device', command=save_click)
    save_button.grid(row = 0, column = 2, padx=10, pady=10)

    #create a button to close the window
    close_button = Button(button_frame, text='Close Window', command=new_window.destroy)
    close_button.grid(row = 0, column = 3, padx=10, pady=10, sticky='e')