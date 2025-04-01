# Project Bank

Этот проект предоставляет набор функций для работы с банковскими данными, такими как маскировка номеров карт и счетов, форматирование дат, фильтрация и сортировка данных о транзакциях.

## Описание

Проект состоит из следующих функций:

-   `get_mask_card_number(user_card_number: str) -> str`: Маскирует номер карты, показывая только первые 6 и последние 4 цифры.
-   `get_mask_account(user_account_number: str) -> str`: Маскирует номер счета, показывая только последние 4 цифры.
-   `mask_account_card(user_bank_details: str) -> str`: Обрабатывает информацию о карте или счете клиента и маскирует номер.
-   `get_date(date_string: str) -> str`: Преобразует дату в формат 'ДД.ММ.ГГГГ'.
-   `filter_by_state(operations: list, state: str='EXECUTED') -> list`: Фильтрует список словарей на основе указанного параметра `state`.
-   `sort_by_date(operations: list) -> list`: Сортирует список словарей на основе ключа 'date'.

## Установка

Для установки и запуска проекта необходимо выполнить следующие шаги:

1.  **Клонируйте репозиторий:**

    ```
    git clone https://github.com/Zabashta-Igor/pythonhomework.git

2.  **Перейдите в папку проекта:**

    ```
    cd pythonhomework
    ```

3.  **Установите зависимости с помощью Poetry:**

    ```
    poetry install
    ```

## Использование

Примеры использования функций:

~~~
from src.widget import get_mask_card_number, get_mask_account, mask_account_card, get_date, filter_by_state, sort_by_date

Маскировка номера карты
card_number = "6831982470375048"
masked_card = get_mask_card_number(card_number)
print(f"Masked card number: {masked_card}") # Output: 6831 98** **** 5048

Маскировка номера счета
account_number = "12345678901234567890"
masked_account = get_mask_account(account_number)
print(f"Masked account number: {masked_account}") # Output: **7890

Маскировка информации о карте/счете
bank_details = "Visa Classic 6831982470375048"
masked_details = mask_account_card(bank_details)
print(f"Masked details: {masked_details}") # Output: Visa Classic 6831 98** **** 5048

Преобразование даты
date_string = "2023-10-26T00:00:00"
formatted_date = get_date(date_string)
print(f"Formatted date: {formatted_date}") # Output: 26.10.2023

Пример данных для фильтрации и сортировки
transactions: List[Dict] = [
{"id": 1, "date": "2023-10-27T10:00:00", "state": "EXECUTED", "amount": 100},
{"id": 2, "date": "2023-10-26T12:00:00", "state": "CANCELED", "amount": 50},
{"id": 3, "date": "2023-10-28T14:00:00", "state": "EXECUTED", "amount": 200},
]

Сортировка по дате
print(sort_by_date(operations))

~~~

## Зависимости

Проект использует следующие зависимости:

*   Python 3.13
*   Poetry (для управления зависимостями)
*   requests-2.32.3
*   pytest-8.3.5
*   pytest-cov-6.0.0


## Тестирование

Запуск тестов
pytest

Покрытие кода
Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\masks.py                  10      0   100%
src\processing.py              7      0   100%
src\widget.py                 20      0   100%
tests\__init__.py              0      0   100%
tests\conftest.py             13      0   100%
tests\test_masks.py           13      0   100%
tests\test_processing.py       8      0   100%
tests\test_widget.py           8      0   100%
----------------------------------------------
TOTAL                         79      0   100%


## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE).