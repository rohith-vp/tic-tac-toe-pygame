import pygame

from utils import resource_path


class Scoreboard:
    def __init__(
            self,
            center,
            size,
            color=(255, 255, 255),
            border_width=3,
            border_radius=20
    ):
        self.center = center
        self.size = size
        self.color = color
        self.border_width = border_width
        self.border_radius = border_radius

        self.rect = pygame.Rect(0, 0, size[0], size[1])
        self.rect.center = center

        font = pygame.font.Font(resource_path("assets/0xProtoNerdFont-Regular.ttf"), 32)

        self.title_surface = font.render("Score", True, color)
        self.title_rect = self.title_surface.get_rect(center=((center[0] - size[0] / 4), center[1]))

        self.x_label_surface = font.render("X", True, color)
        self.x_label_rect = self.x_label_surface.get_rect(
            center=((center[0] + size[0] / 8), (center[1] - size[1] / 4)))

        self.o_label_surface = font.render("O", True, color)
        self.o_label_rect = self.o_label_surface.get_rect(
            center=((center[0] + size[0] / 2.7), (center[1] - size[1] / 4)))


    def draw(self, screen: pygame.Surface):
        # Draw rounded rectange
        pygame.draw.rect(
            surface=screen,
            rect=self.rect,
            color=self.color,
            width=self.border_width,
            border_radius=self.border_radius
        )

        # Draw vertical line at the center of the rectangle
        pygame.draw.line(
            surface=screen,
            start_pos=(self.center[0], (self.center[1] - self.size[1] / 2)),
            end_pos=(self.center[0], (self.center[1] + self.size[1] / 2)),
            width=self.border_width,
            color=self.color
        )

        # Draw vertical line at the center of the 2nd half of the rectangle
        pygame.draw.line(
            surface=screen,
            start_pos=((self.center[0] + self.size[0] / 4), (self.center[1] - self.size[1] / 2)),
            end_pos=((self.center[0] + self.size[0] / 4), (self.center[1] + self.size[1] / 2)),
            width=self.border_width,
            color=self.color
        )

        # Draw horizontal line at the center on the 2nd half of the rectangle
        pygame.draw.line(
            surface=screen,
            start_pos=self.center,
            end_pos=((self.center[0] + self.size[0] / 2), self.center[1]),
            width=self.border_width,
            color=self.color
        )

        # Draw "score" text
        screen.blit(self.title_surface, self.title_rect)
        # Draw "X" label
        screen.blit(self.x_label_surface, self.x_label_rect)
        # Draw "O" label
        screen.blit(self.o_label_surface, self.o_label_rect)
