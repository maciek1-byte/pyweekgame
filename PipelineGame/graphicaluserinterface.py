import pygame
import pygame as pg
import sys
from functions.functions import *
from PipelineGame.objects import *
from workingbuttons import *
from QTGUI import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        self.running = True


    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates
        self.blocks = pygame.sprite.LayeredUpdates
        self.enemies = pygame.sprite.LayeredUpdates
        self.player = Player(self, 1, 2)
    def update(self):
        self.all_sprites.update()
    def main(self):
        while self.playing:
            self.event()
            self.update()
            self.draw()
        self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(fps)
    def event(self):
        x,y = 0
        pos = [x, y]
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, ord('a')]:
                    print("Lewo")
                    pos = [x - speed, y]
                elif event.key in [pygame.K_RIGHT, ord('d')]:
                    print("Prawo")
                    pos = [x + speed, y]
                elif event.key in [pygame.K_UP, ord('w')]:
                    print("Góra")
                    pos = [x, y + speed]
                elif event.key in [pygame.K_DOWN, ord('s')]:
                    print("Dol")
                    pos = [x, y - speed]
                elif event.key in [pygame.K_LEFT, ord('a') and pygame.K_UP, ord('w')]:
                    pos = [x - speed, y + speed]
                    print("lewo gora")
                elif event.key in [pygame.K_RIGHT, ord('d') and pygame.K_UP, ord('w')]:
                    pos = [x + speed, y + speed]
                    print("prawo gora")
                elif event.key in [pygame.K_LEFT, ord('a') and pygame.K_DOWN, ord('s')]:
                    pos = [x - speed, y - speed]
                    print("lewo dol")
                elif event.key in [pygame.K_RIGHT, ord('a') and pygame.K_DOWN, ord('s')]:
                    pos = [x + speed, y - speed]
                    print("Prawo dol")

    def zadawanie_hp(self, attack):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                tower_hp -= attack
                print(f"Zadales {attack} hp")
            elif event.type == pygame.MOUSEBUTTONUP:
                print("Przestales zadawac hp")
    def intro_screen(self):
        pass

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
pygame.quit()
sys.exit()




