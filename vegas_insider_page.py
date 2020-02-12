from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from models.vegas_insider_model import VegasInsider
from database import session
from database import recreate_vegas_insider_table
from database import close_connection

browser = webdriver.Chrome('chromedriver.exe')


def add_vegas_insider():
    browser.get('https://www.vegasinsider.com/college-basketball/stats/iskoe-spreadsheet/')
    tr_list = browser.find_element_by_class_name('viBodyBorderNorm').find_elements_by_tag_name('tr')
    for index, tr in enumerate(tr_list):
        if index <= 3:
            continue
        td_list = tr.find_elements_by_tag_name('td')
        try:
            team_name = td_list[1].find_element_by_class_name('tableText').get_attribute('innerHTML').strip()
        except NoSuchElementException:
            team_name = td_list[1].get_attribute('innerHTML').strip()
        print(team_name)
        new_vegas_insider_model = VegasInsider(team_name, td_list[0].text,
                                               td_list[2].text, td_list[3].text, td_list[4].text, td_list[5].text,
                                               td_list[6].text, td_list[7].text, td_list[8].text, td_list[9].text,
                                               td_list[10].text, td_list[11].text, td_list[12].text, td_list[13].text,
                                               td_list[14].text, td_list[15].text, td_list[16].text, td_list[17].text,
                                               td_list[18].text, td_list[19].text, td_list[20].text, td_list[21].text,
                                               td_list[22].text, td_list[23].text)
        session.add(new_vegas_insider_model)


recreate_vegas_insider_table()
add_vegas_insider()

session.commit()
browser.close()
close_connection()
