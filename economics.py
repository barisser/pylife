import random

commodities = []

class Commodity:
    def __init__(self, name):
        self.name = name
        self.diminishing_returns_exponent = 0.9 #by population
        self.per_capita_consumption = 0.4

def init_commodities():
    global commodities
    food = Commodity('Food')
    commodities.append(food)

def init():
    init_commodities()




city_names = ['Berlin', 'NYC', 'Rome', 'Tokyo', 'Milan', 'Paris', 'Dallas', 'Stockholm', 'Bamako',
  'Moscow',
  'Riga',
  'Hamburg',
  'Madrid',
  'Istanbul',
  'Athens',
  'Cairo',
  'Oslo',
  'Aberdeen',
  'San Francisco',
  'Boston'
]

def random_city_name():
    n = random.randint(0, len(city_names)-1)
    return city_names[n]
