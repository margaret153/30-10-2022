class Human:
    def __init__(self, name='Human'):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passenger_names(self):
        if self.passengers != []:
            print(f'Names of {self.brand} passengers:')
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f'There are not passengers in {self.brand}')


nick = Human('Nick')
kate = Human('kate')

car = Auto('Mercedes')
car.add_passenger(nick)
car.add_passenger(kate)

car.print_passenger_names()

