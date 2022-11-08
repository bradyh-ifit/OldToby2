import subprocess
from subprocess import Popen, PIPE, check_output, CalledProcessError
import logging
import json
import time

def run_bash(command):
    try:
        ps = Popen(command.split(), stdout = PIPE)
        ps.wait()
        

    except CalledProcessError as e:
        logging.error(e)

ip_address = '192.168.1.23'
device_list = []

#create a method which connects to adb via IP address
def adb_connect():
    #establish adb connection via IP address
    adb_conn = 'adb connect ' +  ip_address  +''
    run_bash(adb_conn)

adb_connect()

