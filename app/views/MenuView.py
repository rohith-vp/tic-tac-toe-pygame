from typing import List
import pygame

from views.View import View
from views.GameView import GameView

from components.Textbox import Textbox
from components.PulsingText import PulsingText


class MenuView(View):
    def __init__(
            self,
            screen: pygame.Surface,
            caption: str,
            title_font_path: str,
            main_font_path: str,
            instruction_font_path: str
    ):
        super().__init__(screen)

        self.new_view = self
        self.title_font_path = title_font_path
        size = self.screen.get_size()

        self.title = Textbox(
            center=(size[0]/2, size[1]/8),
            size=56,
            font_path=title_font_path,
            text=caption
        )

        self.main_text = PulsingText(
            center=(size[0]/2, size[1]/2),
            min_size=48,
            max_size=62,
            font_path=main_font_path,
            text="▶ Start"
        )

        self.instruction_text = Textbox(
            center=(size[0]/2, size[1]/1.1),
            size=24,
            font_path=instruction_font_path,
            text=""
        )


    def start_game(self):
        self.new_view = GameView(
            self.screen, self.title_font_path
        )


    def handle_events(self, events: List[pygame.event.Event]):
        super().handle_events(events)

        for event in events:
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mouse_pos = pygame.mouse.get_pos()
                print("Mouse clicked: ", mouse_pos)
                self.start_game()


    def get_new_view(self):
        return self.new_view


    def update(self):
        super().update()

        mouse_pos = pygame.mouse.get_pos()

        if self.main_text.check_click(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        self.main_text.update()


    def draw(self):
        super().draw()
        
        self.title.draw(self.screen)
        self.instruction_text.draw(self.screen)
        self.main_text.draw(self.screen)
