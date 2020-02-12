import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


class ESPNNCAAB(Base):
    __tablename__ = 'ESPNNCAAB'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    TeamName = Column(String, nullable=True)
    TeamNameTemple = Column(String, nullable=True)
    RANKING = Column(String, nullable=True)
    CONF = Column(String, nullable=True)
    W_L = Column(String, nullable=True)
    BPI_OFF = Column(String, nullable=True)
    BPI_DEF = Column(String, nullable=True)
    WEEK_RANK_CHG = Column(String, nullable=True)
    DATE = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, team_name='', team_name_temple='', ranking='', conf='', wl='', bpi_off='',
                 bpi_def='', week_rank_chg='', date=''):
        self.TeamName = team_name
        self.TeamNameTemple = team_name_temple
        self.RANKING = ranking
        self.CONF = conf
        self.W_L = wl
        self.BPI_OFF = bpi_off
        self.BPI_DEF = bpi_def
        self.WEEK_RANK_CHG = week_rank_chg
        self.DATE = date

    def __repr__(self):
        return "<ESPNNCAAB(TeamName='{}', TeamNameTemple='{}', RANKING='{}', CONF={}, " \
               "W_L={}, BPI_OFF={}, BPI_DEF={}, WEEK_RANK_CHG={}, DATE={}, createdDate={})>" \
            .format(self.TeamName, self.TeamNameTemple, self.RANKING, self.CONF, self.W_L,
                    self.BPI_OFF, self.BPI_DEF, self.WEEK_RANK_CHG, self.DATE, self.createdDate)
