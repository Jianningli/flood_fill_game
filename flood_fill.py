import logging
import time
from collections import deque
from typing import List, Set, Tuple


# Configure logging
logging.basicConfig(
    filename='flood_fill.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def get_connected_tiles(board: List[List[str]], color: str) -> Set[Tuple[int, int]]:
    """
    Get all tiles connected to the origin tile (0, 0) that are the given color.

    Args:
        board (List[List[str]]): The game board represented as a 2D list.
        color (str): The color of the tiles to check.

    Returns:
        Set[Tuple[int, int]]: A set of coordinates representing tiles connected to the origin.
    """
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    queue = deque([(0, 0)])
    connected_tiles = set()

    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        connected_tiles.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] == color or (board[nx][ny] == board[0][0] and (nx, ny) in connected_tiles):
                    queue.append((nx, ny))

    return connected_tiles


def get_largest_connected_color(board: List[List[str]], colors: List[str]) -> str:
    """
    Determine the color that would result in the largest number of tiles connected to the origin.

    Args:
        board (List[List[str]]): The game board represented as a 2D list.
        colors (List[str]): The list of available colors.

    Returns:
        str: The color that results in the largest number of connected tiles.
    """
    origin_color = board[0][0]
    max_connected = -1
    best_color = None

    for color in colors:
        if color == origin_color:
            continue
        connected_tiles = get_connected_tiles(board, color)
        num_connected = len(connected_tiles)
        
        if num_connected > max_connected or (num_connected == max_connected and color < best_color):
            max_connected = num_connected
            best_color = color

    return best_color


def flood_fill(board: List[List[str]], colors: List[str]) -> int:
    """
    Solve the flood fill game by changing the color of the origin tile to fill the board.

    Args:
        board (List[List[str]]): The game board represented as a 2D list.
        colors (List[str]): The list of available colors.

    Returns:
        int: The number of moves required to fill the board with a single color.
    """
    start_time = time.time()
    moves = 0
    origin_color = board[0][0]

    while True:
        next_color = get_largest_connected_color(board, colors)
        if next_color is None or next_color == origin_color:
            break

        logging.info(f"Move {moves + 1}: Changing color to '{next_color}'")

        connected_tiles = get_connected_tiles(board, origin_color)
        if not connected_tiles:
            break
        for x, y in connected_tiles:
            board[x][y] = next_color

        logging.info(f"Board status after move {moves + 1}: {board}")
        moves += 1

        # Check if the board is filled with a single color
        if all(board[i][j] == next_color for i in range(len(board)) for j in range(len(board[0]))):
            break

        origin_color = next_color

    end_time = time.time()
    elapsed_time = end_time - start_time

    logging.info(f"Final board after {moves} moves:")
    for row in board:
        logging.info(' '.join(row))

    logging.info(f"Total runtime: {elapsed_time:.4f} seconds")

    return moves


if __name__ == "__main__":
    # Example usage: Board of size 6x6 and 2 colors
    
    '''
    # example
    board = [
        ['G', 'R', 'G', 'G', 'G', 'G'],
        ['R', 'G', 'G', 'G', 'G', 'G'],
        ['R', 'G', 'R', 'R', 'G', 'G'],
        ['R', 'G', 'R', 'R', 'G', 'G'],
        ['R', 'G', 'G', 'G', 'G', 'G'],
        ['R', 'G', 'G', 'G', 'G', 'G']
    ]
    '''

    # another example 

    board = [
        ['R', 'R', 'G', 'G', 'G', 'G'],
        ['R', 'G', 'G', 'G', 'G', 'G'],
        ['R', 'G', 'R', 'R', 'G', 'G'],
        ['R', 'G', 'R', 'R', 'G', 'G'],
        ['R', 'G', 'G', 'G', 'G', 'G'],
        ['R', 'G', 'G', 'G', 'G', 'G']
    ]

    colors = ['R', 'G']  # Two colors

    moves = flood_fill(board, colors)
    print(f"Solved in {moves} moves!")
    
    print("Final board:")
    for row in board:
        print(" ".join(row))
