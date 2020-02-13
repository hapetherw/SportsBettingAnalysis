from selenium import webdriver
from models.computer_pick_models import ComputerPickDetailsNCAAB
from models.computer_pick_models import ComputerPickDetailsNBA
from database import session
from database import recreate_oddshark_table
from database import close_connection
import pandas as pd
from airtable import Airtable
from config import AIRTABLE_BASE_KEY
from config import AIRTABLE_API_KEY
import google_spread_sheet
from google_spread_sheet import get_work_sheet

browser = webdriver.Chrome('chromedriver.exe')

wks_nba = get_work_sheet('OddShark_NBA')
wks_ncaab = get_work_sheet('OddShark_NCAAB')

airtable_ncaab = Airtable(AIRTABLE_BASE_KEY, 'Oddshark_NCAAB', api_key=AIRTABLE_API_KEY)
airtable_nba = Airtable(AIRTABLE_BASE_KEY, 'Oddshark_NBA', api_key=AIRTABLE_API_KEY)


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
            date_time_info = thead.find_element_by_tag_name('th').text.split(" @ ")
            date_time = date_time_info[0] + " " + date_time_info[1]
            # new_computer_pick = ComputerPicksListNCAAB(first_team_name_short, first_team_name_long,
            #                                            second_team_name_short, second_team_name_long, date, time)
            # session.add(new_computer_pick)
            # session.flush()
            tbody = computer_table.find_element_by_tag_name('tbody')
            attr_tr_list = tbody.find_elements_by_tag_name('tr')
            predicted_score_tds = attr_tr_list[0].find_elements_by_tag_name('td')
            computer_pick_tds = attr_tr_list[1].find_elements_by_tag_name('td')
            public_consensus_tds = attr_tr_list[2].find_elements_by_tag_name('td')
            consensus_bet_tds = attr_tr_list[3].find_elements_by_tag_name('td')
            total_sheet_data.append((first_team_name_short, first_team_name_long,
                                     second_team_name_short, second_team_name_long, date_time,
                                     predicted_score_tds[1].text,
                                     predicted_score_tds[2].text, computer_pick_tds[1].text,
                                     computer_pick_tds[2].text, public_consensus_tds[1].text,
                                     public_consensus_tds[2].text, consensus_bet_tds[1].text,
                                     consensus_bet_tds[2].text))
            new_computer_detail = ComputerPickDetailsNCAAB(total_sheet_data[-1][0], total_sheet_data[-1][1],
                                                           total_sheet_data[-1][2], total_sheet_data[-1][3],
                                                           total_sheet_data[-1][4], total_sheet_data[-1][5],
                                                           total_sheet_data[-1][6], total_sheet_data[-1][7],
                                                           total_sheet_data[-1][8], total_sheet_data[-1][9],
                                                           total_sheet_data[-1][10], total_sheet_data[-1][11],
                                                           total_sheet_data[-1][12])
            session.add(new_computer_detail)

            airtable_ncaab.insert({ComputerPickDetailsNCAAB.table_columns[0]: total_sheet_data[-1][0],
                                   ComputerPickDetailsNCAAB.table_columns[1]: total_sheet_data[-1][1],
                                   ComputerPickDetailsNCAAB.table_columns[2]: total_sheet_data[-1][2],
                                   ComputerPickDetailsNCAAB.table_columns[3]: total_sheet_data[-1][3],
                                   ComputerPickDetailsNCAAB.table_columns[4]: total_sheet_data[-1][4],
                                   ComputerPickDetailsNCAAB.table_columns[5]: total_sheet_data[-1][5],
                                   ComputerPickDetailsNCAAB.table_columns[6]: total_sheet_data[-1][6],
                                   ComputerPickDetailsNCAAB.table_columns[7]: total_sheet_data[-1][7],
                                   ComputerPickDetailsNCAAB.table_columns[8]: total_sheet_data[-1][8],
                                   ComputerPickDetailsNCAAB.table_columns[9]: total_sheet_data[-1][9],
                                   ComputerPickDetailsNCAAB.table_columns[10]: total_sheet_data[-1][10],
                                   ComputerPickDetailsNCAAB.table_columns[11]: total_sheet_data[-1][11],
                                   ComputerPickDetailsNCAAB.table_columns[12]: total_sheet_data[-1][12]})
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
            date_time_info = thead.find_element_by_tag_name('th').text.split(" @ ")
            date_time = date_time_info[0] + " " + date_time_info[1]
            # new_computer_pick = ComputerPicksListNBA(first_team_name_short, first_team_name_long,
            #                                            second_team_name_short, second_team_name_long, date, time)
            # session.add(new_computer_pick)
            # session.flush()
            tbody = computer_table.find_element_by_tag_name('tbody')
            attr_tr_list = tbody.find_elements_by_tag_name('tr')
            predicted_score_tds = attr_tr_list[0].find_elements_by_tag_name('td')
            computer_pick_tds = attr_tr_list[1].find_elements_by_tag_name('td')
            public_consensus_tds = attr_tr_list[2].find_elements_by_tag_name('td')
            consensus_bet_tds = attr_tr_list[3].find_elements_by_tag_name('td')
            total_sheet_data.append((first_team_name_short, first_team_name_long,
                                     second_team_name_short, second_team_name_long, date_time,
                                     predicted_score_tds[1].text,
                                     predicted_score_tds[2].text, computer_pick_tds[1].text,
                                     computer_pick_tds[2].text, public_consensus_tds[1].text,
                                     public_consensus_tds[2].text, consensus_bet_tds[1].text,
                                     consensus_bet_tds[2].text))

            new_computer_detail = ComputerPickDetailsNBA(total_sheet_data[-1][0], total_sheet_data[-1][1],
                                                         total_sheet_data[-1][2], total_sheet_data[-1][3],
                                                         total_sheet_data[-1][4], total_sheet_data[-1][5],
                                                         total_sheet_data[-1][6], total_sheet_data[-1][7],
                                                         total_sheet_data[-1][8], total_sheet_data[-1][9],
                                                         total_sheet_data[-1][10], total_sheet_data[-1][11],
                                                         total_sheet_data[-1][12])
            session.add(new_computer_detail)

            airtable_nba.insert({ComputerPickDetailsNBA.table_columns[0]: total_sheet_data[-1][0],
                                 ComputerPickDetailsNBA.table_columns[1]: total_sheet_data[-1][1],
                                 ComputerPickDetailsNBA.table_columns[2]: total_sheet_data[-1][2],
                                 ComputerPickDetailsNBA.table_columns[3]: total_sheet_data[-1][3],
                                 ComputerPickDetailsNBA.table_columns[4]: total_sheet_data[-1][4],
                                 ComputerPickDetailsNBA.table_columns[5]: total_sheet_data[-1][5],
                                 ComputerPickDetailsNBA.table_columns[6]: total_sheet_data[-1][6],
                                 ComputerPickDetailsNBA.table_columns[7]: total_sheet_data[-1][7],
                                 ComputerPickDetailsNBA.table_columns[8]: total_sheet_data[-1][8],
                                 ComputerPickDetailsNBA.table_columns[9]: total_sheet_data[-1][9],
                                 ComputerPickDetailsNBA.table_columns[10]: total_sheet_data[-1][10],
                                 ComputerPickDetailsNBA.table_columns[11]: total_sheet_data[-1][11],
                                 ComputerPickDetailsNBA.table_columns[12]: total_sheet_data[-1][12]})
    # print(total_sheet_data)
    df = pd.DataFrame(total_sheet_data, columns=ComputerPickDetailsNBA.table_columns)
    wks_nba.set_dataframe(df, (1, 1))


recreate_oddshark_table()
add_oddshark_nba()
add_oddshark_ncaab()

session.commit()
browser.close()
close_connection()
