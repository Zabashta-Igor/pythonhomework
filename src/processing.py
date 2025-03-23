
def filter_by_state(operations: list, state: str='EXECUTED') -> list:
    """Функция фильтрует список словарей по указанному значению ключа 'state'. По умолчанию state == EXECUTED"""

    return [item for item in operations if item.get('state') == state]


def sort_by_date(operations: list) -> list:
    """Функция сортирует список словарей, задающий порядок сортировки (по умолчанию — убывание)"""

    return sorted(operations, key=lambda item: item["date"], reverse = True)

