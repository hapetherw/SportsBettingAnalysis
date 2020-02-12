import datetime
from sqlalchemy import Column, Integer, String, DateTime
from models.model import Base


class TeamsList(Base):
    __tablename__ = 'TeamsList'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullTeamName = Column(String, nullable=True)
    shortTeamName = Column(String, nullable=True)
    uniqueTeam_ID = Column(Integer, default=0)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, fullTeamName, shortTeamName):
        self.fullTeamName = fullTeamName
        self.shortTeamName = shortTeamName

    def __repr__(self):
        return "<TeamsList(fullTeamName='{}', shortTeamName='{}', uniqueTeam_ID={}, createdDate={})>" \
            .format(self.fullTeamName, self.shortTeamName, self.uniqueTeam_ID, self.createdDate)


class BooksHeader(Base):
    __tablename__ = 'BooksHeader'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bookName = Column(String, nullable=True)
    vegasType = Column(Integer, default=0)  # 0: opening, 1: las vegas, 2: online sports book
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, bookName, vegasType):
        self.bookName = bookName
        self.vegasType = vegasType

    def __repr__(self):
        return "<BooksHeader(bookName='{}', vegasType={}, createdDate={})>" \
            .format(self.bookName, self.vegasType, self.createdDate)


class OddsList(Base):
    __tablename__ = 'OddsList'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstTeam_ID = Column(Integer, default=0)
    secondTeam_ID = Column(Integer, default=0)
    firstTeamRotationNumber = Column(Integer, default=0)
    secondTeamRotationNumber = Column(Integer, default=0)
    fullDate = Column(String, nullable=True)
    shortDate = Column(String, nullable=True)
    dateGroupName = Column(String, nullable=True)
    time = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, firstTeam_ID, secondTeam_ID, firstTeamRotationNumber, secondTeamRotationNumber, fullDate='',
                 shortDate='', dateGroupName='', time=''):
        self.firstTeam_ID = firstTeam_ID
        self.secondTeam_ID = secondTeam_ID
        self.firstTeamRotationNumber = firstTeamRotationNumber
        self.secondTeamRotationNumber = secondTeamRotationNumber
        self.fullDate = fullDate
        self.shortDate = shortDate
        self.dateGroupName = dateGroupName
        self.time = time

    def __repr__(self):
        return "<OddsList(firstTeam_ID={}, secondTeam_ID={}, firstTeamRotationNumber={}, " \
               "secondTeamRotationNumber={}, fullDate={}, shortDate={}, dateGroupName={}, time={}, createdDate={})>" \
            .format(self.firstTeam_ID, self.secondTeam_ID, self.firstTeamRotationNumber,
                    self.secondTeamRotationNumber, self.fullDate, self.shortDate, self.dateGroupName, self.time,
                    self.createdDate)


class OddDetailsList(Base):
    __tablename__ = 'OddDetailsList'
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_ID = Column(Integer, default=0)
    odd_ID = Column(Integer, default=0)
    firstRowSpreadInfoFullGame = Column(String, nullable=True)
    firstRowSpreadInfoFirstHalf = Column(String, nullable=True)
    firstRowSpreadInfoSecondHalf = Column(String, nullable=True)
    firstRowSpreadMoneyLineFullGame = Column(String, nullable=True)
    firstRowSpreadMoneyLineFirstHalf = Column(String, nullable=True)
    firstRowSpreadMoneyLineSecondHalf = Column(String, nullable=True)
    firstRowSpreadTotalFullGame = Column(String, nullable=True)
    firstRowSpreadTotalFirstHalf = Column(String, nullable=True)
    firstRowSpreadTotalSecondHalf = Column(String, nullable=True)
    firstRowSpreadPriceInfoFullGame = Column(String, nullable=True)
    firstRowSpreadPriceInfoFirstHalf = Column(String, nullable=True)
    firstRowSpreadPriceInfoSecondHalf = Column(String, nullable=True)
    firstRowSpreadPriceTotalFullGame = Column(String, nullable=True)
    firstRowSpreadPriceTotalFirstHalf = Column(String, nullable=True)
    firstRowSpreadPriceTotalSecondHalf = Column(String, nullable=True)
    secondRowSpreadInfoFullGame = Column(String, nullable=True)
    secondRowSpreadInfoFirstHalf = Column(String, nullable=True)
    secondRowSpreadInfoSecondHalf = Column(String, nullable=True)
    secondRowSpreadMoneyLineFullGame = Column(String, nullable=True)
    secondRowSpreadMoneyLineFirstHalf = Column(String, nullable=True)
    secondRowSpreadMoneyLineSecondHalf = Column(String, nullable=True)
    secondRowSpreadTotalFullGame = Column(String, nullable=True)
    secondRowSpreadTotalFirstHalf = Column(String, nullable=True)
    secondRowSpreadTotalSecondHalf = Column(String, nullable=True)
    secondRowSpreadPriceInfoFullGame = Column(String, nullable=True)
    secondRowSpreadPriceInfoFirstHalf = Column(String, nullable=True)
    secondRowSpreadPriceInfoSecondHalf = Column(String, nullable=True)
    secondRowSpreadPriceTotalFullGame = Column(String, nullable=True)
    secondRowSpreadPriceTotalFirstHalf = Column(String, nullable=True)
    secondRowSpreadPriceTotalSecondHalf = Column(String, nullable=True)
    createdDate = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, book_ID, odd_ID, firstRowSpreadInfoFullGame, firstRowSpreadInfoFirstHalf,
                 firstRowSpreadInfoSecondHalf,
                 firstRowSpreadMoneyLineFullGame, firstRowSpreadMoneyLineFirstHalf, firstRowSpreadMoneyLineSecondHalf,
                 firstRowSpreadTotalFullGame, firstRowSpreadTotalFirstHalf, firstRowSpreadTotalSecondHalf,
                 firstRowSpreadPriceInfoFullGame, firstRowSpreadPriceInfoFirstHalf, firstRowSpreadPriceInfoSecondHalf,
                 firstRowSpreadPriceTotalFullGame, firstRowSpreadPriceTotalFirstHalf,
                 firstRowSpreadPriceTotalSecondHalf,
                 secondRowSpreadInfoFullGame, secondRowSpreadInfoFirstHalf, secondRowSpreadInfoSecondHalf,
                 secondRowSpreadMoneyLineFullGame, secondRowSpreadMoneyLineFirstHalf,
                 secondRowSpreadMoneyLineSecondHalf,
                 secondRowSpreadTotalFullGame, secondRowSpreadTotalFirstHalf, secondRowSpreadTotalSecondHalf,
                 secondRowSpreadPriceInfoFullGame, secondRowSpreadPriceInfoFirstHalf,
                 secondRowSpreadPriceInfoSecondHalf,
                 secondRowSpreadPriceTotalFullGame, secondRowSpreadPriceTotalFirstHalf,
                 secondRowSpreadPriceTotalSecondHalf):
        self.book_ID = book_ID
        self.odd_ID = odd_ID
        self.firstRowSpreadInfoFullGame = firstRowSpreadInfoFullGame
        self.firstRowSpreadInfoFirstHalf = firstRowSpreadInfoFirstHalf
        self.firstRowSpreadInfoSecondHalf = firstRowSpreadInfoSecondHalf
        self.firstRowSpreadMoneyLineFullGame = firstRowSpreadMoneyLineFullGame
        self.firstRowSpreadMoneyLineFirstHalf = firstRowSpreadMoneyLineFirstHalf
        self.firstRowSpreadMoneyLineSecondHalf = firstRowSpreadMoneyLineSecondHalf
        self.firstRowSpreadTotalFullGame = firstRowSpreadTotalFullGame
        self.firstRowSpreadTotalFirstHalf = firstRowSpreadTotalFirstHalf
        self.firstRowSpreadTotalSecondHalf = firstRowSpreadTotalSecondHalf
        self.firstRowSpreadPriceInfoFullGame = firstRowSpreadPriceInfoFullGame
        self.firstRowSpreadPriceInfoFirstHalf = firstRowSpreadPriceInfoFirstHalf
        self.firstRowSpreadPriceInfoSecondHalf = firstRowSpreadPriceInfoSecondHalf
        self.firstRowSpreadPriceTotalFullGame = firstRowSpreadPriceTotalFullGame
        self.firstRowSpreadPriceTotalFirstHalf = firstRowSpreadPriceTotalFirstHalf
        self.firstRowSpreadPriceTotalSecondHalf = firstRowSpreadPriceTotalSecondHalf
        self.secondRowSpreadInfoFullGame = secondRowSpreadInfoFullGame
        self.secondRowSpreadInfoFirstHalf = secondRowSpreadInfoFirstHalf
        self.secondRowSpreadInfoSecondHalf = secondRowSpreadInfoSecondHalf
        self.secondRowSpreadMoneyLineFullGame = secondRowSpreadMoneyLineFullGame
        self.secondRowSpreadMoneyLineFirstHalf = secondRowSpreadMoneyLineFirstHalf
        self.secondRowSpreadMoneyLineSecondHalf = secondRowSpreadMoneyLineSecondHalf
        self.secondRowSpreadTotalFullGame = secondRowSpreadTotalFullGame
        self.secondRowSpreadTotalFirstHalf = secondRowSpreadTotalFirstHalf
        self.secondRowSpreadTotalSecondHalf = secondRowSpreadTotalSecondHalf
        self.secondRowSpreadPriceInfoFullGame = secondRowSpreadPriceInfoFullGame
        self.secondRowSpreadPriceInfoFirstHalf = secondRowSpreadPriceInfoFirstHalf
        self.secondRowSpreadPriceInfoSecondHalf = secondRowSpreadPriceInfoSecondHalf
        self.secondRowSpreadPriceTotalFullGame = secondRowSpreadPriceTotalFullGame
        self.secondRowSpreadPriceTotalFirstHalf = secondRowSpreadPriceTotalFirstHalf
        self.secondRowSpreadPriceTotalSecondHalf = secondRowSpreadPriceTotalSecondHalf

    def __repr__(self):
        return "<OddDetailsList(book_ID={}, odd_ID={}, firstRowSpreadInfoFullGame='{}', " \
               "firstRowSpreadInfoFirstHalf='{}', firstRowSpreadInfoSecondHalf='{}', " \
               "firstRowSpreadMoneyLineFullGame='{}', firstRowSpreadMoneyLineFirstHalf='{}', " \
               "firstRowSpreadMoneyLineSecondHalf='{}', firstRowSpreadTotalFullGame='{}', " \
               "firstRowSpreadTotalFirstHalf='{}', firstRowSpreadTotalSecondHalf='{}', " \
               "firstRowSpreadPriceInfoFullGame='{}', firstRowSpreadPriceInfoFirstHalf='{}', " \
               "firstRowSpreadPriceInfoSecondHalf='{}', firstRowSpreadPriceTotalFullGame='{}', " \
               "firstRowSpreadPriceTotalFirstHalf='{}', firstRowSpreadPriceTotalSecondHalf='{}', " \
               "secondRowSpreadInfoFullGame='{}', secondRowSpreadInfoFirstHalf='{}', " \
               "secondRowSpreadInfoSecondHalf='{}', secondRowSpreadMoneyLineFullGame='{}', " \
               "secondRowSpreadMoneyLineFirstHalf='{}', secondRowSpreadMoneyLineSecondHalf='{}', " \
               "secondRowSpreadTotalFullGame='{}', secondRowSpreadTotalFirstHalf='{}', " \
               "secondRowSpreadTotalSecondHalf='{}', secondRowSpreadPriceInfoFullGame='{}', " \
               "secondRowSpreadPriceInfoFirstHalf='{}', secondRowSpreadPriceInfoSecondHalf='{}', " \
               "secondRowSpreadPriceTotalFullGame='{}', secondRowSpreadPriceTotalFirstHalf='{}', " \
               "secondRowSpreadPriceTotalSecondHalf='{}', createdDate={})>" \
            .format(self.book_ID, self.odd_ID, self.firstRowSpreadInfoFullGame,
                    self.firstRowSpreadInfoFirstHalf, self.firstRowSpreadInfoSecondHalf,
                    self.firstRowSpreadMoneyLineFullGame, self.firstRowSpreadMoneyLineFirstHalf,
                    self.firstRowSpreadMoneyLineSecondHalf, self.firstRowSpreadTotalFullGame,
                    self.firstRowSpreadTotalFirstHalf, self.firstRowSpreadTotalSecondHalf,
                    self.firstRowSpreadPriceInfoFullGame, self.firstRowSpreadPriceInfoFirstHalf,
                    self.firstRowSpreadPriceInfoSecondHalf, self.firstRowSpreadPriceTotalFullGame,
                    self.firstRowSpreadPriceTotalFirstHalf, self.firstRowSpreadPriceTotalSecondHalf,
                    self.secondRowSpreadInfoFullGame, self.secondRowSpreadInfoFirstHalf,
                    self.secondRowSpreadInfoSecondHalf, self.secondRowSpreadMoneyLineFullGame,
                    self.secondRowSpreadMoneyLineFirstHalf, self.secondRowSpreadMoneyLineSecondHalf,
                    self.secondRowSpreadTotalFullGame, self.secondRowSpreadTotalFirstHalf,
                    self.secondRowSpreadTotalSecondHalf, self.secondRowSpreadPriceInfoFullGame,
                    self.secondRowSpreadPriceInfoFirstHalf, self.secondRowSpreadPriceInfoSecondHalf,
                    self.secondRowSpreadPriceTotalFullGame, self.secondRowSpreadPriceTotalFirstHalf,
                    self.secondRowSpreadPriceTotalSecondHalf, self.createdDate)
