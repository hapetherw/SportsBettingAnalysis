# from models.espn_model import ESPNNCAAB
# from database import session
# from database import recreate_espn_table
# from database import close_connection
from datetime import datetime
from airtable_init import airtable_ncaa_team
from airtable_init import airtable_espn_ncaa
from airtable_init import airtable_season
from airtable_init import ncaa_team_info
from airtable_init import espn_ncaa_info
from airtable_init import season_info
from selenimum_config import get_browser
browser = get_browser()
browser.maximize_window()


def add_espn_ncaa():
    browser.get('https://www.espn.com/mens-college-basketball/bpi/_/view/bpi')
    date = browser.find_element_by_css_selector('.bpi__updateTime.u-fz-xs').find_elements_by_tag_name('span')[0]. \
        get_attribute('innerHTML')
    season_name = browser.find_element_by_css_selector('.season.button-filter.med.dropdown-toggle').text
    match_content = browser.find_element_by_class_name('matchup-content')
    li_list = match_content.find_element_by_class_name('pagination').find_elements_by_tag_name('li')
    page_count = li_list[len(li_list) - 2].find_element_by_tag_name('a').get_attribute('innerHTML')
    for page in range(1, int(page_count) + 1):
        browser.get('https://www.espn.com/mens-college-basketball/bpi/_/view/bpi/page/' + str(page))
        match_content = browser.find_element_by_class_name('matchup-content')
        tr_list = match_content.find_element_by_class_name('bpi__table').find_element_by_tag_name('tbody'). \
            find_elements_by_tag_name('tr')
        for tr in tr_list:
            td_list = tr.find_elements_by_tag_name('td')
            ranking = td_list[0].get_attribute('innerHTML')
            team_name = td_list[1].find_element_by_class_name('team-names').get_attribute('innerHTML').strip()
            team_name_temple = td_list[1].find_element_by_tag_name('abbr').get_attribute('innerHTML').strip()
            conf = td_list[2].get_attribute('innerHTML')
            w_l = td_list[3].get_attribute('innerHTML')
            bpi_off = td_list[4].get_attribute('innerHTML')
            bpi_def = td_list[5].get_attribute('innerHTML')
            bpi = td_list[6].get_attribute('innerHTML')
            rank_class = td_list[7].find_element_by_tag_name('span').get_attribute('class')
            week_rank_chg = td_list[7].find_element_by_tag_name('span').get_attribute('innerHTML').strip()
            if 'positive' in rank_class:
                week_rank_chg = '+ ' + week_rank_chg
            elif 'negative' in rank_class:
                week_rank_chg = '- ' + week_rank_chg
            # print(week_rank_chg)
            # if action_type == 1:
            #     new_espn_ncaab = ESPNNCAAB(team_name, team_name_temple, ranking, conf, w_l, bpi_off, bpi_def,
            #                                week_rank_chg,
            #                                date)
            #     session.add(new_espn_ncaab)
            if action_type == 2:
                team1_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                                    team_name.replace("'", " ") + '", SUBSTITUTE({' + \
                                    ncaa_team_info[1] + '}, "\'", " ")="' + \
                                    team_name.replace("'", " ") + '")'
                ncaa_first_team = airtable_ncaa_team.get_all(formula=team1_formula_str)
                if not ncaa_first_team:
                    ncaa_first_team = airtable_ncaa_team.insert(
                        {ncaa_team_info[0]: team_name})
                else:
                    ncaa_first_team = ncaa_first_team[0]
                season = airtable_season.match(season_info[0], season_name)
                if not season:
                    season = airtable_season.insert({season_info[0]: season_name})
                formula_str = 'AND(SUBSTITUTE({Team}, "\'", " ")="' + \
                              ncaa_first_team['fields']['NCAA Team Name'].replace("'", " ") + \
                              '", {Season}="' + season_name + '")'
                # print(formula_str)
                if len(airtable_espn_ncaa.get_all(formula=formula_str)) == 0:
                    airtable_espn_ncaa.insert({espn_ncaa_info[0]: [season['id']],
                                               espn_ncaa_info[1]: [ncaa_first_team['id']],
                                               espn_ncaa_info[2]: int(ranking),
                                               espn_ncaa_info[3]: conf,
                                               espn_ncaa_info[4]: w_l,
                                               espn_ncaa_info[5]: float(bpi_off),
                                               espn_ncaa_info[6]: float(bpi_def),
                                               espn_ncaa_info[7]: week_rank_chg})


print(datetime.now().isoformat(), "Start ESPN work")
action_type = 2
# if action_type == 1:
#     recreate_espn_table()
#     add_espn_ncaa()
#
#     session.commit()
#     browser.close()
#     close_connection()
# else:
add_espn_ncaa()
browser.close()
print("Finished ESPN work")
