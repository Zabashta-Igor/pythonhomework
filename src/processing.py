from typing import Any
from typing import Dict
from typing import List


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция фильтрует список словарей по указанному значению ключа 'state'. По умолчанию state == EXECUTED"""

    return [item for item in operations if item.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция сортирует список словарей, задающий порядок сортировки (по умолчанию — убывание)"""

    return sorted(operations, key=lambda item: item["date"], reverse=True)
