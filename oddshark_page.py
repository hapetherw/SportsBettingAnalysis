from selenium import webdriver
from models.computer_pick_models import ComputerPickDetailsNCAAB
from models.computer_pick_models import ComputerPickDetailsNBA
from database import session
from database import recreate_oddshark_table
from database import close_connection
import pandas as pd
import google_spread_sheet
from google_spread_sheet import get_work_sheet

browser = webdriver.Chrome('chromedriver.exe')

wks_nba = get_work_sheet('OddShark_NBA')
wks_ncaab = get_work_sheet('OddShark_NCAAB')


def add_oddshark_ncaab():
    browser.get('https://www.oddsshark.com/ncaab/computer-picks')
    block_system_main = browser.find_element_by_id("block-system-main")
    computer_tables = block_system_main.find_elements_by_css_selector('.table.table--striped.table--fixed-column')
    total_sheet_data = []
    for computer_table in computer_tables:
        if computer_table.get_attribute('class') == 'table table--striped table--fixed-column':
            name_wraps = computer_table.find_elements_by_class_name('name-wrap')

            first_team_name_short = name_wraps[0].find_element_by_class_name('table__name-short').get_attribute(
                'innerHTML')
            first_team_name_long = name_wraps[0].find_element_by_class_name('table__name-long').text

            second_team_name_short = name_wraps[1].find_element_by_class_name('table__name-short').get_attribute(
                'innerHTML')
            second_team_name_long = name_wraps[1].find_element_by_class_name('table__name-long').text
            thead = computer_table.find_element_by_tag_name('thead')
            date_time = thead.find_element_by_tag_name('th').text.split(" @ ")
            date = date_time[0]
            time = date_time[1]
            # new_computer_pick = ComputerPicksListNCAAB(first_team_name_short, first_team_name_long,
            #                                            second_team_name_short, second_team_name_long, date, time)
            # session.add(new_computer_pick)
            # session.flush()
            tbody = computer_table.find_element_by_tag_name('tbody')
            attr_tr_list = tbody.find_elements_by_tag_name('tr')
            for attr in attr_tr_list:
                attr_tds = attr.find_elements_by_tag_name('td')
                new_computer_detail = ComputerPickDetailsNCAAB(first_team_name_short, first_team_name_long,
                                                               second_team_name_short, second_team_name_long, date,
                                                               time, attr_tds[0].text, attr_tds[1].text,
                                                               attr_tds[2].text)
                session.add(new_computer_detail)
                total_sheet_data.append((first_team_name_short, first_team_name_long,
                                         second_team_name_short, second_team_name_long, date, time,
                                         attr_tds[0].text, attr_tds[1].text, attr_tds[2].text))
    # print(total_sheet_data)
    df = pd.DataFrame(total_sheet_data, columns=ComputerPickDetailsNCAAB.table_columns)
    wks_ncaab.set_dataframe(df, (1, 1))


def add_oddshark_nba():
    browser.get('https://www.oddsshark.com/nba/computer-picks')
    block_system_main = browser.find_element_by_id("block-system-main")
    computer_tables = block_system_main.find_elements_by_css_selector('.table.table--striped.table--fixed-column')
    total_sheet_data = []
    for computer_table in computer_tables:
        if computer_table.get_attribute('class') == 'table table--striped table--fixed-column':
            name_wraps = computer_table.find_elements_by_class_name('name-wrap')

            first_team_name_short = name_wraps[0].find_element_by_class_name('table__name-short').get_attribute(
                'innerHTML')
            first_team_name_long = name_wraps[0].find_element_by_class_name('table__name-long').text

            second_team_name_short = name_wraps[1].find_element_by_class_name('table__name-short').get_attribute(
                'innerHTML')
            second_team_name_long = name_wraps[1].find_element_by_class_name('table__name-long').text
            thead = computer_table.find_element_by_tag_name('thead')
            date_time = thead.find_element_by_tag_name('th').text.split(" @ ")
            date = date_time[0]
            time = date_time[1]
            # new_computer_pick = ComputerPicksListNBA(first_team_name_short, first_team_name_long,
            #                                            second_team_name_short, second_team_name_long, date, time)
            # session.add(new_computer_pick)
            # session.flush()
            tbody = computer_table.find_element_by_tag_name('tbody')
            attr_tr_list = tbody.find_elements_by_tag_name('tr')
            for attr in attr_tr_list:
                attr_tds = attr.find_elements_by_tag_name('td')
                new_computer_detail = ComputerPickDetailsNBA(first_team_name_short, first_team_name_long,
                                                             second_team_name_short, second_team_name_long, date, time,
                                                             attr_tds[0].text, attr_tds[1].text, attr_tds[2].text)
                session.add(new_computer_detail)
                total_sheet_data.append((first_team_name_short, first_team_name_long,
                                         second_team_name_short, second_team_name_long, date, time,
                                         attr_tds[0].text, attr_tds[1].text, attr_tds[2].text))
    print(total_sheet_data)
    df = pd.DataFrame(total_sheet_data, columns=ComputerPickDetailsNCAAB.table_columns)
    wks_nba.set_dataframe(df, (1, 1))


recreate_oddshark_table()
add_oddshark_nba()
add_oddshark_ncaab()

session.commit()
browser.close()
close_connection()
