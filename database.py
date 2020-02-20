from sqlalchemy.orm import sessionmaker

import sqlalchemy as db
from models.model import Base
from models.computer_pick_models import ComputerPickDetailsNCAAB
from models.computer_pick_models import ComputerPickDetailsNBA
from models.hasla_metrics_model import TeamScoreHASLAMETRICS
from models.curated_picks_model import CuratedPicksNCAAB
from models.curated_picks_model import CuratedPicksNBA
from models.curated_picks_model import CuratedPicksWiseNCAAB
from models.curated_picks_model import CuratedPicksWiseNBA
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


def recreate_oddshark_table():
    Base.metadata.drop_all(engine, tables=[ComputerPickDetailsNBA.__table__, ComputerPickDetailsNCAAB.__table__])
    Base.metadata.create_all(engine, tables=[ComputerPickDetailsNBA.__table__, ComputerPickDetailsNCAAB.__table__])
    print("Created OddShark Tables")


def recreate_hasla_metrics_table():
    Base.metadata.drop_all(engine, tables=[TeamScoreHASLAMETRICS.__table__])
    Base.metadata.create_all(engine, tables=[TeamScoreHASLAMETRICS.__table__])
    print("Created hasla_metrics Tables")


def recreate_curated_picks_table():
    Base.metadata.drop_all(engine, tables=[CuratedPicksNCAAB.__table__, CuratedPicksNBA.__table__,
                                           CuratedPicksWiseNCAAB.__table__, CuratedPicksWiseNBA.__table__])
    Base.metadata.create_all(engine, tables=[CuratedPicksNCAAB.__table__, CuratedPicksNBA.__table__,
                                             CuratedPicksWiseNCAAB.__table__, CuratedPicksWiseNBA.__table__])
    print("Created CuratedPicks Tables")


def recreate_espn_table():
    Base.metadata.drop_all(engine, tables=[ESPNNCAAB.__table__])
    Base.metadata.create_all(engine, tables=[ESPNNCAAB.__table__])
    print("Created ESPN Tables")


def recreate_vegas_insider_table():
    Base.metadata.drop_all(engine, tables=[VegasInsider.__table__])
    Base.metadata.create_all(engine, tables=[VegasInsider.__table__])
    print("Created VegasInsider Tables")


def recreate_betql_table():
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


def recreate_sportsinsights_table():
    Base.metadata.drop_all(engine, tables=[SportsInsightsBETSIGNALS.__table__, SportsInsightsBESTBETS.__table__])
    Base.metadata.create_all(engine, tables=[SportsInsightsBETSIGNALS.__table__, SportsInsightsBESTBETS.__table__])
    print("Created SportsInsights Tables")


def close_connection():
    if connection:
        connection.close()
    if session:
        session.close()
