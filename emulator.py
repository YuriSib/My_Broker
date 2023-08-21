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
def emulation_entry():
    with sync_playwright() as p:
        # для отображения браузера-эмулятора в аргументе функции прописать - (headless=False, slow_mo=50)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # чтобы получить доступ к портфелю, сперва нужно залогиниться на сайте
        page.goto('https://ru.investing.com/login/', timeout=60000)
        # в аргументе функции указываем почту
        page.fill('input#loginFormUser_email', 'sib_94@vk.com')
        # в аргументе функции указываем пароль
        page.fill('input#loginForm_password', '134grabl')

        html_login = page.content()
        soup_login = BeautifulSoup(html_login, 'lxml')
        privacy_window = soup_login.find('div', class_='ot-sdk-container')

        if privacy_window:
            page.click('button[id=onetrust-accept-btn-handler]')
        page.click('a[onclick="loginFunctions.submitLogin();"][class="newButton orange"]')

        page.goto('https://ru.investing.com/portfolio/?portfolioID=ZGVjNTVmYzpjN29qYTE3NQ%3D%3D', timeout=60000)
        html_ = page.content()
        soup = BeautifulSoup(html_, 'lxml')
        ticker_block = soup.find('tbody', class_='ui-sortable')
        ticker_list = ticker_block.find_all('tr', {'data-pair-exchange-id': '40'})
        browser.close()

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
        page.click('div[class="DatePickerWrapper_input-text__HAN0Z DatePickerWrapper_center__BYe4Q"]')
        page.click('div.NativeDateInput_root__lZxBl')
        # Устанавливаем количество недель, на которое будет расширена выгрузка исторического периода
        for repeat in range(49):
            page.keyboard.press("ArrowUp")
        page.keyboard.press("Enter")
        page.click('button.inv-button.HistoryDatePicker_apply-button__Oj7Hu')
        time.sleep(10)
        page.mouse.wheel(delta_x=0, delta_y=1000)
        time.sleep(10)
        html_ = page.content()
        browser.close()

        return html_


# html = emulation_for_history('https://ru.investing.com/equities/sberbank_rts-historical-data')
# print(history_scrapper(html))


