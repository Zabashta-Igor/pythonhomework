from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Маскирует номер как карты так и счета"""

    account_card_split = account_card.split()
    if "Счет" in account_card_split:
        return f"Счет {get_mask_account(account_card_split[1])}"
    else:
        card_numbers = []
        card_name = []
        for i in account_card_split:
            if i.isdigit():
                card_numbers.append(i)
            if i.isalpha():
                card_name.append(i)
        str_card_numbers = "".join(card_numbers)
        str_card_name = " ".join(card_name)
        return f"{str_card_name} {get_mask_card_number(str_card_numbers)}"


def get_date(inp_inf: str) -> str:
    """Функция обработки даты в формате ДД-ММ-ГГГГ"""

    date_inf = datetime.strptime(inp_inf[:10], "%Y-%m-%d")
    return f"{date_inf.day:02}.{date_inf.month:02}.{date_inf.year}"


# print(get_date('2024-03-11T02:26:18.671407'))

# print(mask_account_card('Maestro 1596837868705199'))
# print(mask_account_card('Счет 64686473678894779589'))
# print(mask_account_card('MasterCard 7158300734726758'))
# print(mask_account_card('Счет 35383033474447895560'))
# print(mask_account_card('Visa Classic 6831982476737658'))
# print(mask_account_card('Visa Platinum 8990922113665229'))
# print(mask_account_card('Visa Gold 5999414228426353'))
# print(mask_account_card('Счет 73654108430135874305'))
