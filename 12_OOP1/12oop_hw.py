class Moving:
    def move(self):
        raise NotImplementedError


class Animal(Moving):
    def voice(self):
        raise NotImplementedError


class Transport(Moving):
    def launch(self):
        raise NotImplementedError


class Duck(Animal):
    def voice(self):
        print("Quack-quack")

    def move(self):
        print("Swimming")


class Tiger(Animal):
    def voice(self):
        print("Grrr-grrr")

    def move(self):
        print("Running")


class Car(Transport):

    launched = False

    def move(self):
        if not self.launched:
            print("Standing")
        else:
            print("Moving")

    def launch(self):
        self.launched = True


if __name__ == "__main__":
    #Create instances of each class
    duck = Duck()
    tiger = Tiger()
    car = Car()

    # Check that duck is alive
    duck.move()
    duck.voice()

    # Check that tiger is alive
    tiger.move()
    tiger.voice()

    # Check that car is not broken
    car.move()

    car.launch()
    car.move()
