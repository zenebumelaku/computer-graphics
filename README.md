# Maze Generator and Solver (Pygame)

## Student Information

**Name:** Zenebu Melaku
**ID:** UGR/6058/16
**Section:** 2
**Course:** Computer Graphics
**Assignment Type:** Individual Assignment

---

## Project Description

This project is a **maze generator and solver** built using Python and Pygame.
It uses **Depth First Search (DFS) with backtracking** to both generate and solve a random maze.

---

## Features

- Random maze generation using DFS
- Animated visualization of generation process
- Automatic maze solving using stack-based DFS
- Backtracking visualization (dead ends shown in blue)
- Final solution path highlighted in red
- Random start and end points

---

## How It Works

1. The maze is generated using recursive backtracking (DFS).
2. Walls are removed between visited cells to form paths.
3. A solver then finds a path from start to end using stack-based DFS.
4. The solution is visualized step-by-step using Pygame.

---

## How to Run

```bash
pip install pygame
python main.py
```

---

## Output Colors

- **White:** Walls
- **Green:** Maze generation cursor
- **Red:** Current solving path
- **Blue:** Dead ends

---

## Tools Used

- Python
- Pygame

---

## Notes

This project demonstrates graph traversal, recursion/stack usage, and real-time visualization in computer graphics.
