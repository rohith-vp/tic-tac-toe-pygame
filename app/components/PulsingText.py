import pygame
from components.Textbox import Textbox


class PulsingText(Textbox):
    def __init__(
            self,
            center,
            min_size: int,
            max_size: int,
            font_path: str,
            color=(255, 255, 255),
            text: str="",
            speed=0.5,
        ):
        super().__init__(center, min_size, font_path, color, text)
        self.min_size = min_size
        self.max_size = max_size
        self.size = min_size
        self._size = min_size
        self.speed = speed
        self.animation = 1

    
    def update(self):
        if self.animation == 1:
            if self._size < self.max_size:
                self._size += self.speed
            else:
                self.animation = -1
        elif self.animation == -1:
            if self._size > self.min_size:
                self._size -= self.speed
            else:
                self.animation = 1
        
        self.size = int(self._size)
        self.set_text(self.text)