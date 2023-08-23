import openpyxl
from bs4 import BeautifulSoup
import pandas as pd

from emulator import emulation_for_history, emulation_for_ticker
from scrapper import history_scrapper, link_scrapper, history_list
from in_excel import save_result


def table_check(list_, path):
    df = pd.read_excel(path)
    # Выбираем нужную колонку (например, "A") и конвертируем ее во множество для быстрого поиска
    column_values = set(df["Ссылка на тикер"])
    # Находим значения из списка b, которых нет в колонке, и добавляем их в DataFrame
    missing_values = [value for value in list_ if value not in column_values]
    if missing_values:
        missing_data = pd.DataFrame({"Ссылка на тикер": missing_values})
        df = df._append(missing_data, ignore_index=True)

        # Записываем обновленный DataFrame обратно в Excel
        df.to_excel(path, index=False)
        print("Отсутствующие значения добавлены в колонку A.")
    else:
        print("Все значения из списка b уже присутствуют в колонке A.")


def historical_tables():
    list_ticker = emulation_for_ticker()

    link_list = link_scrapper(list_ticker)

    for part_link in link_list:
        link = f'https://ru.investing.com{part_link}'
        history_data = emulation_for_history(link)
        save_result(history_data, f'исторические данные/{part_link}.xlsx')


    # list_name = []
    # df = pd.read_excel('исторические данные/Список тикеров.xlsx')
    # column_values_list = df["Ссылка на тикер"].tolist()
    #
    # for part_link in link_list:
    #     if part_link is not column_values_list:
    #         link = f'https://ru.investing.com{part_link}'
    #         try:
    #             history_html = emulation_for_history(link)
    #
    #             html_list = history_list(history_html)
    #
    #             soup = BeautifulSoup(history_html, 'lxml')
    #             name = soup.find('h2', class_='text-lg font-semibold').get_text(strip=True)
    #             list_name.append((name, link))
    #             file_name = f'исторические данные/{name}.xlsx'
    #
    #             workbook = openpyxl.Workbook()
    #             sheet = workbook.active
    #             sheet.append(['Дата', 'Цена закрытия', 'Цена открытия', 'Максимальная цена', 'Минимальная цена', 'Объем торгов'])
    #             for html in html_list:
    #                 sheet.append(history_scrapper(html))
    #             workbook.save(file_name)
    #             print(len(html_list))
    #         except Exception:
    #             print('Не удалось собрать исторические данные по ссылке:', link)
    #     table_check([link], 'исторические данные/Список тикеров.xlsx')

    # table_check(link_list, 'исторические данные/Список тикеров.xlsx')


historical_tables()
