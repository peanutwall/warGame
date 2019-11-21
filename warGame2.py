import pandas as pd
import numpy as np
import pygame
import random

from pygame.locals import *
from sys import exit
from filterWarGame2 import *

mapSize = 3
isBoundary = 1
isEven = 0
isSymmetrical = 1

baseLocationRandom = random.randint(1, mapSize)
width = 600
length = 800
cubeWidth = 60
radius = 25
landList = list(range(-mapSize, mapSize+1, 1))
initialSoldiers = 30
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
drawWarField = DrawWarField(screen, length, width)
drawPolicy = DrawPolicy(screen, length, width)
# printPreface(screen, length, width)
isTypingA = 0
isTypingB = 0
typingPositionA = -1
typingPositionB = -1
position = -1
positionListA = []
positionListB = []
policyA = []
policyB = []
for i in range(mapSize * 2 - isEven - 1):
    policyA.append(0)
    policyB.append(0)
warField = []
for i in range(mapSize * 2 - isEven - 1):
    warField.append(0)
printPreface()
tempList = []

while True:
    fontAnnotations = pygame.font.SysFont('Times New Roman', 20)
    drawCubes(mapSize, isEven, cubeWidth, isBoundary)
    drawBases(mapSize, cubeWidth, isSymmetrical, isEven, baseLocationRandom)
    drawWarField(warField, mapSize, cubeWidth, isEven, typingPositionA, typingPositionB)
    drawPolicy(policyA, policyB, mapSize, cubeWidth)
    positionListA = generatePositionListA(length, width, mapSize, isEven, cubeWidth)
    positionListB = generatePositionListB(length, width, mapSize, isEven, cubeWidth)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            typingPositionA = comparePosition(pos, positionListA)
            typingPositionB = comparePosition(pos, positionListB)
            # print(typingPositionA)
            # print(typingPositionB)
            if typingPositionA != -1:
                isTypingA = 1
            if typingPositionB != -1:
                isTypingB = 1
        if event.type == pygame.KEYDOWN and isTypingA:
            if 48 <= event.key <= 57:
                tempList.append(transformKey(event.key))
            if event.key == pygame.K_SPACE and isTypingA:
                policyA[typingPositionA] = transformList(tempList)
                # print(tempList)
                tempList = []
                # print(policyA[typingPositionA])
                isTypingA = 0
                typingPositionA = -1
        if event.type == pygame.KEYDOWN and isTypingB:
            if 48 <= event.key <= 57:
                tempList.append(transformKey(event.key))
            if event.key == pygame.K_SPACE and isTypingB:
                policyB[typingPositionB] = transformList(tempList)
                # print(tempList)
                tempList = []
                # print(policyB[typingPositionB])
                isTypingB = 0
                typingPositionB = -1
        if event.type == pygame.KEYDOWN and not isTypingB and not isTypingA:
            if event.key == pygame.K_RETURN:
                if sum(policyA) <= initialSoldiers and sum(policyB) <= initialSoldiers:
                    warField = judgeResult(policyA, policyB)
                    # print(warField)







    pygame.display.update()

