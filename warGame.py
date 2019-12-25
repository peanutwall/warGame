
import pygame
import random

from pygame.locals import *
from sys import exit
from filterWarGame import *


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
soldiersA = 30
soldiersB = 30
soldierFromBase = 20
backgroundColor = (255, 250, 240)
screenSize = (length, width)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
showPolicyA = 1
showPolicyB = 1

pygame.init()
screen = pygame.display.set_mode(screenSize, 0, 32)
screen.fill(backgroundColor)
pygame.display.set_caption("War Game")
drawCubes = DrawCubes(screen, length, width)
drawBases = DrawBases(screen, length, width)
printPreface = PrintPreface(screen, length, width)
drawWarField = DrawWarField(screen, length, width)
drawPolicyA = DrawPolicyA(screen, length, width)
drawPolicyB = DrawPolicyB(screen, length, width)
drawLastRun = DrawLastRun(screen, length, width)
drawSoldiersGained = DrawSoldiersGained(screen, length, width)
warning = Warnings(screen, length, width)
drawRemainingSoldiers = DrawRemainingSoldiers(screen, length, width)
# printPreface(screen, length, width)
isTypingA = 0
isTypingB = 0
warningA = 0
warningB = 0
typingPositionA = -1
typingPositionB = -1
position = -1
positionListA = []
positionListB = []
policyA = [0 for i in range(mapSize * 2 - isEven - 1)]
policyB = [0 for i in range(mapSize * 2 - isEven - 1)]
warField = [0 for i in range(mapSize * 2 - isEven - 1)]
remainingSoldiersA = [0 for i in range(mapSize * 2 - isEven - 1)]
remainingSoldiersB = [0 for i in range(mapSize * 2 - isEven - 1)]
soldiersGained = [0 for i in range(mapSize * 2 - isEven - 1)]
tempList = []
showFormer = 0
formerPolicyA = []
formerPolicyB = []

while True:

    screen.fill(backgroundColor)
    printPreface()
    fontAnnotations = pygame.font.SysFont('Times New Roman', 20)
    showSoldierFromBase = fontAnnotations.render('soldiers from base: ' + str(int(soldierFromBase)), True, BLACK)
    screen.blit(showSoldierFromBase, (length/2 - 70, width/2 - 150))
    drawBases(mapSize, cubeWidth, isSymmetrical, isEven, baseLocationRandom, soldiersA, soldiersB)
    drawWarField(warField, mapSize, cubeWidth, isEven, typingPositionA, typingPositionB)
    drawCubes(mapSize, isEven, cubeWidth, isBoundary)
    drawLastRun(formerPolicyA, formerPolicyB, mapSize, cubeWidth, isEven)
    if showPolicyA:
        drawPolicyA(policyA, mapSize, cubeWidth, isEven)
    if showPolicyB:
        drawPolicyB(policyB, mapSize, cubeWidth, isEven)
    drawRemainingSoldiers(remainingSoldiersA, remainingSoldiersB, mapSize, cubeWidth, isEven)
    drawSoldiersGained(soldiersGained, warField, mapSize, cubeWidth, isEven)
    warning(warningA, warningB)
    positionListA = generatePositionListA(length, width, mapSize, isEven, cubeWidth)
    positionListB = generatePositionListB(length, width, mapSize, isEven, cubeWidth)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            typingPositionA = detectPosition(pos, positionListA)
            typingPositionB = detectPosition(pos, positionListB)
            if typingPositionA != -1:
                isTypingA = 1
                isTypingB = 0
            if typingPositionB != -1:
                isTypingB = 1
                isTypingA = 0
        if event.type == pygame.KEYDOWN and isTypingA:
            if 48 <= event.key <= 57:
                tempList.append(transformKeyToInt(event.key))
            if event.key == pygame.K_SPACE and isTypingA:
                policyA[typingPositionA] = transformTempListToInt(tempList)
                tempList = []
                isTypingA = 0
                typingPositionA = -1
        if event.type == pygame.KEYDOWN and isTypingB:
            if 48 <= event.key <= 57:
                tempList.append(transformKeyToInt(event.key))
            if event.key == pygame.K_SPACE and isTypingB:
                policyB[typingPositionB] = transformTempListToInt(tempList)
                tempList = []
                isTypingB = 0
                typingPositionB = -1
        if event.type == pygame.KEYDOWN and not isTypingB and not isTypingA:
            if event.key == pygame.K_RETURN:
                [warningA, warningB] = checkPolicy(policyA, policyB, soldiersA, soldiersB)
                if warningA == 0 and warningB == 0:
                    warField = judgeResult(policyA, policyB, remainingSoldiersA, remainingSoldiersB)
                    [remainingSoldiersA, remainingSoldiersB] = \
                        calculateRemainingSoldiers(policyA, policyB, remainingSoldiersA, remainingSoldiersB)
                    [soldiersA, soldiersB, soldiersGained] = calculateSoldiers(warField, soldierFromBase)
                    formerPolicyA = policyA
                    formerPolicyB = policyB
                    showPolicyA = 1
                    showPolicyB = 1
                    policyA = [0 for i in range(len(policyB))]
                    policyB = [0 for i in range(len(policyA))]
            if event.key == pygame.K_LSHIFT:
                showPolicyA = 1 - showPolicyA
            if event.key == pygame.K_RSHIFT:
                showPolicyB = 1 - showPolicyB
    pygame.display.update()


