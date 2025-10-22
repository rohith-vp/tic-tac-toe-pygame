from typing import List
import pygame


class View:
    def __init__(self, screen: pygame.Surface):
        # Base view class — stores the main display surface
        self.screen = screen
        # Used for switching between views (e.g., menu → game)
        self.new_view = self

    def handle_events(self, events: List[pygame.event.Event]):
        # To be overridden by subclasses that need event handling
        pass

    def get_new_view(self):
        # Return the next active view (can be self or another view)
        return self.new_view

    def update(self):
        # Placeholder for per-frame logic in derived views
        pass

    def draw(self):
        # Placeholder for rendering logic in derived views
        pass
