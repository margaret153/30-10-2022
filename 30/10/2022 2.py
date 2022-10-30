import random

class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.satiety = 50
        self.gladness = 50

    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass

    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass

    def days_indexes(self):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass


brand_of_car = {'BMW':{'fuel': 100, 'strenght': 100, 'consumption': 6},
                'Lada':{'fuel': 50, 'strenght': 40, 'consumption': 10},
                'Volvo':{'fuel': 70, 'strenght': 150, 'consumption': 8},
                'Ferrari':{'fuel': 80, 'strenght': 120, 'consumption': 14}}

