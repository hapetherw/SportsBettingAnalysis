from models.hasla_metrics_model import HaslaMetrics
from models.team_models import NCAATeam
from database import session
from database import recreate_hasla_metrics_table
from database import recreate_team_table
from database import close_connection
import datetime
import time
from sqlalchemy import or_
import pandas as pd
from airtable_init import airtable_ncaa_team
from airtable_init import airtable_haslametrics
from airtable_init import airtable_game_date
from airtable_init import ncaa_team_info
from airtable_init import hasla_metrics_info
from airtable_init import game_date_info
from selenimum_config import get_browser
import google_spread_sheet
from google_spread_sheet import get_work_sheet

wks = get_work_sheet('HaslaMetrics')
browser = get_browser()
browser.maximize_window()
browser.get('http://haslametrics.com/ratings.php')


def add_team_score():
    time.sleep(5)
    total_sheet_data = []
    date_selections = browser.find_element_by_id('cboUpcomingDates')
    date_info = date_selections.find_elements_by_tag_name('option')[0].get_attribute('innerHTML').split(', ')
    date = date_info[1] + ", " + date_info[2]
    date = datetime.datetime.strptime(date, '%B %d, %Y').date()
    date = str(date)
    table = browser.find_element_by_id('myTable4')
    td_list = table.find_elements_by_xpath('//*[starts-with(@id, "tdUpcoming_") and not(contains(@class, "filler"))]')
    new_team_scores = [HaslaMetrics(), HaslaMetrics(), HaslaMetrics(), HaslaMetrics()]
    new_team_scores[0].Date = date
    new_team_scores[1].Date = date
    new_team_scores[2].Date = date
    new_team_scores[3].Date = date
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
                first_team_name = td.find_element_by_tag_name('a').get_attribute('innerHTML')
                new_team_scores[td_infos[1]].Team1Name = first_team_name
                team1 = session.query(NCAATeam).filter(or_(NCAATeam.ShortTeamName == first_team_name,
                                                           NCAATeam.FullTeamName == first_team_name)).first()
                if action_type <= 1:
                    if not team1:
                        team1 = NCAATeam(first_team_name)
                        session.add(team1)
                        session.flush()
                    new_team_scores[td_infos[1]].Team1ID = team1.ID
                new_team_scores[td_infos[1]].Team1Rank = int(td.find_element_by_tag_name('sub').get_attribute(
                    'innerHTML'))
            else:
                new_team_scores[td_infos[1]].Team1Score = float(td.get_attribute('innerHTML'))
        else:
            if '_sc' not in td_id:
                second_team_name = td.find_element_by_tag_name('a').get_attribute('innerHTML')
                new_team_scores[td_infos[1]].Team2Name = second_team_name
                team2 = session.query(NCAATeam).filter(or_(NCAATeam.ShortTeamName == second_team_name,
                                                           NCAATeam.FullTeamName == second_team_name)).first()
                if action_type <= 1:
                    if not team2:
                        team2 = NCAATeam(second_team_name)
                        session.add(team2)
                        session.flush()
                    new_team_scores[td_infos[1]].Team2ID = team2.ID
                new_team_scores[td_infos[1]].Team2Rank = int(td.find_element_by_tag_name('sub').get_attribute(
                    'innerHTML'))
            else:
                new_team_scores[td_infos[1]].Team2Score = float(td.get_attribute('innerHTML'))
        add_index += 1
        if add_index % 16 == 0:
            for idx in range(4):
                if action_type <= 1:
                    db_record = session.query(HaslaMetrics).filter(HaslaMetrics.Team1ID == new_team_scores[idx].Team1ID,
                                                                   HaslaMetrics.Team2ID == new_team_scores[idx].Team2ID,
                                                                   HaslaMetrics.Date == date).first()
                    if not db_record:
                        session.add(new_team_scores[idx])
                        if action_type == 0:
                            first_team = session.query(NCAATeam).filter(NCAATeam.ID ==
                                                                        new_team_scores[idx].Team1ID).first()
                            second_team = session.query(NCAATeam).filter(NCAATeam.ID ==
                                                                         new_team_scores[idx].Team2ID).first()
                            total_sheet_data.append(
                                (first_team.ShortTeamName, first_team.FullTeamName, second_team.ShortTeamName,
                                 second_team.FullTeamName, new_team_scores[idx].Date, new_team_scores[idx].Team1Rank,
                                 new_team_scores[idx].Team2Rank, new_team_scores[idx].Team1Score,
                                 new_team_scores[idx].Team2Score))
                    else:
                        new_team_scores[idx].ID = db_record.ID
                        session.merge(new_team_scores[idx])
                elif action_type == 0 or action_type == 2:
                    team1_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                                        new_team_scores[idx].Team1Name.replace("'", " ") + '", SUBSTITUTE({' + \
                                        ncaa_team_info[1] + '}, "\'", " ")="' + \
                                        new_team_scores[idx].Team1Name.replace("'", " ") + '")'
                    team2_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                                        new_team_scores[idx].Team2Name.replace("'", " ") + '", SUBSTITUTE({' + \
                                        ncaa_team_info[1] + '}, "\'", " ")="' + \
                                        new_team_scores[idx].Team2Name.replace("'", " ") + '")'
                    ncaa_first_team = airtable_ncaa_team.get_all(formula=team1_formula_str)
                    ncaa_second_team = airtable_ncaa_team.get_all(formula=team2_formula_str)
                    if not ncaa_first_team:
                        ncaa_first_team = airtable_ncaa_team.insert(
                            {ncaa_team_info[0]: new_team_scores[idx].Team1Name})
                    else:
                        ncaa_first_team = ncaa_first_team[0]
                    if not ncaa_second_team:
                        ncaa_second_team = airtable_ncaa_team.insert(
                            {ncaa_team_info[0]: new_team_scores[idx].Team2Name})
                    else:
                        ncaa_second_team = ncaa_second_team[0]
                    game_date = airtable_game_date.match(game_date_info[0], date)
                    if not game_date:
                        game_date = airtable_game_date.insert({game_date_info[0]: date})
                    formula_str = 'AND(SUBSTITUTE({Team1}, "\'", " ")="' + \
                                  ncaa_first_team['fields']['NCAA Team Name'].replace("'", " ") + \
                                  '", SUBSTITUTE({Team2}, "\'", " ")="' + \
                                  ncaa_second_team['fields']['NCAA Team Name'].replace("'",
                                                                                       " ") + '", {Date}="' + date + '")'
                    fields = {
                        hasla_metrics_info[0]: [ncaa_first_team['id']],
                        hasla_metrics_info[1]: [ncaa_second_team['id']],
                        hasla_metrics_info[2]: [game_date['id']],
                        hasla_metrics_info[3]: new_team_scores[idx].Team1Rank,
                        hasla_metrics_info[4]: new_team_scores[idx].Team2Rank,
                        hasla_metrics_info[5]: float(new_team_scores[idx].Team1Score),
                        hasla_metrics_info[6]: float(new_team_scores[idx].Team2Score),
                    }
                    record = airtable_haslametrics.get_all(formula=formula_str)
                    if record:
                        airtable_haslametrics.replace(record[0]['id'], fields)
                    else:
                        airtable_haslametrics.insert(fields)
            new_team_scores = [HaslaMetrics(), HaslaMetrics(), HaslaMetrics(),
                               HaslaMetrics()]
            new_team_scores[0].Date = date
            new_team_scores[1].Date = date
            new_team_scores[2].Date = date
            new_team_scores[3].Date = date

    if action_type == 0 and len(total_sheet_data) > 0:  # store into gsheet
        df = pd.DataFrame(total_sheet_data, columns=HaslaMetrics.gsheet_table_columns)
        original_df = wks.get_as_df()
        original_df = original_df.append(df)
        wks.set_dataframe(original_df, (1, 1))


print(datetime.datetime.now().isoformat(), "Start HaslaMetrics work")
action_type = 0
if action_type == 0 or action_type == 1:
    recreate_team_table()
    recreate_hasla_metrics_table()
    add_team_score()
    session.commit()
    browser.close()
    close_connection()
elif action_type == 2:
    add_team_score()
    browser.close()
print("Finished HaslaMetrics work")
