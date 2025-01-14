import csv
import os
from InstantiateCSVError import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    DATA_PATH = os.path.join("src", "items.csv")
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"


    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise ValueError('Складывать можно только объекты Item и дочерние от них.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate



    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data_string):
        name = data_string
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        if not os.path.exists(cls.DATA_PATH):
            raise FileNotFoundError("Отсутствует файл item.csv")
        try:
            with open(cls.DATA_PATH, "r") as f:
                reader = csv.DictReader(f)

            for line in reader:
                item1 = (cls(line["name"],line["price"], line["quantity"]))
                cls.all.append(item1)
        except (KeyError, TypeError):
            raise InstantiateCSVError("Файл item.csv повреждён")



    @staticmethod
    def string_to_number(string):
        string = float(string)
        return int(string)




















