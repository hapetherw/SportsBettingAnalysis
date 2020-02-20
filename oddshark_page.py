from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from models.computer_pick_models import ComputerPickDetailsNCAAB
from models.computer_pick_models import ComputerPickDetailsNBA
import datetime
# from database import session
# from database import recreate_oddshark_table
# from database import close_connection
# import pandas as pd
from airtable_init import airtable_ncaab
from airtable_init import airtable_nba
from airtable_init import airtable_ncaa_team
from airtable_init import airtable_nba_team
from airtable_init import airtable_game_date
from airtable_init import airtable_game_time
from airtable_init import oddshark_ncaa_info
from airtable_init import oddshark_nba_info
from airtable_init import ncaa_team_info
from airtable_init import nba_team_info
from airtable_init import game_date_info
from airtable_init import game_time_info
from config import SERVER_ENVIRONMENT
# import google_spread_sheet
# from google_spread_sheet import get_work_sheet

if SERVER_ENVIRONMENT:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = '/usr/bin/google-chrome'

    chrome_driver = '/usr/bin/chromedriver'
    browser = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
else:
    browser = webdriver.Chrome('chromedriver.exe')
browser.maximize_window()
# wks_nba = get_work_sheet('OddShark_NBA')
# wks_ncaab = get_work_sheet('OddShark_NCAAB')


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
            date_time_ary = thead.find_element_by_tag_name('th').text.split(" @ ")
            date_time = date_time_ary[0] + " " + date_time_ary[1]
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
            # if action_type <= 1:  # store to db
            #     new_computer_detail = ComputerPickDetailsNCAAB(total_sheet_data[-1][0], total_sheet_data[-1][1],
            #                                                    total_sheet_data[-1][2], total_sheet_data[-1][3],
            #                                                    total_sheet_data[-1][4], total_sheet_data[-1][5],
            #                                                    total_sheet_data[-1][6], total_sheet_data[-1][7],
            #                                                    total_sheet_data[-1][8], total_sheet_data[-1][9],
            #                                                    total_sheet_data[-1][10], total_sheet_data[-1][11],
            #                                                    total_sheet_data[-1][12])
            #     session.add(new_computer_detail)

            if action_type == 0 | action_type == 3:  # store to airtable
                ncaa_first_team = airtable_ncaa_team.match(ncaa_team_info[0], first_team_name_short)
                ncaa_second_team = airtable_ncaa_team.match(ncaa_team_info[0], second_team_name_short)
                if not ncaa_first_team:
                    first_team = airtable_ncaa_team.insert({ncaa_team_info[0]: first_team_name_short,
                                                            ncaa_team_info[1]: first_team_name_long})
                else:
                    first_team = airtable_ncaa_team.update(ncaa_first_team['id'],
                                                           {ncaa_team_info[0]: first_team_name_short,
                                                            ncaa_team_info[1]: first_team_name_long})
                if not ncaa_second_team:
                    second_team = airtable_ncaa_team.insert({ncaa_team_info[0]: second_team_name_short,
                                                             ncaa_team_info[1]: second_team_name_long})
                else:
                    second_team = airtable_ncaa_team.update(ncaa_second_team['id'],
                                                            {ncaa_team_info[0]: second_team_name_short,
                                                             ncaa_team_info[1]: second_team_name_long})
                insert_date_time = date_time_ary[0] + ' ' + str(datetime.datetime.now().year)
                insert_date_time = datetime.datetime.strptime(insert_date_time, '%b %d %Y').date()
                insert_date_time = str(insert_date_time)
                game_date = airtable_game_date.match(game_date_info[0], insert_date_time)
                if not game_date:
                    game_date = airtable_game_date.insert({game_date_info[0]: insert_date_time})

                game_time = airtable_game_time.match(game_time_info[0], date_time_ary[1])
                if not game_time:
                    game_time = airtable_game_time.insert({game_time_info[0]: date_time_ary[1]})
                formula_str = "AND(Team1='" + first_team_name_short + "', Team2='" + second_team_name_short + \
                              "', Date='" + insert_date_time + "', Time='" + date_time_ary[1] + "')"
                if len(airtable_ncaab.get_all(formula=formula_str)) == 0:
                    airtable_ncaab.insert({oddshark_ncaa_info[0]: [first_team['id']],
                                           oddshark_ncaa_info[1]: [second_team['id']],
                                           oddshark_ncaa_info[2]: [game_date['id']],
                                           oddshark_ncaa_info[3]: [game_time['id']],
                                           oddshark_ncaa_info[4]: predicted_score_tds[1].text,
                                           oddshark_ncaa_info[5]: predicted_score_tds[2].text,
                                           oddshark_ncaa_info[6]: computer_pick_tds[1].text,
                                           oddshark_ncaa_info[7]: computer_pick_tds[2].text,
                                           oddshark_ncaa_info[8]: public_consensus_tds[1].text,
                                           oddshark_ncaa_info[9]: public_consensus_tds[2].text,
                                           oddshark_ncaa_info[10]: consensus_bet_tds[1].text,
                                           oddshark_ncaa_info[11]: consensus_bet_tds[2].text})
    # if action_type == 0 | action_type == 2:  # store to gsheet
    #     df = pd.DataFrame(total_sheet_data, columns=ComputerPickDetailsNCAAB.table_columns)
    #     wks_ncaab.set_dataframe(df, (1, 1))


def add_oddshark_nba():
    browser.get('https://www.oddsshark.com/nba/computer-picks')
    block_system_main = browser.find_element_by_id("block-system-main")
    computer_tables = block_system_main.find_elements_by_css_selector('.table.table--striped.table--fixed-column')
    total_sheet_data = []
    print(len(computer_tables))
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
            date_time_ary = thead.find_element_by_tag_name('th').text.split(" @ ")
            date_time = date_time_ary[0] + " " + date_time_ary[1]
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
            # if action_type <= 1:  # store to db
            #     new_computer_detail = ComputerPickDetailsNBA(total_sheet_data[-1][0], total_sheet_data[-1][1],
            #                                                  total_sheet_data[-1][2], total_sheet_data[-1][3],
            #                                                  total_sheet_data[-1][4], total_sheet_data[-1][5],
            #                                                  total_sheet_data[-1][6], total_sheet_data[-1][7],
            #                                                  total_sheet_data[-1][8], total_sheet_data[-1][9],
            #                                                  total_sheet_data[-1][10], total_sheet_data[-1][11],
            #                                                  total_sheet_data[-1][12])
            #     session.add(new_computer_detail)
            if action_type == 0 | action_type == 3:  # store to airtable
                nba_first_team = airtable_nba_team.match(nba_team_info[0], first_team_name_short)
                nba_second_team = airtable_nba_team.match(nba_team_info[0], second_team_name_short)
                if not nba_first_team:
                    first_team = airtable_nba_team.insert({nba_team_info[0]: first_team_name_short,
                                                           nba_team_info[1]: first_team_name_long})
                else:
                    first_team = airtable_nba_team.update(nba_first_team['id'],
                                                          {nba_team_info[0]: first_team_name_short,
                                                           nba_team_info[1]: first_team_name_long})
                if not nba_second_team:
                    second_team = airtable_nba_team.insert({nba_team_info[0]: second_team_name_short,
                                                            nba_team_info[1]: second_team_name_long})
                else:
                    second_team = airtable_nba_team.update(nba_second_team['id'],
                                                           {nba_team_info[0]: second_team_name_short,
                                                            nba_team_info[1]: second_team_name_long})
                insert_date_time = date_time_ary[0] + ' ' + str(datetime.datetime.now().year)
                insert_date_time = datetime.datetime.strptime(insert_date_time, '%b %d %Y').date()
                insert_date_time = str(insert_date_time)
                game_date = airtable_game_date.match(game_date_info[0], insert_date_time)
                if not game_date:
                    game_date = airtable_game_date.insert({game_date_info[0]: insert_date_time})

                game_time = airtable_game_time.match(game_time_info[0], date_time_ary[1])
                if not game_time:
                    game_time = airtable_game_time.insert({game_time_info[0]: date_time_ary[1]})
                formula_str = "AND(Team1='" + first_team_name_short + "', Team2='" + second_team_name_short + \
                              "', Date='" + insert_date_time + "', Time='" + date_time_ary[1] + "')"
                if len(airtable_nba.get_all(formula=formula_str)) == 0:
                    airtable_nba.insert({oddshark_nba_info[0]: [first_team['id']],
                                         oddshark_nba_info[1]: [second_team['id']],
                                         oddshark_nba_info[2]: [game_date['id']],
                                         oddshark_nba_info[3]: [game_time['id']],
                                         oddshark_nba_info[4]: predicted_score_tds[1].text,
                                         oddshark_nba_info[5]: predicted_score_tds[2].text,
                                         oddshark_nba_info[6]: computer_pick_tds[1].text,
                                         oddshark_nba_info[7]: computer_pick_tds[2].text,
                                         oddshark_nba_info[8]: public_consensus_tds[1].text,
                                         oddshark_nba_info[9]: public_consensus_tds[2].text,
                                         oddshark_nba_info[10]: consensus_bet_tds[1].text,
                                         oddshark_nba_info[11]: consensus_bet_tds[2].text})
    # if action_type == 0 | action_type == 2:  # store to gsheet
    #     df = pd.DataFrame(total_sheet_data, columns=ComputerPickDetailsNBA.table_columns)
    #     wks_nba.set_dataframe(df, (1, 1))


action_type = 3
print("Start Oddshark work")
# if action_type == 0:
#     recreate_oddshark_table()
#     print("Oddshark-NBA work")
#     add_oddshark_nba()
#     print("Oddshark-NCAA work")
#     add_oddshark_ncaab()
#     session.commit()
#     browser.close()
#     close_connection()
# else:
print("Oddshark-NBA work")
add_oddshark_nba()
print("Oddshark-NCAA work")
add_oddshark_ncaab()
browser.close()
print("Finished Oddshark work")
# exit()
