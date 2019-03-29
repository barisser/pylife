import pygame
import graphics
import map
import economics
import pathfinding

def cycle(screen, tempdata):
    #render_land(screen)
    graphics.draw(screen, tempdata)

def game_turn(tempdata):
    print "END"
    print pathfinding.calculate_path(0, 1, tempdata['world_object'])

  #  tempdata['world_object'].world_logic()

def game_init():
    economics.init()
    return map.init_world()

def temp_init(world_object):
    tempdata = {}
    tempdata['x_position'] = 0
    tempdata['y_position'] = 0
    tempdata['x_max'] = world_object.mapx
    tempdata['y_max'] = world_object.mapy
    tempdata['zoom'] = 2
    tempdata['gridlines'] = False
    tempdata['map_object'] = graphics.regenerate_map(world_object, tempdata['zoom'], tempdata['gridlines'])
    tempdata['world_object'] = world_object


    pygame.image.save(tempdata['map_object'], 'world.jpg')

    return tempdata
