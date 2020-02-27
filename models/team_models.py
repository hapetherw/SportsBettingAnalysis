import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


# ------------------- NCAA ----------------------------#

class NCAATeam(Base):
    __tablename__ = 'NCAATeam'
    table_columns = ['ShortTeamName', 'FullTeamName', 'AbbreviationTeamName']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ShortTeamName = Column(String, nullable=True)
    FullTeamName = Column(String, nullable=True)
    AbbreviationTeamName = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, short_team_name='', full_team_name='', abbreviation_team_name=''):
        self.ShortTeamName = short_team_name
        self.FullTeamName = full_team_name
        self.AbbreviationTeamName = abbreviation_team_name

    def __repr__(self):
        return "<NCAATeam(ShortTeamName='{}', FullTeamName={}, AbbreviationTeamName={}, CreatedDate={})>" \
            .format(self.ShortTeamName, self.FullTeamName, self.AbbreviationTeamName, self.CreatedDate)


# ------------------- NBA ----------------------------#

class NBATeam(Base):
    __tablename__ = 'NBATeam'
    table_columns = ['ShortTeamName', 'FullTeamName', 'AbbreviationTeamName']
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ShortTeamName = Column(String, nullable=True)
    FullTeamName = Column(String, nullable=True)
    AbbreviationTeamName = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, short_team_name='', full_team_name='', abbreviation_team_name=''):
        self.ShortTeamName = short_team_name
        self.FullTeamName = full_team_name
        self.AbbreviationTeamName = abbreviation_team_name

    def __repr__(self):
        return "<NBATeam(ShortTeamName='{}', FullTeamName={}, AbbreviationTeamName={}, CreatedDate={})>" \
            .format(self.ShortTeamName, self.FullTeamName, self.AbbreviationTeamName, self.CreatedDate)
