import math

from cell import Cell
class BFS:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.cells = []
        self.NUM_CELLS = 25
        self.OFFSET = (SCREEN_WIDTH - SCREEN_HEIGHT) / 2
        self.SIZE = SCREEN_HEIGHT / self.NUM_CELLS
        for i in range(0, self.NUM_CELLS):
            x = []
            for j in range(0, self.NUM_CELLS):
                x.append(Cell(i * math.floor(self.SIZE) + self.OFFSET,
                            j * math.floor(self.SIZE), self.SIZE))
            self.cells.append(x)
        self.cells[10][10].is_start = True
        self.cells[10][10].is_discovered = True
        self.cells[self.NUM_CELLS-1][self.NUM_CELLS-1].is_goal = True

        self.queue = [(self.cells[10][10], [])]
        self.goal = self.cells[self.NUM_CELLS-1][self.NUM_CELLS-1]

    def step(self):
        if len(self.queue) > 0:
            current, path = self.queue.pop(0)
            path.append(current)
            current.is_visited = True
            if current == self.goal:
                return path
            index = self.find_cell_index(current)
            for cell in self.get_adjacent_cells(index[0], index[1]):
                cell.is_discovered = True
                self.queue.append((cell, path[:]))
        return None
    
    # gets cells that are not walls and not discovered
    def get_adjacent_cells(self, x_index, y_index):
        for i in range(x_index - 1, x_index + 2):
            for j in range(y_index - 1, y_index + 2):
                if i >= 0 and i < self.NUM_CELLS and j >= 0 and j < self.NUM_CELLS:
                    # disallow diagonal movement
                    if abs(i - x_index) is not abs(j - y_index):
                        if self.cells[i][j].is_wall or self.cells[i][j].is_discovered:
                            continue
                        yield self.cells[i][j]

    # https://stackoverflow.com/questions/9553638/find-the-index-of-an-item-in-a-list-of-lists
    def find_cell_index(self, cell):
        for i, c in enumerate(self.cells):
            try:
                j = c.index(cell)
            except ValueError:
                continue
            return i, j
    
    def draw(self, screen):
        for row in self.cells:
            for cell in row:
                cell.draw(screen)
            
            