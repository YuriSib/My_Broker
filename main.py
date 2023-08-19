import time
import threading

from emulator import emulation
from scrapper import ticker_data, link_scrapper
from in_excel import save_result
from window import update_table, create_gui


def main():
    while True:
        list_ticker = emulation()

        link_list = link_scrapper(list_ticker)
        data_list = []

        for ticker in list_ticker:
            info_about_ticker = ticker_data(ticker)
            data_list.append(info_about_ticker)
        # тут можно изменить название файла, при замене название также необходимо сменить в модуле window.py
        save_result(data_list, 'биржевые данные.xlsx')

        # устанавливаем время ожидания между циклами
        time.sleep(5)


if __name__ == "__main__":
    code_thread = threading.Thread(target=create_gui)
    code_thread.start()
    code_thread2 = threading.Thread(target=update_table)
    code_thread2.start()
    main()


# # Создаем пул потоков с максимальным количеством потоков равным 3
# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#     # Запускаем функции в пуле потоков
#     future1 = executor.submit(main)
#     future2 = executor.submit(update_table)
#     future3 = executor.submit(create_gui)
#
#     # Дожидаемся завершения всех функций
#     concurrent.futures.wait([future1, future2, future3])
