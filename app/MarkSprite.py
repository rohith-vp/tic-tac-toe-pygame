import pygame
import os


X_SPRITE = 0
O_SPRITE = 1


class MarkSprite(pygame.sprite.Sprite):
    def __init__(
            self,
            pos,
            type,
            size=(100, 100)
                ):
        super().__init__()

        self.pos = pos
        self.size = size
        self.type = type

        if type == X_SPRITE:
            file_name = "X.png"
        elif type == O_SPRITE:
            file_name = "O.png"

        self.image = pygame.image.load(os.path.join("assets", file_name))
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = pos
