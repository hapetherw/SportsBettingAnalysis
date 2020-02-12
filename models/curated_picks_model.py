import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


class CuratedPicksNCAAB(Base):
    __tablename__ = 'CuratedPicksNCAAB'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstTeamName = Column(String, nullable=True)
    firstTeamRot = Column(String, nullable=True)
    secondTeamName = Column(String, nullable=True)
    secondTeamRot = Column(String, nullable=True)
    gameWinner = Column(String, nullable=True)
    ATS = Column(String, nullable=True)
    total = Column(String, nullable=True)
    moneyLineValue = Column(String, nullable=True)
    date = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, first_team_name='', first_team_rot='', second_team_name='', second_team_rot='', game_winner='',
                 ats='', total='', money_line_value='', date=''):
        self.firstTeamName = first_team_name
        self.firstTeamRot = first_team_rot
        self.secondTeamName = second_team_name
        self.secondTeamRot = second_team_rot
        self.gameWinner = game_winner
        self.ATS = ats
        self.total = total
        self.moneyLineValue = money_line_value
        self.date = date

    def __repr__(self):
        return "<CuratedPicksNCAAB(firstTeamName='{}', firstTeamRot='{}', secondTeamName={}, " \
               "secondTeamRot={}, gameWinner={}, ATS={}, total={}, moneyLineValue={}, date={}, createdDate={})>" \
            .format(self.firstTeamName, self.firstTeamRot, self.secondTeamName, self.secondTeamRot,
                    self.gameWinner, self.ATS, self.total, self.moneyLineValue, self.date, self.createdDate)


class CuratedPicksNBA(Base):
    __tablename__ = 'CuratedPicksNBA'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstTeamName = Column(String, nullable=True)
    firstTeamRot = Column(String, nullable=True)
    secondTeamName = Column(String, nullable=True)
    secondTeamRot = Column(String, nullable=True)
    gameWinner = Column(String, nullable=True)
    ATS = Column(String, nullable=True)
    total = Column(String, nullable=True)
    moneyLineValue = Column(String, nullable=True)
    date = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, first_team_name='', first_team_rot='', second_team_name='', second_team_rot='', game_winner='',
                 ats='', total='', money_line_value='', date=''):
        self.firstTeamName = first_team_name
        self.firstTeamRot = first_team_rot
        self.secondTeamName = second_team_name
        self.secondTeamRot = second_team_rot
        self.gameWinner = game_winner
        self.ATS = ats
        self.total = total
        self.moneyLineValue = money_line_value
        self.date = date

    def __repr__(self):
        return "<CuratedPicksNBA(firstTeamName='{}', firstTeamRot='{}', secondTeamName={}, " \
               "secondTeamRot={}, gameWinner={}, ATS={}, total={}, moneyLineValue={}, date={}, createdDate={})>" \
            .format(self.firstTeamName, self.firstTeamRot, self.secondTeamName, self.secondTeamRot,
                    self.gameWinner, self.ATS, self.total, self.moneyLineValue, self.date, self.createdDate)


class CuratedPicksWiseNBA(Base):
    __tablename__ = 'CuratedPicksWiseNBA'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstTeamName = Column(String, nullable=True)
    firstTeamPrediction = Column(String, nullable=True)
    firstTeamPickOutcome = Column(String, nullable=True)
    firstTeamPickMarket = Column(String, nullable=True)
    secondTeamName = Column(String, nullable=True)
    secondTeamPrediction = Column(String, nullable=True)
    secondTeamPickOutcome = Column(String, nullable=True)
    secondTeamPickMarket = Column(String, nullable=True)
    date = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, first_team_name='', first_team_prediction='', first_team_pick_outcome='',
                 first_team_pick_market='', second_team_name='', second_team_prediction='', second_team_pick_outcome='',
                 second_team_pick_market='', date=''):
        self.firstTeamName = first_team_name
        self.firstTeamPrediction = first_team_prediction
        self.firstTeamPickOutcome = first_team_pick_outcome
        self.firstTeamPickMarket = first_team_pick_market
        self.secondTeamName = second_team_name
        self.secondTeamPrediction = second_team_prediction
        self.secondTeamPickOutcome = second_team_pick_outcome
        self.secondTeamPickMarket = second_team_pick_market
        self.date = date

    def __repr__(self):
        return "<CuratedPicksWiseNBA(firstTeamName='{}', firstTeamPrediction='{}', firstTeamPickOutcome={}, " \
               "firstTeamPickMarket={}, secondTeamName={}, secondTeamPrediction={}, secondTeamPickOutcome={}, " \
               "secondTeamPickMarket={}, date={}, createdDate={})>" \
            .format(self.firstTeamName, self.firstTeamPrediction, self.firstTeamPickOutcome, self.firstTeamPickMarket,
                    self.secondTeamName, self.secondTeamPrediction, self.secondTeamPickOutcome,
                    self.secondTeamPickMarket, self.date, self.createdDate)


class CuratedPicksWiseNCAAB(Base):
    __tablename__ = 'CuratedPicksWiseNCAAB'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstTeamName = Column(String, nullable=True)
    firstTeamPrediction = Column(String, nullable=True)
    firstTeamPickOutcome = Column(String, nullable=True)
    firstTeamPickMarket = Column(String, nullable=True)
    secondTeamName = Column(String, nullable=True)
    secondTeamPrediction = Column(String, nullable=True)
    secondTeamPickOutcome = Column(String, nullable=True)
    secondTeamPickMarket = Column(String, nullable=True)
    date = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, first_team_name='', first_team_prediction='', first_team_pick_outcome='',
                 first_team_pick_market='', second_team_name='', second_team_prediction='', second_team_pick_outcome='',
                 second_team_pick_market='', date=''):
        self.firstTeamName = first_team_name
        self.firstTeamPrediction = first_team_prediction
        self.firstTeamPickOutcome = first_team_pick_outcome
        self.firstTeamPickMarket = first_team_pick_market
        self.secondTeamName = second_team_name
        self.secondTeamPrediction = second_team_prediction
        self.secondTeamPickOutcome = second_team_pick_outcome
        self.secondTeamPickMarket = second_team_pick_market
        self.date = date

    def __repr__(self):
        return "<CuratedPicksWiseNCAAB(firstTeamName='{}', firstTeamPrediction='{}', firstTeamPickOutcome={}, " \
               "firstTeamPickMarket={}, secondTeamName={}, secondTeamPrediction={}, secondTeamPickOutcome={}, " \
               "secondTeamPickMarket={}, date={}, createdDate={})>" \
            .format(self.firstTeamName, self.firstTeamPrediction, self.firstTeamPickOutcome, self.firstTeamPickMarket,
                    self.secondTeamName, self.secondTeamPrediction, self.secondTeamPickOutcome,
                    self.secondTeamPickMarket, self.date, self.createdDate)
