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
        # Basic setup for pygame window and resources
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(caption)
        pygame.display.set_icon(
            pygame.image.load(resource_path(ICON))
        )

        # Create display surface and frame rate control
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = fps

        # Start with the main menu view
        self.view = MenuView(
            self.screen, caption, TITLE_FONT, MAIN_TEXT_FONT, INSTRUCTION_TEXT_FONT
        )


    def render(self):
        # Clear the screen and draw the current view
        self.screen.fill((0, 0, 0))
        self.view.draw()
        pygame.display.flip()


    def loop(self):
        # Main per-frame event handling and updating
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            # Pass all events to the active view
            self.view.handle_events(events)

        # Update current view logic and transition if needed
        self.view.update()
        self.view = self.view.get_new_view()

        self.render()
        self.clock.tick(self.fps)


    def start_loop(self):
        # Run the main game loop until closed
        self.running = True
        while self.running:
            self.loop()
        self.quit_game()


    def quit_game(self):
        # Cleanly shut down the game
        pygame.quit()
        sys.exit()
