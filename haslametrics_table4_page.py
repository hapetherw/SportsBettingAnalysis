from selenium import webdriver
from models.hasla_metrics_model import TeamScoreHASLAMETRICS
from database import session
from database import recreate_hasla_metrics_table
from database import close_connection

browser = webdriver.Chrome('chromedriver.exe')
browser.get('http://haslametrics.com/ratings.php')


def add_team_score():
    date_selections = browser.find_element_by_id('cboUpcomingDates')
    date = date_selections.find_elements_by_tag_name('option')[0].get_attribute('innerHTML')
    table = browser.find_element_by_id('myTable4')
    td_list = table.find_elements_by_xpath('//*[starts-with(@id, "tdUpcoming_") and not(contains(@class, "filler"))]')
    new_team_scores = [TeamScoreHASLAMETRICS(), TeamScoreHASLAMETRICS(), TeamScoreHASLAMETRICS(),
                       TeamScoreHASLAMETRICS()]
    new_team_scores[0].date = date
    new_team_scores[1].date = date
    new_team_scores[2].date = date
    new_team_scores[3].date = date
    add_index = 0
    for td in td_list:
        td_text = td.get_attribute('innerHTML')
        td_id = td.get_attribute('id')
        # if len(td_text) == 0 and '_sc' not in td_id:
        if len(td_text) == 0:
            continue
        td_infos = td_id.split('_')
        td_infos[1] = int(td_infos[1])
        td_infos[1] -= 1
        td_infos[1] %= 4
        if td_infos[2] == '1':
            if '_sc' not in td_id:
                new_team_scores[td_infos[1]].firstTeamName = td.find_element_by_tag_name('a').get_attribute('innerHTML')
                new_team_scores[td_infos[1]].firstTeamNumber = td.find_element_by_tag_name('sub').get_attribute(
                    'innerHTML')
            else:
                new_team_scores[td_infos[1]].firstTeamScore = td.get_attribute('innerHTML')
        else:
            if '_sc' not in td_id:
                new_team_scores[td_infos[1]].secondTeamName = td.find_element_by_tag_name('a').get_attribute(
                    'innerHTML')
                new_team_scores[td_infos[1]].secondTeamNumber = td.find_element_by_tag_name('sub').get_attribute(
                    'innerHTML')
            else:
                new_team_scores[td_infos[1]].secondTeamScore = td.get_attribute('innerHTML')
        add_index += 1
        if add_index % 16 == 0:
            print(new_team_scores)
            session.add_all(new_team_scores)
            session.flush()
            new_team_scores = [TeamScoreHASLAMETRICS(), TeamScoreHASLAMETRICS(), TeamScoreHASLAMETRICS(),
                               TeamScoreHASLAMETRICS()]
            new_team_scores[0].date = date
            new_team_scores[1].date = date
            new_team_scores[2].date = date
            new_team_scores[3].date = date


recreate_hasla_metrics_table()
add_team_score()

session.commit()
browser.close()
close_connection()
