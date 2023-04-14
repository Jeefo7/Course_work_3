import json


def load_data(json_file):
    """Выгрузка из JSON файла"""
    with open(json_file, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def slice_operation(data):
    """Срез всех операций из ранее выгруженного JSON файла по ключу 'EXECUTED' и реверс по дате"""
    data = [item for item in data if item.get('state') == 'EXECUTED']
    data = sorted(data, key=lambda item: item['date'], reverse=True)
    return data


def format_date(date):
    """Форматирование даты в ДД.ММ.ГГГГ"""
    beautiful_date = date[:10].split("-")[::-1]

    return ".".join(beautiful_date)


def format_from(from_):
    """Маскировка карты/счета отправителя
       Также проверка на то, счёт это или карта"""
    if from_:
        from_ = from_.split(" ")
        if len(from_[-1]) == 20:
            return f"{from_[0] + ' **' + from_[-1][-4:]} -> "
        else:
            return f"{' '.join(from_[:-1])} {from_[-1][:4] + ' ' + from_[-1][4:6] + '** **** ' + from_[-1][-4:]} -> "
    else:
        return ''


def format_to(to_):
    """Маскировка карты/счета получателя
       Также проверка на то, счёт это или карта"""
    if to_:
        to_ = to_.split(" ")
        if len(to_[-1]) == 20:
            return f"{to_[0] + ' **' + to_[-1][-4:]}"
        else:
            return f"{' '.join(to_[:-1])} {to_[-1][:4] + ' ' + to_[-1][4:6] + '** **** ' + to_[-1][-4:]}"
    else:
        return ''


def show_operation(item):
    """Готовое представление вывода операции"""
    date_ = format_date(item.get("date"))
    from_ = format_from(item.get("from"))
    to_ = format_to(item.get("to"))

    return f'{date_} {item.get("description")}\n' \
           f'{from_}{to_}\n' \
           f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'
