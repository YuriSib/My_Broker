import os

from emulator import emulation_for_history, emulation_for_ticker
from scrapper import history_scrapper, link_scrapper, history_list
from in_excel import save_result


def check_have(name):
    check = bool
    folder_path = 'исторические данные'

    if os.path.isfile(os.path.join(folder_path, (name + '.xlsx'))):
        check = True
    else:
        check = False

    return check


def historical_tables():
    list_ticker = emulation_for_ticker()

    link_list, ticker_name_list = link_scrapper(list_ticker)

    count = 0
    for part_link in link_list:
        idx = link_list.index(part_link)
        check = check_have(ticker_name_list[idx])
        if check is False:
            link = f'https://ru.investing.com{part_link}'
            history_data, name = emulation_for_history(link)
            save_result(history_data, f'исторические данные/{name}.xlsx')
        else:
            print(f'Документ {ticker_name_list[idx]}.xlsx уже есть в папке!')
        print(f'Осталось выгрузить {len(link_list) - count} элементов')
        count += 1


historical_tables()
