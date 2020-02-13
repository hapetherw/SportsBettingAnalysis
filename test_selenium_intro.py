from selenium import webdriver
import pandas as pd
from database import recreate_database
recreate_database()
browser = webdriver.Chrome('chromedriver.exe')
# browser.get('https://www.oddsshark.com/ncaab/computer-picks')
pages = 10

for page in range(1,pages):

    url = "http://quotes.toscrape.com/js/page/" + str(page) + "/"

    browser.get(url)

    items = len(browser.find_elements_by_class_name("quote"))

    total = []
    for item in range(items):
        quotes = browser.find_elements_by_class_name("quote")
        for quote in quotes:
            quote_text = quote.find_element_by_class_name('text').text
            author = quote.find_element_by_class_name('author').text
            new = ((quote_text,author))
            total.append(new)
    df = pd.DataFrame(total,columns=['quote','author'])
    df.to_csv('quoted.csv')
browser.close()