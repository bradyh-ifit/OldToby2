import tkinter as tk
import pygsheets
import datetime
import logging
from tobyGui import *


class googleSheetsTablet:

    # connect: function that connects to google sheet
    def connect(self):

         # authorizing script to access google sheet
        GoogleSheet = pygsheets.authorize(service_account_file='./creds/admin-automate-test-c6b824f484ed.json')
        logging.info('google sheets authenticated')
        # opening google sheet 'Tablet Tracker'
        self.MasterListSheet = GoogleSheet.open('Test Tracker') 

    # update: updates the 'Tablet Tracker' Google sheet
    def update(self):
        try:
            self.connect()
            #insert log to gui
            logging.info('Connected to google sheet Successfully')
            self.upload()

            print("successfully connected")    # connecting to google sheets
        except BaseException as ex:
            print('Unable to connect to google sheets')
            print(str(ex))
        else:
            self.upload()    # calls sheet update
 

    def upload(self):
        try:
            MainSheet = self.MasterListSheet.worksheet_by_title(
                'Masterv2.0')    # selecting the Masterv2.0 sheet
            LastColumn = 'AB'    # last column on the tracker sheet
            # retrieving the entire first column and selecting the first empty row
            firstColumn = MainSheet.range(f'A1:A{MainSheet.rows}', 'matrix')
            firstEmptyRow = firstColumn.index(['']) + 1
            Date = datetime.date.strftime(
                datetime.date.today(), '%m/%d/%Y')    # getting today's date
            tabTrackingDict["date"] = Date # set date in the key list
            # list of values that will appear in the google sheet

            sheetVals = list(tabTrackingDict.values())
            print(f"sheetvals: {sheetVals}")
            MainSheet.update_values(crange=f'A{firstEmptyRow}:{LastColumn}{firstEmptyRow}', values=[sheetVals])    # Sending data to Google sheets
        except BaseException as ex:
            logging.info('googleSheetsTablet->upload(): Was unable to upload tablet data to google sheets')
            print(str(ex))
        else:
            # console output to let us know data has been sent to google sheets
            print(f'Data uploaded to {MainSheet.title}')

global tabTrackingDict
global google_tablet
key_list = ["date", "user", "console", "console_num", "software_number", "Vendor", "size", "uuid", "update_type", "server", "target_type", "L", "wolf_version1", "admin_version1", "webview1", "brainboard1", "launcher1", "os_Version1", "S", "wolf_version2", "admin_version2", "webview2", "brainboard2", "launcher2", "os_version2", "Z", "issues", "software_update"]
tabTrackingDict = dict.fromkeys(key_list)
google_tablet = googleSheetsTablet()

google_tablet.connect()

def update_google_sheet():
    google_tablet.update()