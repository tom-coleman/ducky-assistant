# To solve this problem, we can iterate through each cell in the grid. For each land cell (cell with value 1), we check its four neighbors (up, down, left, right). If a neighbor is water (cell with value 0) or it is outside the grid boundaries, we increase the perimeter by 1 for that side. This approach works because the perimeter of the island is essentially the sum of the boundaries between land and water or land and the edge of the grid.

# Let's implement the solution and the test cases in separate files as requested.

### Solution File


# filename: leetcode/island_perimeter.py

class Solution:
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # Check up
                    if row == 0 or grid[row-1][col] == 0:
                        perimeter += 1
                    # Check down
                    if row == rows-1 or grid[row+1][col] == 0:
                        perimeter += 1
                    # Check left
                    if col == 0 or grid[row][col-1] == 0:
                        perimeter += 1
                    # Check right
                    if col == cols-1 or grid[row][col+1] == 0:
                        perimeter += 1
        return perimeter