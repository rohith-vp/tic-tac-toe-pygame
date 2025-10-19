from typing import List
import pygame


class View:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def handle_events(self, events: List[pygame.event.Event]):
        pass

    def get_new_view(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass