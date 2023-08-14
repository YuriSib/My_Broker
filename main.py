import requests
from bs4 import BeautifulSoup

# url = 'http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/tqbr/securities.xml?date=2013-12-20'
url = 'https://ru.investing.com/equities/gazprom_rts-historical-data'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

history = soup.find('div', class_='overflow-x-auto desktop:overflow-visible').find('tbody', class_='datatable_body__tb4jX')
time = history.find('td', class_='datatable_cell__LJp3C font-bold').get_text(strip=True)
price = history.find('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ datatable_cell--up__hIuZF')\
    .get_text(strip=True)
open_ = history.find('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ').get_text(strip=True)
amount = history.find_all('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ')[3].get_text(strip=True)

print(time, price, open_, amount)
