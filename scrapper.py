from bs4 import BeautifulSoup


# берет на вход объект BS4, возвращает список с данными тикера
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


# на вход получает список html тикеров, возвращает ссылки на эти тикеры
def link_scrapper(ticker_list):
    link_list = []
    ticker_name_list = []
    for ticker in ticker_list:
        name = ticker.find('td', {'data-column-name': 'viewData.symbol'}).get_text(strip=True)
        ticker_name_list.append(name)

        link = ticker.find('td', {'data-column-name': 'name_trans'}).find('a')['href']
        link_list.append(link)

    return link_list, ticker_name_list


# превращает html код в исторические данные
def history_scrapper(html):
    try:
        time_ = html.find('td', class_='datatable_cell__LJp3C text-left align-middle overflow-hidden text-v2-black'
                                       ' text-ellipsis whitespace-nowrap text-sm font-semibold leading-4 min-w-[106px]'
                                       ' left-0 sticky bg-white sm:bg-inherit').get_text(strip=True)
        price = html.find('td', {'dir': 'ltr'}).get_text(strip=True)
        price = price.replace('.', '').replace(',', '.')
        open_ = html.find_all('td', class_='text-v2-black text-right text-sm font-normal leading-5 align-middle '
                                           'min-w-[77px]')[0].get_text(strip=True)
        open_ = open_.replace('.', '').replace(',', '.')
        max_ = html.find_all('td', class_='text-v2-black text-right text-sm font-normal leading-5 align-middle '
                                           'min-w-[77px]')[1].get_text(strip=True)
        max_ = max_.replace('.', '').replace(',', '.')
        min_ = html.find_all('td', class_='text-v2-black text-right text-sm font-normal leading-5 align-middle '
                                           'min-w-[77px]')[2].get_text(strip=True)
        min_ = min_.replace('.', '').replace(',', '.')
        amount = html.find('td', class_='text-v2-black text-right text-sm font-normal leading-5 align-middle '
                                        'min-w-[87px]').get_text(strip=True)
    except Exception:
        time_, price, open_, max_, min_, amount = 0, 0, 0, 0, 0, 0

    return time_, price, open_, max_, min_, amount

