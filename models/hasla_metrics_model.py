import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


class HaslaMetrics(Base):
    __tablename__ = 'HaslaMetrics'
    gsheet_table_columns = ['Team1ShortName', 'Team1FullName', 'Team2ShortName', 'Team2FullName', 'Date',
                            'Team1Rank', 'Team2Rank', 'Team1Score', 'Team2Score']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Team1ID = Column(Integer, nullable=True)
    Team2ID = Column(Integer, nullable=True)
    Team1Name = Column(String, nullable=True)
    Team2Name = Column(String, nullable=True)
    Team1Rank = Column(Integer, nullable=True)
    Team2Rank = Column(Integer, nullable=True)
    Team1Score = Column(String, nullable=True)
    Team2Score = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, team1_id=-1, team2_id=-1, team1_name='', team2_name='', team1_rank=0, team2_rank=0, team1_score='', team2_score='', date=''):
        self.Team1ID = team1_id
        self.Team2ID = team2_id
        self.Team1Name = team1_name
        self.Team2Name = team2_name
        self.Team1Rank = team1_rank
        self.Team2Rank = team2_rank
        self.Team1Score = team1_score
        self.Team2Score = team2_score
        self.Date = date

    def __repr__(self):
        return "<HaslaMetrics(Team1ID='{}', Team2ID='{}', Team1Rank={}, " \
               "Team2Rank={}, Team1Score={}, Team2Score={}, Date={}, CreatedDate={})>" \
            .format(self.Team1ID, self.Team2ID, self.Team1Rank, self.Team2Rank,
                    self.Team1Score, self.Team2Score, self.Date, self.CreatedDate)
