#!/usr/bin/env python3
"""snake implementation in python using pygame
"""

import sys
import pygame
import time
import random

# 1 ... 10
DIFFICULTY = 1

START_LENGTH = 10
WAIT	= 0.1 / DIFFICULTY
RADIUS	= 10
RES	= [800, 600]
WALL	= []
BUG     = ()
pygame.init()
SCREEN = pygame.display.set_mode(RES)
pygame.display.set_caption("Snake by franzl")

class Mob():
    """class for moving objects
    """
    def __init__(self):
        self.headx = 100
        self.heady = 100
        self.length = START_LENGTH
        self.elements = [[self.headx, self.heady]]

        while len(self.elements) != (self.length - 1):
            self.elements.append([self.headx, self.heady])
        self.speed = [RADIUS * 2, 0]
        pygame.draw.circle(SCREEN, (255, 255, 0), (self.headx, self.heady),
            RADIUS)
        pygame.display.flip()

    def move(self):
        """move function
        """
        pygame.draw.circle(SCREEN, (0, 0, 0), (self.elements[-1][0],
            self.elements[-1][1]), RADIUS)
        self.elements.pop()
        self.headx += self.speed[0]
        self.heady += self.speed[1]
        self.elements = [[self.headx, self.heady]] + self.elements[0:]
        self.check_dead()
        for element in self.elements[1:]:
            pygame.draw.circle(SCREEN, (255, 255, 0), (element[0], element[1]),
                RADIUS)
        pygame.draw.circle(SCREEN, (0, 255, 0), (self.headx, self.heady),
            RADIUS)
        pygame.display.flip()
        self.check_bug()

    def check_dead(self):
        """check_dead function
        """
        if [self.headx, self.heady] in self.elements[1:]:
            exit_dead()
        if [self.headx, self.heady] in WALL:
            exit_dead()

    def check_bug(self):
        """check_bug function
        """
        if (self.headx, self.heady) == BUG:
            self.elements.append(self.elements[-1])
            create_bug()

def draw_map():
    """draw_map function
    """
    for n in range(20, RES[0], 20):
        pygame.draw.circle(SCREEN, (0, 0, 255), (n, 20), 10)
        WALL.append([n, 20])
        pygame.draw.circle(SCREEN,(0, 0, 255),(n, RES[1] - 20), 10)
        WALL.append([n, RES[1] - 20])
    for n in range(20, RES[1], 20):
        pygame.draw.circle(SCREEN, (0, 0, 255),(20, n), 10)
        WALL.append([20, n])
        pygame.draw.circle(SCREEN, (0, 0, 255), (RES[0] - 20, n), 10)
        WALL.append([RES[0] - 20 , n])
    pygame.display.flip()

def create_bug():
    """create_bug function
    """
    global BUG
    BUG = ()
    while ( list(BUG) in WALL ) or ( list(BUG) in SNAKE.elements) or (not BUG):
        BUG = (random.randrange(40, RES[0] - 40 , 20),
            (random.randrange(40, RES[1] - 40 , 20)))

    pygame.draw.circle(SCREEN, (255, 0, 0), BUG, RADIUS)
    pygame.display.flip()

def event_loop():
    """main event loop
    """
    while True:
        time.sleep(WAIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_DOWN)	and \
                    (SNAKE.speed != [0, -2*RADIUS]):
                    SNAKE.speed = [0, 2*RADIUS]
                elif (event.key == pygame.K_UP) and \
                    (SNAKE.speed != [0, 2*RADIUS]):
                    SNAKE.speed = [0, -2*RADIUS]
                elif (event.key == pygame.K_RIGHT) and \
                    (SNAKE.speed != [-2* RADIUS, 0]):
                    SNAKE.speed = [2*RADIUS, 0]
                elif (event.key == pygame.K_LEFT) and \
                    (SNAKE.speed != [2* RADIUS, 0]):
                    SNAKE.speed = [-2*RADIUS, 0]
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        SNAKE.move()

def exit_dead():
    """exit_dead funtion
    """
    print("Difficulty:\t%d" % DIFFICULTY)
    print("Bugs eaten:\t%d" % (len(SNAKE.elements) - START_LENGTH + 1))
    print("Score:\t\t%d" % ((len(SNAKE.elements) - START_LENGTH + 1) * DIFFICULTY))
    time.sleep(1)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    draw_map()
    SNAKE = Mob()
    create_bug()
    event_loop()
