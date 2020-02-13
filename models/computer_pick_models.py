import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


# ------------------- NCAAB ----------------------------#

class ComputerPickDetailsNCAAB(Base):
    __tablename__ = 'ComputerPickDetailsNCAAB'
    table_columns = ['FirstTeamNameShort', 'FirstTeamNameLong', 'SecondTeamNameShort', 'SecondTeamNameLong', 'DateTime',
                     'PredictedScoreATS', 'PredictedScoreTotal', 'ComputerPickATS', 'ComputerPickTotal',
                     'PublicConsensusATS', 'PublicConsensusTotal', 'ConsensusBetATS', 'ConsensusBetTotal']
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstTeamNameShort = Column(String, nullable=True)
    firstTeamNameLong = Column(String, nullable=True)
    secondTeamNameShort = Column(String, nullable=True)
    secondTeamNameLong = Column(String, nullable=True)
    dateTime = Column(String, nullable=True)
    PredictedScoreATS = Column(String, nullable=True)
    PredictedScoreTotal = Column(String, nullable=True)
    ComputerPickATS = Column(String, nullable=True)
    ComputerPickTotal = Column(String, nullable=True)
    PublicConsensusATS = Column(String, nullable=True)
    PublicConsensusTotal = Column(String, nullable=True)
    ConsensusBetATS = Column(String, nullable=True)
    ConsensusBetTotal = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, first_team_name_short, first_team_name_long, second_team_name_short, second_team_name_long,
                 dateTime, PredictedScoreATS, PredictedScoreTotal, ComputerPickATS, ComputerPickTotal,
                 PublicConsensusATS, PublicConsensusTotal, ConsensusBetATS, ConsensusBetTotal):
        self.firstTeamNameShort = first_team_name_short
        self.firstTeamNameLong = first_team_name_long
        self.secondTeamNameShort = second_team_name_short
        self.secondTeamNameLong = second_team_name_long
        self.dateTime = dateTime
        self.PredictedScoreATS = PredictedScoreATS
        self.PredictedScoreTotal = PredictedScoreTotal
        self.ComputerPickATS = ComputerPickATS
        self.ComputerPickTotal = ComputerPickTotal
        self.PublicConsensusATS = PublicConsensusATS
        self.PublicConsensusTotal = PublicConsensusTotal
        self.ConsensusBetATS = ConsensusBetATS
        self.ConsensusBetTotal = ConsensusBetTotal

    def __repr__(self):
        return "<ComputerPickDetailsNCAAB(firstTeamNameShort='{}', firstTeamNameLong={}, secondTeamNameShort={}, " \
               "secondTeamNameLong={}, dateTime={}, PredictedScoreATS='{}', PredictedScoreTotal={}, " \
               "ComputerPickATS={}, ComputerPickTotal={}, PublicConsensusATS={}, PublicConsensusTotal={}, " \
               "ConsensusBetATS={}, ConsensusBetTotal={}, createdDate={})>" \
            .format(self.firstTeamNameShort, self.firstTeamNameLong, self.secondTeamNameShort, self.secondTeamNameLong,
                    self.dateTime, self.PredictedScoreATS, self.PredictedScoreTotal, self.ComputerPickATS,
                    self.ComputerPickTotal, self.PublicConsensusATS, self.PublicConsensusTotal, self.ConsensusBetATS,
                    self.ConsensusBetTotal, self.createdDate)


# ------------------- NBA ----------------------------#

class ComputerPickDetailsNBA(Base):
    __tablename__ = 'ComputerPickDetailsNBA'
    table_columns = ['FirstTeamNameShort', 'FirstTeamNameLong', 'SecondTeamNameShort', 'SecondTeamNameLong', 'DateTime',
                     'PredictedScoreATS', 'PredictedScoreTotal', 'ComputerPickATS', 'ComputerPickTotal',
                     'PublicConsensusATS', 'PublicConsensusTotal', 'ConsensusBetATS', 'ConsensusBetTotal']
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstTeamNameShort = Column(String, nullable=True)
    firstTeamNameLong = Column(String, nullable=True)
    secondTeamNameShort = Column(String, nullable=True)
    secondTeamNameLong = Column(String, nullable=True)
    dateTime = Column(String, nullable=True)
    PredictedScoreATS = Column(String, nullable=True)
    PredictedScoreTotal = Column(String, nullable=True)
    ComputerPickATS = Column(String, nullable=True)
    ComputerPickTotal = Column(String, nullable=True)
    PublicConsensusATS = Column(String, nullable=True)
    PublicConsensusTotal = Column(String, nullable=True)
    ConsensusBetATS = Column(String, nullable=True)
    ConsensusBetTotal = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, first_team_name_short, first_team_name_long, second_team_name_short, second_team_name_long,
                 dateTime, PredictedScoreATS, PredictedScoreTotal, ComputerPickATS, ComputerPickTotal,
                 PublicConsensusATS, PublicConsensusTotal, ConsensusBetATS, ConsensusBetTotal):
        self.firstTeamNameShort = first_team_name_short
        self.firstTeamNameLong = first_team_name_long
        self.secondTeamNameShort = second_team_name_short
        self.secondTeamNameLong = second_team_name_long
        self.dateTime = dateTime
        self.PredictedScoreATS = PredictedScoreATS
        self.PredictedScoreTotal = PredictedScoreTotal
        self.ComputerPickATS = ComputerPickATS
        self.ComputerPickTotal = ComputerPickTotal
        self.PublicConsensusATS = PublicConsensusATS
        self.PublicConsensusTotal = PublicConsensusTotal
        self.ConsensusBetATS = ConsensusBetATS
        self.ConsensusBetTotal = ConsensusBetTotal

    def __repr__(self):
        return "<ComputerPickDetailsNBA(firstTeamNameShort='{}', firstTeamNameLong={}, secondTeamNameShort={}, " \
               "secondTeamNameLong={}, dateTime={}, PredictedScoreATS='{}', PredictedScoreTotal={}, " \
               "ComputerPickATS={}, ComputerPickTotal={}, PublicConsensusATS={}, PublicConsensusTotal={}, " \
               "ConsensusBetATS={}, ConsensusBetTotal={}, createdDate={})>" \
            .format(self.firstTeamNameShort, self.firstTeamNameLong, self.secondTeamNameShort, self.secondTeamNameLong,
                    self.dateTime, self.PredictedScoreATS, self.PredictedScoreTotal, self.ComputerPickATS,
                    self.ComputerPickTotal, self.PublicConsensusATS, self.PublicConsensusTotal, self.ConsensusBetATS,
                    self.ConsensusBetTotal, self.createdDate)
