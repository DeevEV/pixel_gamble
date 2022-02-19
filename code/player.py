import pygame
from data import *


#  КЛАСС ОТВЕЧАЕТ ЗА ОТРИСОВКУ ИГРОКА В ВЫБРАННОЙ ПОЗИЦИИ
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obs_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("../data/textures/player/player.png")  # ЗАГРУЗКА
        self.rect = self.image.get_rect(topleft=pos)  # ОТРИСОВКА
        self.hitbox = self.rect.inflate(0, -26)  # РАЗМЕР ХИТБОКСА

        self.point = pygame.math.Vector2()  # ПОЗИЦИЯ ИГРОКА
        self.obs_sprites = obs_sprites
        self.speed = 5

    def wasd(self):
        keyboard = pygame.key.get_pressed()

        # ПЕРМЕЩЕНИЕ Y
        if keyboard[pygame.K_w]:
            self.point.y = -1
        elif keyboard[pygame.K_s]:
            self.point.y = 1
        else:
            self.point.y = 0

        # ПЕРМЕЩЕНИЕ X
        if keyboard[pygame.K_a]:
            self.point.x = -1
        elif keyboard[pygame.K_d]:
            self.point.x = 1
        else:
            self.point.x = 0

    def move(self, speed):  # СКОРОСТЬ ПЕРЕДВЕЖЕНИЯ
        if self.point.magnitude() != 0:
            self.point = self.point.normalize()  # ФИКС СКОРОСТИ ПО ДИАГОНАЛИ

        self.hitbox.x += self.point.x * speed
        self.barrier(True)
        self.hitbox.y += self.point.y * speed
        self.barrier(False)

        self.rect.center = self.hitbox.center

    def barrier(self, point):
        if point:
            for sprite in self.obs_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # СТОЛКНОВЕНИЕ ПО ГОРИЗОНТУ
                    if self.point.x > 0:  # влево
                        self.hitbox.right = sprite.hitbox.left
                    if self.point.x < 0:  # вправо
                        self.hitbox.left = sprite.hitbox.right
        else:
            for sprite in self.obs_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # СТОЛКНОВЕНИЕ ПО ВЕРТИКАЛИ
                    if self.point.y > 0:  # вниз
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.point.y < 0:  # вверх
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.wasd()
        self.move(self.speed)
