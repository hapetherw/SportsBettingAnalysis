from airtable import Airtable
from config import AIRTABLE_BASE_KEY
from config import AIRTABLE_API_KEY

airtable = Airtable(AIRTABLE_BASE_KEY, 'Oddshark_NCAAB', api_key=AIRTABLE_API_KEY)
print(airtable.get_all())
