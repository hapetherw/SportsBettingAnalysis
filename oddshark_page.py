from models.oddshark_models import OddSharkNCAA
from models.oddshark_models import OddSharkNBA
from models.team_models import NCAATeam
from models.team_models import NBATeam
import datetime
from sqlalchemy import or_
from database import session
from database import close_connection
from database import recreate_team_table
from database import recreate_oddshark_table
import pandas as pd
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
from selenimum_config import get_browser
import google_spread_sheet
from google_spread_sheet import get_work_sheet

browser = get_browser()
browser.maximize_window()
wks_nba = get_work_sheet('OddShark_NBA')
wks_ncaab = get_work_sheet('OddShark_NCAA')


def add_oddshark_ncaa():
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
            insert_game_date = date_time_ary[0] + ' ' + str(datetime.datetime.now().year)
            insert_game_date = datetime.datetime.strptime(insert_game_date, '%b %d %Y').date()
            insert_game_date = str(insert_game_date)

            tbody = computer_table.find_element_by_tag_name('tbody')
            attr_tr_list = tbody.find_elements_by_tag_name('tr')
            predicted_score_tds = attr_tr_list[0].find_elements_by_tag_name('td')
            computer_pick_tds = attr_tr_list[1].find_elements_by_tag_name('td')
            public_consensus_tds = attr_tr_list[2].find_elements_by_tag_name('td')
            consensus_bet_tds = attr_tr_list[3].find_elements_by_tag_name('td')
            if action_type <= 1:  # store into db
                team1 = session.query(NCAATeam).filter(or_(NCAATeam.ShortTeamName == first_team_name_short,
                                                           NCAATeam.FullTeamName == first_team_name_long)).first()
                team2 = session.query(NCAATeam).filter(or_(NCAATeam.ShortTeamName == second_team_name_short,
                                                           NCAATeam.FullTeamName == second_team_name_long)).first()
                if not team1:
                    team1 = NCAATeam(first_team_name_short, first_team_name_long)
                    session.add(team1)
                    session.flush()
                if not team2:
                    team2 = NCAATeam(second_team_name_short, second_team_name_long)
                    session.add(team2)
                    session.flush()
                db_record = session.query(OddSharkNCAA).filter(OddSharkNCAA.Team1ID == team1.ID,
                                                               OddSharkNCAA.Team2ID == team2.ID,
                                                               OddSharkNCAA.Date == insert_game_date,
                                                               OddSharkNCAA.Time == date_time_ary[1]).first()
                new_oddshark = OddSharkNCAA(team1.ID, team2.ID, insert_game_date, date_time_ary[1],
                                            predicted_score_tds[1].text, predicted_score_tds[2].text,
                                            computer_pick_tds[1].text, computer_pick_tds[2].text,
                                            public_consensus_tds[1].text, public_consensus_tds[2].text,
                                            consensus_bet_tds[1].text, consensus_bet_tds[2].text)
                if not db_record:
                    session.add(new_oddshark)
                    if action_type == 0:
                        total_sheet_data.append((team1.ShortTeamName, team1.FullTeamName, team2.ShortTeamName,
                                                 team2.FullTeamName, insert_game_date, date_time_ary[1],
                                                 predicted_score_tds[1].text,
                                                 predicted_score_tds[2].text, computer_pick_tds[1].text,
                                                 computer_pick_tds[2].text, public_consensus_tds[1].text,
                                                 public_consensus_tds[2].text, consensus_bet_tds[1].text,
                                                 consensus_bet_tds[2].text))
                else:
                    new_oddshark.ID = db_record.ID
                    session.merge(new_oddshark)
            if action_type == 0 or action_type == 3:  # store into airtable
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

                game_date = airtable_game_date.match(game_date_info[0], insert_game_date)
                if not game_date:
                    game_date = airtable_game_date.insert({game_date_info[0]: insert_game_date})

                game_time = airtable_game_time.match(game_time_info[0], date_time_ary[1])
                if not game_time:
                    game_time = airtable_game_time.insert({game_time_info[0]: date_time_ary[1]})
                formula_str = "AND(Team1='" + first_team_name_short + "', Team2='" + second_team_name_short + \
                              "', Date='" + insert_game_date + "', Time='" + date_time_ary[1] + "')"
                fields = {
                    oddshark_ncaa_info[0]: [first_team['id']],
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
                    oddshark_ncaa_info[11]: consensus_bet_tds[2].text
                }
                record = airtable_ncaab.get_all(formula=formula_str)
                if record:
                    airtable_ncaab.replace(record[0]['id'], fields)
                else:
                    airtable_ncaab.insert(fields)
    if action_type == 0 and len(total_sheet_data) > 0:  # store into gsheet
        df = pd.DataFrame(total_sheet_data, columns=OddSharkNCAA.table_columns)
        original_df = wks_ncaab.get_as_df()
        original_df = original_df.append(df)
        wks_ncaab.set_dataframe(original_df, (1, 1))


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
            date_time_ary = thead.find_element_by_tag_name('th').text.split(" @ ")
            date_time = date_time_ary[0] + " " + date_time_ary[1]
            insert_game_date = date_time_ary[0] + ' ' + str(datetime.datetime.now().year)
            insert_game_date = datetime.datetime.strptime(insert_game_date, '%b %d %Y').date()
            insert_game_date = str(insert_game_date)
            tbody = computer_table.find_element_by_tag_name('tbody')
            attr_tr_list = tbody.find_elements_by_tag_name('tr')
            predicted_score_tds = attr_tr_list[0].find_elements_by_tag_name('td')
            computer_pick_tds = attr_tr_list[1].find_elements_by_tag_name('td')
            public_consensus_tds = attr_tr_list[2].find_elements_by_tag_name('td')
            consensus_bet_tds = attr_tr_list[3].find_elements_by_tag_name('td')
            if action_type <= 1:  # store into db
                team1 = session.query(NBATeam).filter(or_(NBATeam.ShortTeamName == first_team_name_short,
                                                          NBATeam.FullTeamName == first_team_name_long)).first()
                team2 = session.query(NBATeam).filter(or_(NBATeam.ShortTeamName == second_team_name_short,
                                                          NBATeam.FullTeamName == second_team_name_long)).first()
                if not team1:
                    team1 = NBATeam(first_team_name_short, first_team_name_long)
                    session.add(team1)
                    session.flush()
                if not team2:
                    team2 = NBATeam(second_team_name_short, second_team_name_long)
                    session.add(team2)
                    session.flush()
                db_record = session.query(OddSharkNBA).filter(OddSharkNBA.Team1ID == team1.ID,
                                                              OddSharkNBA.Team2ID == team2.ID,
                                                              OddSharkNBA.Date == insert_game_date,
                                                              OddSharkNBA.Time == date_time_ary[1]).first()
                new_oddshark = OddSharkNBA(team1.ID, team2.ID, insert_game_date, date_time_ary[1],
                                           predicted_score_tds[1].text, predicted_score_tds[2].text,
                                           computer_pick_tds[1].text, computer_pick_tds[2].text,
                                           public_consensus_tds[1].text, public_consensus_tds[2].text,
                                           consensus_bet_tds[1].text, consensus_bet_tds[2].text)
                if not db_record:
                    session.add(new_oddshark)
                    if action_type == 0:  # store into google sheet
                        total_sheet_data.append((team1.ShortTeamName, team1.FullTeamName, team2.ShortTeamName,
                                                 team2.FullTeamName, insert_game_date, date_time_ary[1],
                                                 predicted_score_tds[1].text,
                                                 predicted_score_tds[2].text, computer_pick_tds[1].text,
                                                 computer_pick_tds[2].text, public_consensus_tds[1].text,
                                                 public_consensus_tds[2].text, consensus_bet_tds[1].text,
                                                 consensus_bet_tds[2].text))
                else:
                    new_oddshark.ID = db_record.ID
                    session.merge(new_oddshark)
            if action_type == 0 or action_type == 3:  # store into airtable
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

                game_date = airtable_game_date.match(game_date_info[0], insert_game_date)
                if not game_date:
                    game_date = airtable_game_date.insert({game_date_info[0]: insert_game_date})

                game_time = airtable_game_time.match(game_time_info[0], date_time_ary[1])
                if not game_time:
                    game_time = airtable_game_time.insert({game_time_info[0]: date_time_ary[1]})
                formula_str = "AND(Team1='" + first_team_name_short + "', Team2='" + second_team_name_short + \
                              "', Date='" + insert_game_date + "', Time='" + date_time_ary[1] + "')"
                fields = {
                    oddshark_nba_info[0]: [first_team['id']],
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
                    oddshark_nba_info[11]: consensus_bet_tds[2].text
                }
                record = airtable_nba.get_all(formula=formula_str)
                if record:
                    airtable_nba.replace(record[0]['id'], fields)
                else:
                    airtable_nba.insert(fields)
    if action_type == 0 and len(total_sheet_data) > 0:  # store into gsheet
        df = pd.DataFrame(total_sheet_data, columns=OddSharkNBA.table_columns)
        original_df = wks_nba.get_as_df()
        original_df = original_df.append(df)
        wks_nba.set_dataframe(original_df, (1, 1))


action_type = 0
print(datetime.datetime.now().isoformat(), "Start Oddshark work")
if action_type == 0 or action_type == 1:
    recreate_team_table()
    recreate_oddshark_table()
    print("Oddshark-NBA work")
    add_oddshark_nba()
    print("Oddshark-NCAA work")
    add_oddshark_ncaa()
    session.commit()
    browser.close()
    close_connection()
    print("Finished Oddshark work")
elif action_type == 3:
    print("Oddshark-NBA work")
    add_oddshark_nba()
    print("Oddshark-NCAA work")
    add_oddshark_ncaa()
    browser.close()
    print("Finished Oddshark work")
