import pandas as pd
import numpy as np
import pygame
import random

from pygame.locals import *
from sys import exit


#固定参数
radius = 25
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)


def printPreface(screen, length, width):
    fontPreface = pygame.font.SysFont('microsoft Yahei', 30)
    preface = fontPreface.render('Game Introduction', True, BLACK)
    screen.blit(preface, (length / 2 - 80, width / 5))
    preface2 = fontPreface.render('This area to put some guidance for subjects', True, BLACK)
    screen.blit(preface2, (length / 2 - 170, width / 5 + 30))
    preface3 = fontPreface.render('This area is reserved for subjects to play the game', True, BLACK)
    screen.blit(preface3, (length / 2 - 200, 2 * width / 3))

def drawCubes(screen, length, width, mapSize, isEven, cubeWidth, isBoundary):
    pygame.draw.line(screen, BLACK, (length/2 - mapSize*cubeWidth - cubeWidth/2, width/2 - cubeWidth),
                     (length/2 + (mapSize-isEven)*cubeWidth + cubeWidth/2, width/2 - cubeWidth))
    pygame.draw.line(screen, BLACK, (length / 2 - mapSize * cubeWidth - cubeWidth / 2, width / 2),
                     (length / 2 + (mapSize-isEven) * cubeWidth + cubeWidth / 2, width / 2))
    fontAnnotations = pygame.font.SysFont('Times New Roman', 20)
    #以下是用直线画法，更加美观，暂时保留在这里
    # for i in range((mapSize+1)*2-isEven):
    #     pygame.draw.line(screen, BLACK, (length / 2 - mapSize * cubeWidth - cubeWidth / 2 + cubeWidth*i, width / 2 - cubeWidth),
    #                      (length / 2 - mapSize * cubeWidth - cubeWidth / 2 + cubeWidth*i, width / 2))
    for i in range((mapSize + 1) * 2 - isEven-1):
        pygame.draw.rect(screen, BLACK, (length / 2 - mapSize * cubeWidth - cubeWidth / 2 + cubeWidth*i, width / 2 - cubeWidth, cubeWidth, cubeWidth), 1)
    for i in range((mapSize + 1) * 2 - isEven - 1):
        positionAnnotation = fontAnnotations.render(str(i-mapSize+isEven*(i >= mapSize)), False, BLACK)
        screen.blit(positionAnnotation, (length / 2 - mapSize * cubeWidth + cubeWidth*i, width / 2 - 1.5*cubeWidth))
    if isBoundary:
        pygame.draw.line(screen, GOLD, (length/2, width/2-cubeWidth), (length/2, width/2), 2)

def drawBases(screen, length, width, mapSize, cubeWidth, isSymmetrical, isEven, baseLocationRandom):
    pygame.draw.circle(screen, BLUE, (int(length / 2 - mapSize * cubeWidth), int(width / 2 - cubeWidth / 2)), radius)
    fontBase = pygame.font.SysFont('microsoft Yahei', 30)
    baseA = fontBase.render('A', True, WHITE)
    screen.blit(baseA, (int(length / 2 - mapSize * cubeWidth) - 8, int(width / 2 - cubeWidth / 2) - 8))
    fontAnnotations = pygame.font.SysFont('Times New Roman', 20)
    initialSoldiersA = fontAnnotations.render('initial soldiers A: 30', False, BLUE)
    screen.blit(initialSoldiersA, (length / 2 - mapSize * cubeWidth - 1.5 * cubeWidth, width / 2))
    initialSoldiersB = fontAnnotations.render('initial soldiers B: 30', False, RED)
    screen.blit(initialSoldiersB, (length / 2 + (mapSize - isEven) * cubeWidth - 1.5 * cubeWidth, width / 2))

    if isSymmetrical:
        pygame.draw.circle(screen, RED, (
            int(length / 2 - mapSize * cubeWidth + (2 * mapSize - isEven) * cubeWidth), int(width / 2 - cubeWidth / 2)),
                           radius)
        baseB = fontBase.render('B', True, WHITE)
        screen.blit(baseB, (int(length / 2 - mapSize * cubeWidth + (2 * mapSize - isEven) * cubeWidth) - 8,
                            int(width / 2 - cubeWidth / 2) - 8))
    else:
        pygame.draw.circle(screen, RED, (
            int(length / 2 - mapSize * cubeWidth + (2 * mapSize - baseLocationRandom - isEven) * cubeWidth),
            int(width / 2 - cubeWidth / 2)), radius)
        baseB = fontBase.render('B', True, WHITE)
        screen.blit(baseB, (
        int(length / 2 - mapSize * cubeWidth + (2 * mapSize - baseLocationRandom - isEven) * cubeWidth) - 8,
        int(width / 2 - cubeWidth / 2) - 8))




