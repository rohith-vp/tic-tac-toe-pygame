from typing import List
import pygame


class View:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.new_view = self

    def handle_events(self, events: List[pygame.event.Event]):
        pass

    def get_new_view(self):
        return self.new_view

    def update(self):
        pass

    def draw(self):
        pass