from selenium import webdriver
from models.odd_models import BooksHeader
from models.odd_models import TeamsList
from models.odd_models import OddsList
from models.odd_models import OddDetailsList
from database import session
from database import recreate_database
from database import close_connection
from sqlalchemy import func
import json

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.oddsshark.com/ncaab/odds')


def add_book_headers():
    book_header_items = browser.find_elements_by_class_name("op-book-header")
    for book_header in book_header_items:
        book_header_attr = book_header.get_attribute('class')
        book_name = book_header.find_element_by_tag_name('img').get_attribute('alt')
        if book_header_attr == 'op-book-header ':
            vegas_type = 0
        elif book_header_attr == 'op-book-header vegas':
            vegas_type = 1
        elif book_header_attr == 'op-book-header no-vegas':
            vegas_type = 2
        new_book_header = BooksHeader(book_name, vegas_type)
        session.add(new_book_header)
    session.flush()


def add_teams_and_odds():
    left_column_wrapper = browser.find_element_by_class_name('op-left-column-wrapper')
    left_odd_not_futures = left_column_wrapper. find_element_by_class_name('not-futures')

    not_future_odd_results = browser.find_element_by_id('op-results')
    not_future_odd_details = not_future_odd_results.find_elements_by_class_name('op-item-row-wrapper')
    odd_detail_index = 0

    left_div_list_not_futures = left_odd_not_futures.find_elements_by_tag_name('div')

    for div_item in left_div_list_not_futures:
        class_name = div_item.get_attribute('class')
        if 'op-separator-bar' in class_name:
            date_json = json.loads(div_item.get_attribute('data-op-date'))
            full_date = date_json['full_date']
            short_date = date_json['short_date']
            date_group_name = date_json['group_name']
        elif 'op-matchup-wrapper' in class_name:
            time = div_item.find_element_by_class_name("op-matchup-time").text
            top_rotation_number = div_item.find_element_by_class_name("op-rotation-top").text
            bottom_rotation_number = div_item.find_element_by_class_name("op-rotation-bottom").text
            top_team_attr = div_item.find_element_by_class_name("op-team-top").get_attribute('data-op-name')
            bottom_team_attr = div_item.find_element_by_class_name("op-team-bottom").get_attribute('data-op-name')
            top_team_json = json.loads(top_team_attr)
            bottom_team_json = json.loads(bottom_team_attr)
            new_top_team = TeamsList(top_team_json['full_name'], top_team_json['short_name'])
            new_bottom_team = TeamsList(bottom_team_json['full_name'], bottom_team_json['short_name'])
            # add team
            session.add(new_top_team)
            session.add(new_bottom_team)
            session.flush()
            new_odd = OddsList(new_top_team.id, new_bottom_team.id, top_rotation_number, bottom_rotation_number, full_date,
                               short_date, date_group_name, time)
            # add odd
            session.add(new_odd)
            session.flush()

            # odd detail part
            book_odd_details = not_future_odd_details[odd_detail_index].find_elements_by_class_name('op-item-wrapper')
            for book_odd_detail in book_odd_details:
                first_row = book_odd_detail.find_element_by_class_name('op-first-row')
                op_spread = first_row.find_element_by_class_name('op-spread')
                class_name = op_spread.get_attribute('class')
                class_name = class_name.replace('op-item op-spread op-', '')
                book_header_id = session.query(BooksHeader).filter(
                    func.lower(BooksHeader.bookName) == class_name).first().id

                first_spread_info = json.loads(op_spread.get_attribute('data-op-info'))
                first_spread_total = json.loads(op_spread.get_attribute('data-op-total'))
                first_spread_money_line = json.loads(op_spread.get_attribute('data-op-moneyline'))
                op_spread_price = first_row.find_element_by_class_name('spread-price')
                first_spread_price_info = json.loads(op_spread_price.get_attribute('data-op-info'))
                first_spread_price_total = json.loads(op_spread_price.get_attribute('data-op-overprice'))

                second_row = book_odd_detail.find_element_by_class_name('op-second-row')
                second_op_spread = second_row.find_element_by_class_name('op-spread')
                second_spread_info = json.loads(second_op_spread.get_attribute('data-op-info'))
                second_spread_total = json.loads(second_op_spread.get_attribute('data-op-total'))
                second_spread_money_line = json.loads(second_op_spread.get_attribute('data-op-moneyline'))
                second_op_spread_price = second_row.find_element_by_class_name('spread-price')
                second_spread_price_info = json.loads(second_op_spread_price.get_attribute('data-op-info'))
                second_spread_price_total = json.loads(second_op_spread_price.get_attribute('data-op-underprice'))

                new_odd_detail = OddDetailsList(book_header_id, new_odd.id, first_spread_info['fullgame'],
                                                first_spread_info['firsthalf'], first_spread_info['secondhalf'],
                                                first_spread_money_line['fullgame'], first_spread_money_line['firsthalf'],
                                                first_spread_money_line['secondhalf'], first_spread_total['fullgame'],
                                                first_spread_total['firsthalf'], first_spread_total['secondhalf'],
                                                first_spread_price_info['fullgame'], first_spread_price_info['firsthalf'],
                                                first_spread_price_info['secondhalf'], first_spread_price_total['fullgame'],
                                                first_spread_price_total['firsthalf'], first_spread_price_total['secondhalf'],
                                                second_spread_info['fullgame'], second_spread_info['firsthalf'],
                                                second_spread_info['secondhalf'], second_spread_money_line['fullgame'],
                                                second_spread_money_line['firsthalf'], second_spread_money_line['secondhalf'],
                                                second_spread_total['fullgame'], second_spread_total['firsthalf'],
                                                second_spread_total['secondhalf'], second_spread_price_info['fullgame'],
                                                second_spread_price_info['firsthalf'], second_spread_price_info['secondhalf'],
                                                second_spread_price_total['fullgame'], second_spread_price_total['firsthalf'],
                                                second_spread_price_total['secondhalf'])
                session.add(new_odd_detail)
            odd_detail_index += 1
            print("added one row")
        else:
            continue


recreate_database()
add_book_headers()
add_teams_and_odds()

session.commit()
browser.close()
close_connection()
