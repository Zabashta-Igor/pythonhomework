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
get_mask_card_number - Принимает номер карты и возвращает номер карты с частично замененными цифрами на *
get_mask_account - Принимает номер счета и возвращает последние четыре цифры
mask_account_card - Маскирует номер как карты так и счета
get_date - Функция обработки даты в формате ДД-ММ-ГГГГ
filter_by_state - Функция фильтрует список словарей по указанному значению ключа 'state'. По умолчанию state == EXECUTED
sort_by_date - Функция сортирует список словарей, задающий порядок сортировки (по умолчанию — убывание)
filter_by_currency - Функция обрабатывает список транзакций и поочередно выдает транзакции, где валюта операции соответствует заданной
transaction_descriptions - Функция обрабатывает список транзакций и поочередно возвращает описание каждой из них
card_number_generator - Функция представляет собой генератор номеров банковских карт:
                        создает номера в заданном диапазоне и возвращает их в формате XXXX XXXX XXXX XXXX

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
src\generators.py             43      2    95%
src\masks.py                  10      0   100%
src\processing.py              7      0   100%
src\widget.py                 20      0   100%
tests\__init__.py              0      0   100%
tests\conftest.py             37      1    97%
tests\test_generators.py      56      0   100%
tests\test_masks.py           13      0   100%
tests\test_processing.py       8      0   100%
tests\test_widget.py           8      0   100%
----------------------------------------------
TOTAL                        202      3    99%



## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE).