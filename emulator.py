from bs4 import BeautifulSoup
import time
import pickle

from playwright.sync_api import sync_playwright


from scrapper import history_scrapper


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time:.6f} секунд")
        return result
    return wrapper


@timing_decorator
def emulation_for_ticker():
    with sync_playwright() as p:
        # для отображения браузера-эмулятора в аргументе функции прописать - (headless=False, slow_mo=50)
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()

        ticker_list = []

        for num in range(1, 8):
            url = f'https://ru.investing.com/stock-screener/?sp=country::56|sector::a|industry::a|equityType::a|' \
                  f'exchange::40%3EviewData.symbol;{num}'
            page.goto(url, timeout=60000)
            html_login = page.content()
            soup_login = BeautifulSoup(html_login, 'lxml')
            privacy_window = soup_login.find('div', class_='ot-sdk-container')
            if privacy_window:
                page.click('button[id=onetrust-accept-btn-handler]')
            while True:
                html = page.content()
                if html is None:
                    continue
                else:
                    break
            soup = BeautifulSoup(html, 'lxml')
            table = soup.find('table', {'id': 'resultsTable'}).find('tbody').find_all('tr')
            ticker_list.extend(table)

        browser.close()
        print(f'Собрано {len(ticker_list)} тикеров')

        return ticker_list


@timing_decorator
def emulation_for_history(url):
    with sync_playwright() as p:
        # для отображения браузера-эмулятора в аргументе функции прописать - (headless=False, slow_mo=50)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        html_login = page.content()
        soup_login = BeautifulSoup(html_login, 'lxml')
        privacy_window = soup_login.find('div', class_='ot-sdk-container')
        if privacy_window:
            page.click('button[id=onetrust-accept-btn-handler]')
        history_link = soup_login.find_all('li', class_='mr-6 last:mr-0 text-xs leading-4 cursor-pointer py-3.5 text-[#5b616e]')[2].find('a')['href']
        history_link = 'https://ru.investing.com' + history_link

        while True:
            page.goto(history_link, timeout=60000)
            page.click('div[class="DatePickerWrapper_input-text__HAN0Z DatePickerWrapper_center__BYe4Q"]', timeout=60000)
            page.click('div[class="NativeDateInput_root__lZxBl"]', timeout=60000)
            time.sleep(9)

            for repeat in range(49):
                page.keyboard.press("ArrowUp")

            time.sleep(9)
            page.keyboard.press("Enter")
            time.sleep(9)
            page.click('button.inv-button.HistoryDatePicker_apply-button__Oj7Hu')
            time.sleep(9)
            html_ = page.content()
            soup = BeautifulSoup(html_, 'lxml')
            html_list = soup.find_all('tr', {'data-test': 'historical-data-table-row'})
            print(len(html_list))
            if len(html_list) > 200:
                break

        browser.close()

        history_data = []
        for html in html_list:
            history_data.append(history_scrapper(html))

        return history_data


# emulation_for_history('https://ru.investing.com/equities/amerisourcebergn')


