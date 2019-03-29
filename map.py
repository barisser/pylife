import random
import economics
import math
import factions

land_colors = {}
land_colors[0] = (0, 0, 0)
land_colors[1] = (0, 0, 0)

pop_growth_rate = 1.02
pop_starvation_rate = 0.9

mapy = 100
mapx = 150


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
        self.cities = []
        self.factions = []

    def world_logic(self):
        for x in range(self.mapx):
            for y in range(self.mapy):
                self.map[x][y].land_logic()

        for f in self.factions:
            f.faction_logic(self)

class Land:
    def __init__(self):
        #starts out formless
        self.terrain = 0
        self.altitude = 0
        self.resources = []


    def land_logic(self):
        k=0 #do nothing


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

def connect_cities(roads_per_city, world_object):
    for c in range(len(world_object.cities)):
        for i in range(0, roads_per_city):
            destination = random.randint(0, len(world_object.cities)-1)
            new_road = factions.Road(1, c, destination)
            world_object.cities[c].roads.append(new_road)
    return world_object

def init_world():
    global last_city_id
    number_of_cities_average = 15
    world = plains_world()
    a = float(number_of_cities_average) / float((world.mapx * world.mapy))

    default_faction = factions.Faction('The Greeks')
    world.factions.append(default_faction)

    for x in range(world.mapx):
      for y in range(world.mapy):
        r = random.random()
        if r <= a:
          random_pop = int(random.random()*5000)
          print "CITY AT "+str(x)+", "+str(y)
          name = economics.random_city_name()

          world.cities.append(factions.City(random_pop, x, y, name, 0))

    world = connect_cities(2, world)

    return world
