import subprocess
from subprocess import CalledProcessError, Popen, PIPE
import os
import logging

logging.info('Starting adbConnect')

#create an empty list to store device serial numbers
device_list = []

def run_bash(command):
    try:
        ps = Popen(command.split(), stdout = PIPE)
        ps.wait()
        

    except CalledProcessError as e:
        logging.error(e)


#Establish if device is connected to adb
def adb_devices():
    #check if device is connected to adb
    if device_list == []:
        try:
            for each in subprocess.check_output(['adb', 'devices']).splitlines():
                if each.endswith(b'device'):
                    device_list.append(each.split()[0].decode('utf-8'))
                    if device_list:
                        logging.info('Device connected')
                        continue
                    else:
                        while i < 5:
                            adb_devices()
                            i += 1
        except:
            #if device is not connected to adb, exit program
            logging.info('No Device Connected, Please Connect or add a device')

def ip_connect():
    #check to see if any item in device list is an IP address
    for each in device_list:
        if each.startswith('192.168.'):
            #if IP address is found, try to connect to adb via IP address
            try:    
                adb_conn = 'adb connect ' +  each  +''
                run_bash(adb_conn)
                logging.info('Connecting to adb via IP address')
                #if connection is successful, log success
                if each in subprocess.check_output(['adb', 'devices']).splitlines():
                    logging.info('Connection Successful')
            except:
                logging.info('Could not connect to adb via IP address')
        else:
            continue

#create a method that if device loses connection via ip address, reconnects to adb via IP address
def ip_reconnect():
    #check to see if any item in device list is an IP address
    for each in device_list:
        if each.startswith('192.168.'):
            #if IP address is found, try to connect to adb via IP address
            try:    
                adb_conn = 'adb connect ' +  each  +''
                run_bash(adb_conn)
                logging.info('Reconnecting to adb via IP address')
                #if connection is successful, log success
                if each in subprocess.check_output(['adb', 'devices']).splitlines():
                    logging.info('Reconnection Successful')
            except:
                logging.info('Could not reconnect to adb via IP address')
        else:
            continue