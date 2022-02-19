import pygame


class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()  # ПОЛУЧЕНИЕ ЭКРАНА
        self.w_half = self.screen.get_size()[0] // 2  # ПОЛОВИНА ШИРИНЫ
        self.h_half = self.screen.get_size()[1] // 2  # ПОЛОВИНА ВЫСОТЫ
        self.atone = pygame.math.Vector2()  # ПОЗИЦИЯ КАМЕРЫ

    def picture(self, player):
        # ПОЛУЧЕНИЕ ПОЗИЦИИ ИГРОКА
        self.atone.x = player.rect.centerx - self.w_half
        self.atone.y = player.rect.centery - self.h_half

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            atone_pos = sprite.rect.topleft - self.atone
            self.screen.blit(sprite.image, atone_pos)  # ОТРИСОВКА
