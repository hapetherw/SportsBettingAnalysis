from selenium.common.exceptions import NoSuchElementException
# from models.vegas_insider_model import VegasInsider
# from database import session
# from database import recreate_vegas_insider_table
# from database import close_connection
from airtable_init import airtable_ncaa_team
from airtable_init import airtable_vegasinsider_ncaa
from airtable_init import airtable_season
from airtable_init import ncaa_team_info
from airtable_init import vegasinsider_ncaa_info
from airtable_init import season_info
from selenimum_config import browser
browser.maximize_window()


def add_vegas_insider():
    browser.get('https://www.vegasinsider.com/college-basketball/stats/iskoe-spreadsheet/')
    season_name = browser.find_element_by_class_name('viHeaderNorm').text
    season_name = season_name.split(' ')[0]
    tr_list = browser.find_element_by_class_name('viBodyBorderNorm').find_elements_by_tag_name('tr')
    for index, tr in enumerate(tr_list):
        if index <= 3:
            continue
        td_list = tr.find_elements_by_tag_name('td')
        try:
            team_name = td_list[1].find_element_by_class_name('tableText').get_attribute('innerHTML').strip()
        except NoSuchElementException:
            team_name = td_list[1].get_attribute('innerHTML').strip()
        # print(team_name)
        # if action_type == 1:
        #     new_vegas_insider_model = VegasInsider(team_name, td_list[0].text,
        #                                            td_list[2].text, td_list[3].text, td_list[4].text, td_list[5].text,
        #                                            td_list[6].text, td_list[7].text, td_list[8].text, td_list[9].text,
        #                                            td_list[10].text, td_list[11].text, td_list[12].text,
        #                                            td_list[13].text,
        #                                            td_list[14].text, td_list[15].text, td_list[16].text,
        #                                            td_list[17].text,
        #                                            td_list[18].text, td_list[19].text, td_list[20].text,
        #                                            td_list[21].text,
        #                                            td_list[22].text, td_list[23].text)
        #     session.add(new_vegas_insider_model)
        if action_type == 2:
            team_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                               team_name.replace("'", " ") + '", SUBSTITUTE({' + \
                               ncaa_team_info[1] + '}, "\'", " ")="' + \
                               team_name.replace("'", " ") + '")'
            ncaa_team = airtable_ncaa_team.get_all(formula=team_formula_str)
            if not ncaa_team:
                ncaa_team = airtable_ncaa_team.insert(
                    {ncaa_team_info[0]: team_name})
            else:
                ncaa_team = ncaa_team[0]
            season = airtable_season.match(season_info[0], season_name)
            if not season:
                season = airtable_season.insert({season_info[0]: season_name})
            formula_str = 'AND(SUBSTITUTE({Team}, "\'", " ")="' + \
                          ncaa_team['fields']['NCAA Team Name'].replace("'", " ") + \
                          '", {Season}="' + season_name + '")'
            # print(formula_str)
            if len(airtable_vegasinsider_ncaa.get_all(formula=formula_str)) == 0:
                airtable_vegasinsider_ncaa.insert({vegasinsider_ncaa_info[0]: [season['id']],
                                                   vegasinsider_ncaa_info[1]: [ncaa_team['id']],
                                                   vegasinsider_ncaa_info[2]: int(td_list[0].text),
                                                   vegasinsider_ncaa_info[3]: float(td_list[2].text),
                                                   vegasinsider_ncaa_info[4]: float(td_list[3].text),
                                                   vegasinsider_ncaa_info[5]: float(td_list[4].text),
                                                   vegasinsider_ncaa_info[6]: float(td_list[5].text),
                                                   vegasinsider_ncaa_info[7]: float(td_list[6].text),
                                                   vegasinsider_ncaa_info[8]: int(td_list[7].text),
                                                   vegasinsider_ncaa_info[9]: int(td_list[8].text),
                                                   vegasinsider_ncaa_info[10]: float(td_list[9].text),
                                                   vegasinsider_ncaa_info[11]: float(td_list[10].text),
                                                   vegasinsider_ncaa_info[12]: float(td_list[11].text),
                                                   vegasinsider_ncaa_info[13]: int(td_list[12].text),
                                                   vegasinsider_ncaa_info[14]: int(td_list[13].text),
                                                   vegasinsider_ncaa_info[15]: int(td_list[14].text),
                                                   vegasinsider_ncaa_info[16]: float(td_list[15].text),
                                                   vegasinsider_ncaa_info[17]: float(td_list[16].text),
                                                   vegasinsider_ncaa_info[18]: float(td_list[17].text),
                                                   vegasinsider_ncaa_info[19]: float(td_list[18].text),
                                                   vegasinsider_ncaa_info[20]: float(td_list[19].text),
                                                   vegasinsider_ncaa_info[21]: float(td_list[20].text),
                                                   vegasinsider_ncaa_info[22]: float(td_list[21].text),
                                                   vegasinsider_ncaa_info[23]: int(td_list[22].text),
                                                   vegasinsider_ncaa_info[24]: int(td_list[23].text)})


print("Start VegasInsider work")
action_type = 2
# if action_type == 1:
#     recreate_vegas_insider_table()
#     add_vegas_insider()
#
#     session.commit()
#     browser.close()
#     close_connection()
# else:
add_vegas_insider()
browser.close()
print("Finished VegasInsider work")
