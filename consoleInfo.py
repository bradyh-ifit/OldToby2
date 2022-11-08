from cProfile import run
import logging
import subprocess
from subprocess import Popen, PIPE, check_output, CalledProcessError
from adbConnect import device_list
import json
from googleSheet import tabTrackingDict, google_tablet

for each in device_list:
    adb_sn = each


logging.info("initializing tablet")

def run_bash(command):
    try:
        ps = Popen(command.split(), stdout = PIPE)
        ps.wait()

    except CalledProcessError as e:
        logging.error(e)

def runBashCommands(bc_list):

    # run a process with a given command, send output to PIPE
    proc = Popen(bc_list[0].split(), stdout=PIPE)
    for i in range(len(bc_list) - 1):
        proc = Popen(bc_list[i + 1].split(), stdin=proc.stdout, stdout=PIPE)

    return proc.communicate()[0].rstrip().decode('ascii')

def get_admin():
    admin = runBashCommands([f'adb -s {adb_sn} shell pm dump com.ifit.eru | grep "versionName"'])
    a = admin.split('=')[1].split()[0]

    admin = runBashCommands([f'adb -s {adb_sn} shell pm dump com.ifit.eru | grep "versionCode"'])
    b = admin.splitlines()[0].split('=')[1].split()[0]

    c = str(f'{a}.{b}')
    
    return c


def get_wolf():
    try:
        admin = runBashCommands([f'adb -s {adb_sn} shell pm dump com.ifit.standalone | grep "versionName"'])
        a = admin.split('=')[1].split()[0]

        admin = runBashCommands([f'adb -s {adb_sn} shell pm dump com.ifit.standalone | grep "versionCode"'])
        b = admin.splitlines()[0].split('=')[1].split()[0]

        c = str(f'{a}.{b}')

        return c
    except:
        logging.info('wolf not installed')
        exit()


def get_webview():
    admin = runBashCommands([f'adb -s {adb_sn} shell pm dump com.android.webview | grep "versionName"'])
    a = admin.splitlines()[0].split('=')[1].split('.')[0]

    return a



def get_launcher():
    launch = runBashCommands([f'adb -s {adb_sn} shell pm dump com.ifit.launcher | grep "versionName"'])
    a = launch.splitlines()[0].split('=')[1]

    launch = runBashCommands([f'adb -s {adb_sn} shell pm dump com.ifit.launcher | grep "versionCode"'])
    b = launch.splitlines()[0].split('=')[1].split()[0]

    c = (f'{a}.{b}')

    return c


def get_uuid():
    uuid = runBashCommands([f'adb -s {adb_sn} shell cat ./sdcard/.ConsoleUpdateId'])
    x = json.loads(uuid)
    y = x['Guid']
    return y


def part_number():
    part_number = runBashCommands([f'adb -s {adb_sn} shell cat ./sdcard/.ConsoleInfo'])
    a = json.loads(part_number)
    b = a['PartNumber']
    return b


def get_brainboard():
    brainboard = runBashCommands([f'adb -s {adb_sn} shell cat ./sdcard/.ConsoleInfo'])
    a = json.loads(brainboard)
    b = a['MasterLibraryVersion']
    c = a['MasterLibraryBuild']
    d = float(f'{b}.{c}')
    return d

def get_console_num():
    console_num = 0
    if get_brainboard == 83.705:
        console_num = 14821 
    else:
        console_num = 0
    return console_num

def get_console():
    console_info = ""
    if get_brainboard == 83.705:
        console_info = "ETPF"
    elif get_brainboard == 83.194 or 83.142:
        console_info = "ETNE"
    else: 
        console_info = 'N/A'

    return console_info


def console_info():
    logging.info('asking for console info')
    tabTrackingDict["uuid"] = get_uuid()
    tabTrackingDict["software_number"] = part_number()
    tabTrackingDict["update_type"] = "Wifi 1 Hour Idle"
    tabTrackingDict["server"] = "Launch Darkly"
    tabTrackingDict["size"] = "N/A"
    tabTrackingDict["console"] = get_console()
    tabTrackingDict["console_num"] = get_console_num()
    logging.info('console info received')

def get_version1():   
    logging.info('asking for version 1 info')
    tabTrackingDict["brainboard1"] = get_brainboard()
    tabTrackingDict["admin_version1"] = get_admin()
    tabTrackingDict["wolf_version1"] = get_wolf()
    tabTrackingDict["webview1"] = get_webview()
    tabTrackingDict["launcher1"] = get_launcher()
    logging.info('version 1 info received')

def get_version2():
    logging.info('asking for version 2 info')
    tabTrackingDict["admin_version2"] = get_admin()
    tabTrackingDict["wolf_version2"] = get_wolf()
    tabTrackingDict["webview2"] = get_webview()
    tabTrackingDict["brainboard2"] = get_brainboard()
    tabTrackingDict["launcher2"] = get_launcher()
    logging.info('version 2 info received')


        
        
        