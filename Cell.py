import pygame

class Cell:

    def __init__(self, pos_x, pos_y, size):
        self.rect = pygame.Rect(pos_x, pos_y, size, size)
        self.is_wall = False
        self.is_goal = False
        self.is_start = False
        self.is_discovered = False
        self.is_visited = False
        self.is_path = False

    def toggle_wall(self):
        if self.is_goal or self.is_start:
            return
        self.is_wall = not self.is_wall

    def draw(self, screen):
        if self.is_wall:
            pygame.draw.rect(screen, (80, 80, 80), self.rect)
        elif self.is_path:
            pygame.draw.rect(screen, (100, 100, 255), self.rect)
        elif self.is_goal:
            pygame.draw.rect(screen, (0, 0, 255), self.rect)
        elif self.is_start:
            pygame.draw.rect(screen, (0, 255, 0), self.rect)
        elif self.is_visited:
            pygame.draw.rect(screen, (150, 0, 0), self.rect)
        elif self.is_discovered:
            pygame.draw.rect(screen, (50, 150, 50), self.rect)
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)