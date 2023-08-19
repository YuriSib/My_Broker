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




