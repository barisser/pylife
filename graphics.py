import pygame
import map
import main
import image_set
import math

map_screen_x_margin_left = 100
map_screen_y_margin_bottom = 100
map_screen_x_margin_right = 0
map_screen_y_margin_top = 0

tilex = 40
tiley = 40

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

def render_geography(screen, px, py, land, width, height, colors):
    terrain_type = land.terrain
    color = colors[terrain_type]
    render_color(screen, px, py, width, height, color)

def render_city(screen, px, py, land, width, height):
    if land.city==0:
      k=0 #do nothing
    else:
      color = (200,0,0)
      render_color(screen, px+width/4, py+height/4, width/2, height/2, color)

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
            render_city(screen, px, py, land, zone_width, zone_height)

    if gridlines:
        add_gridlines(screen, zone_width, zone_height, world_object.mapx, world_object.mapy)
