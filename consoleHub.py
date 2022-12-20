from googleSheet import google_tablet, tabTrackingDict
import consoleInfo
import testMethods
from deviceWindow import device_list, device_ip


tablet_list = []
for each in device_ip and device_list:
    tablet_list.append(each)

for i in tablet_list:
    adb_sn = i


def console_info():
    tabTrackingDict["uuid"] = consoleInfo.get_uuid(adb_sn)
    tabTrackingDict["software_number"] = consoleInfo.part_number(adb_sn)
    tabTrackingDict["update_type"] = "Wifi 1 Hour Idle"
    tabTrackingDict["server"] = "Launch Darkly"
    tabTrackingDict["size"] = "N/A"
    tabTrackingDict["console"] = consoleInfo.get_console()
    tabTrackingDict["console_num"] = consoleInfo.get_console_num()

def get_version1():   
    tabTrackingDict["brainboard1"] = consoleInfo.get_brainboard(adb_sn)
    tabTrackingDict["admin_version1"] = consoleInfo.get_admin(adb_sn)
    tabTrackingDict["wolf_version1"] = consoleInfo.get_wolf(adb_sn)
    tabTrackingDict["webview1"] = consoleInfo.get_webview(adb_sn)
    tabTrackingDict["launcher1"] = consoleInfo.get_launcher(adb_sn)

def get_version2():
    tabTrackingDict["admin_version2"] = consoleInfo.get_admin(adb_sn)
    tabTrackingDict["wolf_version2"] = consoleInfo.get_wolf(adb_sn)
    tabTrackingDict["webview2"] = consoleInfo.get_webview(adb_sn)
    tabTrackingDict["brainboard2"] = consoleInfo.get_brainboard(adb_sn)
    tabTrackingDict["launcher2"] = consoleInfo.get_launcher(adb_sn)

def full_test(adb_sn):
    #creating a test environment for each tablet listed. 
    testMethods.test_environment(adb_sn)

    testMethods.reset_wolf(adb_sn)
    get_version1()
    testMethods.idle_broadcast(adb_sn)
    get_version2()
    if tabTrackingDict["wolf_version1"] == tabTrackingDict["wolf_version2"]:
        testMethods.idle_broadcast(adb_sn)
        get_version2()
    else:
        tabTrackingDict["software_update"] = "Wolf"
        google_tablet.update()

    testMethods.reset_eru(adb_sn)
    get_version1()
    testMethods.idle_broadcast(adb_sn)
    get_version2()
    if tabTrackingDict["admin_version1"] == tabTrackingDict["admin_version2"]:
        testMethods.idle_broadcast(adb_sn)
        get_version2()
    else:
        tabTrackingDict["software_update"] = "Admin"
        google_tablet.update()

    testMethods.reset_launcher(adb_sn)
    get_version1()
    testMethods.idle_broadcast(adb_sn)
    get_version2()
    if tabTrackingDict["launcher1"] == tabTrackingDict["launcher2"]:
        testMethods.idle_broadcast(adb_sn)
        get_version2()
    else:
        tabTrackingDict["software_update"] = "Launcher"
        google_tablet.update()

    testMethods.reset_webview(adb_sn)
    get_version1()
    testMethods.idle_broadcast(adb_sn)
    get_version2()
    if tabTrackingDict["webview1"] == tabTrackingDict["webview2"]:
        testMethods.idle_broadcast(adb_sn)
        get_version2()
    else:    
        tabTrackingDict["software_update"] = "Webview"
        google_tablet.update()

############################################################################################################
#Brainboard support not yet added. 
    # testMethods.reset_brainboard(adb_sn)
    # get_version1()
    # testMethods.idle_broadcast(adb_sn)
    # get_version2()
    # if tabTrackingDict["brainboard1"] == tabTrackingDict["brainboard2"]:
    #     testMethods.idle_broadcast(adb_sn)
    # else:    
    #     tabTrackingDict["software_update"] = "Brainboard"
    #     google_tablet.update()
############################################################################################################

    testMethods.test_one(adb_sn)
    get_version1
    testMethods.idle_broadcast(adb_sn)
    get_version2()
    if (tabTrackingDict["wolf_version1"] == tabTrackingDict["wolf_version2"]) and (tabTrackingDict["admin_version1"] == tabTrackingDict["admin_version2"]):
       testMethods.idle_broadcast(adb_sn)
       get_version2()
    else:
        tabTrackingDict["software_update"] = "Wolf & Admin"
        google_tablet.update()

    testMethods.test_two(adb_sn)
    get_version1
    testMethods.idle_broadcast(adb_sn)
    get_version2()
    if (tabTrackingDict["wolf_version1"] == tabTrackingDict["wolf_version2"]) and (tabTrackingDict["launcher_version1"] == tabTrackingDict["launcher_version2"]):
        testMethods.idle_broadcast(adb_sn)
        get_version2()
    else:
        tabTrackingDict["software_update"] = "Wolf & Launcher"
        google_tablet.update()

    testMethods.test_three(adb_sn)
    get_version1
    testMethods.idle_broadcast(adb_sn)
    get_version2()
    if (tabTrackingDict["wolf_version1"] == tabTrackingDict["wolf_version2"]) and (tabTrackingDict["webview_version1"] == tabTrackingDict["webview_version2"]):
        testMethods.idle_broadcast(adb_sn)
        get_version2()
    else:
        tabTrackingDict["software_update"] = "Wolf & Webview"
        google_tablet.update()
    
    testMethods.test_four(adb_sn)
    get_version1
    testMethods.idle_broadcast(adb_sn)
    get_version2()
    if (tabTrackingDict["admin_version1"] == tabTrackingDict["admin_version2"]) and (tabTrackingDict["launcher_version1"] == tabTrackingDict["launcher_version2"]):
        testMethods.idle_broadcast(adb_sn)
        get_version2()
    else:  
        tabTrackingDict["software_update"] = "Admin & Launcher"
        google_tablet.update()

    testMethods.test_five(adb_sn)
    get_version1
    testMethods.idle_broadcast(adb_sn)
    get_version2()
    if (tabTrackingDict["admin_version1"] == tabTrackingDict["admin_version2"]) and (tabTrackingDict["webview_version1"] == tabTrackingDict["webview_version2"]):
        testMethods.idle_broadcast(adb_sn)
        get_version2()
    else:
        tabTrackingDict["software_update"] = "Admin & Webview"
        google_tablet.update()

    testMethods.test_six(adb_sn)
    get_version1
    testMethods.idle_broadcast(adb_sn)
    get_version2()
    if (tabTrackingDict["launcher_version1"] == tabTrackingDict["launcher_version2"]) and (tabTrackingDict["webview_version1"] == tabTrackingDict["webview_version2"]):
        testMethods.idle_broadcast(adb_sn)
        get_version2()
    else:
        tabTrackingDict["software_update"] = "Launcher & Webview"
        google_tablet.update()

    
    

