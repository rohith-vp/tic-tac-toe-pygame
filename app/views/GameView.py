from typing import List
import pygame

from views.View import View
from components.Grid import Grid
from components.ChangingText import ChangingText
from components.PulsingText import PulsingText
from components.AnimatedLine import AnimatedLine
from components.Scoreboard import Scoreboard
from components.MarkSprite import MarkSprite, X_SPRITE, O_SPRITE
from components.Button import Button


class GameView(View):
    def __init__(
            self,
            screen: pygame.Surface,
            title_font_path: str,
            main_font_path: str
    ):
        super().__init__(screen)

        self.title_font_path = title_font_path
        self.size = screen.get_size()

        # Create a centered 3x3 grid
        self.grid = Grid((self.size[0] / 2, self.size[1] / 2.5))

        # Sprite group to manage all placed marks (X/O)
        self.mark_sprites = pygame.sprite.Group()

        # Define players
        self.player_1 = "X"
        self.player_2 = "O"

        self.new_game()

        # Scoreboard displayed at the bottom
        self.scoreboard = Scoreboard(
            (self.size[0] / 2, self.size[1] - 100),
            (300, 100)
        )

        # Reset button positioned below the grid
        self.reset_btn = Button(
            "⟳ Reset",
            main_font_path,
            24,
            (255, 255, 255),
            (self.size[0] / 2, self.size[1] / 1.35),
            (150, 50),
            (0, 0, 0),
            (255, 255, 255),
            3,
            10
        )


    def new_game(self):
        # Reset board and player turns
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.current_player = self.player_1
        self.next_player = self.player_2

        # Clear marks and any winning line
        self.line = None
        self.mark_sprites.empty()

        # Title text showing current player's turn
        self.title = ChangingText(
            center=(self.size[0] / 2, self.size[1] / 12),
            size=56,
            font_path=self.title_font_path,
            text_list=(
                f"{self.current_player} is playing.",
                f"{self.current_player} is playing..",
                f"{self.current_player} is playing..."
            )
        )


    def update_mark_sprites(self):
        # Sync visual sprites with board data
        for x in range(3):
            for y in range(3):
                if self.board[y][x] == "X":
                    pos = self.grid.get_cell_center((x, y))
                    self.mark_sprites.add(MarkSprite(pos, X_SPRITE))
                elif self.board[y][x] == "O":
                    pos = self.grid.get_cell_center((x, y))
                    self.mark_sprites.add(MarkSprite(pos, O_SPRITE))


    def make_move(self, cell):
        # Place a mark if cell is empty, then swap turns
        cell_x, cell_y = cell
        if self.board[cell_y][cell_x] == "":
            self.board[cell_y][cell_x] = self.current_player
            self.current_player, self.next_player = self.next_player, self.current_player

            # Update title for new player's turn
            self.title = ChangingText(
                center=(self.size[0] / 2, self.size[1] / 12),
                size=56,
                font_path=self.title_font_path,
                text_list=(
                    f"{self.current_player} is playing.",
                    f"{self.current_player} is playing..",
                    f"{self.current_player} is playing..."
                )
            )


    def check_winner(self):
        # Check all rows for a winner
        for y in range(3):
            if self.board[y][0] == self.board[y][1] == self.board[y][2] != "":
                self.line = AnimatedLine(
                    self.grid.get_cell_center((0, y)),
                    self.grid.get_cell_center((2, y))
                )
                return self.board[y][0]

        # Check columns
        for x in range(3):
            if self.board[0][x] == self.board[1][x] == self.board[2][x] != "":
                self.line = AnimatedLine(
                    self.grid.get_cell_center((x, 0)),
                    self.grid.get_cell_center((x, 2))
                )
                return self.board[0][x]

        # Check diagonals
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

        # Check for draw (no empty cells left)
        for row in self.board:
            if "" in row:
                return ""
        return "TIE"


    def mouse_clicked(self, pos: tuple[float, float]):
        # Handle clicks on grid cells or the reset button
        cell = self.grid.cell_clicked(pos)

        if cell is not None:
            print("Cell clicked:", cell)
            self.make_move(cell)
            self.update_mark_sprites()
            winner = self.check_winner()

            if winner == "TIE":
                self.title = PulsingText(
                    center=(self.size[0] / 2, self.size[1] / 8),
                    min_size=48,
                    max_size=56,
                    font_path=self.title_font_path,
                    text="Its a TIE!"
                )
            elif winner != "":
                self.title = PulsingText(
                    center=(self.size[0] / 2, self.size[1] / 12),
                    min_size=48,
                    max_size=56,
                    font_path=self.title_font_path,
                    text=f"{self.next_player} wins!"
                )
                self.scoreboard.increment_score(winner)

        elif self.reset_btn.check_click(pos):
            self.new_game()


    def handle_events(self, events: List[pygame.event.Event]):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                print("Mouse clicked:", mouse_pos)
                self.mouse_clicked(mouse_pos)


    def update(self):
        super().update()

        mouse_pos = pygame.mouse.get_pos()

        # Highlight clickable elements with a hand cursor
        if self.grid.cell_clicked(mouse_pos) or self.reset_btn.check_click(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Animate winning line if present
        if self.line is not None:
            self.line.update()

        self.title.update()


    def draw(self):
        super().draw()

        # Draw title
        self.title.draw(self.screen)

        # Draw grid and marks
        self.grid.draw(self.screen)
        self.mark_sprites.draw(self.screen)

        # Draw animated win line if available
        if self.line is not None:
            self.line.draw(self.screen)

        # Draw scoreboard and reset button
        self.scoreboard.draw(self.screen)
        self.reset_btn.draw(self.screen)
