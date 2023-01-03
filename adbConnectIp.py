import subprocess
from subprocess import CalledProcessError, Popen, PIPE
import logging

adb_ip = []

def run_bash(bc_list):

    # run a process with a given command, send output to PIPE
    proc = Popen(bc_list[0].split(), stdout=PIPE)
    for i in range(len(bc_list) - 1):
       
        proc = Popen(bc_list[i + 1].split(), stdin=proc.stdout, stdout=PIPE)
    return proc.communicate()[0].rstrip().decode('ascii')


#user input an ip address
#need to add the list from newDevice module
# ip = input('Enter an IP Address: ')

def adb_connect_ip(ip):
    try:
        run_bash([f'adb connect {ip}'])
        print(run_bash([f'adb devices']))
        #if connection is successful, add ip to adb_ip list
        adb_ip.append(ip)
        print(adb_ip)

        return True
    except:
        return False

