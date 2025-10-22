import pygame


class Grid:
    def __init__(
            self,
            pos,
            size=400,
            color=(255, 255, 255),
            width=2
    ):
        # Position of the grid center, total size, line color and thickness
        self.pos = pos
        self.size = size
        self.color = color
        self.width = width

        # Each cell is a third of the total grid size
        self.cell_size = self.size / 3

        # Surface to draw grid lines with transparency support
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)

        # Draw initial grid lines
        self.draw_grid()


    def draw_grid(self):
        # Draw horizontal lines
        for i in range(1, 3):
            y = i * self.cell_size
            pygame.draw.line(self.image, self.color, (0, y), (self.size, y), self.width)

        # Draw vertical lines
        for i in range(1, 3):
            x = i * self.cell_size
            pygame.draw.line(self.image, self.color, (x, 0), (x, self.size), self.width)


    def draw(self, screen: pygame.Surface):
        # Render grid onto the main screen
        screen.blit(self.image, self.rect)


    def cell_clicked(self, mouse_pos):
        # Return (col, row) if a cell is clicked, else None
        if not self.rect.collidepoint(mouse_pos):
            return None

        # Convert absolute mouse coordinates to relative grid coordinates
        rel_x = mouse_pos[0] - self.rect.x
        rel_y = mouse_pos[1] - self.rect.y

        col = int(rel_x // self.cell_size)
        row = int(rel_y // self.cell_size)

        if (0 <= row < 3) and (0 <= col < 3):
            return (col, row)

        return None


    # Helper functions to get key positions of a cell
    def get_cell_center(self, cell):
        x_pos = (self.cell_size * (cell[0] + 0.5)) + self.rect.x
        y_pos = (self.cell_size * (cell[1] + 0.5)) + self.rect.y
        return (x_pos, y_pos)


    def get_cell_topleft(self, cell):
        x_pos = (self.cell_size * cell[0]) + self.rect.x
        y_pos = (self.cell_size * cell[1]) + self.rect.y
        return (x_pos, y_pos)


    def get_cell_topright(self, cell):
        x_pos = (self.cell_size * (cell[0] + 1)) + self.rect.x
        y_pos = (self.cell_size * cell[1]) + self.rect.y
        return (x_pos, y_pos)


    def get_cell_bottomleft(self, cell):
        x_pos = (self.cell_size * cell[0]) + self.rect.x
        y_pos = (self.cell_size * (cell[1] + 1)) + self.rect.y
        return (x_pos, y_pos)


    def get_cell_bottomright(self, cell):
        x_pos = (self.cell_size * (cell[0] + 1)) + self.rect.x
        y_pos = (self.cell_size * (cell[1] + 1)) + self.rect.y
        return (x_pos, y_pos)
