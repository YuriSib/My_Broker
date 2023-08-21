from pprint import pprint

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'client_secret.json'
spreadsheet_id = '1rag-znoZjPAUgm7MJUYtkJhb4HSPG7AUyHIhJUc8zsQ'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

values = service.spreadsheets().values().get(
    spreadsheet_ID=spreadsheet_id,
    range='A1:E10',
    majorDimension='ROWS'
).excute()
pprint(values)
exit()
