from masks import get_mask_account, get_mask_card_number



def mask_account_card(account_card: str) -> str:
    """Маскирует номер как карты так и счета"""

    account_card_split = account_card.split()
    if 'Счет' in account_card_split:
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


def get_date():
    """Функция обработки формата даты"""

    pass
