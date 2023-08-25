from bs4 import BeautifulSoup


def ticker_scrapper(soup):
    data_ticker_ = []
    name = soup.find('td', {'data-column-name': 'name_trans'}).get_text(strip=True)
    ticker_ = soup.find('td', {'data-column-name': 'viewData.symbol'}).get_text(strip=True)
    price = soup.find('td', {'data-column-name': 'last'}).get_text(strip=True)
    market_cap = soup.find('td', {'data-column-name': 'eq_market_cap'}).get_text(strip=True)
    max_ = soup.find('td', {'data-column-name': 'a52_week_high'}).get_text(strip=True)
    min_ = soup.find('td', {'data-column-name': 'a52_week_low'}).get_text(strip=True)
    vol = soup.find('td', {'data-column-name': 'turnover_volume'}).get_text(strip=True)
    data_ticker_.append(name)
    data_ticker_.append(ticker_)
    data_ticker_.append(price)
    data_ticker_.append(max_)
    data_ticker_.append(min_)
    data_ticker_.append(vol)
    data_ticker_.append(market_cap)

    return data_ticker_


def link_scrapper(ticker_list):
    link_list = []
    ticker_name_list = []
    for ticker in ticker_list:
        name = ticker.find('td', {'data-column-name': 'viewData.symbol'}).get_text(strip=True)
        ticker_name_list.append(name)

        link = ticker.find('td', {'data-column-name': 'name_trans'}).find('a')['href']
        link_list.append(link)

    return link_list, ticker_name_list


def history_list(html):
    soup = BeautifulSoup(html, 'lxml')
    history = soup.find_all('tr', {'data-test': 'historical-data-table-row'})

    return history


def history_scrapper(html):
    try:
        time_ = html.find('td', class_='datatable_cell__LJp3C font-bold').get_text(strip=True)
    except Exception:
        time_ = 'Не удалось извлечь значение!'
    try:
        price = html.find('td', {'dir': 'ltr'}).get_text(strip=True)
    except Exception:
        price = 'Не удалось извлечь значение!'
    try:
        open_ = html.find_all('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ')[0].get_text(strip=True)
    except Exception:
        open_ = 'Не удалось извлечь значение!'
    try:
        max_ = html.find_all('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ')[1].get_text(strip=True)
    except Exception:
        max_ = 'Не удалось извлечь значение!'
    try:
        min_ = html.find_all('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ')[2].get_text(strip=True)
    except Exception:
        min_ = 'Не удалось извлечь значение!'
    try:
        amount = html.find_all('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ')[3].get_text(strip=True)
    except Exception:
        amount = 'Не удалось извлечь значение!'

    return time_, price, open_, max_, min_, amount

