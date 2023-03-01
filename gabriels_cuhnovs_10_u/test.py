import pygame

pygame.init()

window = pygame.display.set_mode([600, 450])

CHANGE_COLOR = 

while True:

    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()

            print("Notikums: ", events)