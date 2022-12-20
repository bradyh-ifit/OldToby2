from cProfile import run
import logging
from subprocess import Popen, PIPE, check_output, CalledProcessError
import json


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


#methods for getting  versions and console info.
def get_admin(adb_sn):
    admin = runBashCommands([f'adb -s {adb_sn} shell pm dump com.ifit.eru | grep "versionName"'])
    a = admin.split('=')[1].split()[0]

    admin = runBashCommands([f'adb -s {adb_sn} shell pm dump com.ifit.eru | grep "versionCode"'])
    b = admin.splitlines()[0].split('=')[1].split()[0]

    c = str(f'{a}.{b}')
    
    return c


def get_wolf(adb_sn):
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


def get_webview(adb_sn):
    admin = runBashCommands([f'adb -s {adb_sn} shell pm dump com.android.webview | grep "versionName"'])
    a = admin.splitlines()[0].split('=')[1].split('.')[0]

    return a



def get_launcher(adb_sn):
    launch = runBashCommands([f'adb -s {adb_sn} shell pm dump com.ifit.launcher | grep "versionName"'])
    a = launch.splitlines()[0].split('=')[1]

    launch = runBashCommands([f'adb -s {adb_sn} shell pm dump com.ifit.launcher | grep "versionCode"'])
    b = launch.splitlines()[0].split('=')[1].split()[0]

    c = (f'{a}.{b}')

    return c

def get_brainboard(adb_sn):
    brainboard = runBashCommands([f'adb -s {adb_sn} shell cat ./sdcard/.ConsoleInfo'])
    a = json.loads(brainboard)
    b = a['MasterLibraryVersion']
    c = a['MasterLibraryBuild']
    d = float(f'{b}.{c}')
    return d


def get_uuid(adb_sn):
    uuid = runBashCommands([f'adb -s {adb_sn} shell cat ./sdcard/.ConsoleUpdateId'])
    x = json.loads(uuid)
    y = x['Guid']
    return y


def part_number(adb_sn):
    part_number = runBashCommands([f'adb -s {adb_sn} shell cat ./sdcard/.ConsoleInfo'])
    a = json.loads(part_number)
    b = a['PartNumber']
    return b

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



        
        
        