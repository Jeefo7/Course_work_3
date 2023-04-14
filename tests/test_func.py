from utils.func import *


# def test_load_data():
#     example = [
#   {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#   {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }
# ]
#     assert example == load_data('tests/test.json')


def test_slice_operation():
    example = [
        {
            "id": 441945886,
            "state": "CANCEL",
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ]
    slice_example = [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ]

    assert slice_operation(example) == slice_example


def test_format_date():
    example = "2018-07-11T02:26:18.671407"

    assert format_date(example) == "11.07.2018"


def test_format_from():
    example_one = "Visa Gold 5999414228426353"
    example_two = "Счет 27248529432547658655"
    example_three = ""

    assert format_from(example_one) == "Visa Gold 5999 41** **** 6353 -> "
    assert format_from(example_two) == "Счет **8655 -> "
    assert format_from(example_three) == ""


def test_format_to():
    example_one = "Visa Gold 5999414228426353"
    example_two = "Счет 27248529432547658655"
    example_three = ""

    assert format_to(example_one) == "Visa Gold 5999 41** **** 6353"
    assert format_to(example_two) == "Счет **8655"
    assert format_to(example_three) == ""


def test_show_operation():
    example_dict = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
    }
    conclusion = '26.08.2019 Перевод организации\n' \
                 'Maestro 1596 83** **** 5199 -> Счет **9589\n' \
                 '31957.58 руб.\n'

    assert show_operation(example_dict) == conclusion
