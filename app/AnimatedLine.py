import pygame


class AnimatedLine:
    def __init__(
            self,
            start_pos,
            end_pos,
            speed=15,
            color=(255, 50, 50),
            width=10
                ):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.end_pos_now = start_pos
        self.speed = speed
        self.color = color
        self.width = width

    
    def draw(self, screen: pygame.Surface):
        pygame.draw.line(screen, self.color, self.start_pos, self.end_pos_now, self.width)

    
    def update(self):
        if self.end_pos_now[0] < self.end_pos[0]:
            self.end_pos_now = (
                self.end_pos_now[0] + self.speed,
                self.end_pos_now[1]
            )
        else:
            self.end_pos_now = (
                self.end_pos[0],
                self.end_pos_now[1]
            )
        
        if self.end_pos_now[1] < self.end_pos[1]:
            self.end_pos_now = (
                self.end_pos_now[0],
                self.end_pos_now[1] + self.speed
            )
        else:
            self.end_pos_now = (
                self.end_pos_now[0],
                self.end_pos[1]
            )