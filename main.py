import os.path

from button import *
from level1 import main1
from level2 import main2
from level3 import main3
from level4 import main4
from level5 import main5
from level6 import main6
from level7 import main7
from level8 import main8
from level9 import main9
from level10 import main10
from level11 import main11
from level12 import main12
import pygame
import sys

pygame.mixer.init()

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
FONT = pygame.font.SysFont("Roboto", 100)


def level():
    global level1, level2, level3, level4, level5, level6, level7, level8, level10, level9, level11, level12
    pygame.display.set_caption("Levels")
    while True:
        with open("levels.txt", "r") as f:
            levels = f.read()
            levels = int(levels)
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill((3, 54, 73))
        if levels == 1:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
        if levels == 2:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
            level2 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 160), text_input="LEVEL 2",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level2.changeColor(OPTIONS_MOUSE_POS)
            level2.update(SCREEN)
        if levels == 3:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
            level2 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 160), text_input="LEVEL 2",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level2.changeColor(OPTIONS_MOUSE_POS)
            level2.update(SCREEN)
            level3 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 260), text_input="LEVEL 3",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level3.changeColor(OPTIONS_MOUSE_POS)
            level3.update(SCREEN)
        if levels == 4:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
            level2 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 160), text_input="LEVEL 2",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level2.changeColor(OPTIONS_MOUSE_POS)
            level2.update(SCREEN)
            level3 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 260), text_input="LEVEL 3",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level3.changeColor(OPTIONS_MOUSE_POS)
            level3.update(SCREEN)
            level4 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 360), text_input="LEVEL 4",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level4.changeColor(OPTIONS_MOUSE_POS)
            level4.update(SCREEN)
        if levels == 5:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
            level2 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 160), text_input="LEVEL 2",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level2.changeColor(OPTIONS_MOUSE_POS)
            level2.update(SCREEN)
            level3 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 260), text_input="LEVEL 3",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level3.changeColor(OPTIONS_MOUSE_POS)
            level3.update(SCREEN)
            level4 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 360), text_input="LEVEL 4",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level4.changeColor(OPTIONS_MOUSE_POS)
            level4.update(SCREEN)
            level5 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 460), text_input="LEVEL 5",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level5.changeColor(OPTIONS_MOUSE_POS)
            level5.update(SCREEN)
        if levels == 6:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
            level2 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 160), text_input="LEVEL 2",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level2.changeColor(OPTIONS_MOUSE_POS)
            level2.update(SCREEN)
            level3 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 260), text_input="LEVEL 3",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level3.changeColor(OPTIONS_MOUSE_POS)
            level3.update(SCREEN)
            level4 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 360), text_input="LEVEL 4",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level4.changeColor(OPTIONS_MOUSE_POS)
            level4.update(SCREEN)
            level5 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 460), text_input="LEVEL 5",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level5.changeColor(OPTIONS_MOUSE_POS)
            level5.update(SCREEN)
            level6 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 560), text_input="LEVEL 6",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level6.changeColor(OPTIONS_MOUSE_POS)
            level6.update(SCREEN)
        if levels == 7:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
            level2 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 160), text_input="LEVEL 2",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level2.changeColor(OPTIONS_MOUSE_POS)
            level2.update(SCREEN)
            level3 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 260), text_input="LEVEL 3",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level3.changeColor(OPTIONS_MOUSE_POS)
            level3.update(SCREEN)
            level4 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 360), text_input="LEVEL 4",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level4.changeColor(OPTIONS_MOUSE_POS)
            level4.update(SCREEN)
            level5 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 460), text_input="LEVEL 5",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level5.changeColor(OPTIONS_MOUSE_POS)
            level5.update(SCREEN)
            level6 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 560), text_input="LEVEL 6",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level6.changeColor(OPTIONS_MOUSE_POS)
            level6.update(SCREEN)
            level7 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 60), text_input="LEVEL 7",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level7.changeColor(OPTIONS_MOUSE_POS)
            level7.update(SCREEN)
        if levels == 8:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
            level2 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 160), text_input="LEVEL 2",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level2.changeColor(OPTIONS_MOUSE_POS)
            level2.update(SCREEN)
            level3 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 260), text_input="LEVEL 3",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level3.changeColor(OPTIONS_MOUSE_POS)
            level3.update(SCREEN)
            level4 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 360), text_input="LEVEL 4",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level4.changeColor(OPTIONS_MOUSE_POS)
            level4.update(SCREEN)
            level5 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 460), text_input="LEVEL 5",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level5.changeColor(OPTIONS_MOUSE_POS)
            level5.update(SCREEN)
            level6 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 560), text_input="LEVEL 6",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level6.changeColor(OPTIONS_MOUSE_POS)
            level6.update(SCREEN)
            level7 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 60), text_input="LEVEL 7",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level7.changeColor(OPTIONS_MOUSE_POS)
            level7.update(SCREEN)
            level8 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 160), text_input="LEVEL 8",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level8.changeColor(OPTIONS_MOUSE_POS)
            level8.update(SCREEN)
        if levels == 9:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
            level2 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 160), text_input="LEVEL 2",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level2.changeColor(OPTIONS_MOUSE_POS)
            level2.update(SCREEN)
            level3 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 260), text_input="LEVEL 3",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level3.changeColor(OPTIONS_MOUSE_POS)
            level3.update(SCREEN)
            level4 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 360), text_input="LEVEL 4",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level4.changeColor(OPTIONS_MOUSE_POS)
            level4.update(SCREEN)
            level5 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 460), text_input="LEVEL 5",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level5.changeColor(OPTIONS_MOUSE_POS)
            level5.update(SCREEN)
            level6 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 560), text_input="LEVEL 6",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level6.changeColor(OPTIONS_MOUSE_POS)
            level6.update(SCREEN)
            level7 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 60), text_input="LEVEL 7",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level7.changeColor(OPTIONS_MOUSE_POS)
            level7.update(SCREEN)
            level8 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 160), text_input="LEVEL 8",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level8.changeColor(OPTIONS_MOUSE_POS)
            level8.update(SCREEN)
            level9 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 260), text_input="LEVEL 9",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level9.changeColor(OPTIONS_MOUSE_POS)
            level9.update(SCREEN)
        if levels == 10:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
            level2 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 160), text_input="LEVEL 2",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level2.changeColor(OPTIONS_MOUSE_POS)
            level2.update(SCREEN)
            level3 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 260), text_input="LEVEL 3",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level3.changeColor(OPTIONS_MOUSE_POS)
            level3.update(SCREEN)
            level4 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 360), text_input="LEVEL 4",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level4.changeColor(OPTIONS_MOUSE_POS)
            level4.update(SCREEN)
            level5 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 460), text_input="LEVEL 5",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level5.changeColor(OPTIONS_MOUSE_POS)
            level5.update(SCREEN)
            level6 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 560), text_input="LEVEL 6",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level6.changeColor(OPTIONS_MOUSE_POS)
            level6.update(SCREEN)
            level7 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 60), text_input="LEVEL 7",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level7.changeColor(OPTIONS_MOUSE_POS)
            level7.update(SCREEN)
            level8 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 160), text_input="LEVEL 8",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level8.changeColor(OPTIONS_MOUSE_POS)
            level8.update(SCREEN)
            level9 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 260), text_input="LEVEL 9",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level9.changeColor(OPTIONS_MOUSE_POS)
            level9.update(SCREEN)
            level10 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                             pos=(960, 360), text_input="LEVEL 10",
                             base_color="white", hovering_color=(0, 204, 0),
                             music=pygame.mixer.music.load("click sound.wav"))
            level10.changeColor(OPTIONS_MOUSE_POS)
            level10.update(SCREEN)
        if levels == 11:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
            level2 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 160), text_input="LEVEL 2",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level2.changeColor(OPTIONS_MOUSE_POS)
            level2.update(SCREEN)
            level3 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 260), text_input="LEVEL 3",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level3.changeColor(OPTIONS_MOUSE_POS)
            level3.update(SCREEN)
            level4 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 360), text_input="LEVEL 4",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level4.changeColor(OPTIONS_MOUSE_POS)
            level4.update(SCREEN)
            level5 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 460), text_input="LEVEL 5",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level5.changeColor(OPTIONS_MOUSE_POS)
            level5.update(SCREEN)
            level6 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 560), text_input="LEVEL 6",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level6.changeColor(OPTIONS_MOUSE_POS)
            level6.update(SCREEN)
            level7 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 60), text_input="LEVEL 7",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level7.changeColor(OPTIONS_MOUSE_POS)
            level7.update(SCREEN)
            level8 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 160), text_input="LEVEL 8",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level8.changeColor(OPTIONS_MOUSE_POS)
            level8.update(SCREEN)
            level9 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 260), text_input="LEVEL 9",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level9.changeColor(OPTIONS_MOUSE_POS)
            level9.update(SCREEN)
            level10 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                             pos=(960, 360), text_input="LEVEL 10",
                             base_color="white", hovering_color=(0, 204, 0),
                             music=pygame.mixer.music.load("click sound.wav"))
            level10.changeColor(OPTIONS_MOUSE_POS)
            level10.update(SCREEN)
            level11 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                             pos=(960, 460), text_input="LEVEL 11",
                             base_color="white", hovering_color=(0, 204, 0),
                             music=pygame.mixer.music.load("click sound.wav"))
            level11.changeColor(OPTIONS_MOUSE_POS)
            level11.update(SCREEN)
        if levels == 12:
            level1 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 60), text_input="LEVEL 1",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level1.color = level1.changeColor(OPTIONS_MOUSE_POS)
            level1.update(SCREEN)
            level2 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 160), text_input="LEVEL 2",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level2.changeColor(OPTIONS_MOUSE_POS)
            level2.update(SCREEN)
            level3 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 260), text_input="LEVEL 3",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level3.changeColor(OPTIONS_MOUSE_POS)
            level3.update(SCREEN)
            level4 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 360), text_input="LEVEL 4",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level4.changeColor(OPTIONS_MOUSE_POS)
            level4.update(SCREEN)
            level5 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 460), text_input="LEVEL 5",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level5.changeColor(OPTIONS_MOUSE_POS)
            level5.update(SCREEN)
            level6 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(320, 560), text_input="LEVEL 6",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level6.changeColor(OPTIONS_MOUSE_POS)
            level6.update(SCREEN)
            level7 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 60), text_input="LEVEL 7",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level7.changeColor(OPTIONS_MOUSE_POS)
            level7.update(SCREEN)
            level8 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 160), text_input="LEVEL 8",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level8.changeColor(OPTIONS_MOUSE_POS)
            level8.update(SCREEN)
            level9 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                            pos=(960, 260), text_input="LEVEL 9",
                            base_color="white", hovering_color=(0, 204, 0),
                            music=pygame.mixer.music.load("click sound.wav"))
            level9.changeColor(OPTIONS_MOUSE_POS)
            level9.update(SCREEN)
            level10 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                             pos=(960, 360), text_input="LEVEL 10",
                             base_color="white", hovering_color=(0, 204, 0),
                             music=pygame.mixer.music.load("click sound.wav"))
            level10.changeColor(OPTIONS_MOUSE_POS)
            level10.update(SCREEN)
            level11 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                             pos=(960, 460), text_input="LEVEL 11",
                             base_color="white", hovering_color=(0, 204, 0),
                             music=pygame.mixer.music.load("click sound.wav"))
            level11.changeColor(OPTIONS_MOUSE_POS)
            level11.update(SCREEN)
            level12 = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                             pos=(960, 560), text_input="LEVEL 12",
                             base_color="white", hovering_color=(0, 204, 0),
                             music=pygame.mixer.music.load("click sound.wav"))
            level12.changeColor(OPTIONS_MOUSE_POS)
            level12.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level1.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main1()
                if level2.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main2()
                if level3.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main3()
                if level4.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main4()
                if level5.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main5()
                if level6.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main6()
                if level7.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main7()
                if level8.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main8()
                if level9.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main9()
                if level10.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main10()
                if level11.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main11()
                if level12.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()
                    main12()
        pygame.display.update()


def main_menu():
    pygame.display.set_caption("Menu")
    SCREEN.fill((3, 54, 73))
    while True:
        if not os.path.exists("levels.txt"):
            with open("levels.txt", "w") as f:
                f.write("1")
        with open("levels.txt", "r") as f:
            levels = f.read()
            levels = int(levels)
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = FONT.render("MAIN MENU", True, (0, 204, 0))
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        RESET_BUTTON = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                              pos=(640, 220), text_input="RESET",
                              base_color="white", hovering_color=(0, 204, 0),
                              music=pygame.mixer.music.load("click sound.wav"))
        PLAY_BUTTON = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                             pos=(640, 340), text_input="PLAY",
                             base_color="white", hovering_color=(0, 204, 0),
                             music=pygame.mixer.music.load("click sound.wav"))
        LEVELS = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60), pos=(640, 460),
                        text_input="LEVELS", base_color="white", hovering_color=(0, 204, 0),
                        music=pygame.mixer.music.load("click sound.wav"))
        QUIT_BUTTON = Button(image=pygame.image.load("button.png"), font=pygame.font.SysFont("Roboto", 60),
                             pos=(640, 580), text_input="QUIT",
                             base_color="white", hovering_color=(0, 204, 0),
                             music=pygame.mixer.music.load("click sound.wav"))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for button in [RESET_BUTTON, PLAY_BUTTON, LEVELS, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESET_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.play()
                    pygame.mixer.music.fadeout(500)
                    with open("levels.txt", "w") as f:
                        f.write(str(1))
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.play()
                    if levels == 1:
                        main1()
                    if levels == 2:
                        main2()
                    if levels == 3:
                        main3()
                    if levels == 4:
                        main4()
                    if levels == 5:
                        main5()
                    if levels == 6:
                        main6()
                    if levels == 7:
                        main7()
                    if levels == 8:
                        main8()
                    if levels == 9:
                        main9()
                    if levels == 10:
                        main10()
                    if levels == 11:
                        main11()
                    if levels == 12:
                        main12()
                if LEVELS.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.play()
                    pygame.mixer.music.fadeout(500)
                    level()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    quit()
        pygame.display.update()
