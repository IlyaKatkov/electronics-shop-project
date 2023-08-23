from src import item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_calculate_total_price():
    check_class = item.Item("Смартфон", 10000, 20)
    assert check_class.calculate_total_price() == 200000

def test_apply_discount():
    check_class = item.Item("Смартфон", 10000, 20)
    assert check_class.apply_discount() == None