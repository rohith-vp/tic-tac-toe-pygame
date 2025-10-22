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
        # Position, font size, font file path, and text color
        self.center = center
        self.size = size
        self.font_path = font_path
        self.color = color

        # Initialize text rendering
        self.set_text(text)


    def set_text(self, text: str):
        # Update the displayed text
        self.text = text

        # Load font and render text surface
        self.font = pygame.font.Font(resource_path(self.font_path), self.size)
        self.surface = self.font.render(text, True, self.color)

        # Rectangle used for drawing and click detection
        self.rect = self.surface.get_rect(center=self.center)


    def draw(self, screen: pygame.surface.Surface):
        # Draw the text surface on the screen
        screen.blit(self.surface, self.rect)


    def check_click(self, mouse_pos) -> bool:
        # Return True if the mouse click is inside the textbox
        return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])


    def update(self):
        # Placeholder for subclasses that animate or update text
        pass
