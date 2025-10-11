import pygame
import os
import sys

from Grid import Grid
from MarkSprite import MarkSprite, X_SPRITE, O_SPRITE
from AnimatedLine import AnimatedLine


class Game:
    def __init__(self, size, caption, fps):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(caption)
        pygame.display.set_icon(
            pygame.image.load(os.path.join("assets", "tic-tac-toe.png"))
        )

        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.title_font = pygame.font.Font(os.path.join("assets", "BitcountInk.ttf"), 56)
        self.title_text = self.title_font.render(caption, True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(
            center=(
                self.screen.get_width() / 2, 
                self.screen.get_height() / 8
            )
        )

        self.marks = {}

        for x in range(0, 3):
            for y in range(0, 3):
                self.marks[(x, y)] = None
        
        self.load_sprites()

        self.line = AnimatedLine(
            self.grid.get_cell_topleft((0, 0)),
            self.grid.get_cell_bottomright((2, 2))
        )

        self.running = False


    def load_sprites(self):
        self.grid = Grid()
        self.mark_sprites = pygame.sprite.Group()

    
    def update_mark_sprites(self):
        self.mark_sprites.empty()

        for cell in self.marks.keys():
            if self.marks[cell] is not None:
                pos = self.grid.get_cell_center(cell)
                self.mark_sprites.add(
                    MarkSprite(pos, self.marks[cell])
                )


    def mouse_clicked(self, pos):
        cell = self.grid.cell_clicked(pos)

        if cell is not None:
            print("Cell clicked: ", cell)
            self.marks[cell] = O_SPRITE
            self.update_mark_sprites()


    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_text, self.title_rect)
        self.grid.draw(self.screen)
        self.mark_sprites.draw(self.screen)
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
        