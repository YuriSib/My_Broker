import time

from html_master import html_obj
from scrapper import ticker_scrapper
from in_excel import save_result
from google_sheets import save_to_google_sheets


def main():
    error = False
    while True:
        try:
            list_ticker = html_obj()
        except Exception:
            print('Цикл начал новую итерацию из-за неизвестной ошибки')
            continue

        data_list = []

        for ticker in list_ticker:
            try:
                info_about_ticker = ticker_scrapper(ticker)
                data_list.append(info_about_ticker)
            except AttributeError:
                print('Цикл начал новую итерацию из-за ошибки AttributeError')
                error = True
                break
        if error is True:
            continue
            # тут можно изменить название файла
        save_result(data_list, 'биржевые данные.xlsx')
        save_to_google_sheets(data_list)
            # устанавливаем время ожидания между циклами
        time.sleep(1)


if __name__ == "__main__":
        main()

