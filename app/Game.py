import pygame
import os
import sys

from GridSprite import GridSprite


class Game:
    def __init__(self, size, caption, fps):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)
        
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.title_font = pygame.font.Font(os.path.join("assets", "BitcountInk.ttf"), 56)
        self.title_text = self.title_font.render(caption, True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(
            center=(self.screen.get_width()/2, self.screen.get_height()/8))

        self.grid_sprite = GridSprite()
        self.all_sprites = pygame.sprite.Group(self.grid_sprite)

        self.running = False


    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_text, self.title_rect)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


    def mouse_clicked(self, pos):
        cell = self.grid_sprite.cell_clicked(pos)
        print("Cell clicked: ", cell)

    
    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    print("Mouse clicked: ", mouse_pos)
                    self.mouse_clicked(mouse_pos)

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
        