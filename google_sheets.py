import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# сюда вставляем адрес нашей таблицы
SPREADSHEET_ID = "1Nk940U5dssNJXGMyDPs_QBPOuu9rCu7Vdyf-xpyOX-k"


def save_to_google_sheets(values_to_write):
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        # задаем название колонок
        column_name = ['Название компании', 'Тикер', 'Актуальная цена', 'Максимальная цена',
                           'Минимальная цена', 'Объем торгов', 'Рыночная капитализация']
        values_to_write.insert(0, column_name)

        body = {"values": values_to_write}
        result = sheets.values().update(
                # range="test list!A1:H400" - выбираем название листа и устанавливаем диапазон яцеек для заиси
            spreadsheetId=SPREADSHEET_ID, range="test list!A1:H400", valueInputOption="RAW", body=body
        ).execute()

        print("Data updated successfully!")

    except HttpError as error:
        print(error)

