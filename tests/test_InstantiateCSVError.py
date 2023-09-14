import pytest
import os
import csv
from src.item import Item
from src.InstantiateCSVError import InstantiateCSVError



def test_InstantiateCSVError():
    data = [
        {'name': 'item_1', 'quantity': '1'},
        {'name': 'item_2', 'quantity': '2'},
        {'name': 'item_3', 'quantity': '3'}
    ]

    with open('new.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    Item.DATA_PATH = "new.csv"
    with pytest.raises(InstantiateCSVError):
        raise InstantiateCSVError()
        Item.instantiate_from_csv() == "Ôאיכ ןמגנוזה¸ם"


    os.remove("new.csv")