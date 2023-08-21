from bs4 import BeautifulSoup


def ticker_data(soup_obj):
    data_ticker_ = []
    name = soup_obj.find('a', class_='aqlink js-hover-me').get_text(strip=True)
    ticker_ = soup_obj.find('td', class_='left bold').get_text(strip=True)
    price = soup_obj.find('td', {'data-column-name': 'last'}).get_text(strip=True)
    open_ = soup_obj.find('td', {'data-column-name': 'open'}).get_text(strip=True)
    max_ = soup_obj.find('td', {'data-column-name': 'high'}).get_text(strip=True)
    min_ = soup_obj.find('td', {'data-column-name': 'low'}).get_text(strip=True)
    vol = soup_obj.find('td', {'data-column-name': 'vol'}).get_text(strip=True)
    time = soup_obj.find('td', {'data-column-name': 'time'}).get_text(strip=True)
    data_ticker_.append(name), data_ticker_.append(ticker_), data_ticker_.append(price), data_ticker_.append(open_),
    data_ticker_.append(max_), data_ticker_.append(min_), data_ticker_.append(vol), data_ticker_.append(time)

    return data_ticker_


def link_scrapper(ticker_list):
    link_list = []
    for ticker in ticker_list:
        link = ticker.find('span', class_='aqPopupWrapper js-hover-me-wrapper').find('a')['href']
        link_list.append(link)

    return link_list


def history_list(html):
    soup = BeautifulSoup(html, 'lxml')
    history = soup.find_all('tr', {'data-test': 'historical-data-table-row'})

    return history


def history_scrapper(html):
    # soup = BeautifulSoup
    # time_ = html.find('td', class_='datatable_cell__LJp3C font-bold').get_text(strip=True)
    # price = html.find('td', {'dir': 'ltr'}).get_text(strip=True)
    # open_ = html.find_all('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ')[0].get_text(strip=True)
    # max_ = html.find_all('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ')[1].get_text(strip=True)
    # min_ = html.find_all('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ')[2].get_text(strip=True)
    # amount = html.find_all('td', class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ')[3].get_text(
    #     strip=True)
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
