import time
import threading

from emulator import emulation_for_ticker
from scrapper import ticker_scrapper, link_scrapper
from in_excel import save_result
from window import update_table, create_gui


def main():
    # while True:
    list_ticker = emulation_for_ticker()

    # link_list = link_scrapper(list_ticker)
    data_list = []

    for ticker in list_ticker:
        info_about_ticker = ticker_scrapper(ticker)
        data_list.append(info_about_ticker)
        # тут можно изменить название файла, при замене название также необходимо сменить в модуле window.py
    save_result(data_list, 'биржевые данные.xlsx')

        # устанавливаем время ожидания между циклами
    time.sleep(5)


if __name__ == "__main__":
    # code_thread = threading.Thread(target=create_gui)
    # code_thread.start()
    # code_thread2 = threading.Thread(target=update_table)
    # code_thread2.start()
    main()

