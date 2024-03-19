import pygame
import math
import random
from QTGUI import *
from functions.functions import *
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites()
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILE_SIZE
        self.y = y*TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        pass

