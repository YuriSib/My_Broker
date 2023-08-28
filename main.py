import time
import threading

from html_master import html_obj
from emulator import emulation_for_ticker
from scrapper import ticker_scrapper, link_scrapper
from in_excel import save_result
from window import update_table, create_gui


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

            # устанавливаем время ожидания между циклами
        time.sleep(1)


if __name__ == "__main__":
    for i in range(10):
        main()

