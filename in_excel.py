import openpyxl


def save_result(list_, file_name):
    # Создаем новый Excel-файл
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # на этой строке можно изменить название колонок
    sheet.append(['Название компании', 'Тикер', 'Актуальная цена', 'Цена открытия', 'Максимальная цена',
                 'Минимальная цена', 'Объем торгов', 'Последнее обновление'])

    for row_values in list_:
        sheet.append(row_values)
    # Сохраняем Excel-файл
    workbook.save(file_name)
