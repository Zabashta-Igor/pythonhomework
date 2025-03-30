import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_card_number(number_card):
    assert get_mask_card_number(number_card) == "7000 79** **** 6361"

    with pytest.raises(TypeError):
        assert get_mask_card_number()

    assert get_mask_card_number(234562) is None


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "**4305"

    with pytest.raises(TypeError):
        assert get_mask_account()

    assert get_mask_account("werhvbdgffdjbsth") is None
