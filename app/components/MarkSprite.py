import pygame
from utils import resource_path


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

        # Basic sprite info
        self.pos = pos
        self.size = size
        self.type = type

        # Pick correct image file based on mark type
        if type == X_SPRITE:
            file_name = "X.png"
        elif type == O_SPRITE:
            file_name = "O.png"

        # Load and resize image
        self.image = pygame.image.load(resource_path(f"assets/{file_name}"))
        self.image = pygame.transform.scale(self.image, size)

        # Center the sprite at the given position
        self.rect = self.image.get_rect()
        self.rect.center = pos
