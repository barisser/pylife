import pygame
import map
import main
import image_set
import math
import factions

map_screen_x_margin_left = 0
map_screen_y_margin_bottom = 0
map_screen_x_margin_right = 0
map_screen_y_margin_top = 0

tilex = 10
tiley = 10

def map_init(world_object):
    width = world_object.mapx * tilex
    height = world_object.mapy * tiley
    world_map = pygame.Surface((width, height))
    return world_map

def regenerate_map(world_object, zoom, gridlines):
    m = map_init(world_object)
    width = int(world_object.mapx*tilex / zoom)
    height = int(world_object.mapy*tiley / zoom)
    print width
    print height
    render_world(m, world_object, gridlines)
    pygame.image.save(m, 'originalworld.jpg')
    stretched_map = pygame.transform.smoothscale(m, (width, height))
    return stretched_map

def update_map(map_screen, world, gridlines):
    render_world(map_screen, world, gridlines)

def draw(screen, temp_data):
    x = temp_data['x_position']
    y = temp_data['y_position']
    world = temp_data['world_object']
    map_screen = temp_data['map_object']
    position_map(map_screen, screen, temp_data['zoom'], temp_data['x_position'], temp_data['y_position'])

def position_map(map_surface, screen, zoom, x, y):
    px = x * tilex
    py = y * tiley
    p = (px, py)
    width = int(map_surface.get_width() / zoom)
    height = int(map_surface.get_height() / zoom)
    map_view_width = main.screen_width - map_screen_x_margin_right - map_screen_x_margin_left
    map_view_height = main.screen_height - map_screen_y_margin_top - map_screen_y_margin_bottom
    #screen.blit(stretched_map, (map_screen_x_margin_left, map_screen_y_margin_top), (px, py, map_view_width, map_view_height))
    screen.blit(map_surface, (map_screen_x_margin_left, map_screen_y_margin_top), (px, py, map_view_width, map_view_height))

def render_color(screen, x, y, width, height, color):
    r = pygame.Rect(x, y, width, height)
    screen.fill(color, r)

def draw_text(screen, color, text, px, py):
    surface = image_set.font.render(text, False, (0, 128, 0))
    textrect = surface.get_rect()
    textrect.centerx = px
    textrect.centery = py
    screen.blit(surface, textrect)

def render_geography(screen, px, py, land, width, height, colors):
    terrain_type = land.terrain
    color = colors[terrain_type]
    render_color(screen, px, py, width, height, color)

def render_city(screen, px, py, width, height, city_object, world_object):
    color = world_object.factions[city_object.faction].color
    size = math.pow(city_object.population, 0.5)
    render_color(screen, px+width/2 - size/2, py+height/2 - size/2, size/2, size/2, color)
    draw_text(screen, (250, 250, 250), city_object.name+"  "+str(city_object.id) , px, py)

def draw_road(screen, startx, starty, endx, endy, thickness, color):
    pygame.draw.line(screen, color, (startx, starty), (endx, endy), thickness)

def draw_roads(screen, world_object, zone_width, zone_height):  #add start positions ...?
    thickness = 5
    color = (100, 100, 100)
    for c in world_object.cities:
        for r in c.roads:
            if r.source == c.id:
                d = world_object.cities[r.destination]
            else:
                d = world_object.cities[r.source]

            startx = c.x * zone_width
            starty = c.y * zone_height
            endx = d.x * zone_width
            endy = d.y * zone_height
            draw_road(screen, startx, starty, endx, endy, thickness, color)

def add_gridlines(screen, width, height, n, m):
    color = (0, 0, 0)
    for i in range(n):
        a = width * m
        px = 0
        py = i * height
        render_color(screen, px, py, a, 1, color)
        print str(px)+" / "+str(py)+" / "+str(a)
    for i in range(m):
        b = height * n
        px = i * width
        py = 0
        render_color(screen, px, py, 1, b, color)

def render_world(screen, world_object, gridlines):
    start_position_x = 0#map_screen_x_margin_left
    end_position_x = main.screen_width - map_screen_x_margin_right
    start_position_y = 0#map_screen_y_margin_top
    end_position_y = main.screen_height - map_screen_y_margin_bottom
    start_position = (start_position_x, start_position_y)

    total_width = tilex * world_object.mapx
    zone_width = tilex
    total_height = tiley * world_object.mapy
    zone_height = tiley
    colors = image_set.terrain_colors

    for x in range(world_object.mapx):
        for y in range(world_object.mapy):
            px = start_position_x + zone_width*x
            py = start_position_y + zone_height*y
            land = world_object.map[x][y]
            render_geography(screen, px, py, land, zone_width, zone_height, colors)
            #render_city(screen, px, py, land, zone_width, zone_height)

    for c in world_object.cities:
        px = c.x * zone_width + start_position_x
        py = start_position_y + zone_height * c.y
        render_city(screen, px, py, zone_width, zone_height, c, world_object)

    if gridlines:
        add_gridlines(screen, zone_width, zone_height, world_object.mapx, world_object.mapy)

    draw_roads(screen, world_object, zone_width, zone_height)
