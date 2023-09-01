import os

from scrapper import link_scrapper
from in_excel import save_history_result
from html_master import html_obj, history_html_obj


# функция проверяет наличие файлов в папке исторические данные
def check_have(name):
    check = bool
    folder_path = 'исторические данные'

    if os.path.isfile(os.path.join(folder_path, (name + '.xlsx'))):
        check = True
    else:
        check = False

    return check


def historical_tables():
    list_ticker = html_obj()

    link_list, ticker_name_list = link_scrapper(list_ticker)

    count = 0
    for part_link in link_list:
        idx = link_list.index(part_link)
        check = check_have(ticker_name_list[idx])
        if check is False:
            if 'cid=' in part_link:
                part_link = part_link.split('?cid=')[0]
            link = f'https://ru.investing.com{part_link}-historical-data'
            history_data = history_html_obj(link)
            save_history_result(history_data, f'исторические данные/{ticker_name_list[idx]}.xlsx')
        else:
            print(f'Документ {ticker_name_list[idx]}.xlsx уже есть в папке!')
        print(f'Осталось выгрузить {len(link_list) - count} элементов')
        count += 1


historical_tables()
