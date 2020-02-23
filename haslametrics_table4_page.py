from models.hasla_metrics_model import TeamScoreHASLAMETRICS
# from database import session
# from database import recreate_hasla_metrics_table
# from database import close_connection
import datetime
# import pandas as pd
from airtable_init import airtable_ncaa_team
from airtable_init import airtable_haslametrics
from airtable_init import airtable_game_date
from airtable_init import ncaa_team_info
from airtable_init import hasla_metrics_info
from airtable_init import game_date_info
from selenimum_config import get_browser
# import google_spread_sheet
# from google_spread_sheet import get_work_sheet
#
# wks = get_work_sheet('HaslaMetrics')
browser = get_browser()
browser.maximize_window()
browser.get('http://haslametrics.com/ratings.php')


def add_team_score():
    date_selections = browser.find_element_by_id('cboUpcomingDates')
    date_info = date_selections.find_elements_by_tag_name('option')[0].get_attribute('innerHTML').split(', ')
    date = date_info[1] + ", " + date_info[2]
    date = datetime.datetime.strptime(date, '%B %d, %Y').date()
    date = str(date)
    table = browser.find_element_by_id('myTable4')
    total_sheet_data = []
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
            for idx in range(4):
                if action_type == 2:
                    total_sheet_data.append((new_team_scores[idx].firstTeamName, new_team_scores[idx].firstTeamScore,
                                             new_team_scores[idx].firstTeamNumber, new_team_scores[idx].secondTeamName,
                                             new_team_scores[idx].secondTeamScore,
                                             new_team_scores[idx].secondTeamNumber,
                                             new_team_scores[idx].date))
                elif action_type == 3:
                    team1_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                                        new_team_scores[idx].firstTeamName.replace("'", " ") + '", SUBSTITUTE({' + \
                                        ncaa_team_info[1] + '}, "\'", " ")="' + \
                                        new_team_scores[idx].firstTeamName.replace("'", " ") + '")'
                    team2_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                                        new_team_scores[idx].secondTeamName.replace("'", " ") + '", SUBSTITUTE({' + \
                                        ncaa_team_info[1] + '}, "\'", " ")="' + \
                                        new_team_scores[idx].secondTeamName.replace("'", " ") + '")'
                    ncaa_first_team = airtable_ncaa_team.get_all(formula=team1_formula_str)
                    ncaa_second_team = airtable_ncaa_team.get_all(formula=team2_formula_str)
                    if not ncaa_first_team:
                        ncaa_first_team = airtable_ncaa_team.insert(
                            {ncaa_team_info[0]: new_team_scores[idx].firstTeamName})
                    else:
                        ncaa_first_team = ncaa_first_team[0]
                    if not ncaa_second_team:
                        ncaa_second_team = airtable_ncaa_team.insert(
                            {ncaa_team_info[0]: new_team_scores[idx].secondTeamName})
                    else:
                        ncaa_second_team = ncaa_second_team[0]
                    game_date = airtable_game_date.match(game_date_info[0], date)
                    if not game_date:
                        game_date = airtable_game_date.insert({game_date_info[0]: date})
                    score1 = float(new_team_scores[idx].firstTeamScore)
                    score2 = float(new_team_scores[idx].secondTeamScore)
                    formula_str = 'AND(SUBSTITUTE({Team1}, "\'", " ")="' + \
                                  ncaa_first_team['fields']['NCAA Team Name'].replace("'", " ") + \
                                  '", SUBSTITUTE({Team2}, "\'", " ")="' + \
                                  ncaa_second_team['fields']['NCAA Team Name'].replace("'",
                                                                                       " ") + '", {Date}="' + date + '")'
                    # print(formula_str)
                    if len(airtable_haslametrics.get_all(formula=formula_str)) == 0:
                        airtable_haslametrics.insert({hasla_metrics_info[0]: [ncaa_first_team['id']],
                                                      hasla_metrics_info[1]: [ncaa_second_team['id']],
                                                      hasla_metrics_info[2]: [game_date['id']],
                                                      hasla_metrics_info[3]: score1,
                                                      hasla_metrics_info[4]: score2})
            # if action_type == 1:
            #     session.add_all(new_team_scores)
            #     session.flush()
            new_team_scores = [TeamScoreHASLAMETRICS(), TeamScoreHASLAMETRICS(), TeamScoreHASLAMETRICS(),
                               TeamScoreHASLAMETRICS()]
            new_team_scores[0].date = date
            new_team_scores[1].date = date
            new_team_scores[2].date = date
            new_team_scores[3].date = date

    # if action_type == 2:
    #     df = pd.DataFrame(total_sheet_data, columns=TeamScoreHASLAMETRICS.table_columns)
    #     wks.set_dataframe(df, (1, 1))


print(datetime.datetime.now().isoformat(), "Start HaslaMetrics work")
action_type = 3
# if action_type == 0:
#     recreate_hasla_metrics_table()
#     add_team_score()
#     session.commit()
#     browser.close()
#     close_connection()
# else:
add_team_score()
browser.close()
print("Finished HaslaMetrics work")
