#!/usr/bin/python3
"""Defines island perimeter finding function."""

def island_perimeter(grid):
    """Return the perimeter of an island.
    
    The grid represents water by 0 and land by 1.
    
    Args:
        grid (list): A list of lists of integers representing an island.
        
    Returns:
        int: The perimeter of the island defined in grid.
    """
    
    # Check if the grid is empty
    if not grid or not grid[0]:
        return 0
    
    width = len(grid[0])
    height = len(grid)
    edges = 0  # Count the number of shared edges
    size = 0   # Count the total number of land cells

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:  # Land cell found
                size += 1
                # Check left cell
                if j > 0 and grid[i][j - 1] == 1:
                    edges += 1
                # Check top cell
                if i > 0 and grid[i - 1][j] == 1:
                    edges += 1
    
    # Calculate perimeter: Perimeter = total edges - shared edges
    return size * 4 - edges * 2
