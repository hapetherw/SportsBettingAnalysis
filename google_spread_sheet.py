import pygsheets
from pygsheets import SpreadsheetNotFound, WorksheetNotFound
from config import GOOGLE_SPREAD_SHEET_CREDENTIAL
from config import GOOGLE_SPREAD_SHEET_NAME
from config import SHARE_EMAIL

gc = pygsheets.authorize(service_file=GOOGLE_SPREAD_SHEET_CREDENTIAL)
try:
    sh = gc.open(GOOGLE_SPREAD_SHEET_NAME)
except SpreadsheetNotFound:
    res = gc.sheet.create(GOOGLE_SPREAD_SHEET_NAME)
    sh = gc.open_by_key(res['spreadsheetId'])
    print("Create Google SpreadSheet- " + GOOGLE_SPREAD_SHEET_NAME)
    # sh.share('aglityman@gmail.com', role='writer', type='user')
    sh.share(SHARE_EMAIL, role='writer', type='user')


# sh.share('', role='writer', type='anyone')
# print(sh)

def get_work_sheet(sheet_name):
    try:
        wks = sh.worksheet_by_title(sheet_name)
    except WorksheetNotFound:
        wks = sh.add_worksheet(sheet_name)
        print("Add new worksheet- " + sheet_name)
    wks.clear()
    return wks
