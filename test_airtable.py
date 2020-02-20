from airtable import Airtable
from config import AIRTABLE_BASE_KEY
from config import AIRTABLE_API_KEY

airtable = Airtable(AIRTABLE_BASE_KEY, 'BetQL_NBA', api_key=AIRTABLE_API_KEY)
print(airtable.get_all())
# print(airtable.get_all(formula="FIND('2020-02-15', {Game Date})=1", fields=['Game Date']))
# data = airtable.get_all(formula="AND(Team1='DAYTN', Team2='UMASS')")
# print(data[0]['fields']['PredictedScoreATS'])
# print(airtable.get_all(formula=
#                        "AND(FIND('recgwWGvCCW8CuBj6', {Team1}), FIND('reckfZBsaD2sKSVAF', {Team2}), "
#                        "FIND('recbNS4hdhA5c2Opf', {Date}), FIND('recWmJe7kOesx8oXu', {Time}))=1"))
# print(airtable.match('Live Results', '123'))
