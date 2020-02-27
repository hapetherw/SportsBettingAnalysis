import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


class TeamRankingNCAA(Base):
    __tablename__ = 'TeamRankingNCAA'
    gsheet_table_columns = ['Team1ShortName', 'Team1FullName', 'Team2ShortName', 'Team2FullName', 'Team1Rot',
                            'Team2Rot', 'GameWinner', 'ATS', 'Total', 'MoneyLineValue', 'Date']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Team1ID = Column(Integer, nullable=True)
    Team1Rot = Column(Integer, nullable=True)
    Team2ID = Column(Integer, nullable=True)
    Team2Rot = Column(Integer, nullable=True)
    GameWinner = Column(String, nullable=True)
    ATS = Column(String, nullable=True)
    Total = Column(String, nullable=True)
    MoneyLineValue = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, team1_id, team1_rot, team2_id, team2_rot, game_winner='',
                 ats='', total='', money_line_value='', date=''):
        self.Team1ID = team1_id
        self.Team1Rot = team1_rot
        self.Team2ID = team2_id
        self.Team2Rot = team2_rot
        self.GameWinner = game_winner
        self.ATS = ats
        self.Total = total
        self.MoneyLineValue = money_line_value
        self.Date = date

    def __repr__(self):
        return "<TeamRankingNCAA(Team1ID='{}', Team1Rot='{}', Team2ID={}, " \
               "Team2Rot={}, GameWinner={}, ATS={}, Total={}, MoneyLineValue={}, Date={}, CreatedDate={})>" \
            .format(self.Team1ID, self.Team1Rot, self.Team2ID, self.Team2Rot,
                    self.GameWinner, self.ATS, self.Total, self.MoneyLineValue, self.Date, self.CreatedDate)


class TeamRankingNBA(Base):
    __tablename__ = 'TeamRankingNBA'
    gsheet_table_columns = ['Team1ShortName', 'Team1FullName', 'Team2ShortName', 'Team2FullName', 'Team1Rot',
                            'Team2Rot', 'GameWinner', 'ATS', 'Total', 'MoneyLineValue', 'Date']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Team1ID = Column(Integer, nullable=True)
    Team1Rot = Column(Integer, nullable=True)
    Team2ID = Column(Integer, nullable=True)
    Team2Rot = Column(Integer, nullable=True)
    GameWinner = Column(String, nullable=True)
    ATS = Column(String, nullable=True)
    Total = Column(String, nullable=True)
    MoneyLineValue = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, team1_id, team1_rot, team2_id, team2_rot, game_winner='',
                 ats='', total='', money_line_value='', date=''):
        self.Team1ID = team1_id
        self.Team1Rot = team1_rot
        self.Team2ID = team2_id
        self.Team2Rot = team2_rot
        self.GameWinner = game_winner
        self.ATS = ats
        self.Total = total
        self.MoneyLineValue = money_line_value
        self.Date = date

    def __repr__(self):
        return "<TeamRankingNBA(Team1ID='{}', Team1Rot='{}', Team2ID={}, " \
               "Team2Rot={}, GameWinner={}, ATS={}, Total={}, MoneyLineValue={}, Date={}, CreatedDate={})>" \
            .format(self.Team1ID, self.Team1Rot, self.Team2ID, self.Team2Rot,
                    self.GameWinner, self.ATS, self.Total, self.MoneyLineValue, self.Date, self.CreatedDate)


class PicksWiseNBA(Base):
    __tablename__ = 'PicksWiseNBA'
    gsheet_table_columns = ['Team1ShortName', 'Team1FullName', 'Team2ShortName', 'Team2FullName', 'Date', 'Time',
                            'Team1Prediction', 'Team1PickOutcome', 'Team1PickMarket', 'Team2Prediction',
                            'Team2PickOutcome', 'Team2PickMarket']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Team1ID = Column(Integer, nullable=True)
    Team2ID = Column(Integer, nullable=True)
    Team1Prediction = Column(String, nullable=True)
    Team1PickOutcome = Column(String, nullable=True)
    Team1PickMarket = Column(String, nullable=True)
    Team2Prediction = Column(String, nullable=True)
    Team2PickOutcome = Column(String, nullable=True)
    Team2PickMarket = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, team1_id, team2_id, team1_prediction='', team1_pick_outcome='',
                 team1_pick_market='', team2_prediction='', team2_pick_outcome='',
                 team2_pick_market='', date='', time=''):
        self.Team1ID = team1_id
        self.Team2ID = team2_id
        self.Team1Prediction = team1_prediction
        self.Team1PickOutcome = team1_pick_outcome
        self.Team1PickMarket = team1_pick_market
        self.Team2Prediction = team2_prediction
        self.Team2PickOutcome = team2_pick_outcome
        self.Team2PickMarket = team2_pick_market
        self.Date = date
        self.Time = time

    def __repr__(self):
        return "<PicksWiseNBA(Team1ID='{}', Team2ID='{}', Team1Prediction={}, " \
               "Team1PickOutcome={}, Team1PickMarket={}, Team2Prediction={}, Team2PickOutcome={}, " \
               "Team2PickMarket={}, Date={}, Time={}, CreatedDate={})>" \
            .format(self.Team1ID, self.Team2ID, self.Team1Prediction, self.Team1PickOutcome,
                    self.Team1PickMarket, self.Team2Prediction, self.Team2PickOutcome,
                    self.Team2PickMarket, self.Date, self.Time, self.CreatedDate)


class PicksWiseNCAA(Base):
    __tablename__ = 'PicksWiseNCAA'
    gsheet_table_columns = ['Team1ShortName', 'Team1FullName', 'Team2ShortName', 'Team2FullName', 'Date', 'Time',
                            'Team1Prediction', 'Team1PickOutcome', 'Team1PickMarket', 'Team2Prediction',
                            'Team2PickOutcome', 'Team2PickMarket']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Team1ID = Column(Integer, nullable=True)
    Team2ID = Column(Integer, nullable=True)
    Team1Prediction = Column(String, nullable=True)
    Team1PickOutcome = Column(String, nullable=True)
    Team1PickMarket = Column(String, nullable=True)
    Team2Prediction = Column(String, nullable=True)
    Team2PickOutcome = Column(String, nullable=True)
    Team2PickMarket = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, team1_id, team2_id, team1_prediction='', team1_pick_outcome='',
                 team1_pick_market='', team2_prediction='', team2_pick_outcome='',
                 team2_pick_market='', date='', time=''):
        self.Team1ID = team1_id
        self.Team2ID = team2_id
        self.Team1Prediction = team1_prediction
        self.Team1PickOutcome = team1_pick_outcome
        self.Team1PickMarket = team1_pick_market
        self.Team2Prediction = team2_prediction
        self.Team2PickOutcome = team2_pick_outcome
        self.Team2PickMarket = team2_pick_market
        self.Date = date
        self.Time = time

    def __repr__(self):
        return "<PicksWiseNCAA(Team1ID='{}', Team2ID='{}', Team1Prediction={}, " \
               "Team1PickOutcome={}, Team1PickMarket={}, Team2Prediction={}, Team2PickOutcome={}, " \
               "Team2PickMarket={}, Date={}, Time={}, CreatedDate={})>" \
            .format(self.Team1ID, self.Team2ID, self.Team1Prediction, self.Team1PickOutcome,
                    self.Team1PickMarket, self.Team2Prediction, self.Team2PickOutcome,
                    self.Team2PickMarket, self.Date, self.Time, self.CreatedDate)
