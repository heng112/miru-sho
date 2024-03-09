
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

SPREADSHEET_KEY = '1VRIn55BflM6bwc-7TlKExG3yZNEG2HjtDH9hlcgyECQ' # 「docs.google.com/spreadsheets/d/xxxxxxxxxxxxx/edit#gid=0」の「xxxxxxxxxxxxx」部分

# If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
scope = 'https://spreadsheets.google.com/feeds'
credentials_file_path = '../credentials.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file_path, scope)

gc = gspread.authorize(credentials)
workbook = gc.open_by_key(SPREADSHEET_KEY)

workbook.values_update(
    'シート1', # どのシートに書き込むのかを指定
    params={'valueInputOption': 'USER_ENTERED'},
    body={'values': list(csv.reader(open('./test.csv', encoding='utf_8_sig')))}
)