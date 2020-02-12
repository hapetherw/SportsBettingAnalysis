from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from models.sportsinsights_model import SportsInsightsBETSIGNALS
from models.sportsinsights_model import SportsInsightsBESTBETS
from database import session
from database import recreate_sportsinsights_table
from database import close_connection
import time

browser = webdriver.Chrome('chromedriver.exe')
browser.maximize_window()
email = 'shanehvizdzak@gmail.com'
password = 'bigboy4!'


def add_bet_signals():
    browser.get('https://sportsinsights.actionnetwork.com/login/')
    browser.find_element_by_tag_name('form').find_element_by_name('email').send_keys(email)
    browser.find_element_by_tag_name('form').find_element_by_name('password').send_keys(password)
    browser.find_element_by_tag_name('form').submit()

    try:
        WebDriverWait(browser, 20).until(EC.title_contains('Dashboard'))
        print("Sportsinsights page is ready!")
    except TimeoutException:
        print("Sportsinsights page Loading took too much time!")

    browser.get('https://sportsinsights.actionnetwork.com/bet-signals/')
    time.sleep(8)
    main_tab = browser.find_element_by_id('s1').find_element_by_id(
        'borderLayout_eRootPanel').find_element_by_class_name('ag-body-container')
    div_list = main_tab.find_elements_by_css_selector('.ag-row.ag-row-no-focus')
    for div in div_list:
        cell_list = div.find_elements_by_tag_name('div')
        new_bet_signals = SportsInsightsBETSIGNALS(cell_list[0].get_attribute('innerHTML'),
                                                   cell_list[1].get_attribute('innerHTML'),
                                                   cell_list[2].get_attribute('innerHTML'),
                                                   cell_list[3].get_attribute('innerHTML'),
                                                   cell_list[4].get_attribute('innerHTML'),
                                                   cell_list[5].get_attribute('innerHTML'),
                                                   cell_list[6].get_attribute('innerHTML'),
                                                   cell_list[7].get_attribute('innerHTML').replace(
                                                       '<b>', '').replace('</b>', ''),
                                                   cell_list[8].get_attribute('innerHTML'))
        session.add(new_bet_signals)
        print(new_bet_signals)


def add_best_bets():
    browser.get('https://sportsinsights.actionnetwork.com/best-bets/')
    time.sleep(7)
    a_s3 = browser.find_element_by_id('myTab1').find_elements_by_tag_name('a')[2]
    browser.execute_script('arguments[0].click()', a_s3)
    time.sleep(1)
    main_tab = browser.find_element_by_id('s3').find_elements_by_id('borderLayout_eRootPanel')[1]
    div_list = main_tab.find_element_by_class_name('ag-body-container').find_elements_by_css_selector(
        '.ag-row.ag-row-no-focus')
    for div in div_list:
        cell_list = div.find_elements_by_tag_name('div')
        new_best_bets = SportsInsightsBESTBETS(cell_list[0].get_attribute('innerHTML'),
                                               cell_list[1].get_attribute('innerHTML'),
                                               cell_list[2].get_attribute('innerHTML'),
                                               cell_list[3].get_attribute('innerHTML'),
                                               cell_list[4].get_attribute('innerHTML').replace(
                                                   '<b>', '').replace('</b>', ''),
                                               cell_list[5].get_attribute('innerHTML'))
        session.add(new_best_bets)
        print(new_best_bets)


recreate_sportsinsights_table()
add_bet_signals()
add_best_bets()

session.commit()
browser.close()
close_connection()
