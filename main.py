from const import *
import random
import pygame
pygame.init()


def main():
    run = True
    clock = pygame.time.Clock()

# random objects N-Body simulation
    for i in range(400):
        x = random.randrange(-HALF_SCREEN_WIDTH, HALF_SCREEN_WIDTH)
        y = random.randint(-HALF_SCREEN_HEIGHT, HALF_SCREEN_HEIGHT)/2
        Vx = random.randint(-15,15)
        Vy = random.randint(-15,15)
        r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        mass_upper, mass_lower = 30, 20
        max_radius = 600000
        mass_magnitude = random.randint(mass_lower,mass_upper)
        radius_magnitude = ((mass_magnitude-mass_lower) / (mass_upper-mass_lower)) * max_radius #radius from mass
    
        i = Objects(x * AU, y*AU, Vx*1000, 0, 10**mass_magnitude, radius_magnitude, (r,g,b))
        all.append(i)


    while run:
        clock.tick(120)
        window.fill((0, 0, 0))

        for event in pygame.event.get():

            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    const.SCALE *= 1.5
                    const.radius_scale*= 1.5
                if event.y == -1:
                    const.SCALE /= 1.5
                    const.radius_scale /= 1.5
            if event.type == pygame.QUIT:
                run = False

        for object in all:
            object.update(all)
            object.draw(window)

        pygame.display.update()

main()
