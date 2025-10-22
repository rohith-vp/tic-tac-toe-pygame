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
        # Position and size of the scoreboard
        self.center = center
        self.size = size
        self.color = color
        self.border_width = border_width
        self.border_radius = border_radius

        # Rectangle representing the scoreboard
        self.rect = pygame.Rect(0, 0, size[0], size[1])
        self.rect.center = center

        # Font for text
        self.font = pygame.font.Font(resource_path("assets/0xProtoNerdFont-Regular.ttf"), 32)

        # "Score" title
        self.title_surface = self.font.render("Score", True, color)
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.center = (center[0] - size[0] / 4, center[1])

        # Labels for X and O
        self.x_label_surface = self.font.render("X", True, color)
        self.x_label_rect = self.x_label_surface.get_rect()
        self.x_label_rect.center = (center[0] + size[0] / 8, center[1] - size[1] / 4)

        self.o_label_surface = self.font.render("O", True, color)
        self.o_label_rect = self.o_label_surface.get_rect()
        self.o_label_rect.center = (center[0] + size[0] / 2.7, center[1] - size[1] / 4)

        # Positions to render the actual scores
        self.x_score_pos = (center[0] + size[0] / 8, center[1] + size[1] / 4)
        self.o_score_pos = (center[0] + size[0] / 2.7, center[1] + size[1] / 4)

        # Initialize scores
        self.x_score = 0
        self.o_score = 0
        self.update_score_text()


    def update_score_text(self):
        # Render score text surfaces for X and O
        self.x_score_surface = self.font.render(str(self.x_score), True, self.color)
        self.x_score_rect = self.x_score_surface.get_rect(center=self.x_score_pos)

        self.o_score_surface = self.font.render(str(self.o_score), True, self.color)
        self.o_score_rect = self.o_score_surface.get_rect(center=self.o_score_pos)


    def draw(self, screen: pygame.Surface):
        # Draw the main scoreboard rectangle
        pygame.draw.rect(
            surface=screen,
            rect=self.rect,
            color=self.color,
            width=self.border_width,
            border_radius=self.border_radius
        )

        # Draw dividing lines for layout
        pygame.draw.line(
            surface=screen,
            start_pos=(self.center[0], self.center[1] - self.size[1] / 2),
            end_pos=(self.center[0], self.center[1] + self.size[1] / 2),
            width=self.border_width,
            color=self.color
        )

        pygame.draw.line(
            surface=screen,
            start_pos=(self.center[0] + self.size[0] / 4, self.center[1] - self.size[1] / 2),
            end_pos=(self.center[0] + self.size[0] / 4, self.center[1] + self.size[1] / 2),
            width=self.border_width,
            color=self.color
        )

        pygame.draw.line(
            surface=screen,
            start_pos=self.center,
            end_pos=(self.center[0] + self.size[0] / 2, self.center[1]),
            width=self.border_width,
            color=self.color
        )

        # Draw all text: title, labels, and scores
        screen.blit(self.title_surface, self.title_rect)
        screen.blit(self.x_label_surface, self.x_label_rect)
        screen.blit(self.o_label_surface, self.o_label_rect)
        screen.blit(self.x_score_surface, self.x_score_rect)
        screen.blit(self.o_score_surface, self.o_score_rect)


    def increment_score(self, player, i=1):
        # Increase score for given player and update text
        if player == "X":
            self.x_score += i
        elif player == "O":
            self.o_score += i

        self.update_score_text()
