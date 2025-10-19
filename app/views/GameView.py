from typing import List
import pygame

from views.View import View

from components.Grid import Grid
from components.ChangingText import ChangingText
from components.PulsingText import PulsingText
from components.AnimatedLine import AnimatedLine
from components.Scoreboard import Scoreboard
from components.MarkSprite import MarkSprite, X_SPRITE, O_SPRITE



class GameView(View):
    def __init__(
            self,
            screen: pygame.Surface,
            title_font_path: str
    ):
        super().__init__(screen)

        self.size = screen.get_size()
        self.title_font_path = title_font_path

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
            font_path=title_font_path,
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
                font_path=self.title_font_path,
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


    def mouse_clicked(self, pos: tuple[float, float]):
        cell = self.grid.cell_clicked(pos)

        if cell is not None:
                print("Cell clicked:", cell)
                self.make_move(cell)
                self.update_mark_sprites()
                winner = self.check_winner()

                if winner == "TIE":
                    
                    self.title = PulsingText(
                        center=(self.size[0]/2, self.size[1]/8),
                        min_size=48,
                        max_size=56,
                        font_path=self.title_font_path,
                        text=f"Its a TIE!"
                    )

                elif winner != "":
                    
                    # self.mode = MODE_GAME_ENDED
                    
                    self.title = PulsingText(
                        center=(self.size[0]/2, self.size[1]/8),
                        min_size=48,
                        max_size=56,
                        font_path=self.title_font_path,
                        text=f"{self.next_player} wins!"
                    )

                    self.scoreboard.increment_score(winner)


    def handle_events(self, events: List[pygame.event.Event]):
        super().handle_events(events)

        for event in events:
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mouse_pos = pygame.mouse.get_pos()
                print("Mouse clicked: ", mouse_pos)
                self.mouse_clicked(mouse_pos) 


    def update(self):
        super().update()

        mouse_pos = pygame.mouse.get_pos()

        if self.grid.cell_clicked(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

        if self.line is not None:
            self.line.update()

        self.title.update()    


    def draw(self):
        super().draw()

        # Draw title
        self.title.draw(self.screen)

        # Draw grid and mark sprites
        self.grid.draw(self.screen)
        self.mark_sprites.draw(self.screen)

        # Draw the striking line if it exists
        if self.line is not None:
            self.line.draw(self.screen)

        # Draw scoreboard
        self.scoreboard.draw(self.screen)
