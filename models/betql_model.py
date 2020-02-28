import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float

from models.model import Base


class BetQL_NCAA(Base):
    __tablename__ = 'BetQL_NCAA'
    gsheet_table_columns = ['SlugID', 'HomeTeamShortName', 'HomeTeamFullName', 'AwayTeamShortName', 'AwayTeamFullName',
                            'EventState', 'StartDate', 'H_current_spread', 'A_current_spread', 'Spread_best_rating',
                            'H_current_moneyline', 'A_current_moneyline', 'Moneyline_best_rating', 'Current_U',
                            'Current_O', 'Total_best_rating', 'H_current_1h_spread', 'A_current_1h_spread',
                            '1h_spread_best_rating', 'H_current_1h_moneyline', 'A_current_1h_moneyline',
                            '1h_moneyline_best_rating', 'Current_1h_U', 'Current_1h_O', '1h_total_best_rating',
                            'H_current_2h_spread', 'A_current_2h_spread', 'H_current_2h_moneyline',
                            'A_current_2h_moneyline', 'H_road_ou', 'A_road_ou', 'H_home_ou', 'A_home_ou', 'H_under',
                            'A_under', 'H_over', 'A_over', 'H_under_record', 'A_under_record', 'H_over_record',
                            'A_over_record', 'H_net_units', 'A_net_units', 'H_road', 'A_road', 'H_home', 'A_home',
                            'H_season_win', 'A_season_win', 'H_games', 'A_games', 'H_ATS_units', 'A_ATS_units',
                            'H_road_ATS', 'A_road_ATS', 'H_home_ATS', 'A_home_ATS', 'H_ATS_win', 'A_ATS_win',
                            'H_ATS_rec', 'A_ATS_rec', 'U_of_tickets', 'O_of_tickets', 'H_ml_of_tickets',
                            'A_ml_of_tickets', 'H_sp_of_tickets', 'A_sp_of_tickets', 'H_open_spread', 'A_open_spread',
                            'H_open_moneyline', 'A_open_moneyline', 'Open_U', 'Open_O', 'H_open_1h_spread',
                            'A_open_1h_spread', 'H_open_1h_moneyline', 'A_open_1h_moneyline', 'Open_1h_U', 'Open_1h_O',
                            'H_open_2h_spread', 'A_open_2h_spread', 'H_open_2h_moneyline', 'A_open_2h_moneyline']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    SlugID = Column(String, nullable=True)
    HomeTeamID = Column(Integer, nullable=True)
    AwayTeamID = Column(Integer, nullable=True)
    EventState = Column(String, nullable=True)
    StartDate = Column(String, nullable=True)
    H_current_spread = Column(Float, nullable=True)
    A_current_spread = Column(Float, nullable=True)
    Spread_best_rating = Column(Integer, nullable=True)
    H_current_moneyline = Column(Float, nullable=True)
    A_current_moneyline = Column(Float, nullable=True)
    Moneyline_best_rating = Column(Integer, nullable=True)
    Current_U = Column(Float, nullable=True)
    Current_O = Column(Float, nullable=True)
    Total_best_rating = Column(Integer, nullable=True)
    H_current_1h_spread = Column(Float, nullable=True)
    A_current_1h_spread = Column(Float, nullable=True)
    First_spread_best_rating = Column(Integer, nullable=True)
    H_current_1h_moneyline = Column(Float, nullable=True)
    A_current_1h_moneyline = Column(Float, nullable=True)
    First_moneyline_best_rating = Column(Integer, nullable=True)
    Current_1h_U = Column(Float, nullable=True)
    Current_1h_O = Column(Float, nullable=True)
    First_total_best_rating = Column(Integer, nullable=True)
    H_current_2h_spread = Column(Float, nullable=True)
    A_current_2h_spread = Column(Float, nullable=True)
    H_current_2h_moneyline = Column(Float, nullable=True)
    A_current_2h_moneyline = Column(Float, nullable=True)
    H_road_ou = Column(String, nullable=True)
    A_road_ou = Column(String, nullable=True)
    H_home_ou = Column(String, nullable=True)
    A_home_ou = Column(String, nullable=True)
    H_under = Column(Float, nullable=True)
    A_under = Column(Float, nullable=True)
    H_over = Column(Float, nullable=True)
    A_over = Column(Float, nullable=True)
    H_under_record = Column(String, nullable=True)
    A_under_record = Column(String, nullable=True)
    H_over_record = Column(String, nullable=True)
    A_over_record = Column(String, nullable=True)
    H_net_units = Column(Float, nullable=True)
    A_net_units = Column(Float, nullable=True)
    H_road = Column(String, nullable=True)
    A_road = Column(String, nullable=True)
    H_home = Column(String, nullable=True)
    A_home = Column(String, nullable=True)
    H_season_win = Column(Float, nullable=True)
    A_season_win = Column(Float, nullable=True)
    H_games = Column(Integer, nullable=True)
    A_games = Column(Integer, nullable=True)
    H_ATS_units = Column(Float, nullable=True)
    A_ATS_units = Column(Float, nullable=True)
    H_road_ATS = Column(String, nullable=True)
    A_road_ATS = Column(String, nullable=True)
    H_home_ATS = Column(String, nullable=True)
    A_home_ATS = Column(String, nullable=True)
    H_ATS_win = Column(Float, nullable=True)
    A_ATS_win = Column(Float, nullable=True)
    H_ATS_rec = Column(String, nullable=True)
    A_ATS_rec = Column(String, nullable=True)
    U_of_tickets = Column(Float, nullable=True)
    O_of_tickets = Column(Float, nullable=True)
    H_ml_of_tickets = Column(Float, nullable=True)
    A_ml_of_tickets = Column(Float, nullable=True)
    H_sp_of_tickets = Column(Float, nullable=True)
    A_sp_of_tickets = Column(Float, nullable=True)
    H_open_spread = Column(Float, nullable=True)
    A_open_spread = Column(Float, nullable=True)
    H_open_moneyline = Column(Float, nullable=True)
    A_open_moneyline = Column(Float, nullable=True)
    Open_U = Column(Float, nullable=True)
    Open_O = Column(Float, nullable=True)
    H_open_1h_spread = Column(Float, nullable=True)
    A_open_1h_spread = Column(Float, nullable=True)
    H_open_1h_moneyline = Column(Float, nullable=True)
    A_open_1h_moneyline = Column(Float, nullable=True)
    Open_1h_U = Column(Float, nullable=True)
    Open_1h_O = Column(Float, nullable=True)
    H_open_2h_spread = Column(Float, nullable=True)
    A_open_2h_spread = Column(Float, nullable=True)
    H_open_2h_moneyline = Column(Float, nullable=True)
    A_open_2h_moneyline = Column(Float, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, SlugID='', HomeTeamID=-1, AwayTeamID=-1, EventState='', StartDate='',
                 H_current_spread=0, A_current_spread=0, Spread_best_rating=0, H_current_moneyline=0,
                 A_current_moneyline=0, Moneyline_best_rating=0, Current_U=0, Current_O=0, Total_best_rating=0,
                 H_current_1h_spread=0, A_current_1h_spread=0, First_spread_best_rating=0, H_current_1h_moneyline=0,
                 A_current_1h_moneyline=0, First_moneyline_best_rating=0, Current_1h_U=0, Current_1h_O=0,
                 First_total_best_rating=0, H_current_2h_spread=0, A_current_2h_spread=0, H_current_2h_moneyline=0,
                 A_current_2h_moneyline=0, H_road_ou='', A_road_ou='', H_home_ou='', A_home_ou='', H_under=0,
                 A_under=0, H_over=0, A_over=0, H_under_record='', A_under_record='', H_over_record='',
                 A_over_record='', H_net_units=0, A_net_units=0, H_road='', A_road='', H_home='', A_home='',
                 H_season_win=0,
                 A_season_win=0, H_games=0, A_games=0, H_ATS_units=0, A_ATS_units=0, H_road_ATS='', A_road_ATS='',
                 H_home_ATS='', A_home_ATS='', H_ATS_win=0, A_ATS_win=0, H_ATS_rec='', A_ATS_rec='',
                 U_of_tickets=0, O_of_tickets=0, H_ml_of_tickets=0, A_ml_of_tickets=0, H_sp_of_tickets=0,
                 A_sp_of_tickets=0, H_open_spread=0, A_open_spread=0, H_open_moneyline=0, A_open_moneyline=0,
                 Open_U=0, Open_O=0, H_open_1h_spread=0, A_open_1h_spread=0, H_open_1h_moneyline=0,
                 A_open_1h_moneyline=0, Open_1h_U=0, Open_1h_O=0, H_open_2h_spread=0, A_open_2h_spread=0,
                 H_open_2h_moneyline=0, A_open_2h_moneyline=0):
        self.SlugID = SlugID
        self.HomeTeamID = HomeTeamID
        self.AwayTeamID = AwayTeamID
        self.EventState = EventState
        self.StartDate = StartDate
        self.H_current_spread = H_current_spread
        self.A_current_spread = A_current_spread
        self.Spread_best_rating = Spread_best_rating
        self.H_current_moneyline = H_current_moneyline
        self.A_current_moneyline = A_current_moneyline
        self.Moneyline_best_rating = Moneyline_best_rating
        self.Current_U = Current_U
        self.Current_O = Current_O
        self.Total_best_rating = Total_best_rating
        self.H_current_1h_spread = H_current_1h_spread
        self.A_current_1h_spread = A_current_1h_spread
        self.First_spread_best_rating = First_spread_best_rating
        self.H_current_1h_moneyline = H_current_1h_moneyline
        self.A_current_1h_moneyline = A_current_1h_moneyline
        self.First_moneyline_best_rating = First_moneyline_best_rating
        self.Current_1h_U = Current_1h_U
        self.Current_1h_O = Current_1h_O
        self.First_total_best_rating = First_total_best_rating
        self.H_current_2h_spread = H_current_2h_spread
        self.A_current_2h_spread = A_current_2h_spread
        self.H_current_2h_moneyline = H_current_2h_moneyline
        self.A_current_2h_moneyline = A_current_2h_moneyline
        self.H_road_ou = H_road_ou
        self.A_road_ou = A_road_ou
        self.H_home_ou = H_home_ou
        self.A_home_ou = A_home_ou
        self.H_under = H_under
        self.A_under = A_under
        self.H_over = H_over
        self.A_over = A_over
        self.H_under_record = H_under_record
        self.A_under_record = A_under_record
        self.H_over_record = H_over_record
        self.A_over_record = A_over_record
        self.H_net_units = H_net_units
        self.A_net_units = A_net_units
        self.H_road = H_road
        self.A_road = A_road
        self.H_home = H_home
        self.A_home = A_home
        self.H_season_win = H_season_win
        self.A_season_win = A_season_win
        self.H_games = H_games
        self.A_games = A_games
        self.H_ATS_units = H_ATS_units
        self.A_ATS_units = A_ATS_units
        self.H_road_ATS = H_road_ATS
        self.A_road_ATS = A_road_ATS
        self.H_home_ATS = H_home_ATS
        self.A_home_ATS = A_home_ATS
        self.H_ATS_win = H_ATS_win
        self.A_ATS_win = A_ATS_win
        self.H_ATS_rec = H_ATS_rec
        self.A_ATS_rec = A_ATS_rec
        self.U_of_tickets = U_of_tickets
        self.O_of_tickets = O_of_tickets
        self.H_ml_of_tickets = H_ml_of_tickets
        self.A_ml_of_tickets = A_ml_of_tickets
        self.H_sp_of_tickets = H_sp_of_tickets
        self.A_sp_of_tickets = A_sp_of_tickets
        self.H_open_spread = H_open_spread
        self.A_open_spread = A_open_spread
        self.H_open_moneyline = H_open_moneyline
        self.A_open_moneyline = A_open_moneyline
        self.Open_U = Open_U
        self.Open_O = Open_O
        self.H_open_1h_spread = H_open_1h_spread
        self.A_open_1h_spread = A_open_1h_spread
        self.H_open_1h_moneyline = H_open_1h_moneyline
        self.A_open_1h_moneyline = A_open_1h_moneyline
        self.Open_1h_U = Open_1h_U
        self.Open_1h_O = Open_1h_O
        self.H_open_2h_spread = H_open_2h_spread
        self.A_open_2h_spread = A_open_2h_spread
        self.H_open_2h_moneyline = H_open_2h_moneyline
        self.A_open_2h_moneyline = A_open_2h_moneyline

    def __repr__(self):
        return "<BetQL_NCAA(SlugID={}, HomeTeamID={}, AwayTeamID={}, EventState={}, StartDate={}, " \
               "H_current_spread={}, A_current_spread={}, Spread_best_rating={}, H_current_moneyline={}, " \
               "A_current_moneyline={}, Moneyline_best_rating={}, Current_U={}, Current_O={}, " \
               "Total_best_rating={}, H_current_1h_spread={}, A_current_1h_spread={}, First_spread_best_rating={}, " \
               "H_current_1h_moneyline={}, A_current_1h_moneyline={}, First_moneyline_best_rating={}, Current_1h_U={}, " \
               "Current_1h_O={}, First_total_best_rating={}, " \
               "H_current_2h_spread={}, A_current_2h_spread={}, H_current_2h_moneyline={}, A_current_2h_moneyline={}, " \
               "H_road_ou={}, A_road_ou={}, H_home_ou={}, " \
               "A_home_ou={}, H_under={}, A_under={}, H_over={}, A_over={}, H_under_record={}, A_under_record={}, " \
               "H_over_record={}, A_over_record={}, H_net_units={}, A_net_units={}, H_road={}, A_road={}, " \
               "H_home={}, A_home={}, " \
               "H_season_win={}, A_season_win={}, H_games={}, A_games={}, H_ATS_units={}, A_ATS_units={}, " \
               "H_road_ATS={}, A_road_ATS={}, H_home_ATS={}, A_home_ATS={}, H_ATS_win={}, A_ATS_win={}, " \
               "H_ATS_rec={}, A_ATS_rec={}, U_of_tickets={}, O_of_tickets={}, H_ml_of_tickets={}, " \
               "A_ml_of_tickets={}, H_sp_of_tickets={}, A_sp_of_tickets={}, H_open_spread={}, A_open_spread={}, " \
               "H_open_moneyline={}, " \
               "A_open_moneyline={}, Open_U={}, Open_O={}, H_open_1h_spread={}, A_open_1h_spread={}, " \
               "H_open_1h_moneyline={}, A_open_1h_moneyline={}, " \
               "Open_1h_U={}, Open_1h_O={}, H_open_2h_spread={}, A_open_2h_spread={}, H_open_2h_moneyline={}, " \
               "A_open_2h_moneyline={}, CreatedDate={})>" \
            .format(self.SlugID, self.HomeTeamID, self.AwayTeamID, self.EventState, self.StartDate,
                    self.H_current_spread, self.A_current_spread, self.Spread_best_rating, self.H_current_moneyline,
                    self.A_current_moneyline, self.Moneyline_best_rating, self.Current_U, self.Current_O,
                    self.Total_best_rating,
                    self.H_current_1h_spread, self.A_current_1h_spread, self.First_spread_best_rating,
                    self.H_current_1h_moneyline,
                    self.A_current_1h_moneyline, self.First_moneyline_best_rating, self.Current_1h_U, self.Current_1h_O,
                    self.First_total_best_rating, self.H_current_2h_spread, self.A_current_2h_spread,
                    self.H_current_2h_moneyline,
                    self.A_current_2h_moneyline, self.H_road_ou, self.A_road_ou, self.H_home_ou, self.A_home_ou,
                    self.H_under,
                    self.A_under, self.H_over, self.A_over, self.H_under_record, self.A_under_record,
                    self.H_over_record,
                    self.A_over_record, self.H_net_units, self.A_net_units, self.H_road, self.A_road, self.H_home,
                    self.A_home,
                    self.H_season_win,
                    self.A_season_win, self.H_games, self.A_games, self.H_ATS_units, self.A_ATS_units, self.H_road_ATS,
                    self.A_road_ATS,
                    self.H_home_ATS, self.A_home_ATS, self.H_ATS_win, self.A_ATS_win, self.H_ATS_rec, self.A_ATS_rec,
                    self.U_of_tickets, self.O_of_tickets, self.H_ml_of_tickets, self.A_ml_of_tickets,
                    self.H_sp_of_tickets,
                    self.A_sp_of_tickets, self.H_open_spread, self.A_open_spread, self.H_open_moneyline,
                    self.A_open_moneyline,
                    self.Open_U, self.Open_O, self.H_open_1h_spread, self.A_open_1h_spread, self.H_open_1h_moneyline,
                    self.A_open_1h_moneyline, self.Open_1h_U, self.Open_1h_O, self.H_open_2h_spread,
                    self.A_open_2h_spread,
                    self.H_open_2h_moneyline, self.A_open_2h_moneyline, self.CreatedDate)


class BetQL_NBA(Base):
    __tablename__ = 'BetQL_NBA'
    gsheet_table_columns = ['SlugID', 'HomeTeamShortName', 'HomeTeamFullName', 'AwayTeamShortName', 'AwayTeamFullName',
                            'EventState', 'StartDate', 'H_current_spread', 'A_current_spread', 'Spread_best_rating',
                            'H_current_moneyline', 'A_current_moneyline', 'Moneyline_best_rating', 'Current_U',
                            'Current_O', 'Total_best_rating', 'H_current_1h_spread', 'A_current_1h_spread',
                            '1h_spread_best_rating', 'H_current_1h_moneyline', 'A_current_1h_moneyline',
                            '1h_moneyline_best_rating', 'Current_1h_U', 'Current_1h_O', '1h_total_best_rating',
                            'H_current_2h_spread', 'A_current_2h_spread', 'H_current_2h_moneyline',
                            'A_current_2h_moneyline', 'H_points_against', 'A_points_against', 'H_points_for',
                            'A_points_for', 'H_road_ou', 'A_road_ou', 'H_home_ou', 'A_home_ou', 'H_under',
                            'A_under', 'H_over', 'A_over', 'H_under_record', 'A_under_record', 'H_over_record',
                            'A_over_record', 'H_net_units', 'A_net_units', 'H_road', 'A_road', 'H_home', 'A_home',
                            'H_season_win', 'A_season_win', 'H_games', 'A_games', 'H_ATS_units', 'A_ATS_units',
                            'H_road_ATS', 'A_road_ATS', 'H_home_ATS', 'A_home_ATS', 'H_ATS_win', 'A_ATS_win',
                            'H_ATS_rec', 'A_ATS_rec', 'U_of_tickets', 'O_of_tickets', 'H_ml_of_tickets',
                            'A_ml_of_tickets', 'H_sp_of_tickets', 'A_sp_of_tickets', 'H_open_spread', 'A_open_spread',
                            'H_open_moneyline', 'A_open_moneyline', 'Open_U', 'Open_O', 'H_open_1h_spread',
                            'A_open_1h_spread', 'H_open_1h_moneyline', 'A_open_1h_moneyline', 'Open_1h_U', 'Open_1h_O',
                            'H_open_2h_spread', 'A_open_2h_spread', 'H_open_2h_moneyline', 'A_open_2h_moneyline']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    SlugID = Column(String, nullable=True)
    HomeTeamID = Column(Integer, nullable=True)
    AwayTeamID = Column(Integer, nullable=True)
    EventState = Column(String, nullable=True)
    StartDate = Column(String, nullable=True)
    H_current_spread = Column(Float, nullable=True)
    A_current_spread = Column(Float, nullable=True)
    Spread_best_rating = Column(Integer, nullable=True)
    H_current_moneyline = Column(Float, nullable=True)
    A_current_moneyline = Column(Float, nullable=True)
    Moneyline_best_rating = Column(Integer, nullable=True)
    Current_U = Column(Float, nullable=True)
    Current_O = Column(Float, nullable=True)
    Total_best_rating = Column(Integer, nullable=True)
    H_current_1h_spread = Column(Float, nullable=True)
    A_current_1h_spread = Column(Float, nullable=True)
    First_spread_best_rating = Column(Integer, nullable=True)
    H_current_1h_moneyline = Column(Float, nullable=True)
    A_current_1h_moneyline = Column(Float, nullable=True)
    First_moneyline_best_rating = Column(Integer, nullable=True)
    Current_1h_U = Column(Float, nullable=True)
    Current_1h_O = Column(Float, nullable=True)
    First_total_best_rating = Column(Integer, nullable=True)
    H_current_2h_spread = Column(Float, nullable=True)
    A_current_2h_spread = Column(Float, nullable=True)
    H_current_2h_moneyline = Column(Float, nullable=True)
    A_current_2h_moneyline = Column(Float, nullable=True)
    H_points_against = Column(Float, nullable=True)
    A_points_against = Column(Float, nullable=True)
    H_points_for = Column(Float, nullable=True)
    A_points_for = Column(Float, nullable=True)
    H_road_ou = Column(String, nullable=True)
    A_road_ou = Column(String, nullable=True)
    H_home_ou = Column(String, nullable=True)
    A_home_ou = Column(String, nullable=True)
    H_under = Column(Float, nullable=True)
    A_under = Column(Float, nullable=True)
    H_over = Column(Float, nullable=True)
    A_over = Column(Float, nullable=True)
    H_under_record = Column(String, nullable=True)
    A_under_record = Column(String, nullable=True)
    H_over_record = Column(String, nullable=True)
    A_over_record = Column(String, nullable=True)
    H_net_units = Column(Float, nullable=True)
    A_net_units = Column(Float, nullable=True)
    H_road = Column(String, nullable=True)
    A_road = Column(String, nullable=True)
    H_home = Column(String, nullable=True)
    A_home = Column(String, nullable=True)
    H_season_win = Column(Float, nullable=True)
    A_season_win = Column(Float, nullable=True)
    H_games = Column(Integer, nullable=True)
    A_games = Column(Integer, nullable=True)
    H_ATS_units = Column(Float, nullable=True)
    A_ATS_units = Column(Float, nullable=True)
    H_road_ATS = Column(String, nullable=True)
    A_road_ATS = Column(String, nullable=True)
    H_home_ATS = Column(String, nullable=True)
    A_home_ATS = Column(String, nullable=True)
    H_ATS_win = Column(Float, nullable=True)
    A_ATS_win = Column(Float, nullable=True)
    H_ATS_rec = Column(String, nullable=True)
    A_ATS_rec = Column(String, nullable=True)
    U_of_tickets = Column(Float, nullable=True)
    O_of_tickets = Column(Float, nullable=True)
    H_ml_of_tickets = Column(Float, nullable=True)
    A_ml_of_tickets = Column(Float, nullable=True)
    H_sp_of_tickets = Column(Float, nullable=True)
    A_sp_of_tickets = Column(Float, nullable=True)
    H_open_spread = Column(Float, nullable=True)
    A_open_spread = Column(Float, nullable=True)
    H_open_moneyline = Column(Float, nullable=True)
    A_open_moneyline = Column(Float, nullable=True)
    Open_U = Column(Float, nullable=True)
    Open_O = Column(Float, nullable=True)
    H_open_1h_spread = Column(Float, nullable=True)
    A_open_1h_spread = Column(Float, nullable=True)
    H_open_1h_moneyline = Column(Float, nullable=True)
    A_open_1h_moneyline = Column(Float, nullable=True)
    Open_1h_U = Column(Float, nullable=True)
    Open_1h_O = Column(Float, nullable=True)
    H_open_2h_spread = Column(Float, nullable=True)
    A_open_2h_spread = Column(Float, nullable=True)
    H_open_2h_moneyline = Column(Float, nullable=True)
    A_open_2h_moneyline = Column(Float, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, SlugID='', HomeTeamID=-1, AwayTeamID=-1, EventState='', StartDate='',
                 H_current_spread=0, A_current_spread=0, Spread_best_rating=0, H_current_moneyline=0,
                 A_current_moneyline=0, Moneyline_best_rating=0, Current_U=0, Current_O=0, Total_best_rating=0,
                 H_current_1h_spread=0, A_current_1h_spread=0, First_spread_best_rating=0, H_current_1h_moneyline=0,
                 A_current_1h_moneyline=0, First_moneyline_best_rating=0, Current_1h_U=0, Current_1h_O=0,
                 First_total_best_rating=0, H_current_2h_spread=0, A_current_2h_spread=0, H_current_2h_moneyline=0,
                 A_current_2h_moneyline=0, H_points_against=0, A_points_against=0, H_points_for=0, A_points_for=0,
                 H_road_ou='', A_road_ou='', H_home_ou='', A_home_ou='', H_under=0,
                 A_under=0, H_over=0, A_over=0, H_under_record='', A_under_record='', H_over_record='',
                 A_over_record='', H_net_units=0, A_net_units=0, H_road='', A_road='', H_home='', A_home='',
                 H_season_win=0,
                 A_season_win=0, H_games=0, A_games=0, H_ATS_units=0, A_ATS_units=0, H_road_ATS='', A_road_ATS='',
                 H_home_ATS='', A_home_ATS='', H_ATS_win=0, A_ATS_win=0, H_ATS_rec='', A_ATS_rec='',
                 U_of_tickets=0, O_of_tickets=0, H_ml_of_tickets=0, A_ml_of_tickets=0, H_sp_of_tickets=0,
                 A_sp_of_tickets=0, H_open_spread=0, A_open_spread=0, H_open_moneyline=0, A_open_moneyline=0,
                 Open_U=0, Open_O=0, H_open_1h_spread=0, A_open_1h_spread=0, H_open_1h_moneyline=0,
                 A_open_1h_moneyline=0, Open_1h_U=0, Open_1h_O=0, H_open_2h_spread=0, A_open_2h_spread=0,
                 H_open_2h_moneyline=0, A_open_2h_moneyline=0):
        self.SlugID = SlugID
        self.HomeTeamID = HomeTeamID
        self.AwayTeamID = AwayTeamID
        self.EventState = EventState
        self.StartDate = StartDate
        self.H_current_spread = H_current_spread
        self.A_current_spread = A_current_spread
        self.Spread_best_rating = Spread_best_rating
        self.H_current_moneyline = H_current_moneyline
        self.A_current_moneyline = A_current_moneyline
        self.Moneyline_best_rating = Moneyline_best_rating
        self.Current_U = Current_U
        self.Current_O = Current_O
        self.Total_best_rating = Total_best_rating
        self.H_current_1h_spread = H_current_1h_spread
        self.A_current_1h_spread = A_current_1h_spread
        self.First_spread_best_rating = First_spread_best_rating
        self.H_current_1h_moneyline = H_current_1h_moneyline
        self.A_current_1h_moneyline = A_current_1h_moneyline
        self.First_moneyline_best_rating = First_moneyline_best_rating
        self.Current_1h_U = Current_1h_U
        self.Current_1h_O = Current_1h_O
        self.First_total_best_rating = First_total_best_rating
        self.H_current_2h_spread = H_current_2h_spread
        self.A_current_2h_spread = A_current_2h_spread
        self.H_current_2h_moneyline = H_current_2h_moneyline
        self.A_current_2h_moneyline = A_current_2h_moneyline
        self.H_points_against = H_points_against
        self.A_points_against = A_points_against
        self.H_points_for = H_points_for
        self.A_points_for = A_points_for
        self.H_road_ou = H_road_ou
        self.A_road_ou = A_road_ou
        self.H_home_ou = H_home_ou
        self.A_home_ou = A_home_ou
        self.H_under = H_under
        self.A_under = A_under
        self.H_over = H_over
        self.A_over = A_over
        self.H_under_record = H_under_record
        self.A_under_record = A_under_record
        self.H_over_record = H_over_record
        self.A_over_record = A_over_record
        self.H_net_units = H_net_units
        self.A_net_units = A_net_units
        self.H_road = H_road
        self.A_road = A_road
        self.H_home = H_home
        self.A_home = A_home
        self.H_season_win = H_season_win
        self.A_season_win = A_season_win
        self.H_games = H_games
        self.A_games = A_games
        self.H_ATS_units = H_ATS_units
        self.A_ATS_units = A_ATS_units
        self.H_road_ATS = H_road_ATS
        self.A_road_ATS = A_road_ATS
        self.H_home_ATS = H_home_ATS
        self.A_home_ATS = A_home_ATS
        self.H_ATS_win = H_ATS_win
        self.A_ATS_win = A_ATS_win
        self.H_ATS_rec = H_ATS_rec
        self.A_ATS_rec = A_ATS_rec
        self.U_of_tickets = U_of_tickets
        self.O_of_tickets = O_of_tickets
        self.H_ml_of_tickets = H_ml_of_tickets
        self.A_ml_of_tickets = A_ml_of_tickets
        self.H_sp_of_tickets = H_sp_of_tickets
        self.A_sp_of_tickets = A_sp_of_tickets
        self.H_open_spread = H_open_spread
        self.A_open_spread = A_open_spread
        self.H_open_moneyline = H_open_moneyline
        self.A_open_moneyline = A_open_moneyline
        self.Open_U = Open_U
        self.Open_O = Open_O
        self.H_open_1h_spread = H_open_1h_spread
        self.A_open_1h_spread = A_open_1h_spread
        self.H_open_1h_moneyline = H_open_1h_moneyline
        self.A_open_1h_moneyline = A_open_1h_moneyline
        self.Open_1h_U = Open_1h_U
        self.Open_1h_O = Open_1h_O
        self.H_open_2h_spread = H_open_2h_spread
        self.A_open_2h_spread = A_open_2h_spread
        self.H_open_2h_moneyline = H_open_2h_moneyline
        self.A_open_2h_moneyline = A_open_2h_moneyline

    def __repr__(self):
        return "<BetQL_NBA(SlugID={}, HomeTeamID={}, AwayTeamID={}, EventState={}, StartDate={}, " \
               "H_current_spread={}, A_current_spread={}, Spread_best_rating={}, H_current_moneyline={}, " \
               "A_current_moneyline={}, Moneyline_best_rating={}, Current_U={}, Current_O={}, " \
               "Total_best_rating={}, H_current_1h_spread={}, A_current_1h_spread={}, First_spread_best_rating={}, " \
               "H_current_1h_moneyline={}, A_current_1h_moneyline={}, First_moneyline_best_rating={}, Current_1h_U={}, " \
               "Current_1h_O={}, First_total_best_rating={}, " \
               "H_current_2h_spread={}, A_current_2h_spread={}, H_current_2h_moneyline={}, A_current_2h_moneyline={}, " \
               "H_points_against={}, A_points_against={}, H_points_for={}, A_points_for={}, " \
               "H_road_ou={}, A_road_ou={}, H_home_ou={}, " \
               "A_home_ou={}, H_under={}, A_under={}, H_over={}, A_over={}, H_under_record={}, A_under_record={}, " \
               "H_over_record={}, A_over_record={}, H_net_units={}, A_net_units={}, H_road={}, " \
               "A_road={}, H_home={}, A_home={}, " \
               "H_season_win={}, A_season_win={}, H_games={}, A_games={}, H_ATS_units={}, A_ATS_units={}, " \
               "H_road_ATS={}, A_road_ATS={}, H_home_ATS={}, A_home_ATS={}, H_ATS_win={}, A_ATS_win={}, " \
               "H_ATS_rec={}, A_ATS_rec={}, U_of_tickets={}, O_of_tickets={}, H_ml_of_tickets={}, " \
               "A_ml_of_tickets={}, H_sp_of_tickets={}, A_sp_of_tickets={}, H_open_spread={}, A_open_spread={}, " \
               "H_open_moneyline={}, " \
               "A_open_moneyline={}, Open_U={}, Open_O={}, H_open_1h_spread={}, A_open_1h_spread={}, " \
               "H_open_1h_moneyline={}, A_open_1h_moneyline={}, " \
               "Open_1h_U={}, Open_1h_O={}, H_open_2h_spread={}, A_open_2h_spread={}, H_open_2h_moneyline={}, " \
               "A_open_2h_moneyline={}, CreatedDate={})>" \
            .format(self.SlugID, self.HomeTeamID, self.AwayTeamID, self.EventState, self.StartDate,
                    self.H_current_spread, self.A_current_spread, self.Spread_best_rating, self.H_current_moneyline,
                    self.A_current_moneyline, self.Moneyline_best_rating, self.Current_U, self.Current_O,
                    self.Total_best_rating,
                    self.H_current_1h_spread, self.A_current_1h_spread, self.First_spread_best_rating,
                    self.H_current_1h_moneyline,
                    self.A_current_1h_moneyline, self.First_moneyline_best_rating, self.Current_1h_U, self.Current_1h_O,
                    self.First_total_best_rating, self.H_current_2h_spread, self.A_current_2h_spread,
                    self.H_current_2h_moneyline, self.A_current_2h_moneyline, self.H_points_against,
                    self.A_points_against, self.H_points_for, self.A_points_for,
                    self.H_road_ou, self.A_road_ou, self.H_home_ou, self.A_home_ou, self.H_under,
                    self.A_under, self.H_over, self.A_over, self.H_under_record, self.A_under_record,
                    self.H_over_record, self.A_over_record,
                    self.H_net_units, self.A_net_units, self.H_road, self.A_road, self.H_home, self.A_home,
                    self.H_season_win,
                    self.A_season_win, self.H_games, self.A_games, self.H_ATS_units, self.A_ATS_units, self.H_road_ATS,
                    self.A_road_ATS,
                    self.H_home_ATS, self.A_home_ATS, self.H_ATS_win, self.A_ATS_win, self.H_ATS_rec, self.A_ATS_rec,
                    self.U_of_tickets, self.O_of_tickets, self.H_ml_of_tickets, self.A_ml_of_tickets,
                    self.H_sp_of_tickets,
                    self.A_sp_of_tickets, self.H_open_spread, self.A_open_spread, self.H_open_moneyline,
                    self.A_open_moneyline,
                    self.Open_U, self.Open_O, self.H_open_1h_spread, self.A_open_1h_spread, self.H_open_1h_moneyline,
                    self.A_open_1h_moneyline, self.Open_1h_U, self.Open_1h_O, self.H_open_2h_spread,
                    self.A_open_2h_spread,
                    self.H_open_2h_moneyline, self.A_open_2h_moneyline, self.CreatedDate)
