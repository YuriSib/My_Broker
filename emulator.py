from bs4 import BeautifulSoup
import time

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
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        ticker_list = []

        for num in range(1, 8):
            page.goto(f'https://ru.investing.com/stock-screener/?sp=country::56|sector::a|industry::a|'
                      f'equityType::a|exchange::40%3EviewData.symbol;{num}', timeout=60000)

            page.wait_for_selector('#resultsTable')
            html = page.content()
            if html is not None:
                soup = BeautifulSoup(html, 'lxml')
                table = soup.find('table', {'id': 'resultsTable'}).find('tbody').find_all('tr')
                ticker_list.extend(table)
            else:
                continue


        browser.close()

        return ticker_list


@timing_decorator
def emulation_for_history(url):
    with sync_playwright() as p:
        # для отображения браузера-эмулятора в аргументе функции прописать - (headless=False, slow_mo=50)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        html_login = page.content()
        soup_login = BeautifulSoup(html_login, 'lxml')
        privacy_window = soup_login.find('div', class_='ot-sdk-container')
        if privacy_window:
            page.click('button[id=onetrust-accept-btn-handler]')
        page.click('div[class="DatePickerWrapper_input-text__HAN0Z DatePickerWrapper_center__BYe4Q"]')
        page.click('div.NativeDateInput_root__lZxBl')
        # Устанавливаем количество недель, на которое будет расширена выгрузка исторического периода
        for repeat in range(49):
            page.keyboard.press("ArrowUp")
        page.keyboard.press("Enter")
        page.click('button.inv-button.HistoryDatePicker_apply-button__Oj7Hu')
        page.wait_for_selector('#resultsTable')
        html_ = page.content()
        browser.close()

        return html_


# emulation_for_ticker()


