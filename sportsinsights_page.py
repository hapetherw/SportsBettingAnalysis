from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from models.sportsinsights_model import SportsInsightsBETSIGNALS
from models.sportsinsights_model import SportsInsightsBESTBETS
from database import session
from database import recreate_sportsinsights_table
from database import close_connection
from selenimum_config import get_browser
import time
import pandas as pd
from datetime import datetime
from airtable_init import airtable_sportsinsights_betsignals
from airtable_init import airtable_sportsinsights_bestbets
import google_spread_sheet
from google_spread_sheet import get_work_sheet

wks_bet_signals = get_work_sheet('SportsInsights_BetSignals')
wks_best_bets = get_work_sheet('SportsInsights_BestBets')
browser = get_browser()
browser.maximize_window()
email = 'shanehvizdzak@gmail.com'
password = 'bigboy4!'


def add_bet_signals():
    total_sheet_data = []
    browser.get('https://sportsinsights.actionnetwork.com/login/')
    browser.find_element_by_tag_name('form').find_element_by_name('email').send_keys(email)
    browser.find_element_by_tag_name('form').find_element_by_name('password').send_keys(password)
    browser.find_element_by_tag_name('form').submit()

    try:
        WebDriverWait(browser, 20).until(EC.title_contains('Dashboard'))
        print("Sportsinsights page is ready!")
    except TimeoutException:
        print("Sportsinsights page Loading took too much time!")

    # cookie_list = browser.get_cookies()
    # for cook in cookie_list:
    #     print(cook['name']+" = ", cook['value'])
    # return
    browser.get('https://sportsinsights.actionnetwork.com/bet-signals/')
    time.sleep(8)
    main_tab = browser.find_element_by_id('s1').find_element_by_id(
        'borderLayout_eRootPanel').find_element_by_class_name('ag-body-container')
    div_list = main_tab.find_elements_by_css_selector('.ag-row.ag-row-no-focus')
    for div in div_list:
        cell_list = div.find_elements_by_tag_name('div')
        game_time = cell_list[1].get_attribute('innerHTML')
        play_on = cell_list[3].get_attribute('innerHTML')
        if action_type <= 1:
            db_record = session.query(SportsInsightsBETSIGNALS).filter(
                SportsInsightsBETSIGNALS.GameTime == cell_list[1].get_attribute('innerHTML'),
                SportsInsightsBETSIGNALS.PlayOn == cell_list[3].get_attribute('innerHTML')).first()
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
            if not db_record:
                session.add(new_bet_signals)
                if action_type == 0:
                    total_sheet_data.append((cell_list[0].get_attribute('innerHTML'),
                                             cell_list[1].get_attribute('innerHTML'),
                                             cell_list[2].get_attribute('innerHTML'),
                                             cell_list[3].get_attribute('innerHTML'),
                                             cell_list[4].get_attribute('innerHTML'),
                                             cell_list[5].get_attribute('innerHTML'),
                                             cell_list[6].get_attribute('innerHTML'),
                                             cell_list[7].get_attribute('innerHTML').replace(
                                                 '<b>', '').replace('</b>', ''),
                                             cell_list[8].get_attribute('innerHTML')))
            else:
                new_bet_signals.ID = db_record.ID
                session.merge(new_bet_signals)
            print(new_bet_signals)
        if action_type == 0 or action_type == 2:
            formula_str = 'AND(SUBSTITUTE({PlayOn}, "\'", " ")="' + \
                          play_on.replace("'", " ") + \
                          '", {GameTime}="' + game_time + '")'
            fields = {
                "TriggerTime": cell_list[0].get_attribute('innerHTML'),
                "GameTime": cell_list[1].get_attribute('innerHTML'),
                "Signal": cell_list[2].get_attribute('innerHTML'),
                "PlayOn": cell_list[3].get_attribute('innerHTML'),
                "BetType": cell_list[4].get_attribute('innerHTML'),
                "TriggerBook": cell_list[5].get_attribute('innerHTML'),
                "TriggerUnits": cell_list[6].get_attribute('innerHTML'),
                "Score": cell_list[7].get_attribute('innerHTML').replace(
                    '<b>', '').replace('</b>', ''),
                "Result": cell_list[8].get_attribute('innerHTML'),
            }
            record = airtable_sportsinsights_betsignals.get_all(formula=formula_str)
            if record:
                airtable_sportsinsights_betsignals.replace(record[0]['id'], fields)
            else:
                airtable_sportsinsights_betsignals.insert(fields)
    if action_type == 0 and len(total_sheet_data) > 0:  # store into gsheet
        df = pd.DataFrame(total_sheet_data, columns=SportsInsightsBETSIGNALS.gsheet_table_columns)
        original_df = wks_bet_signals.get_as_df()
        original_df = original_df.append(df)
        wks_bet_signals.set_dataframe(original_df, (1, 1))


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


action_type = 0
print(datetime.now().isoformat(), "SportsInsights work")
if action_type <= 1:
    recreate_sportsinsights_table()
    print("Bet Signals work")
    add_bet_signals()
    print("Best Bets work")
    # add_best_bets()
    #
    session.commit()
    browser.close()
    close_connection()
elif action_type == 2:
    print("Bet Signals work")
    add_bet_signals()
    print("Bet Signals work")
    add_best_bets()

    browser.close()
    close_connection()
print("Finished SportsInsights work")
