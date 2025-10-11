import pygame
import os
import sys

from Grid import Grid
from MarkSprite import MarkSprite, X_SPRITE, O_SPRITE
from AnimatedLine import AnimatedLine


MODE_GAME_SELECTION = 0
MODE_GAME_STARTING = 1
MODE_GAME_PLAYING = 2


class Game:
    def __init__(self, size, caption, fps):
        # Initialize pygame, set window caption and icon
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(caption)
        pygame.display.set_icon(
            pygame.image.load(os.path.join("assets", "tic-tac-toe.png"))
        )

        self.size = size
        self.set_title(caption)
        self.set_instruction_text("Click on a box to begin")

        # Intialize screen and clock for fps
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = fps

        # Board for storing X and O
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        
        # Initialize grid
        self.grid = Grid((size[0]/2, size[1]/2))

        # Sprite group for storing X and O marks
        self.mark_sprites = pygame.sprite.Group()

        # Set marks for both players
        self.player_1 = "X"
        self.player_2 = "O"
        self.current_player = self.player_1

        # Animated line for marking victory
        self.line = None

        # Initialize game variables
        self.mode = MODE_GAME_SELECTION
        self.running = False

    
    def set_title(self, title: str):
        title_font = pygame.font.Font(os.path.join("assets", "BitcountInk.ttf"), 56)
        self.title_text = title_font.render(title, True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(
            center=( self.size[0] / 2 , self.size[1] / 8 )
        )


    def set_instruction_text(self, text: str):
        instruction_text_font = pygame.font.Font(os.path.join("assets", "0xProtoNerdFont-Regular.ttf"), 24)
        self.instruction_text = instruction_text_font.render(text, True, (255, 255, 255))
        self.instruction_rect = self.instruction_text.get_rect(
            center=( self.size[0] / 2 , self.size[1] / 1.1 )
        )

    
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

            if self.current_player == self.player_1:
                self.current_player = self.player_2
            else:
                self.current_player = self.player_1


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


    def mouse_clicked(self, pos):
        cell = self.grid.cell_clicked(pos)

        if cell is not None:
            print("Cell clicked: ", cell)
            self.make_move(cell)
            self.update_mark_sprites()
            winner = self.check_winner()
            print("Winner:", winner)


    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_text, self.title_rect)
        self.screen.blit(self.instruction_text, self.instruction_rect)
        self.grid.draw(self.screen)
        self.mark_sprites.draw(self.screen)
        
        if self.line is not None:
            self.line.draw(self.screen)

        pygame.display.flip()


    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                print("Mouse clicked: ", mouse_pos)
                self.mouse_clicked(mouse_pos)

        if self.line is not None:
            self.line.update()

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
        