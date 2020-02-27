from sqlalchemy.orm import sessionmaker

import sqlalchemy as db
from models.model import Base
from models.team_models import NCAATeam
from models.team_models import NBATeam
from models.oddshark_models import OddSharkNCAA
from models.oddshark_models import OddSharkNBA
from models.hasla_metrics_model import HaslaMetrics
from models.curated_picks_model import TeamRankingNCAA
from models.curated_picks_model import TeamRankingNBA
from models.curated_picks_model import PicksWiseNCAA
from models.curated_picks_model import PicksWiseNBA
from models.vegas_insider_model import VegasInsider
from models.espn_model import ESPNNCAAB
from models.betql_model import BetQLSpreadNCAAB
from models.betql_model import BetQLMoneylineNCAAB
from models.betql_model import BetQLTotalNCAAB
from models.betql_model import BetQL1stHalfSpreadNCAAB
from models.betql_model import BetQL1stHalfMoneylineNCAAB
from models.betql_model import BetQL1stHalfTotalNCAAB
from models.betql_model import BetQL2ndHalfSpreadNCAAB
from models.betql_model import BetQL2ndHalfMoneylineNCAAB
from models.betql_model import BetQLSpreadNBA
from models.betql_model import BetQLMoneylineNBA
from models.betql_model import BetQLTotalNBA
from models.betql_model import BetQL1stHalfSpreadNBA
from models.betql_model import BetQL1stHalfMoneylineNBA
from models.betql_model import BetQL1stHalfTotalNBA
from models.betql_model import BetQL2ndHalfSpreadNBA
from models.betql_model import BetQL2ndHalfMoneylineNBA
from models.sportsinsights_model import SportsInsightsBETSIGNALS
from models.sportsinsights_model import SportsInsightsBESTBETS
from config import DATABASE_URI

engine = db.create_engine(DATABASE_URI)
connection = engine.connect()
if connection:
    print("Database opened successfully")
else:
    print("failed")
Session = sessionmaker(bind=engine)
session = Session()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Created All Tables")


def recreate_team_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[NCAATeam.__table__, NBATeam.__table__])
    Base.metadata.create_all(engine, tables=[NCAATeam.__table__, NBATeam.__table__])
    print("Created Team Tables")


def recreate_oddshark_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[OddSharkNBA.__table__, OddSharkNCAA.__table__])
    Base.metadata.create_all(engine, tables=[OddSharkNBA.__table__, OddSharkNCAA.__table__])
    print("Created OddShark Tables")


def recreate_hasla_metrics_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[HaslaMetrics.__table__])
    Base.metadata.create_all(engine, tables=[HaslaMetrics.__table__])
    print("Created hasla_metrics Tables")


def recreate_curated_picks_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[TeamRankingNCAA.__table__, TeamRankingNBA.__table__,
                                               PicksWiseNCAA.__table__, PicksWiseNBA.__table__])
    Base.metadata.create_all(engine, tables=[TeamRankingNCAA.__table__, TeamRankingNBA.__table__,
                                             PicksWiseNCAA.__table__, PicksWiseNBA.__table__])
    print("Created CuratedPicks Tables")


def recreate_espn_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[ESPNNCAAB.__table__])
    Base.metadata.create_all(engine, tables=[ESPNNCAAB.__table__])
    print("Created ESPN Tables")


def recreate_vegas_insider_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[VegasInsider.__table__])
    Base.metadata.create_all(engine, tables=[VegasInsider.__table__])
    print("Created VegasInsider Tables")


def recreate_betql_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[BetQLSpreadNCAAB.__table__, BetQLMoneylineNCAAB.__table__,
                                               BetQLTotalNCAAB.__table__, BetQL1stHalfSpreadNCAAB.__table__,
                                               BetQL1stHalfMoneylineNCAAB.__table__, BetQL1stHalfTotalNCAAB.__table__,
                                               BetQL2ndHalfSpreadNCAAB.__table__, BetQL2ndHalfMoneylineNCAAB.__table__,
                                               BetQLSpreadNBA.__table__, BetQLMoneylineNBA.__table__,
                                               BetQLTotalNBA.__table__, BetQL1stHalfSpreadNBA.__table__,
                                               BetQL1stHalfMoneylineNBA.__table__, BetQL1stHalfTotalNBA.__table__,
                                               BetQL2ndHalfSpreadNBA.__table__, BetQL2ndHalfMoneylineNBA.__table__])
    Base.metadata.create_all(engine, tables=[BetQLSpreadNCAAB.__table__, BetQLMoneylineNCAAB.__table__,
                                             BetQLTotalNCAAB.__table__, BetQL1stHalfSpreadNCAAB.__table__,
                                             BetQL1stHalfMoneylineNCAAB.__table__, BetQL1stHalfTotalNCAAB.__table__,
                                             BetQL2ndHalfSpreadNCAAB.__table__, BetQL2ndHalfMoneylineNCAAB.__table__,
                                             BetQLSpreadNBA.__table__, BetQLMoneylineNBA.__table__,
                                             BetQLTotalNBA.__table__, BetQL1stHalfSpreadNBA.__table__,
                                             BetQL1stHalfMoneylineNBA.__table__, BetQL1stHalfTotalNBA.__table__,
                                             BetQL2ndHalfSpreadNBA.__table__, BetQL2ndHalfMoneylineNBA.__table__])
    print("Created BetQL Tables")


def recreate_sportsinsights_table(is_reset=0):
    if is_reset:
        Base.metadata.drop_all(engine, tables=[SportsInsightsBETSIGNALS.__table__, SportsInsightsBESTBETS.__table__])
    Base.metadata.create_all(engine, tables=[SportsInsightsBETSIGNALS.__table__, SportsInsightsBESTBETS.__table__])
    print("Created SportsInsights Tables")


def close_connection():
    if connection:
        connection.close()
    if session:
        session.close()
