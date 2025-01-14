from src import item
from src.item import Item
from src.phone import Phone
import pytest
"""Здесь надо написать тесты с использованием pytest для модуля item."""



def test_calculate_total_price():
    check_class = item.Item("Смартфон", 10000, 20)
    assert check_class.calculate_total_price() == 200000



def test_apply_discount():
    check_class = item.Item("Смартфон", 10000, 20)
    assert check_class.apply_discount() == None


def test_string_to_number():
    check_class = item.Item("Смартфон", 10000, 20)
    assert check_class.string_to_number("5") == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv() == "Отсутствует файл item.csv"

def test_repr():
    item1 = Item('Смартфон', 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_str():
    item1 = Item('Смартфон', 10000, 20)
    assert str(item1) == 'Смартфон'

def test_add():
    item1 = Item("Смартфон", 10000, 30)
    phone1 = Phone("iPhone 14", 120_000, 10, 2)
    assert item1 + phone1 == 40
    assert phone1 + phone1 == 20
    with pytest.raises(ValueError):
        assert phone1 + 10 == "Складывать можно только объекты Item и дочерние от них"
        assert phone1 + 10 == "Складывать можно только объекты Item и дочерние от них"


