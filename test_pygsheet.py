import pygsheets
from pygsheets import WorksheetNotFound
import google_spread_sheet
from google_spread_sheet import get_work_sheet
from selenium import webdriver
import pandas as pd

browser = webdriver.Chrome('chromedriver.exe')

# gc = pygsheets.authorize(service_file='test1-3301c1f1cf08.json')
# sh = gc.open('scraping')
# try:
#     wks = sh.worksheet_by_title('OddShark_NBA')
# except WorksheetNotFound:
#     wks = sh.add_worksheet('OddShark_NBA')
# wks.clear()
wks = get_work_sheet('test')
# wks = sh.sheet1
# wks.clear()


url = "http://quotes.toscrape.com/js/page/1/"

browser.get(url)

items = len(browser.find_elements_by_class_name("quote"))

total = []
for item in range(items):
    quotes = browser.find_elements_by_class_name("quote")
    for quote in quotes:
        quote_text = quote.find_element_by_class_name('text').text
        author = quote.find_element_by_class_name('author').text
        new = (quote_text, author)
        total.append(new)
df = pd.DataFrame(total, columns=['quote', 'author'])
wks.set_dataframe(df, (1, 1))
# df.to_csv('quoted.csv')
browser.close()
# # Update a cell with value (just to let him know values is updated ;) )
# wks.update_value('A1', "Hey yank this numpy array")
# my_nparray = np.random.randint(10, size=(3, 4))
#
# # update the sheet with array
# wks.update_values('A2', my_nparray.tolist())
