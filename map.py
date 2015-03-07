import random
import economics
import math

land_colors = {}
land_colors[0] = (0,0,255)
land_colors[1] = (50, 200, 10)

pop_growth_rate = 1.02
pop_starvation_rate = 0.9

mapy = 20
mapx = 20

class World:
    def __init__(self, mapx, mapy):
        self.map = []
        for i in range(mapx):
            r=[]
            for a in range(mapy):
                newland = Land()
                r.append(newland)
            self.map.append(r)
        self.mapx = mapx
        self.mapy = mapy

    def world_logic(self):
        for x in range(self.mapx):
            for y in range(self.mapy):
                self.map[x][y].land_logic()

class Land:
    def __init__(self):
        #starts out formless
        self.terrain = 0
        self.altitude = 0
        self.resources = []
        self.city = 0

    def land_logic(self):
        if self.city == 0:
            k=0 #do nothing
        else:
            self.city.city_logic(self)

class City:
    def __init__(self, pop, x, y, name):
        self.x = x
        self.y = y
        self.population = pop
        self.assets = [0] * len(economics.commodities)
        self.money = 0
        self.name = name
        self.prices = [0] * len(economics.commodities)

    def city_logic(self, my_land_object):
        self.consume()
        self.grow()
        self.produce(my_land_object)
        self.set_prices()


    def consume(self):
        for n, x in enumerate(economics.commodities):
            need = x.per_capita_consumption * self.population
            print need
            self.assets[n] = self.assets[n] - need
            if self.assets[n] < 0:
                self.assets[n] = 0

    def produce(self, my_land_object):
        for n, x in enumerate(my_land_object.resources):
            commodity = economics.commodities[n]
            new_resources = x * math.pow(self.population, commodity.diminishing_returns_exponent)
            print new_resources
            self.assets[n] = self.assets[n] + new_resources

    def grow(self):
        if self.assets[0] > 0: #food
            self.population = self.population * pop_growth_rate
        else:
            self.population = self.population * pop_starvation_rate
        print str(self.name) + "  "+str(self.population)

    def set_prices(self):
        for n, x in enumerate(self.prices):
            amount = self.assets[n]
            p = economics.set_price(self.money, self.population, amount)

def blank_world():
    return World(mapx, mapy)

def island_world():
    w = World(mapx, mapy)
    w = islands(w)
    return w

def plains_world():
    w = World(mapx, mapy)
    for x in range(w.mapx):
        for y in range(w.mapy):
            w.map[x][y].terrain = 0
            w.map[x][y].resources = [random.random()]
    return w

def islands(world):
    for x in range(world.mapx):
        for y in range(world.mapy):
            dx = int((x-world.mapx/2))
            dy = int((y-world.mapy/2))
            d = math.pow(dx*dx+dy*dy, 0.5)
            f = math.sin(d/3)
            if f>0.7:
                world.map[x][y].terrain=1
    return world

def init_world():
    number_of_cities_average = 8
    world = plains_world()
    a = float(number_of_cities_average) / float((world.mapx * world.mapy))
    for x in range(world.mapx):
      for y in range(world.mapy):
        r = random.random()
        if r <= a:
          random_pop = int(random.random()*5000)
          print "CITY AT "+str(x)+", "+str(y)
          name = economics.random_city_name()
          world.map[x][y].city = City(random_pop, x, y, name)
    return world
