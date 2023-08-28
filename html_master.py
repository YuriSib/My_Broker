from bs4 import BeautifulSoup
import time
import re


from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from scrapper import history_scrapper


def ticker_name(value):
    pattern = r'\((.*?)\)'
    match = re.search(pattern, value)

    text_inside_brackets = match.group(1)

    return text_inside_brackets


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
def html_obj():
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("start-maximized")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # Пробуем избежать вывода сообщений об уставершей версии в консоль
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)

        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        url_ = 'https://ru.investing.com/stock-screener/?sp=country::56%7Csector::a%7Cindustry::a%7CequityType::a%3Ceq_market_cap;'
        ticker_list = []
        for count in range(1, 8):
                print(f'Гружу {count}-ю страницу...')
                driver.get(url=f'{url_}{count}')
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.visibility_of_element_located((By.XPATH, '//td[@data-column-name="name_trans" and contains(@class, "symbol left bold elp")]/a')))

                # html = driver.page_source
                # soup_login = BeautifulSoup(html, 'lxml')
                # privacy_window = soup_login.find('div', class_='ot-sdk-container')
                # if privacy_window:
                #         button = driver.find_element('id', 'onetrust-accept-btn-handler')
                #         button.click()
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                table = soup.find('table', {'id': 'resultsTable'}).find('tbody').find_all('tr')
                ticker_list.extend(table)
        print(f'Собрано {len(ticker_list)} тикеров')

        return ticker_list


def history_html_obj(url):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        options.add_argument("--headless")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # Пробуем избежать вывода сообщений об уставершей версии в консоль
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)

        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        driver.get(url=url)

        html = driver.page_source
        soup_login = BeautifulSoup(html, 'lxml')
        privacy_window = soup_login.find('div', class_='ot-sdk-container')
        if privacy_window:
                button = driver.find_element('id', 'onetrust-accept-btn-handler')
                button.click()
        button = driver.find_element("xpath", "//div[contains(@class, 'DatePickerWrapper_input-text__HAN0Z') and "
                                              "contains(@class, 'DatePickerWrapper_center__BYe4Q')]")
        button.click()

        button = driver.find_element("xpath", "//input[@type='date']")
        try:
                button.click()
        except Exception:
                button2 = driver.find_element("xpath", "//input[@type='date']")
                button2.click()
                button.click()

        for i in range(42):
                button.send_keys("\ue013")
        button.send_keys("\ue007")

        button = driver.find_element('xpath', '//button[@class="inv-button HistoryDatePicker_apply-button__Oj7Hu"]')
        try:
                button.click()
        except Exception:
                driver.execute_script("arguments[0].click();", button)

        time.sleep(10)

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        # name = soup.find('h1', {'class': 'text-2xl font-semibold instrument-header_title__6W2Qr mobile:mb-2'}).get_text(
        #         strip=True)
        # name = ticker_name(name)
        history_data_list = soup.find_all('tr', {'data-test': 'historical-data-table-row'})
        history_data = []
        for html in history_data_list:
                history_data.append(history_scrapper(html))

        return history_data

#
# url = 'https://ru.investing.com/equities/sberbank_rts-historical-data'
# history_html_obj(url)
