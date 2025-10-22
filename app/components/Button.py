import pygame
from utils import resource_path


class Button:
    def __init__(
        self,
        label: str,
        font_path: str,
        font_size: float,
        font_color: pygame.Color,
        center: tuple[float, float],
        btn_size: tuple[float, float],
        bg_color: pygame.Color,
        border_color: pygame.Color,
        border_width: float,
        border_radius: float
    ):
        # Button properties
        self.label = label
        self.center = center
        self.btn_size = btn_size
        self.bg_color = bg_color
        self.border_color = border_color
        self.border_width = border_width
        self.border_radius = border_radius

        # Rectangle for button area and collision detection
        self.rect = pygame.Rect(0, 0, btn_size[0], btn_size[1])
        self.rect.center = center

        # Font and rendered label
        self.font = pygame.font.Font(resource_path(font_path), font_size)
        self.label_surface = self.font.render(label, True, font_color)    
        self.label_rect = self.label_surface.get_rect(center=center)


    def check_click(self, mouse_pos: tuple[float, float]):
        # Return True if the mouse click is within the button
        return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])


    def draw(self, screen: pygame.Surface):
        # Draw button border (rounded rectangle)
        pygame.draw.rect(
            surface=screen,
            rect=self.rect,
            color=self.border_color,
            width=self.border_width,
            border_radius=self.border_radius
        )

        # Draw the button text
        screen.blit(self.label_surface, self.label_rect)
