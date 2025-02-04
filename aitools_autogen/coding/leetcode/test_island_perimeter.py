

### Test File


# filename: leetcode/test_island_perimeter.py

import unittest
from island_perimeter import Solution

class TestIslandPerimeter(unittest.TestCase):
    def test_example1(self):
        grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        self.assertEqual(Solution().islandPerimeter(grid), 16)

    def test_example2(self):
        grid = [[1]]
        self.assertEqual(Solution().islandPerimeter(grid), 4)

    def test_example3(self):
        grid = [[1,0]]
        self.assertEqual(Solution().islandPerimeter(grid), 4)

    def test_large_grid(self):
        grid = [[1] * 100 for _ in range(100)]
        self.assertEqual(Solution().islandPerimeter(grid), 400)

if __name__ == '__main__':
    unittest.main()