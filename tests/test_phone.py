from src import phone
from src.phone import Phone
import pytest

def test_number_of_sim():
    check_class = phone.Phone("iPhone 14", 120_000, 5, 2)
    assert check_class.number_of_sim == 2
    with pytest.raises(ValueError):
        check_class.number_of_sim = 0
        assert check_class.number_of_sim == 'The number of physical SIM-cards must be an integer greater than zero'


def test_repr():
    phone1 = Phone('iPhone 14', 120000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    phone1 = Phone('iPhone 14', 120000, 5, 2)
    assert str(phone1) == 'iPhone 14'