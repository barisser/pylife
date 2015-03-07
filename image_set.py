import pygame
import graphics

colorkey = (199, 43, 199)

terrain_colors ={}

def load():
    terrain_colors = {}
    terrain_colors[0] = (0,255,0)#pygame.image.load('./images/terrain/ocean.png').convert()
    terrain_colors[1] = (0,0,255)#pygame.image.load('./images/terrain/plains.png').convert()
    # for t in terrain_colors:
    #     terrain_colors[t] = pygame.transform.smoothscale(terrain_colors[t], (graphics.tilex, graphics.tiley))
    #     terrain_colors[t].set_colorkey(colorkey)
    return terrain_colors

def init():
    global terrain_colors
    terrain_colors = load()
