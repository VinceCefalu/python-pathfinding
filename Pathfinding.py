import sys
import pygame

from bfs import BFS

# General setup
pygame.init()
clock = pygame.time.Clock()
RUNNING = False

# Set up main window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pathfinding')

# Add pathfinding classes
bfs = BFS(SCREEN_WIDTH, SCREEN_HEIGHT)

while True:
    # handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not RUNNING:
                pos = pygame.mouse.get_pos()
                clicked_cells = []
                for row in bfs.cells:
                    for c in row:
                        if c.rect.collidepoint(pos):
                            clicked_cells.append(c)
                for c in clicked_cells:
                    c.toggle_wall()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                RUNNING = True

    screen.fill((255, 255, 255))

    if RUNNING:
        path = bfs.step()
        if path is not None:
            break

    bfs.draw(screen)
    pygame.display.flip()
    clock.tick(60)

for cell in path:
    cell.is_path = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    bfs.draw(screen)
    pygame.display.flip()
    clock.tick(60)
