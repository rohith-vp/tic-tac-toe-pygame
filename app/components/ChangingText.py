import pygame
from components.Textbox import Textbox


class ChangingText(Textbox):
    def __init__(
            self,
            center,
            size: int,
            font_path: str,
            text_list: tuple[str],
            speed: int = 30,
            fix_left: bool = True,
            color=(255, 255, 255)
    ):
        # Initialize base Textbox with the first text
        super().__init__(center, size, font_path, color, text_list[0])

        # List of texts to cycle through
        self.text_list = text_list
        self.text_current = 0  # Index of current text

        self.speed = speed      # Frames per text change
        self.counter = 0        # Frame counter
        self.fix_left = fix_left  # Keep left-alignment if True
        self.x = None

        self.update()           # Initialize first text
        self.x = self.rect.x    # Save x position for alignment if needed


    def update(self):
        # Increment frame counter
        self.counter += 1

        if self.counter >= self.speed:
            self.counter = 0
            # Move to the next text in the list
            self.text_current += 1

            # Loop back to the start if end of list is reached
            if self.text_current >= len(self.text_list):
                self.text_current = 0

            # Update the displayed text
            self.set_text(self.text_list[self.text_current])

            # Maintain left alignment if fix_left is True
            if self.fix_left and self.x is not None:
                self.rect.x = self.x
