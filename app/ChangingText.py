import pygame
from Textbox import Textbox


class ChangingText(Textbox):
    def __init__(
            self,
            center,
            size: int,
            font_path: str,
            text_list: tuple[str],
            speed: int=30,
            fix_left: bool=True,
            color=(255, 255, 255)
    ):
        super().__init__(center, size, font_path, color, text_list[0])
        self.text_list = text_list
        self.text_current = 0
        self.speed = speed
        self.counter = 0
        self.fix_left = fix_left
        self.x = None
        self.update()
        self.x = self.rect.x

    
    def update(self):
        self.counter += 1

        if self.counter >= self.speed:
            self.counter = 0
            self.text_current += 1

            if self.text_current >= len(self.text_list):
                self.text_current = 0

            self.set_text(self.text_list[self.text_current])

            if self.fix_left and self.x is not None:
                self.rect.x = self.x
