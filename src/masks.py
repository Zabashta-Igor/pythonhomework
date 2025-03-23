from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str, None]:
    """Принимает номер карты и возвращает номер карты с частично замененными цифрами на *"""

    str_card_number = str(card_number)
    if card_number.isdigit() and len(card_number) == 16:
        return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[12:]}"
    else:
        return None


def get_mask_account(account_number: Union[str]) -> Union[str, None]:
    """Принимает номер счета и возвращает последние четыре цифры"""

    str_account_number = str(account_number)
    if str_account_number.isdigit() and len(str_account_number) == 20:
        return f"**{str_account_number[-4:]}"
    else:
        return None


print(get_mask_card_number("8888888888888888"))
print(get_mask_account("88888888888888888888"))
