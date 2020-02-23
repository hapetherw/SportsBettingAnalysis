import datetime
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
# from models.curated_picks_model import CuratedPicksNCAAB
# from models.curated_picks_model import CuratedPicksNBA
# from models.curated_picks_model import CuratedPicksWiseNBA
# from models.curated_picks_model import CuratedPicksWiseNCAAB
# from database import session
# from database import recreate_curated_picks_table
# from database import close_connection
import time
from airtable_init import airtable_ncaa_team
from airtable_init import airtable_nba_team
from airtable_init import airtable_teamranking_ncaa
from airtable_init import airtable_teamranking_nba
from airtable_init import airtable_pickwise_ncaa
from airtable_init import airtable_pickwise_nba
from airtable_init import airtable_game_date
from airtable_init import airtable_game_time
from airtable_init import ncaa_team_info
from airtable_init import nba_team_info
from airtable_init import teamranking_ncaa_info
from airtable_init import teamranking_nba_info
from airtable_init import pickwise_ncaa_info
from airtable_init import pickwise_nba_info
from airtable_init import game_date_info
from airtable_init import game_time_info
from selenimum_config import browser
browser.maximize_window()


def add_curated_picks_ncaab():
    browser.get('https://www.teamrankings.com/ncaa-basketball-betting-picks/')
    time.sleep(3)
    body = browser.find_element_by_id('DataTables_Table_0').find_element_by_tag_name('tbody')
    tr_list = body.find_elements_by_tag_name('tr')
    first_td_list = tr_list[0].find_elements_by_tag_name('td')
    if len(first_td_list) == 1:
        print("no TeamRanking-NCAA data")
        return
    date = Select(browser.find_element_by_class_name('redirectOnChange')).first_selected_option.text
    date_info = date.split(' ')[1] + "," + date.split(' ')[2] + "," + str(datetime.datetime.now().year)
    date = datetime.datetime.strptime(date_info, '%b,%d,%Y').date()
    date = str(date)
    for tr in tr_list:
        td_list = tr.find_elements_by_tag_name('td')
        rot_list = td_list[0].get_attribute('innerHTML').strip().split('<br>')
        team_list = td_list[1].get_attribute('innerHTML').strip().split('<br>')
        team_list[0] = team_list[0].strip()
        team_list[1] = team_list[1].strip()
        game_winner = td_list[2].find_element_by_class_name('picks-block-in').text.strip()
        ATS = td_list[3].find_element_by_class_name('picks-block-in').text.strip()
        total = td_list[4].find_element_by_class_name('picks-block-in').text.strip()
        money_line_value = td_list[5].find_element_by_class_name('picks-block-in').text.strip()
        # if action_type == 1:
        #     new_curated_picks_ncabb = CuratedPicksNCAAB(team_list[0], rot_list[0], team_list[1], rot_list[1],
        #                                                 game_winner, ATS, total, money_line_value, date)
        #     session.add(new_curated_picks_ncabb)
        if action_type == 2:
            team1_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                                team_list[0].replace("'", " ") + '", SUBSTITUTE({' + \
                                ncaa_team_info[1] + '}, "\'", " ")="' + \
                                team_list[0].replace("'", " ") + '")'
            team2_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                                team_list[1].replace("'", " ") + '", SUBSTITUTE({' + \
                                ncaa_team_info[1] + '}, "\'", " ")="' + \
                                team_list[1].replace("'", " ") + '")'
            ncaa_first_team = airtable_ncaa_team.get_all(formula=team1_formula_str)
            ncaa_second_team = airtable_ncaa_team.get_all(formula=team2_formula_str)
            if not ncaa_first_team:
                ncaa_first_team = airtable_ncaa_team.insert(
                    {ncaa_team_info[0]: team_list[0]})
            else:
                ncaa_first_team = ncaa_first_team[0]
            if not ncaa_second_team:
                ncaa_second_team = airtable_ncaa_team.insert(
                    {ncaa_team_info[0]: team_list[1]})
            else:
                ncaa_second_team = ncaa_second_team[0]
            game_date = airtable_game_date.match(game_date_info[0], date)
            if not game_date:
                game_date = airtable_game_date.insert({game_date_info[0]: date})
            formula_str = 'AND(SUBSTITUTE({Team1}, "\'", " ")="' + \
                          ncaa_first_team['fields']['NCAA Team Name'].replace("'", " ") + \
                          '", SUBSTITUTE({Team2}, "\'", " ")="' + \
                          ncaa_second_team['fields']['NCAA Team Name'].replace("'", " ") + '", {Date}="' + date + '")'
            # print(formula_str)
            if len(airtable_teamranking_ncaa.get_all(formula=formula_str)) == 0:
                airtable_teamranking_ncaa.insert({teamranking_ncaa_info[0]: [ncaa_first_team['id']],
                                                  teamranking_ncaa_info[1]: [ncaa_second_team['id']],
                                                  teamranking_ncaa_info[2]: [game_date['id']],
                                                  teamranking_ncaa_info[3]: int(rot_list[0]),
                                                  teamranking_ncaa_info[4]: int(rot_list[1]),
                                                  teamranking_ncaa_info[5]: game_winner,
                                                  teamranking_ncaa_info[6]: ATS,
                                                  teamranking_ncaa_info[7]: total,
                                                  teamranking_ncaa_info[8]: money_line_value})


def add_curated_picks_nba():
    browser.get('https://www.teamrankings.com/nba-betting-picks/')
    time.sleep(3)
    body = browser.find_element_by_id('DataTables_Table_0').find_element_by_tag_name('tbody')
    tr_list = body.find_elements_by_tag_name('tr')
    first_td_list = tr_list[0].find_elements_by_tag_name('td')
    if len(first_td_list) == 1:
        print("no TeamRanking-NBA data")
        return
    date = Select(browser.find_element_by_class_name('redirectOnChange')).first_selected_option.text
    date_info = date.split(' ')[1] + "," + date.split(' ')[2] + "," + str(datetime.datetime.now().year)
    date = datetime.datetime.strptime(date_info, '%b,%d,%Y').date()
    date = str(date)
    for tr in tr_list:
        td_list = tr.find_elements_by_tag_name('td')
        rot_list = td_list[0].get_attribute('innerHTML').strip().split('<br>')
        team_list = td_list[1].get_attribute('innerHTML').strip().split('<br>')
        team_list[0] = team_list[0].strip()
        team_list[1] = team_list[1].strip()
        game_winner = td_list[2].find_element_by_class_name('picks-block-in').text.strip()
        ATS = td_list[3].find_element_by_class_name('picks-block-in').text.strip()
        total = td_list[4].find_element_by_class_name('picks-block-in').text.strip()
        money_line_value = td_list[5].find_element_by_class_name('picks-block-in').text.strip()
        # if action_type == 1:
        #     new_curated_picks_nba = CuratedPicksNBA(team_list[0], rot_list[0], team_list[1], rot_list[1], game_winner,
        #                                             ATS, total, money_line_value, date)
        #     session.add(new_curated_picks_nba)
        if action_type == 2:
            team1_formula_str = 'OR(SUBSTITUTE({' + nba_team_info[0] + '}, "\'", " ")="' + \
                                team_list[0].replace("'", " ") + '", SUBSTITUTE({' + \
                                nba_team_info[1] + '}, "\'", " ")="' + \
                                team_list[0].replace("'", " ") + '")'
            team2_formula_str = 'OR(SUBSTITUTE({' + nba_team_info[0] + '}, "\'", " ")="' + \
                                team_list[1].replace("'", " ") + '", SUBSTITUTE({' + \
                                nba_team_info[1] + '}, "\'", " ")="' + \
                                team_list[1].replace("'", " ") + '")'
            nba_first_team = airtable_nba_team.get_all(formula=team1_formula_str)
            nba_second_team = airtable_nba_team.get_all(formula=team2_formula_str)
            if not nba_first_team:
                nba_first_team = airtable_nba_team.insert(
                    {nba_team_info[0]: team_list[0]})
            else:
                nba_first_team = nba_first_team[0]
            if not nba_second_team:
                nba_second_team = airtable_nba_team.insert(
                    {nba_team_info[0]: team_list[1]})
            else:
                nba_second_team = nba_second_team[0]
            game_date = airtable_game_date.match(game_date_info[0], date)
            if not game_date:
                game_date = airtable_game_date.insert({game_date_info[0]: date})
            formula_str = 'AND(SUBSTITUTE({Team1}, "\'", " ")="' + \
                          nba_first_team['fields']['NBA Team Name'].replace("'", " ") + \
                          '", SUBSTITUTE({Team2}, "\'", " ")="' + \
                          nba_second_team['fields']['NBA Team Name'].replace("'", " ") + '", {Date}="' + date + '")'
            # print(formula_str)
            if len(airtable_teamranking_nba.get_all(formula=formula_str)) == 0:
                airtable_teamranking_nba.insert({teamranking_nba_info[0]: [nba_first_team['id']],
                                                 teamranking_nba_info[1]: [nba_second_team['id']],
                                                 teamranking_nba_info[2]: [game_date['id']],
                                                 teamranking_nba_info[3]: int(rot_list[0]),
                                                 teamranking_nba_info[4]: int(rot_list[1]),
                                                 teamranking_nba_info[5]: game_winner,
                                                 teamranking_nba_info[6]: ATS,
                                                 teamranking_nba_info[7]: total,
                                                 teamranking_nba_info[8]: money_line_value})


def add_curated_picks_wise_nba():
    browser.get('https://www.pickswise.com/sports/nba/')
    div_list = browser.find_elements_by_css_selector('.ContentPanel.ContentPanel--block.ContentPanel--no-padding')

    for div in div_list:
        datetime_info = div.find_element_by_tag_name('h2').get_attribute('innerHTML').strip()
        if '<br>' not in datetime_info:
            continue
        datetime_info = datetime_info.split('<br>')[0]
        datetime_info = datetime_info.strip()
        datetime_info = datetime_info.split(', ')[1]
        date = datetime_info.split(' - ')[0][:-2]
        time = datetime_info.split(' - ')[1]
        time = time.split(' ')[0]
        date = date + "," + str(datetime.datetime.now().year)
        date = datetime.datetime.strptime(date, '%b %d,%Y').date()
        date = str(date)
        try:
            team_list = div.find_element_by_class_name('PreviewCard__teams-container').find_elements_by_class_name(
                'Pick')
            first_team_name = team_list[0].find_element_by_class_name('Pick__team-name').text
            second_team_name = team_list[1].find_element_by_class_name('Pick__team-name').text
            first_team_name = first_team_name.strip()
            second_team_name = second_team_name.strip()
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
            # if action_type == 1:
            #     new_curated_picks_wise_nba = CuratedPicksWiseNBA(first_team_name, first_team_prediction,
            #                                                      first_team_pick_outcome, first_team_pick_market,
            #                                                      second_team_name, second_team_prediction,
            #                                                      second_team_pick_outcome, second_team_pick_market,
            #                                                      date)
            #     session.add(new_curated_picks_wise_nba)
            if action_type == 2:
                team1_formula_str = 'OR(SUBSTITUTE({' + nba_team_info[0] + '}, "\'", " ")="' + \
                                    first_team_name.replace("'", " ") + '", SUBSTITUTE({' + \
                                    nba_team_info[1] + '}, "\'", " ")="' + \
                                    second_team_name.replace("'", " ") + '")'
                team2_formula_str = 'OR(SUBSTITUTE({' + nba_team_info[0] + '}, "\'", " ")="' + \
                                    first_team_name.replace("'", " ") + '", SUBSTITUTE({' + \
                                    nba_team_info[1] + '}, "\'", " ")="' + \
                                    second_team_name.replace("'", " ") + '")'
                nba_first_team = airtable_nba_team.get_all(formula=team1_formula_str)
                nba_second_team = airtable_nba_team.get_all(formula=team2_formula_str)
                if not nba_first_team:
                    nba_first_team = airtable_nba_team.insert(
                        {nba_team_info[0]: first_team_name})
                else:
                    nba_first_team = nba_first_team[0]
                if not nba_second_team:
                    nba_second_team = airtable_nba_team.insert(
                        {nba_team_info[0]: second_team_name})
                else:
                    nba_second_team = nba_second_team[0]
                game_date = airtable_game_date.match(game_date_info[0], date)
                if not game_date:
                    game_date = airtable_game_date.insert({game_date_info[0]: date})
                game_time = airtable_game_time.match(game_time_info[0], time)
                if not game_time:
                    game_time = airtable_game_time.insert({game_time_info[0]: time})
                formula_str = 'AND(SUBSTITUTE({Team1}, "\'", " ")="' + \
                              nba_first_team['fields']['NBA Team Name'].replace("'", " ") + \
                              '", SUBSTITUTE({Team2}, "\'", " ")="' + \
                              nba_second_team['fields']['NBA Team Name'].replace("'",
                                                                                 " ") + '", {Date}="' + date + '")'
                if len(airtable_pickwise_nba.get_all(formula=formula_str)) == 0:
                    airtable_pickwise_nba.insert({pickwise_nba_info[0]: [nba_first_team['id']],
                                                  pickwise_nba_info[1]: [nba_second_team['id']],
                                                  pickwise_nba_info[2]: [game_date['id']],
                                                  pickwise_nba_info[3]: [game_time['id']],
                                                  pickwise_nba_info[4]: first_team_prediction,
                                                  pickwise_nba_info[5]: second_team_prediction,
                                                  pickwise_nba_info[6]: first_team_pick_outcome,
                                                  pickwise_nba_info[7]: second_team_pick_outcome,
                                                  pickwise_nba_info[8]: first_team_pick_market,
                                                  pickwise_nba_info[9]: second_team_pick_market})
        except NoSuchElementException:
            print("No Pickwise NBA data")
            continue


def add_curated_picks_wise_ncaab():
    browser.get('https://www.pickswise.com/sports/college-basketball/')
    div_list = browser.find_elements_by_css_selector('.ContentPanel.ContentPanel--block.ContentPanel--no-padding')

    for div in div_list:
        datetime_info = div.find_element_by_tag_name('h2').get_attribute('innerHTML').strip()
        if '<br>' not in datetime_info:
            continue
        datetime_info = datetime_info.split('<br>')[0]
        datetime_info = datetime_info.strip()
        datetime_info = datetime_info.split(', ')[1]
        date = datetime_info.split(' - ')[0][:-2]
        time = datetime_info.split(' - ')[1]
        time = time.split(' ')[0]
        date = date + "," + str(datetime.datetime.now().year)
        date = datetime.datetime.strptime(date, '%b %d,%Y').date()
        date = str(date)
        try:
            team_list = div.find_element_by_class_name('PreviewCard__teams-container').find_elements_by_class_name(
                'Pick')
            first_team_name = team_list[0].find_element_by_class_name('Pick__team-name').text
            second_team_name = team_list[1].find_element_by_class_name('Pick__team-name').text
            first_team_name = first_team_name.strip()
            second_team_name = second_team_name.strip()
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
            # if action_type == 1:
            #     new_curated_picks_wise_ncaab = CuratedPicksWiseNCAAB(first_team_name, first_team_prediction,
            #                                                          first_team_pick_outcome, first_team_pick_market,
            #                                                          second_team_name, second_team_prediction,
            #                                                          second_team_pick_outcome, second_team_pick_market,
            #                                                          date)
            #     session.add(new_curated_picks_wise_ncaab)
            if action_type == 2:
                team1_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                                    first_team_name.replace("'", " ") + '", SUBSTITUTE({' + \
                                    ncaa_team_info[1] + '}, "\'", " ")="' + \
                                    first_team_name.replace("'", " ") + '")'
                team2_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                                    second_team_name.replace("'", " ") + '", SUBSTITUTE({' + \
                                    ncaa_team_info[1] + '}, "\'", " ")="' + \
                                    second_team_name.replace("'", " ") + '")'
                ncaa_first_team = airtable_ncaa_team.get_all(formula=team1_formula_str)
                ncaa_second_team = airtable_ncaa_team.get_all(formula=team2_formula_str)
                if not ncaa_first_team:
                    ncaa_first_team = airtable_ncaa_team.insert(
                        {ncaa_team_info[0]: first_team_name})
                else:
                    ncaa_first_team = ncaa_first_team[0]
                if not ncaa_second_team:
                    ncaa_second_team = airtable_ncaa_team.insert(
                        {ncaa_team_info[0]: second_team_name})
                else:
                    ncaa_second_team = ncaa_second_team[0]
                game_date = airtable_game_date.match(game_date_info[0], date)
                if not game_date:
                    game_date = airtable_game_date.insert({game_date_info[0]: date})
                game_time = airtable_game_time.match(game_time_info[0], time)
                if not game_time:
                    game_time = airtable_game_time.insert({game_time_info[0]: time})
                formula_str = 'AND(SUBSTITUTE({Team1}, "\'", " ")="' + \
                              ncaa_first_team['fields']['NCAA Team Name'].replace("'", " ") + \
                              '", SUBSTITUTE({Team2}, "\'", " ")="' + \
                              ncaa_second_team['fields']['NCAA Team Name'].replace("'",
                                                                                   " ") + '", {Date}="' + date + '")'
                if len(airtable_pickwise_ncaa.get_all(formula=formula_str)) == 0:
                    airtable_pickwise_ncaa.insert({pickwise_ncaa_info[0]: [ncaa_first_team['id']],
                                                   pickwise_ncaa_info[1]: [ncaa_second_team['id']],
                                                   pickwise_ncaa_info[2]: [game_date['id']],
                                                   pickwise_ncaa_info[3]: [game_time['id']],
                                                   pickwise_ncaa_info[4]: first_team_prediction,
                                                   pickwise_ncaa_info[5]: second_team_prediction,
                                                   pickwise_ncaa_info[6]: first_team_pick_outcome,
                                                   pickwise_ncaa_info[7]: second_team_pick_outcome,
                                                   pickwise_ncaa_info[8]: first_team_pick_market,
                                                   pickwise_ncaa_info[9]: second_team_pick_market})
        except NoSuchElementException:
            print("No Pickwise NCAAB data")
            continue


print(datetime.datetime.now().isoformat(), "Start Curated picks work")
action_type = 2
# if action_type == 1:
#     recreate_curated_picks_table()
#     add_curated_picks_ncaab()
#     add_curated_picks_nba()
#     print("Finished TeamRanking work")
#     add_curated_picks_wise_ncaab()
#     add_curated_picks_wise_nba()
#
#     session.commit()
#     browser.close()
#     close_connection()
# else:
add_curated_picks_ncaab()
add_curated_picks_nba()
print("Finished TeamRanking work")
add_curated_picks_wise_ncaab()
add_curated_picks_wise_nba()

browser.close()
print("Finished PickWise work")
