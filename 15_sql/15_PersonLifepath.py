from random import randint


class Person:
    def __init__(self, _account: int = 0, house: bool = False, car: bool = False):
        self._account = _account
        self.house = house
        self.car = car

    def work(self):
        self._account += randint(5, 10)

    def buy_a_car(self):
        if self._account >= 40:
            self.car = True
        else:
            print("Not enough resources to buy a house!")

    def sell_a_car(self):
        self.car = False
        self._account += 40

    def buy_a_house(self):
        if self.car is True and self._account >= 100:
            self.house = True
        elif self.car is False:
            print("Customers without cars are not allowed to buy a car!")
        else:
            print("Not enough resources to buy a house!")

    def sell_a_house(self):
        self.house = False
        self._account += 100


if __name__ == '__main__':
    human1 = Person()
    counter = 0

    while human1.car == False and human1.house == False:
        human1.work()
        human1.buy_a_car()
        human1.buy_a_house()
        counter += 1

    print(f"You are a successful human being: you have a house, you have a car and you have {human1._account} coins in your bank account")
    print(f"You've achieved your goal in {counter} steps")
