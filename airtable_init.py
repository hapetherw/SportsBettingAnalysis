from airtable import Airtable
from config import AIRTABLE_BASE_KEY
from config import AIRTABLE_API_KEY

airtable_ncaab = Airtable(AIRTABLE_BASE_KEY, 'Oddshark_NCAA', api_key=AIRTABLE_API_KEY)
airtable_nba = Airtable(AIRTABLE_BASE_KEY, 'Oddshark_NBA', api_key=AIRTABLE_API_KEY)
airtable_haslametrics = Airtable(AIRTABLE_BASE_KEY, 'HaslaMetrics', api_key=AIRTABLE_API_KEY)
airtable_teamranking_ncaa = Airtable(AIRTABLE_BASE_KEY, 'TeamRanking_NCAA', api_key=AIRTABLE_API_KEY)
airtable_teamranking_nba = Airtable(AIRTABLE_BASE_KEY, 'TeamRanking_NBA', api_key=AIRTABLE_API_KEY)
airtable_pickwise_ncaa = Airtable(AIRTABLE_BASE_KEY, 'Pickwise_NCAA', api_key=AIRTABLE_API_KEY)
airtable_pickwise_nba = Airtable(AIRTABLE_BASE_KEY, 'Pickwise_NBA', api_key=AIRTABLE_API_KEY)
airtable_espn_ncaa = Airtable(AIRTABLE_BASE_KEY, 'Espn_NCAA', api_key=AIRTABLE_API_KEY)
airtable_vegasinsider_ncaa = Airtable(AIRTABLE_BASE_KEY, 'VegasInsider_NCAA', api_key=AIRTABLE_API_KEY)
airtable_betql_ncaa = Airtable(AIRTABLE_BASE_KEY, 'BetQL_NCAA', api_key=AIRTABLE_API_KEY)
airtable_betql_nba = Airtable(AIRTABLE_BASE_KEY, 'BetQL_NBA', api_key=AIRTABLE_API_KEY)
airtable_season = Airtable(AIRTABLE_BASE_KEY, 'Season', api_key=AIRTABLE_API_KEY)
airtable_ncaa_team = Airtable(AIRTABLE_BASE_KEY, 'NCAA Teams', api_key=AIRTABLE_API_KEY)
airtable_nba_team = Airtable(AIRTABLE_BASE_KEY, 'NBA Teams', api_key=AIRTABLE_API_KEY)
airtable_game_date = Airtable(AIRTABLE_BASE_KEY, 'Event_Date', api_key=AIRTABLE_API_KEY)
airtable_game_time = Airtable(AIRTABLE_BASE_KEY, 'Game Time', api_key=AIRTABLE_API_KEY)
airtable_bet_type = Airtable(AIRTABLE_BASE_KEY, 'Bet Types', api_key=AIRTABLE_API_KEY)

oddshark_ncaa_info = ['Team1', 'Team2', 'Date', 'Time', 'PredictedScoreATS', 'PredictedScoreTotal', 'ComputerPickATS',
                      'ComputerPickTotal', 'PublicConsensusATS', 'PublicConsensusTotal', 'ConsensusBetATS',
                      'ConsensusBetTotal']
oddshark_nba_info = ['Team1', 'Team2', 'Date', 'Time', 'PredictedScoreATS', 'PredictedScoreTotal', 'ComputerPickATS',
                     'ComputerPickTotal', 'PublicConsensusATS', 'PublicConsensusTotal', 'ConsensusBetATS',
                     'ConsensusBetTotal']
teamranking_ncaa_info = ['Team1', 'Team2', 'Date', 'Team1Rot', 'Team2Rot', 'GameWinner', 'ATS', 'Total',
                         'MoneyLineValue']
teamranking_nba_info = ['Team1', 'Team2', 'Date', 'Team1Rot', 'Team2Rot', 'GameWinner', 'ATS', 'Total',
                        'MoneyLineValue']
pickwise_ncaa_info = ['Team1', 'Team2', 'Date', 'Time', 'Team1Prediction', 'Team2Prediction', 'Team1Outcome',
                      'Team2Outcome', 'Team1Market', 'Team2Market']
pickwise_nba_info = ['Team1', 'Team2', 'Date', 'Time', 'Team1Prediction', 'Team2Prediction', 'Team1Outcome',
                     'Team2Outcome', 'Team1Market', 'Team2Market']
espn_ncaa_info = ['Season', 'Team', 'Ranking', 'Conf', 'W_L', 'BPI_OFF', 'BPI_DEF', 'WEEK_RANK_CHANGE']
vegasinsider_ncaa_info = ['Season', 'Team', 'Rank', 'TOTAL_POWER', 'CONF_ADJ_PERF_NDEX', 'RAW_PERF_NDEX', 'CONF_ADJ_RTG',
                          'PURE_RTG', 'SU_W', 'SU_L', 'AVE_PF', 'AVE_PA', 'AVE_MGN', 'PS_W', 'PS_L', 'PS_P', 'HCV',
                          'PURE_AOPR', 'CONF_ADJ_AOPR', 'ALPA', 'ARVL', 'Sked_Strgth', 'Sked_Strgth_Conf_Comp',
                          'RN_W', 'RN_L']
hasla_metrics_info = ['Team1', 'Team2', 'Date', 'Team1Rank', 'Team2Rank', 'Team1Score', 'Team2Score']
ncaa_team_info = ['NCAA Team Name', 'Name Variations 1', 'Name Variations 2']
nba_team_info = ['NBA Team Name', 'Name Variation 1']
game_date_info = ['Game Date']
game_time_info = ['Game Time']
season_info = ['SeasonName']
bet_type_info = ['Bet Types']
