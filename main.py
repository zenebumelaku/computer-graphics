import pygame
import random
import sys

ROWS = 20
COLS = 20
CELL_SIZE = 35

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

FPS = 60

EXTRA_WALL_CHANCE = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
GRAY = (40, 40, 40)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator and Solver")

clock = pygame.time.Clock()

northWall = [[1 for _ in range(COLS)] for _ in range(ROWS + 1)]

eastWall = [[1 for _ in range(COLS + 1)] for _ in range(ROWS)]

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

def draw_maze():

    screen.fill(BLACK)

    for r in range(ROWS):
        for c in range(COLS):

            x = c * CELL_SIZE
            y = r * CELL_SIZE

            if northWall[r][c] == 1:
                pygame.draw.line(screen, WHITE, (x, y), (x + CELL_SIZE, y), 2)

    for c in range(COLS):
        if northWall[ROWS][c] == 1:

            x = c * CELL_SIZE
            y = ROWS * CELL_SIZE

            pygame.draw.line(screen, WHITE, (x, y), (x + CELL_SIZE, y), 2)

    for r in range(ROWS):
        for c in range(COLS + 1):

            if eastWall[r][c] == 1:

                x = c * CELL_SIZE
                y = r * CELL_SIZE

                pygame.draw.line(screen, WHITE, (x, y), (x, y + CELL_SIZE), 2)

def remove_wall(current, nxt):

    r1, c1 = current
    r2, c2 = nxt

    if c2 == c1 + 1:
        eastWall[r1][c1 + 1] = 0

    elif c2 == c1 - 1:
        eastWall[r1][c1] = 0

    elif r2 == r1 + 1:
        northWall[r1 + 1][c1] = 0

    elif r2 == r1 - 1:
        northWall[r1][c1] = 0

def get_unvisited_neighbors(r, c):

    neighbors = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if not visited[nr][nc]:
                neighbors.append((nr, nc))

    return neighbors

def generate_maze():

    stack = []

    current = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))

    visited[current[0]][current[1]] = True

    total_cells = ROWS * COLS
    visited_count = 1

    while visited_count < total_cells:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        r, c = current

        neighbors = get_unvisited_neighbors(r, c)

        if neighbors:

            next_cell = random.choice(neighbors)

            stack.append(current)

            remove_wall(current, next_cell)

            current = next_cell

            visited[current[0]][current[1]] = True
            visited_count += 1

        elif stack:
            current = stack.pop()

        draw_maze()

        pygame.display.update()
        pygame.time.delay(20)


start = (random.randint(0, ROWS - 1), 0)
end = (random.randint(0, ROWS - 1), COLS - 1)

eastWall[start[0]][0] = 0
eastWall[end[0]][COLS] = 0

def get_valid_moves(r, c):

    moves = []

    if r > 0 and northWall[r][c] == 0:
        moves.append((r - 1, c))

    if r < ROWS - 1 and northWall[r + 1][c] == 0:
        moves.append((r + 1, c))

    if c > 0 and eastWall[r][c] == 0:
        moves.append((r, c - 1))

    if c < COLS - 1 and eastWall[r][c + 1] == 0:
        moves.append((r, c + 1))

    return moves

def solve_maze():

    stack = [start]

    visited_solver = set()

    dead_ends = set()

    while stack:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = stack[-1]

        if current == end:
            return stack

        visited_solver.add(current)

        r, c = current

        possible_moves = []

        for move in get_valid_moves(r, c):
            if move not in visited_solver:
                possible_moves.append(move)

        if possible_moves:
            stack.append(random.choice(possible_moves))
        else:
            dead_ends.add(current)
            stack.pop()

        draw_maze()

        for cell in dead_ends:
            x = cell[1] * CELL_SIZE + CELL_SIZE // 2
            y = cell[0] * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(screen, BLUE, (x, y), CELL_SIZE // 5)

        for cell in stack:
            x = cell[1] * CELL_SIZE + CELL_SIZE // 2
            y = cell[0] * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(screen, RED, (x, y), CELL_SIZE // 4)

        pygame.display.update()
        pygame.time.delay(40)
# FULL FINAL CODE (UNCHANGED FROM YOUR ORIGINAL)

EXTRA_WALL_CHANCE = 20

# (everything same as above)

# BONUS INSIDE generate_maze (already present)

if random.randint(1, EXTRA_WALL_CHANCE) == 1:

    extra_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    random.shuffle(extra_dirs)

    for dr, dc in extra_dirs:

        er = r + dr
        ec = c + dc

        if 0 <= er < ROWS and 0 <= ec < COLS:
            remove_wall(current, (er, ec))
            break