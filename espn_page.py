from selenium import webdriver
from selenium.webdriver.support.ui import Select
from models.espn_model import ESPNNCAAB
from database import session
from database import recreate_espn_table
from database import close_connection

browser = webdriver.Chrome('chromedriver.exe')


def add_espn_ncaa():
    browser.get('https://www.espn.com/mens-college-basketball/bpi/_/view/bpi')
    date = browser.find_element_by_css_selector('.bpi__updateTime.u-fz-xs').find_elements_by_tag_name('span')[0].\
        get_attribute('innerHTML')
    match_content = browser.find_element_by_class_name('matchup-content')
    li_list = match_content.find_element_by_class_name('pagination').find_elements_by_tag_name('li')
    page_count = li_list[len(li_list)-2].find_element_by_tag_name('a').get_attribute('innerHTML')
    for page in range(1, int(page_count)+1):
        browser.get('https://www.espn.com/mens-college-basketball/bpi/_/view/bpi/page/'+str(page))
        match_content = browser.find_element_by_class_name('matchup-content')
        tr_list = match_content.find_element_by_class_name('bpi__table').find_element_by_tag_name('tbody').\
            find_elements_by_tag_name('tr')
        for tr in tr_list:
            td_list = tr.find_elements_by_tag_name('td')
            ranking = td_list[0].get_attribute('innerHTML')
            team_name = td_list[1].find_element_by_class_name('team-names').get_attribute('innerHTML')
            team_name_temple = td_list[1].find_element_by_tag_name('abbr').get_attribute('innerHTML')
            conf = td_list[2].get_attribute('innerHTML')
            w_l = td_list[3].get_attribute('innerHTML')
            bpi_off = td_list[4].get_attribute('innerHTML')
            bpi_def = td_list[5].get_attribute('innerHTML')
            bpi = td_list[6].get_attribute('innerHTML')
            rank_class = td_list[7].find_element_by_tag_name('span').get_attribute('class')
            week_rank_chg = td_list[7].find_element_by_tag_name('span').text
            if 'positive' in rank_class:
                week_rank_chg = '+ ' + week_rank_chg
            elif 'negative' in rank_class:
                week_rank_chg = '- ' + week_rank_chg
            print(week_rank_chg)
            new_espn_ncaab = ESPNNCAAB(team_name, team_name_temple, ranking, conf, w_l, bpi_off, bpi_def, week_rank_chg, date)
            session.add(new_espn_ncaab)


recreate_espn_table()
add_espn_ncaa()

session.commit()
browser.close()
close_connection()
