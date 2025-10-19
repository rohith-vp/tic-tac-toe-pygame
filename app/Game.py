import pygame
import sys

from Grid import Grid
from MarkSprite import MarkSprite, X_SPRITE, O_SPRITE
from AnimatedLine import AnimatedLine
from Textbox import Textbox
from PulsingText import PulsingText
from ChangingText import ChangingText
from Scoreboard import Scoreboard

from utils import resource_path


ICON = "assets/tic-tac-toe.png"

TITLE_FONT = "assets/BitcountInk.ttf"
MAIN_TEXT_FONT = "assets/FiraCode-Regular.ttf"
INSTRUCTION_TEXT_FONT = "assets/0xProtoNerdFont-Regular.ttf"

MODE_GAME_SELECTION = 0
MODE_GAME_STARTING = 1
MODE_GAME_PLAYING = 2
MODE_GAME_ENDED = 3


class Game:
    def __init__(self, size, caption, fps):
        # Initialize pygame, set window caption and icon
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(caption)
        pygame.display.set_icon(
            pygame.image.load(resource_path(ICON))
        )

        self.size = size

        self.title = Textbox(
            center=(size[0]/2, size[1]/8),
            size=56,
            font_path=TITLE_FONT,
            text=caption
        )

        self.main_text = PulsingText(
            center=(size[0]/2, size[1]/2),
            min_size=48,
            max_size=62,
            font_path=MAIN_TEXT_FONT,
            text="▶ Start"
        )

        self.instruction_text = Textbox(
            center=(size[0]/2, size[1]/1.1),
            size=24,
            font_path=INSTRUCTION_TEXT_FONT,
            text=""
        )

        # Intialize screen and clock for fps
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = fps

        # Create variables for grid and striking line
        self.grid = None
        self.line = None

        # Create variable for scoreboard
        self.scoreboard = None
        
        # Initialize game variables
        self.mode = MODE_GAME_STARTING
        self.running = False


    def start_game(self):
        # Board for storing X and O
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        # Initialize grid
        self.grid = Grid((self.size[0]/2, self.size[1]/2))

        # Sprite group for storing X and O marks
        self.mark_sprites = pygame.sprite.Group()

        # Set marks for both players
        self.player_1 = "X"
        self.player_2 = "O"
        self.current_player = self.player_1
        self.next_player = self.player_2

        # Animated line for marking victory
        self.line = None

        # Set title
        self.title = ChangingText(
            center=(self.size[0]/2, self.size[1]/8),
            size=56,
            font_path=TITLE_FONT,
            text_list=(
                f"{self.current_player} is playing.",
                f"{self.current_player} is playing..",
                f"{self.current_player} is playing..."
            )
        )

        # Initialize scoreboard
        self.scoreboard = Scoreboard(
            (self.size[0] / 2, self.size[1] - 100),
            (500, 100)
        )

        # Set game mode
        self.mode = MODE_GAME_PLAYING
    

    def update_mark_sprites(self):
        for x in range(0, 3):
            for y in range(0, 3):
                if self.board[y][x] == "X":
                    pos = self.grid.get_cell_center((x, y))
                    self.mark_sprites.add(MarkSprite(pos, X_SPRITE))
                elif self.board[y][x] == "O":
                    pos = self.grid.get_cell_center((x, y))
                    self.mark_sprites.add(MarkSprite(pos, O_SPRITE))


    def make_move(self, cell):
        cell_x, cell_y = cell
        
        if self.board[cell_y][cell_x] == "":
            self.board[cell_y][cell_x] = self.current_player
            self.current_player, self.next_player = self.next_player, self.current_player

            self.title = ChangingText(
                center=(self.size[0]/2, self.size[1]/8),
                size=56,
                font_path=TITLE_FONT,
                text_list=(
                    f"{self.current_player} is playing.",
                    f"{self.current_player} is playing..",
                    f"{self.current_player} is playing..."
                )
            )


    def check_winner(self):
        # Rows
        for y in range(0, 3):
            if self.board[y][0] == self.board[y][1] == self.board[y][2] != "":
                self.line = AnimatedLine(
                    self.grid.get_cell_center((0, y)),
                    self.grid.get_cell_center((2, y))
                )
                return self.board[y][0]
            
        # Columns
        for x in range(0, 3):
            if self.board[0][x] == self.board[1][x] == self.board[2][x] != "":
                self.line = AnimatedLine(
                    self.grid.get_cell_center((x, 0)),
                    self.grid.get_cell_center((x, 2))
                )
                return self.board[0][x]
            
        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.line = AnimatedLine(
                self.grid.get_cell_center((0, 0)),
                self.grid.get_cell_center((2, 2))
            )
            return self.board[2][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.line = AnimatedLine(
                self.grid.get_cell_center((0, 2)),
                self.grid.get_cell_center((2, 0))
            )
            return self.board[0][2]
        
        # Draw
        for y in range(0, 3):
            for x in range(0, 3):
                if self.board[y][x] == "":
                    return ""
            
        return "TIE"


    def mouse_clicked(self, pos):
        if self.mode == MODE_GAME_STARTING:
            if self.main_text.check_click(pos):
                self.start_game()

        elif self.mode == MODE_GAME_PLAYING:
            cell = self.grid.cell_clicked(pos)

            if cell is not None and self.mode == MODE_GAME_PLAYING:
                print("Cell clicked:", cell)
                self.make_move(cell)
                self.update_mark_sprites()
                winner = self.check_winner()

                if winner == "TIE":
                    
                    self.title = PulsingText(
                        center=(self.size[0]/2, self.size[1]/8),
                        min_size=48,
                        max_size=56,
                        font_path=TITLE_FONT,
                        text=f"Its a TIE!"
                    )

                elif winner != "":
                    
                    self.mode = MODE_GAME_ENDED
                    
                    self.title = PulsingText(
                        center=(self.size[0]/2, self.size[1]/8),
                        min_size=48,
                        max_size=56,
                        font_path=TITLE_FONT,
                        text=f"{self.next_player} wins!"
                    )


    def render(self):
        self.screen.fill((0, 0, 0))
        self.title.draw(self.screen)
        self.instruction_text.draw(self.screen)

        if self.mode == MODE_GAME_STARTING:

            self.main_text.update()
            self.main_text.draw(self.screen)

        elif self.mode in (MODE_GAME_PLAYING, MODE_GAME_ENDED):

            self.grid.draw(self.screen)
            self.mark_sprites.draw(self.screen)

            if self.line is not None:
                self.line.draw(self.screen)

            # Draw scoreboard
            self.scoreboard.draw(self.screen)

        pygame.display.flip()


    def loop(self):
        mouse_pos = pygame.mouse.get_pos()

        if (
            (self.mode == MODE_GAME_STARTING and self.main_text.check_click(mouse_pos)) or
            (self.mode == MODE_GAME_PLAYING and self.grid.cell_clicked(mouse_pos))
            ):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                print("Mouse clicked: ", mouse_pos)
                self.mouse_clicked(mouse_pos)

        if self.line is not None:
            self.line.update()

        self.title.update()

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
        