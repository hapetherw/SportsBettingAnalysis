import datetime
from sqlalchemy import Column, Integer, String, DateTime

from models.model import Base


class BetQLSpreadNCAAB(Base):
    __tablename__ = 'BetQLSpreadNCAAB'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_RoadOU='', A_RoadOU='', H_HomeOU='',
                 A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQLSpreadNCAAB(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={}, " \
               "A_BetRating={}, H_RoadOU={}, A_RoadOU={}, H_HomeOU={}, " \
               "A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQLMoneylineNCAAB(Base):
    __tablename__ = 'BetQLMoneylineNCAAB'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_RoadOU='', A_RoadOU='', H_HomeOU='',
                 A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQLMoneylineNCAAB(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={}, " \
               "A_BetRating={}, H_RoadOU={}, A_RoadOU={}, H_HomeOU={}, " \
               "A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQLTotalNCAAB(Base):
    __tablename__ = 'BetQLTotalNCAAB'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_RoadOU='', A_RoadOU='', H_HomeOU='',
                 A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQLTotalNCAAB(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={}, " \
               "A_BetRating={}, H_RoadOU={}, A_RoadOU={}, H_HomeOU={}, " \
               "A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQL1stHalfSpreadNCAAB(Base):
    __tablename__ = 'BetQL1stHalfSpreadNCAAB'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_RoadOU='', A_RoadOU='', H_HomeOU='',
                 A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQL1stHalfSpreadNCAAB(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, " \
               "H_BetRating={}, " \
               "A_BetRating={}, H_RoadOU={}, A_RoadOU={}, H_HomeOU={}, " \
               "A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQL1stHalfMoneylineNCAAB(Base):
    __tablename__ = 'BetQL1stHalfMoneylineNCAAB'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_RoadOU='', A_RoadOU='', H_HomeOU='',
                 A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQL1stHalfMoneylineNCAAB(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, " \
               "H_BetRating={}, " \
               "A_BetRating={}, H_RoadOU={}, A_RoadOU={}, H_HomeOU={}, " \
               "A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQL1stHalfTotalNCAAB(Base):
    __tablename__ = 'BetQL1stHalfTotalNCAAB'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_RoadOU='', A_RoadOU='', H_HomeOU='',
                 A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQL1stHalfTotalNCAAB(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={" \
               "}, " \
               "A_BetRating={}, H_RoadOU={}, A_RoadOU={}, H_HomeOU={}, " \
               "A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQL2ndHalfSpreadNCAAB(Base):
    __tablename__ = 'BetQL2ndHalfSpreadNCAAB'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_RoadOU='', A_RoadOU='', H_HomeOU='',
                 A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQL2ndHalfSpreadNCAAB(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, " \
               "H_BetRating={}, " \
               "A_BetRating={}, H_RoadOU={}, A_RoadOU={}, H_HomeOU={}, " \
               "A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQL2ndHalfMoneylineNCAAB(Base):
    __tablename__ = 'BetQL2ndHalfMoneylineNCAAB'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_RoadOU='', A_RoadOU='', H_HomeOU='',
                 A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQL2ndHalfMoneylineNCAAB(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, " \
               "H_BetRating={}, " \
               "A_BetRating={}, H_RoadOU={}, A_RoadOU={}, H_HomeOU={}, " \
               "A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


# NBA
class BetQLSpreadNBA(Base):
    __tablename__ = 'BetQLSpreadNBA'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_PointsAgainst = Column(String, nullable=True)
    A_PointsAgainst = Column(String, nullable=True)
    H_PointsFor = Column(String, nullable=True)
    A_PointsFor = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_PointsAgainst='', A_PointsAgainst='', H_PointsFor='', A_PointsFor='', H_RoadOU='',
                 A_RoadOU='', H_HomeOU='', A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_PointsAgainst = H_PointsAgainst
        self.A_PointsAgainst = A_PointsAgainst
        self.H_PointsFor = H_PointsFor
        self.A_PointsFor = A_PointsFor
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQLSpreadNBA(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={}, " \
               "A_BetRating={}, H_PointsAgainst={}, A_PointsAgainst={}, H_PointsFor={}, A_PointsFor={}, H_RoadOU={}, " \
               "A_RoadOU={}, H_HomeOU={}, A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_PointsAgainst, self.A_PointsAgainst, self.H_PointsFor, self.A_PointsFor,
                    self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQLMoneylineNBA(Base):
    __tablename__ = 'BetQLMoneylineNBA'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_PointsAgainst = Column(String, nullable=True)
    A_PointsAgainst = Column(String, nullable=True)
    H_PointsFor = Column(String, nullable=True)
    A_PointsFor = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_PointsAgainst='', A_PointsAgainst='', H_PointsFor='', A_PointsFor='', H_RoadOU='',
                 A_RoadOU='', H_HomeOU='', A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_PointsAgainst = H_PointsAgainst
        self.A_PointsAgainst = A_PointsAgainst
        self.H_PointsFor = H_PointsFor
        self.A_PointsFor = A_PointsFor
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQLMoneylineNBA(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={}, " \
               "A_BetRating={}, H_PointsAgainst={}, A_PointsAgainst={}, H_PointsFor={}, A_PointsFor={}, H_RoadOU={}, " \
               "A_RoadOU={}, H_HomeOU={}, A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_PointsAgainst, self.A_PointsAgainst, self.H_PointsFor, self.A_PointsFor,
                    self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQLTotalNBA(Base):
    __tablename__ = 'BetQLTotalNBA'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_PointsAgainst = Column(String, nullable=True)
    A_PointsAgainst = Column(String, nullable=True)
    H_PointsFor = Column(String, nullable=True)
    A_PointsFor = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_PointsAgainst='', A_PointsAgainst='', H_PointsFor='', A_PointsFor='', H_RoadOU='',
                 A_RoadOU='', H_HomeOU='', A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_PointsAgainst = H_PointsAgainst
        self.A_PointsAgainst = A_PointsAgainst
        self.H_PointsFor = H_PointsFor
        self.A_PointsFor = A_PointsFor
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQLTotalNBA(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={}, " \
               "A_BetRating={}, H_PointsAgainst={}, A_PointsAgainst={}, H_PointsFor={}, A_PointsFor={}, H_RoadOU={}, " \
               "A_RoadOU={}, H_HomeOU={}, A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_PointsAgainst, self.A_PointsAgainst, self.H_PointsFor, self.A_PointsFor,
                    self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQL1stHalfSpreadNBA(Base):
    __tablename__ = 'BetQL1stHalfSpreadNBA'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_PointsAgainst = Column(String, nullable=True)
    A_PointsAgainst = Column(String, nullable=True)
    H_PointsFor = Column(String, nullable=True)
    A_PointsFor = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_PointsAgainst='', A_PointsAgainst='', H_PointsFor='', A_PointsFor='', H_RoadOU='',
                 A_RoadOU='', H_HomeOU='', A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_PointsAgainst = H_PointsAgainst
        self.A_PointsAgainst = A_PointsAgainst
        self.H_PointsFor = H_PointsFor
        self.A_PointsFor = A_PointsFor
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQL1stHalfSpreadNBA(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={}, " \
               "A_BetRating={}, H_PointsAgainst={}, A_PointsAgainst={}, H_PointsFor={}, A_PointsFor={}, H_RoadOU={}, " \
               "A_RoadOU={}, H_HomeOU={}, A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_PointsAgainst, self.A_PointsAgainst, self.H_PointsFor, self.A_PointsFor,
                    self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQL1stHalfMoneylineNBA(Base):
    __tablename__ = 'BetQL1stHalfMoneylineNBA'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_PointsAgainst = Column(String, nullable=True)
    A_PointsAgainst = Column(String, nullable=True)
    H_PointsFor = Column(String, nullable=True)
    A_PointsFor = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_PointsAgainst='', A_PointsAgainst='', H_PointsFor='', A_PointsFor='', H_RoadOU='',
                 A_RoadOU='', H_HomeOU='', A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_PointsAgainst = H_PointsAgainst
        self.A_PointsAgainst = A_PointsAgainst
        self.H_PointsFor = H_PointsFor
        self.A_PointsFor = A_PointsFor
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQL1stHalfMoneylineNBA(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={}, " \
               "A_BetRating={}, H_PointsAgainst={}, A_PointsAgainst={}, H_PointsFor={}, A_PointsFor={}, H_RoadOU={}, " \
               "A_RoadOU={}, H_HomeOU={}, A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_PointsAgainst, self.A_PointsAgainst, self.H_PointsFor, self.A_PointsFor,
                    self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQL1stHalfTotalNBA(Base):
    __tablename__ = 'BetQL1stHalfTotalNBA'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_PointsAgainst = Column(String, nullable=True)
    A_PointsAgainst = Column(String, nullable=True)
    H_PointsFor = Column(String, nullable=True)
    A_PointsFor = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_PointsAgainst='', A_PointsAgainst='', H_PointsFor='', A_PointsFor='', H_RoadOU='',
                 A_RoadOU='', H_HomeOU='', A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_PointsAgainst = H_PointsAgainst
        self.A_PointsAgainst = A_PointsAgainst
        self.H_PointsFor = H_PointsFor
        self.A_PointsFor = A_PointsFor
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQL1stHalfTotalNBA(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={}, " \
               "A_BetRating={}, H_PointsAgainst={}, A_PointsAgainst={}, H_PointsFor={}, A_PointsFor={}, H_RoadOU={}, " \
               "A_RoadOU={}, H_HomeOU={}, A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_PointsAgainst, self.A_PointsAgainst, self.H_PointsFor, self.A_PointsFor,
                    self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQL2ndHalfSpreadNBA(Base):
    __tablename__ = 'BetQL2ndHalfSpreadNBA'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_PointsAgainst = Column(String, nullable=True)
    A_PointsAgainst = Column(String, nullable=True)
    H_PointsFor = Column(String, nullable=True)
    A_PointsFor = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_PointsAgainst='', A_PointsAgainst='', H_PointsFor='', A_PointsFor='', H_RoadOU='',
                 A_RoadOU='', H_HomeOU='', A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_PointsAgainst = H_PointsAgainst
        self.A_PointsAgainst = A_PointsAgainst
        self.H_PointsFor = H_PointsFor
        self.A_PointsFor = A_PointsFor
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQL2ndHalfSpreadNBA(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={}, " \
               "A_BetRating={}, H_PointsAgainst={}, A_PointsAgainst={}, H_PointsFor={}, A_PointsFor={}, H_RoadOU={}, " \
               "A_RoadOU={}, H_HomeOU={}, A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_PointsAgainst, self.A_PointsAgainst, self.H_PointsFor, self.A_PointsFor,
                    self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)


class BetQL2ndHalfMoneylineNBA(Base):
    __tablename__ = 'BetQL2ndHalfMoneylineNBA'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    HomeTeam = Column(String, nullable=True)
    AwayTeam = Column(String, nullable=True)
    H_CurrentSP = Column(String, nullable=True)
    A_CurrentSP = Column(String, nullable=True)
    H_BetRating = Column(String, nullable=True)
    A_BetRating = Column(String, nullable=True)
    H_PointsAgainst = Column(String, nullable=True)
    A_PointsAgainst = Column(String, nullable=True)
    H_PointsFor = Column(String, nullable=True)
    A_PointsFor = Column(String, nullable=True)
    H_RoadOU = Column(String, nullable=True)
    A_RoadOU = Column(String, nullable=True)
    H_HomeOU = Column(String, nullable=True)
    A_HomeOU = Column(String, nullable=True)
    H_Under = Column(String, nullable=True)
    A_Under = Column(String, nullable=True)
    H_Over = Column(String, nullable=True)
    A_Over = Column(String, nullable=True)
    H_UnderRecord = Column(String, nullable=True)
    A_UnderRecord = Column(String, nullable=True)
    H_OverRecord = Column(String, nullable=True)
    A_OverRecord = Column(String, nullable=True)
    H_NetUnits = Column(String, nullable=True)
    A_NetUnits = Column(String, nullable=True)
    H_Road = Column(String, nullable=True)
    A_Road = Column(String, nullable=True)
    H_Home = Column(String, nullable=True)
    A_Home = Column(String, nullable=True)
    H_SeasonWin = Column(String, nullable=True)
    A_SeasonWin = Column(String, nullable=True)
    H_Games = Column(String, nullable=True)
    A_Games = Column(String, nullable=True)
    H_ATSUnits = Column(String, nullable=True)
    A_ATSUnits = Column(String, nullable=True)
    H_RoadATS = Column(String, nullable=True)
    A_RoadATS = Column(String, nullable=True)
    H_HomeATS = Column(String, nullable=True)
    A_HomeATS = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSWin = Column(String, nullable=True)
    H_ATSRec = Column(String, nullable=True)
    A_ATSRec = Column(String, nullable=True)
    H_ProEdgeSP = Column(String, nullable=True)
    A_ProEdgeSP = Column(String, nullable=True)
    H_TicketsU = Column(String, nullable=True)
    A_TicketsU = Column(String, nullable=True)
    H_TicketsO = Column(String, nullable=True)
    A_TicketsO = Column(String, nullable=True)
    H_TicketsML = Column(String, nullable=True)
    A_TicketsML = Column(String, nullable=True)
    H_TicketsSP = Column(String, nullable=True)
    A_TicketsSP = Column(String, nullable=True)
    H_MoneySP = Column(String, nullable=True)
    A_MoneySP = Column(String, nullable=True)
    H_TicketSP = Column(String, nullable=True)
    A_TicketSP = Column(String, nullable=True)
    H_LineMoveOU = Column(String, nullable=True)
    A_LineMoveOU = Column(String, nullable=True)
    H_LineMoveML = Column(String, nullable=True)
    A_LineMoveML = Column(String, nullable=True)
    H_LineMoveSP = Column(String, nullable=True)
    A_LineMoveSP = Column(String, nullable=True)
    H_OpenOU = Column(String, nullable=True)
    A_OpenOU = Column(String, nullable=True)
    H_CurrentOU = Column(String, nullable=True)
    A_CurrentOU = Column(String, nullable=True)
    H_OpenML = Column(String, nullable=True)
    A_OpenML = Column(String, nullable=True)
    H_CurrentML = Column(String, nullable=True)
    A_CurrentML = Column(String, nullable=True)
    H_OpenSP = Column(String, nullable=True)
    A_OpenSP = Column(String, nullable=True)
    Date = Column(String, nullable=True)
    Time = Column(String, nullable=True)
    CreatedDate = Column(DateTime, default=datetime.datetime.now())
    HomeFirst = Column(Integer, default=0)

    def __init__(self, HomeTeam='', AwayTeam='', H_CurrentSP='', A_CurrentSP='', H_BetRating='',
                 A_BetRating='', H_PointsAgainst='', A_PointsAgainst='', H_PointsFor='', A_PointsFor='', H_RoadOU='',
                 A_RoadOU='', H_HomeOU='', A_HomeOU='', H_Under='', A_Under='',
                 H_Over='', A_Over='', H_UnderRecord='',
                 A_UnderRecord='', H_OverRecord='', A_OverRecord='', H_NetUnits='', A_NetUnits='', H_Road='',
                 A_Road='', H_Home='', A_Home='', H_SeasonWin='', A_SeasonWin='', H_Games='', A_Games='', H_ATSUnits='',
                 A_ATSUnits='', H_RoadATS='', A_RoadATS='', H_HomeATS='', A_HomeATS='', H_ATSWin='', A_ATSWin='',
                 H_ATSRec='', A_ATSRec='', H_ProEdgeSP='', A_ProEdgeSP='', H_TicketsU='', A_TicketsU='', H_TicketsO='',
                 A_TicketsO='', H_TicketsML='', A_TicketsML='', H_TicketsSP='', A_TicketsSP='', H_MoneySP='',
                 A_MoneySP='', H_TicketSP='', A_TicketSP='', H_LineMoveOU='', A_LineMoveOU='', H_LineMoveML='',
                 A_LineMoveML='', H_LineMoveSP='', A_LineMoveSP='', H_OpenOU='', A_OpenOU='', H_CurrentOU='',
                 A_CurrentOU='', H_OpenML='', A_OpenML='', H_CurrentML='', A_CurrentML='', H_OpenSP='', A_OpenSP='',
                 Date='', Time='', HomeFirst=0):
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.H_CurrentSP = H_CurrentSP
        self.A_CurrentSP = A_CurrentSP
        self.H_BetRating = H_BetRating
        self.A_BetRating = A_BetRating
        self.H_PointsAgainst = H_PointsAgainst
        self.A_PointsAgainst = A_PointsAgainst
        self.H_PointsFor = H_PointsFor
        self.A_PointsFor = A_PointsFor
        self.H_RoadOU = H_RoadOU
        self.A_RoadOU = A_RoadOU
        self.H_HomeOU = H_HomeOU
        self.A_HomeOU = A_HomeOU
        self.H_Under = H_Under
        self.A_Under = A_Under
        self.H_Over = H_Over
        self.A_Over = A_Over
        self.H_UnderRecord = H_UnderRecord
        self.A_UnderRecord = A_UnderRecord
        self.H_OverRecord = H_OverRecord
        self.A_OverRecord = A_OverRecord
        self.H_NetUnits = H_NetUnits
        self.A_NetUnits = A_NetUnits
        self.H_Road = H_Road
        self.A_Road = A_Road
        self.H_Home = H_Home
        self.A_Home = A_Home
        self.H_SeasonWin = H_SeasonWin
        self.A_SeasonWin = A_SeasonWin
        self.H_Games = H_Games
        self.A_Games = A_Games
        self.H_ATSUnits = H_ATSUnits
        self.A_ATSUnits = A_ATSUnits
        self.H_RoadATS = H_RoadATS
        self.A_RoadATS = A_RoadATS
        self.H_HomeATS = H_HomeATS
        self.A_HomeATS = A_HomeATS
        self.H_ATSWin = H_ATSWin
        self.A_ATSWin = A_ATSWin
        self.H_ATSRec = H_ATSRec
        self.A_ATSRec = A_ATSRec
        self.H_ProEdgeSP = H_ProEdgeSP
        self.A_ProEdgeSP = A_ProEdgeSP
        self.H_TicketsU = H_TicketsU
        self.A_TicketsU = A_TicketsU
        self.H_TicketsO = H_TicketsO
        self.A_TicketsO = A_TicketsO
        self.H_TicketsML = H_TicketsML
        self.A_TicketsML = A_TicketsML
        self.H_TicketsSP = H_TicketsSP
        self.A_TicketsSP = A_TicketsSP
        self.H_MoneySP = H_MoneySP
        self.A_MoneySP = A_MoneySP
        self.H_TicketSP = H_TicketSP
        self.A_TicketSP = A_TicketSP
        self.H_LineMoveOU = H_LineMoveOU
        self.A_LineMoveOU = A_LineMoveOU
        self.H_LineMoveML = H_LineMoveML
        self.A_LineMoveML = A_LineMoveML
        self.H_LineMoveSP = H_LineMoveSP
        self.A_LineMoveSP = A_LineMoveSP
        self.H_OpenOU = H_OpenOU
        self.A_OpenOU = A_OpenOU
        self.H_CurrentOU = H_CurrentOU
        self.A_CurrentOU = A_CurrentOU
        self.H_OpenML = H_OpenML
        self.A_OpenML = A_OpenML
        self.H_CurrentML = H_CurrentML
        self.A_CurrentML = A_CurrentML
        self.H_OpenSP = H_OpenSP
        self.A_OpenSP = A_OpenSP
        self.Date = Date
        self.Time = Time
        self.HomeFirst = HomeFirst

    def __repr__(self):
        return "<BetQL2ndHalfMoneylineNBA(HomeTeam='{}', AwayTeam='{}', H_CurrentSP='{}', A_CurrentSP={}, H_BetRating={}, " \
               "A_BetRating={}, H_PointsAgainst={}, A_PointsAgainst={}, H_PointsFor={}, A_PointsFor={}, H_RoadOU={}, " \
               "A_RoadOU={}, H_HomeOU={}, A_HomeOU={}, H_Under={}, A_Under={}, " \
               "H_Over={}, A_Over={}, H_UnderRecord={}, " \
               "A_UnderRecord={}, H_OverRecord={}, A_OverRecord={}, H_NetUnits={}, A_NetUnits={}, H_Road={}, " \
               "A_Road={}, H_Home={}, A_Home={}, H_SeasonWin={}, A_SeasonWin={}, H_Games={}, A_Games={}, " \
               "H_ATSUnits={}, A_ATSUnits={}, H_RoadATS={}, A_RoadATS={}, H_HomeATS={}, A_HomeATS={}, " \
               "H_ATSWin={}, A_ATSWin={}, H_ATSRec={}, A_ATSRec={}, H_ProEdgeSP={}, A_ProEdgeSP={}, " \
               "H_TicketsU={}, A_TicketsU={}, H_TicketsO={}, A_TicketsO={}, H_TicketsML={}, A_TicketsML={}, " \
               "H_TicketsSP={}, A_TicketsSP={}, H_MoneySP={}, A_MoneySP={}, H_TicketSP={}, A_TicketSP={}, " \
               "H_LineMoveOU={}, A_LineMoveOU={}, H_LineMoveML={}, A_LineMoveML={}, H_LineMoveSP={}, " \
               "A_LineMoveSP={}, H_OpenOU={}, A_OpenOU={}, H_CurrentOU={}, A_CurrentOU={}, H_OpenML={}, " \
               "A_OpenML={}, H_CurrentML={}, A_CurrentML={}, H_OpenSP={}, A_OpenSP={}, Date={}, Time={}, " \
               "CreatedDate={}, HomeFirst={})>" \
            .format(self.HomeTeam, self.AwayTeam, self.H_CurrentSP, self.A_CurrentSP, self.H_BetRating,
                    self.A_BetRating, self.H_PointsAgainst, self.A_PointsAgainst, self.H_PointsFor, self.A_PointsFor,
                    self.H_RoadOU, self.A_RoadOU, self.H_HomeOU, self.A_HomeOU, self.H_Under,
                    self.A_Under, self.H_Over, self.A_Over, self.H_UnderRecord, self.A_UnderRecord,
                    self.H_OverRecord, self.A_OverRecord, self.H_NetUnits, self.A_NetUnits, self.H_Road,
                    self.A_Road, self.H_Home, self.A_Home, self.H_SeasonWin, self.A_SeasonWin, self.H_Games,
                    self.A_Games, self.H_ATSUnits, self.A_ATSUnits, self.H_RoadATS, self.A_RoadATS, self.H_HomeATS,
                    self.A_HomeATS, self.H_ATSWin, self.H_ATSWin, self.H_ATSRec, self.A_ATSRec, self.H_ProEdgeSP,
                    self.A_ProEdgeSP, self.H_TicketsU, self.A_TicketsU, self.H_TicketsO, self.A_TicketsO,
                    self.H_TicketsML, self.A_TicketsML, self.H_TicketsSP, self.A_TicketsSP, self.H_MoneySP,
                    self.A_MoneySP, self.H_TicketSP, self.A_TicketSP, self.H_LineMoveOU, self.A_LineMoveOU,
                    self.H_LineMoveML, self.A_LineMoveML, self.H_LineMoveSP, self.A_LineMoveSP, self.H_OpenOU,
                    self.A_OpenOU, self.H_CurrentOU, self.A_CurrentOU, self.H_OpenML, self.A_OpenML, self.H_CurrentML,
                    self.A_CurrentML, self.H_OpenSP, self.A_OpenSP, self.Date, self.Time, self.CreatedDate,
                    self.HomeFirst)