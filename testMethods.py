import logging
from subprocess import Popen, PIPE, check_output, CalledProcessError
import time
from googleSheet import google_tablet, tabTrackingDict



def run_bash(command):
    try:
        ps = Popen(command.split(), stdout = PIPE)
        ps.wait()

    except CalledProcessError as e:
        logging.error(e)

def idle_broadcast(adb_sn):    
    run_bash(f'adb -s {adb_sn} shell am broadcast -a com.ifit.eru.IDLE_UPDATE')
    time.sleep(60)
    run_bash(f'adb -s {adb_sn} shell am broadcast -a com.ifit.eru.IDLE_UPDATE')
    time.sleep(60)

def test_environment(adb_sn):    
    run_bash(f'adb -s {adb_sn} shell touch ./sdcard/.wolfDev')
    run_bash(f'adb -s {adb_sn} shell am broadcast -a com.ifit.eru.UPDATE_ENVIRONMENT --ez  USE_TEST true')
    tablet_reboot()
    time.sleep(60)

def tablet_reboot(adb_sn):  
    run_bash(f'adb -s {adb_sn} reboot')
    time.sleep(60)

def idle_broadcast(adb_sn):    
    run_bash(f'adb -s {adb_sn} shell am broadcast -a com.ifit.eru.IDLE_UPDATE')
    time.sleep(60)
    run_bash(f'adb -s {adb_sn} shell am broadcast -a com.ifit.eru.IDLE_UPDATE')
    time.sleep(60)

def reset_wolf(adb_sn):    
    run_bash(f'adb -s {adb_sn} uninstall com.ifit.standalone')
    time.sleep(15)
    run_bash(f'adb -s {adb_sn} install -r -d ./apkFiles/com.ifit.standalone-2.6.73.3252.apk')
    time.sleep(90)

def reset_eru(adb_sn):    
    run_bash(f'adb -s {adb_sn} uninstall com.ifit.eru')
    time.sleep(15)
    run_bash(f'adb -s {adb_sn} install -r -d ./apkFiles/com.ifit.eru-2.0.5.1213.apk')
    time.sleep(90)
    test_environment()

def reset_launcher(adb_sn):    
    run_bash(f'adb -s {adb_sn} uninstall com.ifit.launcher')
    time.sleep(15)
    run_bash(f'adb -s {adb_sn} install -r -d ./apkFiles/com.ifit.launcher-1.0.17.22.apk')
    time.sleep(90)

def reset_webview(adb_sn):   
    run_bash(f'adb -s {adb_sn} uninstall com.android.webview')
    time.sleep(90)

def test_one():
    reset_wolf()
    reset_eru()

def test_two():
    reset_wolf()
    reset_launcher()

def test_three():
    reset_wolf()
    reset_webview()

def test_four():
    reset_eru()
    reset_launcher()

def test_five():
    reset_eru()
    reset_webview()

def test_six():
    reset_launcher()
    reset_webview()

def test_seven():
    reset_wolf()
    reset_eru()
    reset_launcher()

def test_eight():
    reset_wolf()
    reset_eru()
    reset_webview()

def test_nine():
    reset_wolf()
    reset_launcher()
    reset_webview()

def test_ten():
    reset_eru()
    reset_launcher()
    reset_webview()

def test_eleven():
    reset_wolf()
    reset_eru()
    reset_launcher()
    reset_webview()

def test_twelve():
    reset_wolf()
    reset_eru()
    reset_launcher()
    reset_webview()










