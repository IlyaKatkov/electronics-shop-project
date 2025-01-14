from src.item import Item


class MixinLog:
    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language == "EN":
            self.__language = "RU"
        elif self.language == "RU":
            self.__language = "EN"
        return self


class Keyboard(Item, MixinLog):
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self, language)





