import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


class SportsInsightsBETSIGNALS(Base):
    __tablename__ = 'SportsInsightsBETSIGNALS'
    gsheet_table_columns = ['TriggerTime', 'GameTime', 'Signal', 'PlayOn', 'BetType', 'TriggerBook',
                            'TriggerUnits', 'Score', 'Result']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    TriggerTime = Column(String, nullable=True)
    GameTime = Column(String, nullable=True)
    Signal = Column(String, nullable=True)
    PlayOn = Column(String, nullable=True)
    BetType = Column(String, nullable=True)
    TriggerBook = Column(String, nullable=True)
    TriggerUnits = Column(String, nullable=True)
    Score = Column(String, nullable=True)
    Result = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, TriggerTime='', GameTime='', Signal='', PlayOn='', BetType='', TriggerBook='', TriggerUnits='',
                 Score='', Result=''):
        self.TriggerTime = TriggerTime
        self.GameTime = GameTime
        self.Signal = Signal
        self.PlayOn = PlayOn
        self.BetType = BetType
        self.TriggerBook = TriggerBook
        self.TriggerUnits = TriggerUnits
        self.Score = Score
        self.Result = Result

    def __repr__(self):
        return "<SportsInsightsBETSIGNALS(TriggerTime='{}', GameTime='{}', Signal={}, PlayOn={}, BetType={}, " \
               "TriggerBook={}, TriggerUnits={}, Score={}, Result={}, CreatedDate={})>" \
            .format(self.TriggerTime, self.GameTime, self.Signal, self.PlayOn, self.BetType,
                    self.TriggerBook, self.TriggerUnits, self.Score, self.Result, self.CreatedDate)


class SportsInsightsBESTBETS(Base):
    __tablename__ = 'SportsInsightsBESTBETS'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    TriggerTime = Column(String, nullable=True)
    GameTime = Column(String, nullable=True)
    PlayOn = Column(String, nullable=True)
    BetType = Column(String, nullable=True)
    Score = Column(String, nullable=True)
    Result = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, TriggerTime='', GameTime='', PlayOn='', BetType='',
                 Score='', Result=''):
        self.TriggerTime = TriggerTime
        self.GameTime = GameTime
        self.PlayOn = PlayOn
        self.BetType = BetType
        self.Score = Score
        self.Result = Result

    def __repr__(self):
        return "<SportsInsightsBESTBETS(TriggerTime='{}', GameTime='{}', PlayOn={}, BetType={}, " \
               "Score={}, Result={}, CreatedDate={})>" \
            .format(self.TriggerTime, self.GameTime, self.PlayOn, self.BetType,
                    self.Score, self.Result, self.CreatedDate)
