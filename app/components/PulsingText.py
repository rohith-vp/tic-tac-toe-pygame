import pygame
from components.Textbox import Textbox


class PulsingText(Textbox):
    def __init__(
            self,
            center,
            min_size: int,
            max_size: int,
            font_path: str,
            color: pygame.Color=(255, 255, 255),
            text: str="",
            speed=0.5,
    ):
        # Initialize base Textbox with minimum size
        super().__init__(center, min_size, font_path, color, text)

        # Minimum and maximum font size for pulsing
        self.min_size = min_size
        self.max_size = max_size

        # Current size (float for smooth animation) and displayed size
        self.size = min_size
        self._size = min_size

        # Speed of size change per frame
        self.speed = speed

        # Animation direction: 1 = growing, -1 = shrinking
        self.animation = 1


    def update(self):
        # Adjust size based on current animation direction
        if self.animation == 1:
            if self._size < self.max_size:
                self._size += self.speed
            else:
                # Reverse direction when reaching max size
                self.animation = -1
        elif self.animation == -1:
            if self._size > self.min_size:
                self._size -= self.speed
            else:
                # Reverse direction when reaching min size
                self.animation = 1

        # Update displayed size and refresh text rendering
        self.size = int(self._size)
        self.set_text(self.text)
