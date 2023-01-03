import subprocess
from subprocess import CalledProcessError, Popen, PIPE
import time

#logging.info('Starting adbConnect')
adb_sl = []

def runBashCommands(bc_list):

    # run a process with a given command, send output to PIPE
    proc = Popen(bc_list[0].split(), stdout=PIPE)
    for i in range(len(bc_list) - 1):
       
        proc = Popen(bc_list[i + 1].split(), stdin=proc.stdout, stdout=PIPE)
    return proc.communicate()[0].rstrip().decode('ascii')

adb_conn = "adb devices"
adb_process = Popen(adb_conn.split(), stdout=PIPE)
adb_data = adb_process.communicate()[0].rstrip().decode('ascii').splitlines()

print(adb_data)


def conn_success(input):

    if len(input) <= 1:
        return conn_attempt()
        
    else:
        print("Successfully connected")
        return input


def conn_attempt():
    i = 0
    print("Looking for wired connections")
    while i < 1:
        adb_conn = "adb devices"
        adb_process = Popen(adb_conn.split(), stdout=PIPE)
        adb_data = adb_process.communicate()[0].rstrip().decode('ascii').splitlines()
        if len(adb_data) > 1:
            return adb_data

        time.sleep(10)
        i = i + 1
        
    else:
        print("Unable to establish connection")
        return


def start_connect():                        
    tablet_sn = conn_success(adb_data)


    for i in range(len(tablet_sn)):
        if i > 0:
            adb_sl.append(tablet_sn[i].split()[0])