import math
import random

last_city_id = -1
last_faction_id = -1
last_trade_route_id = -1
last_road_id = -1

class Faction:
    def __init__(self, name):
        global last_faction_id
        last_faction_id = last_faction_id + 1
        self.id = last_faction_id
        self.name = name
        self.cities = []
        self.color = (random.randint(0,2525252)%255, random.randint(0,2525252)%255, random.randint(0,2525252)%255)

    def faction_logic(self, world_object):
        for c in self.cities:
              c.city_logic(self, world_object, faction_object)

class TradeRoute:
    def __init__(self, source, destination, amount):  #source and destination should be identical??
        global last_trade_route_id
        last_trade_route_id = last_trade_route_id + 1
        self.id = last_trade_route_id
        self.source = source
        self.destination = destination
        self.amount = amount
        self.cost = calculate_trade_route_cost(self)

class Road:
    def __init__(self, quality, source, destination):
        global last_road_id
        self.quality = quality
        last_road_id = last_road_id + 1
        self.id = last_road_id
        self.source = source
        self.destination = destination

class City:
    def __init__(self, pop, x, y, name, faction_id):
        global last_city_id
        last_city_id = last_city_id + 1
        self.id = last_city_id
        self.faction_id = faction_id
        self.x = x
        self.y = y
        self.population = pop
        self.prosperity = 0
        self.name = name
        self.faction = 0
        self.trading_relationships = []
        self.roads = []

    def city_logic(self, world_object, faction_object):
        self.trading_relationships = []  #clear all old trade routes from last turn
        self.trade(self, world_object, faction_object)  #creates trade routes
        self.calculate_prosperity()
        self.consume()
        self.grow()

    def trade(self, world_object, faction_object):
        trade_amount = self.population
        for i in range(0, trade_amount):
            partner = find_trading_partners(faction_object)
            trade_with_partner(self, partner)


    def find_trading_partners(self, faction_object):
        found = False
        while not found:
          n = random.randint(0, len(faction_object.cities)-1)
          if n == self.id:
              k=0
          else:
              found=True
        return faction_object(cities[n])

    def trade_with_partner(self, partner):
        amount = self.population * partner.population
        traderoute = TradeRoute(self.id, partner.id, amount)
        self.trading_relationships.append(traderoute)

    def calculate_prosperity(self):
        k=0

    def consume(self):
        k=0

    def grow(self):
        k=0
