import pygame
from data import *


#  КЛАСС ОТВЕЧАЕТ ЗА ОТРИСОВКУ ОДНОГО СПРАЙТА КАРТЫ В ВЫБРАННОЙ ПОЗИЦИИ
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../data/textures/earth/rock.png").convert_alpha()  # ЗАГРУЗКА
        self.rect = self.image.get_rect(topleft=pos)  # ОТРИСОВКА
        self.hitbox = self.rect.inflate(0, -10)  # РАЗМЕР ХИТБОКСА
