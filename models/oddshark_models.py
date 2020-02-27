import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


# ------------------- NCAA ----------------------------#

class OddSharkNCAA(Base):
    __tablename__ = 'OddSharkNCAA'
    table_columns = ['Team1ShortName', 'Team1FullName', 'Team2ShortName', 'Team2FullName', 'Date', 'Time',
                     'PredictedScoreATS', 'PredictedScoreTotal', 'ComputerPickATS', 'ComputerPickTotal',
                     'PublicConsensusATS', 'PublicConsensusTotal', 'ConsensusBetATS', 'ConsensusBetTotal']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Team1ID = Column(Integer, nullable=True)
    Team2ID = Column(Integer, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    PredictedScoreATS = Column(String, nullable=True)
    PredictedScoreTotal = Column(String, nullable=True)
    ComputerPickATS = Column(String, nullable=True)
    ComputerPickTotal = Column(String, nullable=True)
    PublicConsensusATS = Column(String, nullable=True)
    PublicConsensusTotal = Column(String, nullable=True)
    ConsensusBetATS = Column(String, nullable=True)
    ConsensusBetTotal = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, Team1ID, Team2ID, Date, Time, PredictedScoreATS, PredictedScoreTotal, ComputerPickATS,
                 ComputerPickTotal, PublicConsensusATS, PublicConsensusTotal, ConsensusBetATS, ConsensusBetTotal):
        self.Team1ID = Team1ID
        self.Team2ID = Team2ID
        self.Date = Date
        self.Time = Time
        self.PredictedScoreATS = PredictedScoreATS
        self.PredictedScoreTotal = PredictedScoreTotal
        self.ComputerPickATS = ComputerPickATS
        self.ComputerPickTotal = ComputerPickTotal
        self.PublicConsensusATS = PublicConsensusATS
        self.PublicConsensusTotal = PublicConsensusTotal
        self.ConsensusBetATS = ConsensusBetATS
        self.ConsensusBetTotal = ConsensusBetTotal

    def __repr__(self):
        return "<OddSharkNCAA(Team1ID='{}', Team2ID={}, Date={}, Time={}, PredictedScoreATS='{}', " \
               "PredictedScoreTotal={}, " \
               "ComputerPickATS={}, ComputerPickTotal={}, PublicConsensusATS={}, PublicConsensusTotal={}, " \
               "ConsensusBetATS={}, ConsensusBetTotal={}, CreatedDate={})>" \
            .format(self.Team1ID, self.Team2ID, self.Date, self.Time, self.PredictedScoreATS, self.PredictedScoreTotal,
                    self.ComputerPickATS, self.ComputerPickTotal, self.PublicConsensusATS, self.PublicConsensusTotal,
                    self.ConsensusBetATS, self.ConsensusBetTotal, self.CreatedDate)


# ------------------- NBA ----------------------------#

class OddSharkNBA(Base):
    __tablename__ = 'OddSharkNBA'
    table_columns = ['Team1ShortName', 'Team1FullName', 'Team2ShortName', 'Team2FullName', 'Date', 'Time',
                     'PredictedScoreATS', 'PredictedScoreTotal', 'ComputerPickATS', 'ComputerPickTotal',
                     'PublicConsensusATS', 'PublicConsensusTotal', 'ConsensusBetATS', 'ConsensusBetTotal']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Team1ID = Column(Integer, nullable=True)
    Team2ID = Column(Integer, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    PredictedScoreATS = Column(String, nullable=True)
    PredictedScoreTotal = Column(String, nullable=True)
    ComputerPickATS = Column(String, nullable=True)
    ComputerPickTotal = Column(String, nullable=True)
    PublicConsensusATS = Column(String, nullable=True)
    PublicConsensusTotal = Column(String, nullable=True)
    ConsensusBetATS = Column(String, nullable=True)
    ConsensusBetTotal = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, Team1ID, Team2ID, Date, Time, PredictedScoreATS, PredictedScoreTotal, ComputerPickATS,
                 ComputerPickTotal, PublicConsensusATS, PublicConsensusTotal, ConsensusBetATS, ConsensusBetTotal):
        self.Team1ID = Team1ID
        self.Team2ID = Team2ID
        self.Date = Date
        self.Time = Time
        self.PredictedScoreATS = PredictedScoreATS
        self.PredictedScoreTotal = PredictedScoreTotal
        self.ComputerPickATS = ComputerPickATS
        self.ComputerPickTotal = ComputerPickTotal
        self.PublicConsensusATS = PublicConsensusATS
        self.PublicConsensusTotal = PublicConsensusTotal
        self.ConsensusBetATS = ConsensusBetATS
        self.ConsensusBetTotal = ConsensusBetTotal

    def __repr__(self):
        return "<OddSharkNBA(Team1ID='{}', Team2ID={}, Date={}, Time={}, PredictedScoreATS='{}', " \
               "PredictedScoreTotal={}, " \
               "ComputerPickATS={}, ComputerPickTotal={}, PublicConsensusATS={}, PublicConsensusTotal={}, " \
               "ConsensusBetATS={}, ConsensusBetTotal={}, CreatedDate={})>" \
            .format(self.Team1ID, self.Team2ID, self.Date, self.Time, self.PredictedScoreATS, self.PredictedScoreTotal,
                    self.ComputerPickATS, self.ComputerPickTotal, self.PublicConsensusATS, self.PublicConsensusTotal,
                    self.ConsensusBetATS, self.ConsensusBetTotal, self.CreatedDate)
