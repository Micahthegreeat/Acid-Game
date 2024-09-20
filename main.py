#Code by Micah Knox and Robert Palmer  Art by Space Monkey Mafia   started 09-09-24
#
#https://stackoverflow.com/questions/73378518/how-to-import-and-call-main-functions-from-different-files
#
#https://www.piskelapp.com/p/create/sprite
import math
import pygame
import time

pygame.font.init()

WIDTH, HEIGHT = 960, 540
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Dodge")
#player size
PLAYER_WIDTH = 10
PLAYER_HEIGHT = 15
#Tiles to build the wall around
Tile_size = 20

FONT = pygame.font.SysFont("comicsans", 30)

input()