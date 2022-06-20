from main import main_menu
import pygame
import sys
import threading

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Math Puzzle")
FONT = pygame.font.SysFont("Roboto", 50)
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
text = FONT.render("Loading", True, (0, 204, 0))
text_rect = text.get_rect(center=(640, 580))
CLOCK = pygame.time.Clock()
WORK = 100000000
LOADING_BG = pygame.image.load("loading background.png")
LOADING_BG = pygame.transform.scale(LOADING_BG, (600, 90))
LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 580))
loading_bar = pygame.image.load("loading.png")
logo = pygame.image.load("LOGO.png")
logo_rect = logo.get_rect(center=(640, 150))
loading_finished = False
loading_progress = 0


def dowork():
    global loading_finished, loading_progress
    for i in range(WORK):
        loading_progress = i
    loading_finished = True


threading.Thread(target=dowork).start()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if not loading_finished:
        loading_bar_width = loading_progress / WORK * 550
        loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 60))
        loading_bar_rect = loading_bar.get_rect(midleft=(365, 580))
        screen.fill((3, 54, 73))
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        screen.blit(loading_bar, loading_bar_rect)
        screen.blit(text, text_rect)
        screen.blit(logo, logo_rect)
    else:
        pygame.time.wait(2000)
        main_menu()
    pygame.display.update()
    CLOCK.tick(60)
