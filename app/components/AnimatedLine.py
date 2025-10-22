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
        # Start and target positions
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.end_pos_now = start_pos  # Current endpoint for animation

        self.color = color
        self.width = width

        # Determine horizontal direction of movement
        if self.end_pos_now[0] < self.end_pos[0]:
            self.x_speed = speed
        else:
            self.x_speed = -speed
        
        # Determine vertical direction of movement
        if self.end_pos_now[1] < self.end_pos[1]:
            self.y_speed = speed
        else:
            self.y_speed = -speed


    def draw(self, screen: pygame.Surface):
        # Draw the line from start to current animated endpoint
        pygame.draw.line(screen, self.color, self.start_pos, self.end_pos_now, self.width)


    def update(self):
        # Animate horizontal movement
        if (
            (self.end_pos_now[0] < self.end_pos[0] and self.x_speed > 0) or
            (self.end_pos_now[0] > self.end_pos[0] and self.x_speed < 0)
        ):
            self.end_pos_now = (self.end_pos_now[0] + self.x_speed, self.end_pos_now[1])
        else:
            self.end_pos_now = (self.end_pos[0], self.end_pos_now[1])

        # Animate vertical movement
        if (
            (self.end_pos_now[1] < self.end_pos[1] and self.y_speed > 0) or
            (self.end_pos_now[1] > self.end_pos[1] and self.y_speed < 0)
        ):
            self.end_pos_now = (self.end_pos_now[0], self.end_pos_now[1] + self.y_speed)
        else:
            self.end_pos_now = (self.end_pos_now[0], self.end_pos[1])
