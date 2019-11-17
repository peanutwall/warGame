import pandas as pd
import numpy as np
import pygame
import random

from pygame.locals import *
from sys import exit
from filterWarGame import *
from filterWarGame2 import *

mapSize = 4
isBoundary = 1
isEven = 0
isSymmetrical = 1

baseLocationRandom = random.randint(1, mapSize)
width = 600
length = 800
cubeWidth = 60
radius = 25
landList = list(range(-mapSize, mapSize+1, 1))
backgroundColor = (255, 250, 240)
screenSize = (length, width)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)


pygame.init()
screen = pygame.display.set_mode(screenSize, 0, 32)
screen.fill(backgroundColor)
pygame.display.set_caption("War Game")
drawCubes = DrawCubes(screen, length, width)
drawBases = DrawBases(screen, length, width)
printPreface = PrintPreface(screen, length, width)
# printPreface(screen, length, width)

printPreface()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    fontAnnotations = pygame.font.SysFont('Times New Roman', 20)

    drawCubes(mapSize, isEven, cubeWidth, isBoundary)

    drawBases(mapSize, cubeWidth, isSymmetrical, isEven, baseLocationRandom)
    pygame.display.update()