import logging
import subprocess
from subprocess import Popen, PIPE, check_output, CalledProcessError
import time
from adbConnect import device_list
import consoleInfo as ci
from googleSheet import google_tablet, tabTrackingDict



def check_device():
    if not device_list: 
        #logging.error('No Devices Connected, Please connect a device or add a device using IP address')
        adb_sn = 0
        exit()
    else:
        for each in device_list:
            adb_sn = each
            return adb_sn


def run_bash(command):
    try:
        ps = Popen(command.split(), stdout = PIPE)
        ps.wait()

    except CalledProcessError as e:
        logging.error(e)

# logging.info('Developer Mode Enabled')
# logging.info('Resetting Apps')

def idle_broadcast():
    adb_sn = check_device()
    run_bash(f'adb -s {adb_sn} shell am broadcast -a com.ifit.eru.IDLE_UPDATE')
    time.sleep(60)
    run_bash(f'adb -s {adb_sn} shell am broadcast -a com.ifit.eru.IDLE_UPDATE')
    time.sleep(60)

def test_environment():
    adb_sn = check_device()
    run_bash(f'adb -s {adb_sn} shell touch ./sdcard/.wolfDev')
    run_bash(f'adb -s {adb_sn} shell am broadcast -a com.ifit.eru.UPDATE_ENVIRONMENT --ez  USE_TEST true')
    tablet_reboot()
    time.sleep(60)
    #logging.info('Test Environment Enabled in Dev Move')

def tablet_reboot():
    adb_sn = check_device()
    run_bash(f'adb -s {adb_sn} reboot')
    time.sleep(60)

def idle_broadcast():
    adb_sn = check_device()
    run_bash(f'adb -s {adb_sn} shell am broadcast -a com.ifit.eru.IDLE_UPDATE')

    time.sleep(60)

    run_bash(f'adb -s {adb_sn} shell am broadcast -a com.ifit.eru.IDLE_UPDATE')

    time.sleep(60)

def reset_wolf():
    adb_sn = check_device()
    run_bash(f'adb -s {adb_sn} uninstall com.ifit.standalone')
    time.sleep(15)
    run_bash(f'adb -s {adb_sn} install -r -d ./apkFiles/com.ifit.standalone-2.6.73.3252.apk')
    time.sleep(90)


def reset_eru():
    adb_sn = check_device()
    run_bash(f'adb -s {adb_sn} uninstall com.ifit.eru')
    time.sleep(15)
    run_bash(f'adb -s {adb_sn} install -r -d ./apkFiles/com.ifit.eru-2.0.5.1213.apk')
    time.sleep(90)

    test_environment()

def reset_launcher():
    adb_sn = check_device()
    run_bash(f'adb -s {adb_sn} uninstall com.ifit.launcher')
    time.sleep(15)
    run_bash(f'adb -s {adb_sn} install -r -d ./apkFiles/com.ifit.launcher-1.0.17.22.apk')
    time.sleep(90)

def reset_webview():
    adb_sn = check_device()
    run_bash(f'adb -s {adb_sn} uninstall com.android.webview')
    time.sleep(90)

def reset_app():
    test_environment()
    ci.console_info()

    try:
        ci.get_version1()
        reset_wolf()
        tablet_reboot()
        idle_broadcast()
        tablet_reboot()
        ci.get_version2()
        if tabTrackingDict['wolfVersion'] == tabTrackingDict['wolfVersion2']:
            #logging.error('Update FAILED, retrying')
            idle_broadcast()
            tablet_reboot()
            ci.get_version2()
        else:
            tabTrackingDict['software_update'] = 'Wolf'
            google_tablet.update()
        


    except:
        logging.info('Wolf Not Installed')
        adb_sn = check_device()
        run_bash('adb -s ' + adb_sn + ' install com.ifit.standalone-2.6.73.3252.apk')
        time.sleep(90)

    try:

        ci.get_version1()
        reset_eru()
        tablet_reboot()
        idle_broadcast()
        tablet_reboot()
        ci.get_version2()
        if tabTrackingDict['adminVersion'] == tabTrackingDict['adminVersion2']:
            #logging.error('Update FAILED, retrying')
            idle_broadcast()
            tablet_reboot()
            ci.get_version2()
        else:
            tabTrackingDict['software_update'] = 'Eru'
            google_tablet.update()


    except:

        logging.info('ERU Not Installed')
        run_bash('adb -s ' + adb_sn + ' install com.ifit.eru-2.1.0.1223.apk')
        time.sleep(90)

    # ci.get_version1()
    # reset_launcher()
    # tablet_reboot()
    # idle_broadcast()
    # tablet_reboot()
    # ci.get_version2()








