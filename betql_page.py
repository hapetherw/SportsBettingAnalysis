import requests
from datetime import datetime, timedelta
import pytz
from airtable_init import airtable_ncaa_team
from airtable_init import airtable_nba_team
from airtable_init import airtable_betql_ncaa
from airtable_init import airtable_betql_nba
from airtable_init import ncaa_team_info
from airtable_init import nba_team_info

api_url = 'https://api.betql.co/graphql'
email = 'bonagamble@gmail.com'
password = 'Br@df0rd$$'
# eastern = pytz.timezone('US/Eastern')

today = datetime.now()
before_date = today.strftime('%Y-%m-%dT') + '16:59:59.999Z'
after_date = datetime.strftime(today - timedelta(1), '%Y-%m-%dT') + '17:00:00.000Z'
book_id = "2a09f6df-5b47-4f87-82ef-91a77d26eef9"
print("Start BetQL work")
login_res = requests.post(api_url,
                          json={"operationName": "login",
                                "variables": {"email": email, "password": password},
                                "query": "mutation login($email: String!, $password: String!, $longitude: Float, " "$latitude: Float) {\n  login(username: $email, password: $password, " "longitude:$longitude, latitude: $latitude, product: \"bet\") {\n    token\n  " "  userId\n    sports {\nupdatedTime\n      sport\n      __typename\n    " "}\n    __typename\n  }\n}\n"},
                          headers={'Content-Type': 'application/json'})

token = login_res.json()['data']['login']['token']


def betql_work(is_nba):
    betql_res = requests.post(api_url,
                              json={
                                  "operationName": "eventsQuery",
                                  "variables": {
                                      "league": "NBA" if is_nba else "CBK",
                                      "lineType": ["CURRENT", "OPEN"],
                                      "before": before_date,
                                      "after": after_date,
                                      "period": ["FULLGAME", "FIRSTHALF", "SECONDHALF"],
                                      "books": [book_id],
                                      "book": book_id,
                                      "hasTeamPowerProjectionGrades": True,
                                      "hasFGspreadPowerRating": True,
                                      "hasFGmoneylinePowerRating": True,
                                      "hasFGtotalPowerRating": True,
                                      "has1HspreadPowerRating": True,
                                      "has1HmoneylinePowerRating": True,
                                      "has1HtotalPowerRating": True,
                                      "has1PspreadPowerRating": False,
                                      "has1PmoneylinePowerRating": False,
                                      "has1PtotalPowerRating": False,
                                      "hasPitchers": False,
                                      "isNBA": True if is_nba else False
                                  },
                                  "query": "query eventsQuery($league: LeagueEnum, $before: DateTime, $after: DateTime, $period: [LinePeriodEnum], $books: [UUID], $book: UUID!, $lineType: [LineTypeEnum], $conference: CFBConferenceEnum, $hasTeamPowerProjectionGrades: Boolean!, $hasFGspreadPowerRating: Boolean!, $hasFGmoneylinePowerRating: Boolean!, $hasFGtotalPowerRating: Boolean!, $has1HspreadPowerRating: Boolean!, $has1HmoneylinePowerRating: Boolean!, $has1HtotalPowerRating: Boolean!, $has1PspreadPowerRating: Boolean!, $has1PmoneylinePowerRating: Boolean!, $has1PtotalPowerRating: Boolean!, $hasPitchers: Boolean!, $isNBA: Boolean!) {\n  auth {\n    events(league: $league, before: $before, after: $after, eventType: TEAM, conference: $conference) {\n      id\n      dbId\n      freeGame\n      slugId\n      eventState\n      startDate\n      awayRot\n      awayScore\n      homeRot\n      homeScore\n      period\n      statfoxGamecode\n      awayTeamPowerRating\n      homeTeamPowerRating\n      neutral\n      stadium\n      location\n      projection @include(if: $hasTeamPowerProjectionGrades) {\n        projHomeScore\n        projAwayScore\n        projHomeFirstHalfScore\n        projAwayFirstHalfScore\n        projHomeKeyPlayerGradeScore\n        projHomeKeyPlayerGrade\n        projAwayKeyPlayerGradeScore\n        projAwayKeyPlayerGrade\n        projHomeOffenseGradeScore\n        projHomeOffenseGrade\n        projAwayOffenseGradeScore\n        projAwayOffenseGrade\n        projHomeDefenseGradeScore\n        projHomeDefenseGrade\n        projAwayDefenseGradeScore\n        projAwayDefenseGrade\n        projHomeTeamGrade\n        projHomeTeamGradeScore\n        projAwayTeamGrade\n        projAwayTeamGradeScore\n        projHomeGoalie\n        projAwayGoalie\n        __typename\n      }\n      spRating(bookUuid: $book) @include(if: $hasFGspreadPowerRating) {\n        rating\n        differential\n        preferredLine\n        preferredTeamId\n        __typename\n      }\n      mlRating(bookUuid: $book) @include(if: $hasFGmoneylinePowerRating) {\n        rating\n        differential\n        preferredLine\n        preferredTeamId\n        __typename\n      }\n      ouRating(bookUuid: $book) @include(if: $hasFGtotalPowerRating) {\n        rating\n        differential\n        preferredLine\n        preferredTotal\n        __typename\n      }\n      sp1HRating(bookUuid: $book) @include(if: $has1HspreadPowerRating) {\n        rating\n        differential\n        preferredLine\n        preferredTeamId\n        __typename\n      }\n      ml1HRating(bookUuid: $book) @include(if: $has1HmoneylinePowerRating) {\n        rating\n        differential\n        preferredLine\n        preferredTeamId\n        __typename\n      }\n      ou1HRating(bookUuid: $book) @include(if: $has1HtotalPowerRating) {\n        rating\n        differential\n        preferredLine\n        preferredTotal\n        __typename\n      }\n      sp1PRating(bookUuid: $book) @include(if: $has1PspreadPowerRating) {\n        rating\n        differential\n        preferredLine\n        preferredTeamId\n        __typename\n      }\n      ml1PRating(bookUuid: $book) @include(if: $has1PmoneylinePowerRating) {\n        rating\n        differential\n        preferredLine\n        preferredTeamId\n        __typename\n      }\n      ou1PRating(bookUuid: $book) @include(if: $has1PtotalPowerRating) {\n        rating\n        differential\n        preferredLine\n        preferredTotal\n        __typename\n      }\n      awayTeamPitcher @include(if: $hasPitchers) {\n        id\n        fullName\n        firstName\n        lastName\n        position\n        imageUrl\n        __typename\n      }\n      homeTeamPitcher @include(if: $hasPitchers) {\n        id\n        fullName\n        firstName\n        lastName\n        position\n        imageUrl\n        __typename\n      }\n      homeTeam {\n        id\n        fullName\n        lastName\n        preferredAbbreviation\n        conference\n        division\n        teamStats {\n          id\n          atsUnits\n          atswins\n          atslosses\n          atsties\n          atsWinPercent\n          games\n          netUnits\n          overPercent\n          overs\n          pushes\n          underPercent\n          unders\n          rank\n          wins\n          losses\n          confWins\n          confLosses\n          pointsAgainst @include(if: $isNBA)\n          pointsFor @include(if: $isNBA)\n          homeSuWins\n          awaySuWins\n          homeSuLosses\n          awaySuLosses\n          homeSuTies\n          awaySuTies\n          homeAtsWins\n          awayAtsWins\n          homeAtsLosses\n          awayAtsLosses\n          homeAtsTies\n          awayAtsTies\n          homeOvers\n          awayOvers\n          homeUnders\n          awayUnders\n          homePushes\n          awayPushes\n          __typename\n        }\n        injuredPlayers(maxPriority: 3) {\n          id\n          fullName\n          imageUrl\n          injuryStatus\n          active\n          depthPositionCategory\n          depthPosition\n          depthOrder\n          news {\n            id\n            playerId\n            title\n            newsTime\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      awayTeam {\n        id\n        fullName\n        lastName\n        preferredAbbreviation\n        conference\n        division\n        injuredPlayers(maxPriority: 3) {\n          id\n          fullName\n          imageUrl\n          injuryStatus\n          active\n          depthPositionCategory\n          depthPosition\n          depthOrder\n          news {\n            id\n            playerId\n            title\n            newsTime\n            __typename\n          }\n          __typename\n        }\n        teamStats {\n          id\n          atsUnits\n          atswins\n          atslosses\n          atsties\n          atsWinPercent\n          games\n          netUnits\n          overPercent\n          overs\n          pushes\n          underPercent\n          unders\n          rank\n          wins\n          losses\n          confWins\n          confLosses\n          pointsAgainst @include(if: $isNBA)\n          pointsFor @include(if: $isNBA)\n          homeSuWins\n          awaySuWins\n          homeSuLosses\n          awaySuLosses\n          homeSuTies\n          awaySuTies\n          homeAtsWins\n          awayAtsWins\n          homeAtsLosses\n          awayAtsLosses\n          homeAtsTies\n          awayAtsTies\n          homeOvers\n          awayOvers\n          homeUnders\n          awayUnders\n          homePushes\n          awayPushes\n          __typename\n        }\n        __typename\n      }\n      league {\n        id\n        name\n        __typename\n      }\n      lines(bookIds: $books, period: $period, lineType: $lineType) {\n        bookId\n        book {\n          id\n          name\n          __typename\n        }\n        id\n        time\n        type\n        lineType\n        period\n        awaySpread\n        awayMoney\n        awayPrice\n        homeSpread\n        homeMoney\n        homePrice\n        drawMoney\n        total\n        overPrice\n        underPrice\n        __typename\n      }\n      userNotificationSetting {\n        id\n        importantNews\n        gameStart\n        secondHalfLineAvailable\n        __typename\n      }\n      periodScores {\n        id\n        eventId\n        period\n        time\n        homeScore\n        awayScore\n        order\n        __typename\n      }\n      eventStats(period: $period) {\n        id\n        period\n        homeSpreadCount\n        awaySpreadCount\n        homeMoneyCount\n        awayMoneyCount\n        overCount\n        underCount\n        homeSharpSpreadPercent\n        awaySharpSpreadPercent\n        homeSharpMoneyPercent\n        awaySharpMoneyPercent\n        overSharpPercent\n        underSharpPercent\n        homeTicketSpreadPercent\n        awayTicketSpreadPercent\n        homeTicketMoneyPercent\n        awayTicketMoneyPercent\n        overTicketPercent\n        underTicketPercent\n        publicSpreadHome\n        publicSpreadAway\n        publicMoneyHome\n        publicMoneyAway\n        publicTotalOver\n        publicTotalUnder\n        __typename\n      }\n      eventTrends(bookUuid: $book, trendTypes: [ATS, ML, HTATS, OU]) {\n        id\n        teamId\n        timePeriod\n        description\n        typeGames\n        rating\n        trendType\n        reportType\n        wins\n        losses\n        games\n        units\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"},
                              headers={
                                  'Content-Type': 'application/json',
                                  'Authorization': 'Bearer ' + token})
    # print(betql_res.json()['data']['auth']['events'])
    event_list = betql_res.json()['data']['auth']['events']
    for event in event_list:
        home_team_info = event['homeTeam']
        away_team_info = event['awayTeam']
        if is_nba:
            team1_formula_str = 'OR(SUBSTITUTE({' + nba_team_info[0] + '}, "\'", " ")="' + \
                                home_team_info['fullName'].replace("'", " ") + '", SUBSTITUTE({' + \
                                nba_team_info[1] + '}, "\'", " ")="' + \
                                home_team_info['fullName'].replace("'", " ") + '")'
            team2_formula_str = 'OR(SUBSTITUTE({' + nba_team_info[0] + '}, "\'", " ")="' + \
                                away_team_info['fullName'].replace("'", " ") + '", SUBSTITUTE({' + \
                                nba_team_info[1] + '}, "\'", " ")="' + \
                                away_team_info['fullName'].replace("'", " ") + '")'
            home_team = airtable_nba_team.get_all(formula=team1_formula_str)
            away_team = airtable_nba_team.get_all(formula=team2_formula_str)
            if not home_team:
                home_team = airtable_nba_team.insert(
                    {nba_team_info[0]: home_team_info['preferredAbbreviation'],
                     nba_team_info[1]: home_team_info['fullName'], })
            else:
                home_team = home_team[0]
            if not away_team:
                away_team = airtable_nba_team.insert(
                    {nba_team_info[0]: away_team_info['preferredAbbreviation'],
                     nba_team_info[1]: away_team_info['fullName']})
            else:
                away_team = away_team[0]
        else:
            team1_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                                home_team_info['fullName'].replace("'", " ") + '", SUBSTITUTE({' + \
                                ncaa_team_info[1] + '}, "\'", " ")="' + \
                                home_team_info['fullName'].replace("'", " ") + '")'
            team2_formula_str = 'OR(SUBSTITUTE({' + ncaa_team_info[0] + '}, "\'", " ")="' + \
                                away_team_info['fullName'].replace("'", " ") + '", SUBSTITUTE({' + \
                                ncaa_team_info[1] + '}, "\'", " ")="' + \
                                away_team_info['fullName'].replace("'", " ") + '")'
            home_team = airtable_ncaa_team.get_all(formula=team1_formula_str)
            away_team = airtable_ncaa_team.get_all(formula=team2_formula_str)
            if not home_team:
                home_team = airtable_ncaa_team.insert(
                    {ncaa_team_info[0]: home_team_info['preferredAbbreviation'],
                     ncaa_team_info[1]: home_team_info['fullName'], })
            else:
                home_team = home_team[0]
            if not away_team:
                away_team = airtable_ncaa_team.insert(
                    {ncaa_team_info[0]: away_team_info['preferredAbbreviation'],
                     ncaa_team_info[1]: away_team_info['fullName']})
            else:
                away_team = away_team[0]
        open_info = [None] * 3
        current_info = [None] * 3
        event_stats = [None] * 3
        for line in event['lines']:
            if line['lineType'] == 'open' and line['period'] == 'FG':
                open_info[0] = line
            elif line['lineType'] == 'open' and line['period'] == '1H':
                open_info[1] = line
            elif line['lineType'] == 'open' and line['period'] == '2H':
                open_info[2] = line
            elif line['lineType'] == 'current' and line['period'] == 'FG':
                current_info[0] = line
            elif line['lineType'] == 'current' and line['period'] == '1H':
                current_info[1] = line
            elif line['lineType'] == 'current' and line['period'] == '2H':
                current_info[2] = line
        for event_stat in event['eventStats']:
            if event_stat['period'] == 'FG':
                event_stats[0] = event_stat
            elif event_stat['period'] == '1H':
                event_stats[1] = event_stat
            elif event_stat['period'] == '2H':
                event_stats[2] = event_stat

        fields = {
            'ID': event['id'],
            'SlugID': event['slugId'],
            'HomeTeam': [home_team['id']],
            'AwayTeam': [away_team['id']],
            'EventState': event['eventState'],
            'StartDate': event['startDate'],
            'H_current_spread': current_info[0]['homeSpread'] if
            current_info[0] is not None and current_info[0]['homeSpread'] is not None else None,
            'A_current_spread': current_info[0]['awaySpread'] if
            current_info[0] is not None and current_info[0]['awaySpread'] is not None else None,
            'Spread_best_rating': event['spRating']['rating'] if
            event['spRating'] is not None and event['spRating']['rating'] is not None else None,
            'H_current_moneyline': current_info[0]['homeMoney'] if
            current_info[0] is not None and current_info[0]['homeMoney'] is not None else None,
            'A_current_moneyline': current_info[0]['awayMoney'] if
            current_info[0] is not None and current_info[0]['awayMoney'] is not None else None,
            'Moneyline_best_rating': event['mlRating']['rating'] if
            event['mlRating'] is not None and event['mlRating']['rating'] is not None else None,
            'Current_U': current_info[0]['total'] if
            current_info[0] is not None and current_info[0]['total'] is not None and
            event['ouRating'] is not None and event['ouRating']['preferredTotal'] is not None and
            event['ouRating']['preferredTotal'] is 'under' else None,
            'Current_O': current_info[0]['total'] if
            current_info[0] is not None and current_info[0]['total'] is not None and
            event['ouRating'] is not None and event['ouRating']['preferredTotal'] is not None and
            event['ouRating']['preferredTotal'] is 'over' else None,
            'Total_best_rating': event['ouRating']['rating'] if
            event['ouRating'] is not None and event['ouRating']['rating'] is not None else None,
            'H_current_1h_spread': current_info[1]['homeSpread'] if
            current_info[1] is not None and current_info[1]['homeSpread'] is not None else None,
            'A_current_1h_spread': current_info[1]['awaySpread'] if
            current_info[1] is not None and current_info[1]['awaySpread'] is not None else None,
            '1h_spread_best_rating': event['sp1HRating']['rating'] if
            event['sp1HRating'] is not None and event['sp1HRating']['rating'] is not None else None,
            'H_current_1h_moneyline': current_info[1]['homeMoney'] if
            current_info[1] is not None and current_info[1]['homeMoney'] is not None else None,
            'A_current_1h_moneyline': current_info[1]['awayMoney'] if
            current_info[1] is not None and current_info[1]['awayMoney'] is not None else None,
            '1h_moneyline_best_rating': event['ml1HRating']['rating'] if
            event['ml1HRating'] is not None and event['ml1HRating']['rating'] is not None else None,
            'Current_1h_U': current_info[1]['total'] if
            current_info[1] is not None and current_info[1]['total'] is not None and
            event['ou1HRating'] is not None and event['ou1HRating']['preferredTotal'] is not None and
            event['ou1HRating']['preferredTotal'] is 'under' else None,
            'Current_1h_O': current_info[1]['total'] if
            current_info[1] is not None and current_info[1]['total'] is not None and
            event['ou1HRating'] is not None and event['ou1HRating']['preferredTotal'] is not None and
            event['ou1HRating']['preferredTotal'] is 'over' else None,
            '1h_total_best_rating': event['ou1HRating']['rating'] if
            event['ou1HRating'] is not None and event['ou1HRating']['rating'] is not None else None,
            'H_current_2h_spread': current_info[2]['homeSpread'] if
            current_info[2] is not None and current_info[2]['homeSpread'] is not None else None,
            'A_current_2h_spread': current_info[2]['awaySpread'] if
            current_info[2] is not None and current_info[2]['awaySpread'] is not None else None,
            'H_current_2h_moneyline': current_info[2]['homeMoney'] if
            current_info[2] is not None and current_info[2]['homeMoney'] is not None else None,
            'A_current_2h_moneyline': current_info[2]['awayMoney'] if
            current_info[2] is not None and current_info[2]['awayMoney'] is not None else None,
            'H_road_ou': str(home_team_info['teamStats']['awayOvers']) + ' - ' + str(home_team_info['teamStats'][
                                                                                         'awayUnders']) + ' - ' + str(
                home_team_info['teamStats']['awayPushes']) if
            home_team_info['teamStats']['awayOvers'] is not None and
            home_team_info['teamStats']['awayUnders'] is not None and
            home_team_info['teamStats']['awayPushes'] is not None else None,
            'A_road_ou': str(away_team_info['teamStats']['awayOvers']) + ' - ' + str(away_team_info['teamStats'][
                                                                                         'awayUnders']) + ' - ' + str(
                away_team_info['teamStats']['awayPushes']) if
            away_team_info['teamStats']['awayOvers'] is not None and
            away_team_info['teamStats']['awayUnders'] is not None and
            away_team_info['teamStats']['awayPushes'] is not None else None,
            'H_home_ou': str(home_team_info['teamStats']['homeOvers']) + ' - ' + str(home_team_info['teamStats'][
                                                                                         'homeUnders']) + ' - ' + str(
                home_team_info['teamStats']['homePushes']) if
            home_team_info['teamStats']['homeOvers'] is not None and
            home_team_info['teamStats']['homeUnders'] is not None and
            home_team_info['teamStats']['homePushes'] is not None else None,
            'A_home_ou': str(away_team_info['teamStats']['homeOvers']) + ' - ' + str(away_team_info['teamStats'][
                                                                                         'homeUnders']) + ' - ' + str(
                away_team_info['teamStats']['homePushes']) if
            away_team_info['teamStats']['homeOvers'] is not None and
            away_team_info['teamStats']['homeUnders'] is not None and
            away_team_info['teamStats']['homePushes'] is not None else None,
            'H_under': home_team_info['teamStats']['underPercent'] / 100 if
            home_team_info['teamStats']['underPercent'] is not None else None,
            'A_under': away_team_info['teamStats']['underPercent'] / 100 if
            away_team_info['teamStats']['underPercent'] is not None else None,
            'H_over': home_team_info['teamStats']['overPercent'] / 100 if
            home_team_info['teamStats']['overPercent'] is not None else None,
            'A_over': away_team_info['teamStats']['overPercent'] / 100 if
            away_team_info['teamStats']['overPercent'] is not None else None,
            'H_under_record': str(home_team_info['teamStats']['unders']) + ' - ' + str(
                home_team_info['teamStats']['overs']) + ' - ' + str(home_team_info['teamStats']['pushes']) if
            home_team_info['teamStats']['unders'] is not None and
            home_team_info['teamStats']['overs'] is not None and
            home_team_info['teamStats']['pushes'] is not None else None,
            'A_under_record': str(away_team_info['teamStats']['unders']) + ' - ' + str(
                away_team_info['teamStats']['overs']) + ' - ' + str(away_team_info['teamStats']['pushes']) if
            away_team_info['teamStats']['unders'] is not None and
            away_team_info['teamStats']['overs'] is not None and
            away_team_info['teamStats']['pushes'] is not None else None,
            'H_over_record': str(home_team_info['teamStats']['overs']) + ' - ' + str(
                home_team_info['teamStats']['unders']) + ' - ' + str(home_team_info['teamStats']['pushes']) if
            home_team_info['teamStats']['overs'] is not None and
            home_team_info['teamStats']['unders'] is not None and
            home_team_info['teamStats']['pushes'] is not None else None,
            'A_over_record': str(away_team_info['teamStats']['overs']) + ' - ' + str(
                away_team_info['teamStats']['unders']) + ' - ' + str(away_team_info['teamStats']['pushes']) if
            away_team_info['teamStats']['overs'] is not None and
            away_team_info['teamStats']['unders'] is not None and
            away_team_info['teamStats']['pushes'] is not None else None,
            'H_net_units': home_team_info['teamStats']['netUnits'] if
            home_team_info['teamStats']['netUnits'] is not None else None,
            'A_net_units': away_team_info['teamStats']['netUnits'] if
            away_team_info['teamStats']['netUnits'] is not None else None,
            'H_road': str(home_team_info['teamStats']['awaySuWins']) + ' - ' + str(home_team_info['teamStats'][
                                                                                       'awaySuLosses']) + ' - ' + str(
                home_team_info['teamStats']['awaySuTies']) if
            home_team_info['teamStats']['awaySuWins'] is not None and
            home_team_info['teamStats']['awaySuLosses'] is not None and
            home_team_info['teamStats']['awaySuTies'] is not None else None,
            'A_road': str(away_team_info['teamStats']['awaySuWins']) + ' - ' + str(away_team_info['teamStats'][
                                                                                       'awaySuLosses']) + ' - ' + str(
                away_team_info['teamStats']['awaySuTies']) if
            away_team_info['teamStats']['awaySuWins'] is not None and
            away_team_info['teamStats']['awaySuLosses'] is not None and
            away_team_info['teamStats']['awaySuTies'] is not None else None,
            'H_home': str(home_team_info['teamStats']['homeSuWins']) + ' - ' + str(home_team_info['teamStats'][
                                                                                       'homeSuLosses']) + ' - ' + str(
                home_team_info['teamStats']['homeSuTies']) if
            home_team_info['teamStats']['homeSuWins'] is not None and
            home_team_info['teamStats']['homeSuLosses'] is not None and
            home_team_info['teamStats']['homeSuTies'] is not None else None,
            'A_home': str(away_team_info['teamStats']['homeSuWins']) + ' - ' + str(away_team_info['teamStats'][
                                                                                       'homeSuLosses']) + ' - ' + str(
                away_team_info['teamStats']['homeSuTies']) if
            away_team_info['teamStats']['homeSuWins'] is not None and
            away_team_info['teamStats']['homeSuLosses'] is not None and
            away_team_info['teamStats']['homeSuTies'] is not None else None,
            'H_season_win': home_team_info['teamStats']['wins'] / (
                    home_team_info['teamStats']['wins'] + home_team_info['teamStats']['losses']) if
            home_team_info['teamStats']['wins'] is not None and home_team_info['teamStats'][
                'losses'] is not None else None,
            'A_season_win': away_team_info['teamStats']['wins'] / (
                    away_team_info['teamStats']['wins'] + away_team_info['teamStats']['losses']) if
            away_team_info['teamStats']['wins'] is not None and away_team_info['teamStats'][
                'losses'] is not None else None,
            'H_games': home_team_info['teamStats']['games'] if home_team_info['teamStats'][
                                                                   'games'] is not None else None,
            'A_games': away_team_info['teamStats']['games'] if away_team_info['teamStats'][
                                                                   'games'] is not None else None,
            'H_ATS_units': home_team_info['teamStats']['atsUnits'] if
            home_team_info['teamStats']['atsUnits'] is not None else None,
            'A_ATS_units': away_team_info['teamStats']['atsUnits'] if
            away_team_info['teamStats']['atsUnits'] is not None else None,
            'H_road_ATS': str(home_team_info['teamStats']['awayAtsWins']) + ' - ' + str(home_team_info['teamStats'][
                                                                                            'awayAtsLosses']) + ' - ' + str(
                home_team_info['teamStats']['awayAtsTies']) if
            home_team_info['teamStats']['awayAtsWins'] is not None and
            home_team_info['teamStats']['awayAtsLosses'] is not None and
            home_team_info['teamStats']['awayAtsTies'] is not None else None,
            'A_road_ATS': str(away_team_info['teamStats']['awayAtsWins']) + ' - ' + str(away_team_info['teamStats'][
                                                                                            'awayAtsLosses']) + ' - ' + str(
                away_team_info['teamStats']['awayAtsTies']) if
            away_team_info['teamStats']['awayAtsWins'] is not None and
            away_team_info['teamStats']['awayAtsLosses'] is not None and
            away_team_info['teamStats']['awayAtsTies'] is not None else None,
            'H_home_ATS': str(home_team_info['teamStats']['homeAtsWins']) + ' - ' + str(home_team_info['teamStats'][
                                                                                            'homeAtsLosses']) + ' - ' + str(
                home_team_info['teamStats']['homeAtsTies']) if
            home_team_info['teamStats']['homeAtsWins'] is not None and
            home_team_info['teamStats']['homeAtsLosses'] is not None and
            home_team_info['teamStats']['homeAtsTies'] is not None else None,
            'A_home_ATS': str(away_team_info['teamStats']['homeAtsWins']) + ' - ' + str(away_team_info['teamStats'][
                                                                                            'homeAtsLosses']) + ' - ' + str(
                away_team_info['teamStats']['homeAtsTies']) if
            away_team_info['teamStats']['homeAtsWins'] is not None and
            away_team_info['teamStats']['homeAtsLosses'] is not None and
            away_team_info['teamStats']['homeAtsTies'] is not None else None,
            'H_ATS_win': home_team_info['teamStats']['atsWinPercent'] / 100 if
            home_team_info['teamStats']['atsWinPercent'] is not None else None,
            'A_ATS_win': away_team_info['teamStats']['atsWinPercent'] / 100 if
            away_team_info['teamStats']['atsWinPercent'] is not None else None,
            'H_ATS_rec': str(home_team_info['teamStats']['atswins']) + ' - ' + str(home_team_info[
                                                                                       'teamStats'][
                                                                                       'atslosses']) + ' - ' + str(
                home_team_info['teamStats']['atsties']) if
            home_team_info['teamStats']['atswins'] is not None and
            home_team_info['teamStats']['atslosses'] is not None and
            home_team_info['teamStats']['atsties'] is not None else None,
            'A_ATS_rec': str(away_team_info['teamStats']['atswins']) + ' - ' + str(away_team_info[
                                                                                       'teamStats'][
                                                                                       'atslosses']) + ' - ' + str(
                away_team_info['teamStats']['atsties']) if
            away_team_info['teamStats']['atswins'] is not None and
            away_team_info['teamStats']['atslosses'] is not None and
            away_team_info['teamStats']['atsties'] is not None else None,
            'U_of_tickets': event_stats[0]['underCount'] if
            event_stats[0] is not None and event_stats[0]['underCount'] is not None else None,
            'O_of_tickets': event_stats[0]['overCount'] if
            event_stats[0] is not None and event_stats[0]['overCount'] is not None else None,
            'H_ml_of_tickets': event_stats[0]['homeMoneyCount'] if
            event_stats[0] is not None and event_stats[0]['homeMoneyCount'] is not None else None,
            'A_ml_of_tickets': event_stats[0]['awayMoneyCount'] if
            event_stats[0] is not None and event_stats[0]['awayMoneyCount'] is not None else None,
            'H_sp_of_tickets': event_stats[0]['homeSpreadCount'] if
            event_stats[0] is not None and event_stats[0]['homeSpreadCount'] is not None else None,
            'A_sp_of_tickets': event_stats[0]['awaySpreadCount'] if
            event_stats[0] is not None and event_stats[0]['awaySpreadCount'] is not None else None,
            'H_open_spread': open_info[0]['homeSpread'] if
            open_info[0] is not None and open_info[0]['homeSpread'] is not None else None,
            'A_open_spread': open_info[0]['awaySpread'] if
            open_info[0] is not None and open_info[0]['awaySpread'] is not None else None,
            'H_open_moneyline': open_info[0]['homeMoney'] if
            open_info[0] is not None and open_info[0]['homeMoney'] is not None else None,
            'A_open_moneyline': open_info[0]['awayMoney'] if
            open_info[0] is not None and open_info[0]['awayMoney'] is not None else None,
            'Open_U': open_info[0]['total'] if open_info[0] is not None and open_info[0]['total'] is not None and
                                               event['ouRating']['preferredTotal'] is not None and
                                               event['ouRating']['preferredTotal'] is 'under' else None,
            'Open_O': open_info[0]['total'] if open_info[0] is not None and open_info[0]['total'] is not None and
                                               event['ouRating']['preferredTotal'] is not None and
                                               event['ouRating']['preferredTotal'] is 'over' else None,
            'H_open_1h_spread': open_info[1]['homeSpread'] if
            open_info[1] is not None and open_info[1]['homeSpread'] is not None else None,
            'A_open_1h_spread': open_info[1]['awaySpread'] if
            open_info[1] is not None and open_info[1]['awaySpread'] is not None else None,
            'H_open_1h_moneyline': open_info[1]['homeMoney'] if
            open_info[1] is not None and open_info[1]['homeMoney'] is not None else None,
            'A_open_1h_moneyline': open_info[1]['awayMoney'] if
            open_info[1] is not None and open_info[1]['awayMoney'] is not None else None,
            'Open_1h_U': open_info[1]['total'] if open_info[1] is not None and open_info[1]['total'] is not None and
                                                  event['ou1HRating']['preferredTotal'] is not None and
                                                  event['ou1HRating']['preferredTotal'] is 'under' else None,
            'Open_1h_O': open_info[1]['total'] if open_info[1] is not None and open_info[1]['total'] is not None and
                                                  event['ou1HRating']['preferredTotal'] is not None and
                                                  event['ou1HRating']['preferredTotal'] is 'over' else None,
            'H_open_2h_spread': open_info[2]['homeSpread'] if
            open_info[2] is not None and open_info[2]['homeSpread'] is not None else None,
            'A_open_2h_spread': open_info[2]['awaySpread'] if
            open_info[2] is not None and open_info[2]['awaySpread'] is not None else None,
            'H_open_2h_moneyline': open_info[2]['homeMoney'] if
            open_info[2] is not None and open_info[2]['homeMoney'] is not None else None,
            'A_open_2h_moneyline': open_info[2]['awayMoney'] if
            open_info[2] is not None and open_info[2]['awayMoney'] is not None else None
        }
        if is_nba:
            fields['H_points_against'] = home_team_info['teamStats']['pointsAgainst'] if \
                home_team_info['teamStats']['pointsAgainst'] is not None else None
            fields['A_points_against'] = away_team_info['teamStats']['pointsAgainst'] if \
                away_team_info['teamStats']['pointsAgainst'] is not None else None
            fields['H_points_for'] = home_team_info['teamStats']['pointsFor'] if \
                home_team_info['teamStats']['pointsFor'] is not None else None
            fields['A_points_for'] = away_team_info['teamStats']['pointsFor'] if \
                away_team_info['teamStats']['pointsFor'] is not None else None
            record = airtable_betql_nba.match('ID', event['id'])
            if record:
                airtable_betql_nba.replace(record['id'], fields)
            else:
                airtable_betql_nba.insert(fields)
        else:
            record = airtable_betql_ncaa.match('ID', event['id'])
            if record:
                airtable_betql_ncaa.replace(record['id'], fields)
            else:
                airtable_betql_ncaa.insert(fields)


print("Betql-NCAA work")
betql_work(0)
print("Betql-NBA work")
betql_work(1)
print("Finished betql work")
