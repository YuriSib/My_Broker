from bs4 import BeautifulSoup

from playwright.sync_api import sync_playwright


def emulation():
    with sync_playwright() as p:
        # для отображения браузера-эмулятора в аргументе функции прописать - (headless=False, slow_mo=50)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # чтобы получить доступ к портфелю, сперва нужно залогиниться на сайте
        page.goto('https://ru.investing.com/login/')
        # в аргументе функции указываем почту
        page.fill('input#loginFormUser_email', 'your login')
        # в аргументе функции указываем пароль
        page.fill('input#loginForm_password', 'your password')
        # если при попытке входа высвечиватся диалоговое меню, строку кода ниже разкоментировать
        page.click('button[id=onetrust-accept-btn-handler]')
        page.click('a[onclick="loginFunctions.submitLogin();"][class="newButton orange"]')
        page.goto('https://ru.investing.com/portfolio/?portfolioID=ZGVjNTVmYzpjN29qYTE3NQ%3D%3D', timeout=60000)
        html_ = page.content()
        soup = BeautifulSoup(html_, 'lxml')
        ticker_block = soup.find('tbody', class_='ui-sortable')
        ticker_list = ticker_block.find_all('tr', {'data-pair-exchange-id': '40'})
        browser.close()

        return ticker_list



