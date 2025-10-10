import pygame


class GridSprite(pygame.sprite.Sprite):
    def __init__(
            self,
            pos=(500, 400),
            size=400,
            color=(255, 255, 255),
            width=2
                 ):
        
        super().__init__()
        self.pos = pos
        self.size = size
        self.color = color
        self.width = width
        self.cell_size = self.size / 3

        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)

        self.draw_grid()

    
    def draw_grid(self):
        # Horizontal lines
        for i in range(1, 3):
            y = i * self.cell_size
            pygame.draw.line(self.image, self.color, (0, y), (self.size, y), self.width)

        # Vertical lines
        for i in range(1, 3):
            x = i * self.cell_size
            pygame.draw.line(self.image, self.color, (x, 0), (x, self.size), self.width)


    def cell_clicked(self, mouse_pos):
        # Check if mouse is outside the grid
        if not self.rect.collidepoint(mouse_pos):
            return None
        
        # Convert absolute mouse position to relative mouse position
        rel_x = mouse_pos[0] - self.rect.x
        rel_y = mouse_pos[1] - self.rect.y

        col = int(rel_x // self.cell_size)
        row = int(rel_y // self.cell_size)

        if (0 <= row < 3) and (0 <= col < 3):
            return (col, row)
        
        return None