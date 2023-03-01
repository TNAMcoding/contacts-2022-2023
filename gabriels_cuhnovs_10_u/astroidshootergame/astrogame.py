import pygame
import random

pygame.init()

window = pygame.display.set_mode([480, 715])
pygame.display.set_caption('Pew pew Spaceship')

BACKGROUND = pygame.image.load('stars.jpg')
SPACESHIP = pygame.image.load('spaceship.png')
ASTEROID = pygame.image.load('asteroid.png')

spaceship_x = 100
spaceship_y = 100

spaceship_x_change = 0
spaceship_y_change = 0

asteroid_x = random.randint(20, 420)
asteroid_y = random.randint(20, 650)

asteroids_coord = []

def add_asteroid():
    asteroid_x = random.randint(20, 420)
    asteroid_y = random.randint(20, 650)

    asteroids_coord.append([asteroid_x, asteroid_y])

# izveidoju custom notikumu
CREATE_ASTEROID = pygame.USEREVENT
pygame.time.set_timer(CREATE_ASTEROID, 250)

while True:

    # saraksts ar visiem notikumiem
    events = pygame.event.get()

    for event in events: 

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                spaceship_y_change = -0.3
                spaceship_x_change = 0

            elif event.key == pygame.K_a:
                spaceship_y_change = 0
                spaceship_x_change = -0.3

            elif event.key == pygame.K_s:
                spaceship_y_change = 0.3
                spaceship_x_change = 0

            elif event.key == pygame.K_d:
                spaceship_y_change = 0
                spaceship_x_change = 0.3

            elif event.key == pygame.K_r:
                pass

        if event.type == CREATE_ASTEROID:
            add_asteroid()

    if spaceship_x < 0 or spaceship_x > 436:
        spaceship_x_change = -spaceship_x_change

    if spaceship_y < 0 or spaceship_y > 651:
        spaceship_y_change = -spaceship_y_change

    spaceship_x += spaceship_x_change
    spaceship_y += spaceship_y_change

    window.blit(BACKGROUND, [0, 0])
    window.blit(SPACESHIP, [spaceship_x, spaceship_y])
    
    for coords in asteroids_coord:
        coords[1] += 0.4
        window.blit(ASTEROID, coords)

        if asteroid_y > 800:
            asteroids_coord.remove(coords)

    pygame.display.update()
