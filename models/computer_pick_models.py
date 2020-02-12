import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


# ------------------- NCAAB ----------------------------#

class ComputerPickDetailsNCAAB(Base):
    __tablename__ = 'ComputerPickDetailsNCAAB'
    table_columns = ['FirstTeamNameShort', 'FirstTeamNameLong', 'SecondTeamNameShort', 'SecondTeamNameLong', 'Date',
                     'Time', 'Attribute', 'ATS', 'Total']
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstTeamNameShort = Column(String, nullable=True)
    firstTeamNameLong = Column(String, nullable=True)
    secondTeamNameShort = Column(String, nullable=True)
    secondTeamNameLong = Column(String, nullable=True)
    date = Column(String, nullable=True)
    time = Column(String, nullable=True)
    attribute = Column(String, nullable=True)
    ATS = Column(String, nullable=True)
    total = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, first_team_name_short, first_team_name_long, second_team_name_short, second_team_name_long,
                 date, time, attribute, ats, total):
        self.firstTeamNameShort = first_team_name_short
        self.firstTeamNameLong = first_team_name_long
        self.secondTeamNameShort = second_team_name_short
        self.secondTeamNameLong = second_team_name_long
        self.date = date
        self.time = time
        self.attribute = attribute
        self.ATS = ats
        self.total = total

    def __repr__(self):
        return "<ComputerPickDetailsNCAAB(firstTeamNameShort='{}', firstTeamNameLong={}, secondTeamNameShort={}, " \
               "secondTeamNameLong={}, date={}, time={}, attribute='{}', ATS={}, " \
               "total={}, createdDate={})>" \
            .format(self.firstTeamNameShort, self.firstTeamNameLong, self.secondTeamNameShort, self.secondTeamNameLong,
                    self.date, self.time, self.attribute, self.ATS, self.total, self.createdDate)


# ------------------- NBA ----------------------------#

class ComputerPickDetailsNBA(Base):
    __tablename__ = 'ComputerPickDetailsNBA'
    table_columns = ['FirstTeamNameShort', 'FirstTeamNameLong', 'SecondTeamNameShort', 'SecondTeamNameLong', 'Date',
                     'Time', 'Attribute', 'ATS', 'Total']
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstTeamNameShort = Column(String, nullable=True)
    firstTeamNameLong = Column(String, nullable=True)
    secondTeamNameShort = Column(String, nullable=True)
    secondTeamNameLong = Column(String, nullable=True)
    date = Column(String, nullable=True)
    time = Column(String, nullable=True)
    attribute = Column(String, nullable=True)
    ATS = Column(String, nullable=True)
    total = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, first_team_name_short, first_team_name_long, second_team_name_short, second_team_name_long,
                 date, time, attribute, ats, total):
        self.firstTeamNameShort = first_team_name_short
        self.firstTeamNameLong = first_team_name_long
        self.secondTeamNameShort = second_team_name_short
        self.secondTeamNameLong = second_team_name_long
        self.date = date
        self.time = time
        self.attribute = attribute
        self.ATS = ats
        self.total = total

    def __repr__(self):
        return "<ComputerPickDetailsNBA(firstTeamNameShort='{}', firstTeamNameLong={}, secondTeamNameShort={}, " \
               "secondTeamNameLong={}, date={}, time={}, attribute='{}', ATS={}, " \
               "total={}, createdDate={})>" \
            .format(self.firstTeamNameShort, self.firstTeamNameLong, self.secondTeamNameShort, self.secondTeamNameLong,
                    self.date, self.time, self.attribute, self.ATS, self.total, self.createdDate)
