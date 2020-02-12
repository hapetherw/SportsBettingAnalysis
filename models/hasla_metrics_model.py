import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


class TeamScoreHASLAMETRICS(Base):
    __tablename__ = 'TeamScoreHASLAMETRICS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstTeamName = Column(String, nullable=True)
    firstTeamScore = Column(String, nullable=True)
    firstTeamNumber = Column(String, nullable=True)
    secondTeamName = Column(String, nullable=True)
    secondTeamScore = Column(String, nullable=True)
    secondTeamNumber = Column(String, nullable=True)
    date = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, first_team_name='', first_team_score='', first_team_number='', second_team_name='', second_team_score='', second_team_number='', date=''):
        self.firstTeamName = first_team_name
        self.firstTeamScore = first_team_score
        self.firstTeamNumber = first_team_number
        self.secondTeamName = second_team_name
        self.secondTeamScore = second_team_score
        self.secondTeamNumber = second_team_number
        self.date = date

    def __repr__(self):
        return "<TeamScoreHASLAMETRICS(firstTeamName='{}', firstTeamScore='{}', firstTeamNumber={}, " \
               "secondTeamName={}, secondTeamScore={}, secondTeamNumber={}, date={}, createdDate={})>" \
            .format(self.firstTeamName, self.firstTeamScore, self.firstTeamNumber, self.secondTeamName,
                    self.secondTeamScore, self.secondTeamNumber, self.date, self.createdDate)
