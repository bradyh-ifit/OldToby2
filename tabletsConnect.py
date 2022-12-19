import adbConnect
import adbConnectIp

device_list = []

for each in adbConnect.adb_sl:
    device_list.append(each)

