from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from models.curated_picks_model import CuratedPicksNCAAB
from models.curated_picks_model import CuratedPicksNBA
from models.curated_picks_model import CuratedPicksWiseNBA
from models.curated_picks_model import CuratedPicksWiseNCAAB
from database import session
from database import recreate_curated_picks_table
from database import close_connection

browser = webdriver.Chrome('chromedriver.exe')


def add_curated_picks_ncaab():
    browser.get('https://www.teamrankings.com/ncaa-basketball-betting-picks/')
    date = Select(browser.find_element_by_class_name('redirectOnChange')).first_selected_option.text
    body = browser.find_element_by_id('DataTables_Table_0').find_element_by_tag_name('tbody')
    tr_list = body.find_elements_by_tag_name('tr')
    for tr in tr_list:
        td_list = tr.find_elements_by_tag_name('td')
        rot_list = td_list[0].get_attribute('innerHTML').strip().split('<br>')
        team_list = td_list[1].get_attribute('innerHTML').strip().split('<br>')
        game_winner = td_list[2].find_element_by_class_name('picks-block-in').text.strip()
        ATS = td_list[3].find_element_by_class_name('picks-block-in').text.strip()
        total = td_list[4].find_element_by_class_name('picks-block-in').text.strip()
        money_line_value = td_list[5].find_element_by_class_name('picks-block-in').text.strip()
        new_curated_picks_ncabb = CuratedPicksNCAAB(team_list[0], rot_list[0], team_list[1], rot_list[1], game_winner,
                                                    ATS, total, money_line_value, date)
        session.add(new_curated_picks_ncabb)


def add_curated_picks_nba():
    browser.get('https://www.teamrankings.com/nba-betting-picks/')
    date = Select(browser.find_element_by_class_name('redirectOnChange')).first_selected_option.text
    body = browser.find_element_by_id('DataTables_Table_0').find_element_by_tag_name('tbody')
    tr_list = body.find_elements_by_tag_name('tr')
    for tr in tr_list:
        td_list = tr.find_elements_by_tag_name('td')
        rot_list = td_list[0].get_attribute('innerHTML').strip().split('<br>')
        team_list = td_list[1].get_attribute('innerHTML').strip().split('<br>')
        game_winner = td_list[2].find_element_by_class_name('picks-block-in').text.strip()
        ATS = td_list[3].find_element_by_class_name('picks-block-in').text.strip()
        total = td_list[4].find_element_by_class_name('picks-block-in').text.strip()
        money_line_value = td_list[5].find_element_by_class_name('picks-block-in').text.strip()
        new_curated_picks_nba = CuratedPicksNBA(team_list[0], rot_list[0], team_list[1], rot_list[1], game_winner,
                                                ATS, total, money_line_value, date)
        session.add(new_curated_picks_nba)


def add_curated_picks_wise_nba():
    browser.get('https://www.pickswise.com/sports/nba/')
    div_list = browser.find_elements_by_css_selector('.ContentPanel.ContentPanel--block.ContentPanel--no-padding')

    for div in div_list:
        date = div.find_element_by_tag_name('h2').get_attribute('innerHTML').strip().split('<br>')[0]
        try:
            team_list = div.find_element_by_class_name('PreviewCard__teams-container').find_elements_by_class_name('Pick')
            first_team_name = team_list[0].find_element_by_class_name('Pick__team-name').text
            second_team_name = team_list[1].find_element_by_class_name('Pick__team-name').text
            pick_list = div.find_element_by_css_selector('.TabbedContent__tab.TabbedContent__tab--active') \
                .find_elements_by_class_name('Pick')
            first_team_pick_outcome = pick_list[0].find_element_by_class_name('Pick__outcome').get_attribute('innerHTML')
            first_team_pick_market = pick_list[0].find_element_by_class_name('Pick__market').get_attribute('innerHTML')
            first_team_prediction = pick_list[0].find_element_by_css_selector('.Button.Button--border-red').get_attribute(
                'innerHTML')
            second_team_pick_outcome = pick_list[1].find_element_by_class_name('Pick__outcome').get_attribute('innerHTML')
            second_team_pick_market = pick_list[1].find_element_by_class_name('Pick__market').get_attribute('innerHTML')
            second_team_prediction = pick_list[1].find_element_by_css_selector('.Button.Button--border-red').get_attribute(
                'innerHTML')
            new_curated_picks_wise_nba = CuratedPicksWiseNBA(first_team_name, first_team_prediction,
                                                             first_team_pick_outcome, first_team_pick_market,
                                                             second_team_name, second_team_prediction,
                                                             second_team_pick_outcome, second_team_pick_market, date)
            session.add(new_curated_picks_wise_nba)
        except NoSuchElementException:
            print("No Pickwise NBA data")
            continue


def add_curated_picks_wise_ncaab():
    browser.get('https://www.pickswise.com/sports/college-basketball/')
    div_list = browser.find_elements_by_css_selector('.ContentPanel.ContentPanel--block.ContentPanel--no-padding')

    for div in div_list:
        date = div.find_element_by_tag_name('h2').get_attribute('innerHTML').strip().split('<br>')[0]
        try:
            team_list = div.find_element_by_class_name('PreviewCard__teams-container').find_elements_by_class_name(
                'Pick')
            first_team_name = team_list[0].find_element_by_class_name('Pick__team-name').text
            second_team_name = team_list[1].find_element_by_class_name('Pick__team-name').text
            pick_list = div.find_element_by_css_selector('.TabbedContent__tab.TabbedContent__tab--active') \
                .find_elements_by_class_name('Pick')
            first_team_pick_outcome = pick_list[0].find_element_by_class_name('Pick__outcome').get_attribute(
                'innerHTML')
            first_team_pick_market = pick_list[0].find_element_by_class_name('Pick__market').get_attribute('innerHTML')
            first_team_prediction = pick_list[0].find_element_by_css_selector(
                '.Button.Button--border-red').get_attribute(
                'innerHTML')
            second_team_pick_outcome = pick_list[1].find_element_by_class_name('Pick__outcome').get_attribute(
                'innerHTML')
            second_team_pick_market = pick_list[1].find_element_by_class_name('Pick__market').get_attribute('innerHTML')
            second_team_prediction = pick_list[1].find_element_by_css_selector(
                '.Button.Button--border-red').get_attribute(
                'innerHTML')
            new_curated_picks_wise_ncaab = CuratedPicksWiseNCAAB(first_team_name, first_team_prediction,
                                                                 first_team_pick_outcome, first_team_pick_market,
                                                                 second_team_name, second_team_prediction,
                                                                 second_team_pick_outcome, second_team_pick_market,
                                                                 date)
            session.add(new_curated_picks_wise_ncaab)
        except NoSuchElementException:
            print("No Pickwise NCAAB data")
            continue


recreate_curated_picks_table()
add_curated_picks_ncaab()
add_curated_picks_nba()

add_curated_picks_wise_ncaab()
add_curated_picks_wise_nba()

session.commit()
browser.close()
close_connection()
