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


class PrintPreface:

    def __init__(self, screen, length, width):
        self.screen = screen
        self.length = length
        self.width = width

    def __call__(self):

        fontPreface = pygame.font.SysFont('microsoft Yahei', 30)
        preface = fontPreface.render('Game Introduction', True, BLACK)
        self.screen.blit(preface, (self.length / 2 - 80, self.width / 5))
        preface2 = fontPreface.render('This area to put some guidance for subjects', True, BLACK)
        self.screen.blit(preface2, (self.length / 2 - 170, self.width / 5 + 30))
        preface3 = fontPreface.render('This area is reserved for subjects to play the game', True, BLACK)
        self.screen.blit(preface3, (self.length / 2 - 200, 2 * self.width / 3))
        return self.screen


class DrawCubes:

    def __init__(self, screen, length, width):
        self.screen = screen
        self.length = length
        self.width = width

    def __call__(self, mapSize, isEven, cubeWidth, isBoundary):
        pygame.draw.line(self.screen, BLACK, (self.length / 2 - mapSize * cubeWidth - cubeWidth / 2, self.width / 2 - cubeWidth),
                         (self.length / 2 + (mapSize - isEven) * cubeWidth + cubeWidth / 2, self.width / 2 - cubeWidth))
        pygame.draw.line(self.screen, BLACK, (self.length / 2 - mapSize * cubeWidth - cubeWidth / 2, self.width / 2),
                         (self.length / 2 + (mapSize - isEven) * cubeWidth + cubeWidth / 2, self.width / 2))
        fontAnnotations = pygame.font.SysFont('Times New Roman', 20)
        # 以下是用直线画法，更加美观，暂时保留在这里
        # for i in range((mapSize+1)*2-isEven):
        #     pygame.draw.line(screen, BLACK, (length / 2 - mapSize * cubeWidth - cubeWidth / 2 + cubeWidth*i, width / 2 - cubeWidth),
        #                      (length / 2 - mapSize * cubeWidth - cubeWidth / 2 + cubeWidth*i, width / 2))
        for i in range((mapSize + 1) * 2 - isEven - 1):
            pygame.draw.rect(self.screen, BLACK, (
            self.length / 2 - mapSize * cubeWidth - cubeWidth / 2 + cubeWidth * i, self.width / 2 - cubeWidth, cubeWidth,
            cubeWidth), 1)
        for i in range((mapSize + 1) * 2 - isEven - 1):
            positionAnnotation = fontAnnotations.render(str(i - mapSize + isEven * (i >= mapSize)), False, BLACK)
            self.screen.blit(positionAnnotation,
                        (self.length / 2 - mapSize * cubeWidth + cubeWidth * i, self.width / 2 - 1.5 * cubeWidth))
        if isBoundary:
            pygame.draw.line(self.screen, GOLD, (self.length / 2, self.width / 2 - cubeWidth), (self.length / 2, self.width / 2), 2)
        return self.screen


class DrawBases:

    def __init__(self, screen, length, width):
        self.screen = screen
        self.length = length
        self.width = width

    def __call__(self, mapSize, cubeWidth, isSymmetrical, isEven, baseLocationRandom):
        pygame.draw.circle(self.screen, BLUE, (int(self.length / 2 - mapSize * cubeWidth), int(self.width / 2 - cubeWidth / 2)),
                           radius)
        fontBase = pygame.font.SysFont('microsoft Yahei', 30)
        baseA = fontBase.render('A', True, WHITE)
        self.screen.blit(baseA, (int(self.length / 2 - mapSize * cubeWidth) - 8, int(self.width / 2 - cubeWidth / 2) - 8))
        fontAnnotations = pygame.font.SysFont('Times New Roman', 20)
        initialSoldiersA = fontAnnotations.render('initial soldiers A: 30', False, BLUE)
        self.screen.blit(initialSoldiersA, (self.length / 2 - mapSize * cubeWidth - 1.5 * cubeWidth, self.width / 2))
        initialSoldiersB = fontAnnotations.render('initial soldiers B: 30', False, RED)
        self.screen.blit(initialSoldiersB, (self.length / 2 + (mapSize - isEven) * cubeWidth - 1.5 * cubeWidth, self.width / 2))

        if isSymmetrical:
            pygame.draw.circle(self.screen, RED, (
                int(self.length / 2 - mapSize * cubeWidth + (2 * mapSize - isEven) * cubeWidth),
                int(self.width / 2 - cubeWidth / 2)),
                               radius)
            baseB = fontBase.render('B', True, WHITE)
            self.screen.blit(baseB, (int(self.length / 2 - mapSize * cubeWidth + (2 * mapSize - isEven) * cubeWidth) - 8,
                                int(self.width / 2 - cubeWidth / 2) - 8))
        else:
            pygame.draw.circle(screen, RED, (
                int(self.length / 2 - mapSize * cubeWidth + (2 * mapSize - baseLocationRandom - isEven) * cubeWidth),
                int(self.width / 2 - cubeWidth / 2)), radius)
            baseB = fontBase.render('B', True, WHITE)
            self.screen.blit(baseB, (
                int(self.length / 2 - mapSize * cubeWidth + (2 * mapSize - baseLocationRandom - isEven) * cubeWidth) - 8,
                int(self.width / 2 - cubeWidth / 2) - 8))
        return self.screen