import pygame
from utils import resource_path


class Textbox:
    def __init__(
            self,
            center,
            size: int,
            font_path: str,
            color=(255, 255, 255),
            text: str=""
    ):
        self.center = center
        self.size = size
        self.font_path = font_path
        self.color = color
        self.set_text(text)


    def set_text(self, text: str):
        self.text = text
        self.font = pygame.font.Font(resource_path(self.font_path), self.size)
        self.surface = self.font.render(text, True, self.color)
        self.rect = self.surface.get_rect(center=self.center)


    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self.surface, self.rect)


    def check_click(self, mouse_pos) -> bool:
        return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])


    def update(self):
        pass