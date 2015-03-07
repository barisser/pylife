import pygame
import gamelogic
import io

screen_width = 1200
screen_height = 800
frame_rate = 50

def init():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    gamelogic.graphics.image_set.init()
    return screen

def main_loop():
    clock = pygame.time.Clock()
    screen = init()

    map_surface = pygame.surface

    done = False

    world = gamelogic.game_init()
    map_screen = gamelogic.graphics.map_init(world)
    tempdata = gamelogic.temp_init(world)
    gamelogic.graphics.update_map(map_screen, world, tempdata['gridlines'])

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            else:
                pressed = pygame.key.get_pressed()
                tempdata = io.respond_to_inputs(event, pressed, tempdata, world)

        screen.fill((0, 0, 0))
        gamelogic.cycle(screen, tempdata)

        pygame.display.flip()
        clock.tick(frame_rate)

if __name__ == '__main__':
    main_loop()
