import pygame
import sys

from views.MenuView import MenuView

from utils import resource_path


ICON = "assets/tic-tac-toe.png"

TITLE_FONT = "assets/BitcountInk.ttf"
MAIN_TEXT_FONT = "assets/FiraCode-Regular.ttf"
INSTRUCTION_TEXT_FONT = "assets/0xProtoNerdFont-Regular.ttf"


class Game:
    def __init__(self, size, caption, fps):
        # Initialize pygame, set window caption and icon
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(caption)
        pygame.display.set_icon(
            pygame.image.load(resource_path(ICON))
        )

        # Intialize screen and clock for fps
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = fps

        # Initialize menu view
        self.view = None
        self.view = MenuView(
            self.screen, caption, TITLE_FONT, MAIN_TEXT_FONT, INSTRUCTION_TEXT_FONT
        )

        # Initialize game variables
        self.running = False


    def render(self):
        self.screen.fill((0, 0, 0))
        self.view.draw()
        pygame.display.flip()


    def loop(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            self.view.handle_events(events)

        self.view.update()
        self.view = self.view.get_new_view()

        self.render()
        self.clock.tick(self.fps)


    def start_loop(self):
        self.running = True
        while self.running:
            self.loop()
        self.quit_game()

    
    def quit_game(self):
        pygame.quit()
        sys.exit()
        