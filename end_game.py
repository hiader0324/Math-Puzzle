import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Roboto', 100)


def end():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((3, 54, 73))
        screen.blit(font.render("Game End... Thanks For Playing!", True, (255, 255, 250)), (100, 360))
        pygame.display.update()
        clock.tick(60)
