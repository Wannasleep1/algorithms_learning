from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from chapter_2.generic_search import dfs, bfs, astar, Node, node_to_path


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:

    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2,
                 start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(9, 9)):
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self._randomly_fill(rows, columns, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows, columns, sparseness):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self) -> str:
        output: str = f"{'_'*(self._columns+2)}\n"
        for row in self._grid:
            output += "|" + "".join([c.value for c in row]) + "|\n"
        output += f"{'-'*(self._columns+2)}\n"
        return output

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 > 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 > 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))
        return locations

    def mark(self, path: List[MazeLocation]) -> None:
        self.__change_grid(path, "mark")

    def clear(self, path: List[MazeLocation]) -> None:
        self.__change_grid(path, "clear")

    def __change_grid(self, path, option: str) -> None:
        if option == "mark":
            cell_marker = Cell.PATH
        elif option == "clear":
            cell_marker = Cell.EMPTY
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = cell_marker
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL


def euclidian_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:

    def distance(ml: MazeLocation) -> float:
        xdist: int = ml.column - goal.column
        ydist: int = ml.row - goal.row
        return sqrt((xdist * xdist) + (ydist * ydist))

    return distance


def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:

    def distance(ml: MazeLocation) -> float:
        xdist: int = abs(ml.column - goal.column)
        ydist: int = abs(ml.row - goal.row)
        return xdist + ydist

    return distance


if __name__ == "__main__":
    maze: Maze = Maze()
    print(maze)

    solution_1: Optional[Node[MazeLocation]] = dfs(maze.start, maze.goal_test, maze.successors)
    if solution_1 is None:
        print("No solutions found using depth-first search!")
    else:
        path_1: List[MazeLocation] = node_to_path(solution_1)
        maze.mark(path_1)
        print(maze)
        maze.clear(path_1)

    solution_2: Optional[Node[MazeLocation]] = bfs(maze.start, maze.goal_test, maze.successors)
    if solution_2 is None:
        print("No solutions found using depth-first search!")
    else:
        path_2: List[MazeLocation] = node_to_path(solution_2)
        maze.mark(path_2)
        print(maze)
        maze.clear(path_2)

    distance: Callable[[MazeLocation], float] = manhattan_distance(maze.goal)
    solution_3: Optional[Node[MazeLocation]] = astar(maze.start, maze.goal_test, maze.successors, distance)
    if solution_3 is None:
        print("No solutions found using depth-first search!")
    else:
        path_3: List[MazeLocation] = node_to_path(solution_3)
        maze.mark(path_3)
        print(maze)
        maze.clear(path_3)
