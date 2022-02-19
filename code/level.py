import pygame
from tile import Tile
from player import Player
from camera import Camera

from data import *


#  КЛАСС ОТВЕЧАЕТ ЗА ОТРИСОВКУ И ОБНОВЛЕНИЕ УРОВНЯ
class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()  # ПОЛУЧЕНИЕ ЭКРАНА

        # СПРАЙТЫ
        self.vis_sprites = Camera()  # ВИДИМЫЕ
        self.obs_sprites = pygame.sprite.Group()  # ОБСТРАКТНЫЕ

        self.load_map()

    def load_map(self):  # ЗАГРУЗКА СОХРАНЁННОЙ КАРТЫ
        for i, row in enumerate(WORLD_MAP):
            for j, col in enumerate(row):
                x, y = j * TILESIZE, i * TILESIZE

                if col == "x":
                    Tile((x, y), [self.vis_sprites, self.obs_sprites])  # ОТРИСОВКА СПРАЙТА КАРТЫ
                if col == "p":
                    self.player = Player((x, y), [self.vis_sprites], self.obs_sprites)  # ОТРИСОВКА СПРАЙТА ИГРОКА

    def run(self):  # ОТРИСОВКА И ОБНОВЛЕНИЕ СПРАЙТОВ
        self.vis_sprites.picture(self.player)
        self.vis_sprites.update()
