class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        XorList = [[set() for _ in row] for row in grid]

        XorList[0][0].add(grid[0][0])

        for j in range(1, cols):
            for xor in XorList[0][j-1]:
                XorList[0][j].add(xor ^ grid[0][j])

        for i in range(1, rows):
            for xor in XorList[i-1][0]:
                XorList[i][0].add(xor ^ grid[i][0])

        for i in range(1, rows):
            for j in range(1, cols):
                for xor in XorList[i-1][j]:
                    XorList[i][j].add(xor ^ grid[i][j])
                for xor in XorList[i][j-1]:
                    XorList[i][j].add(xor ^ grid[i][j])
        
        return min(XorList[rows - 1][cols - 1])

# --- Driver Code for Testing ---
if __name__ == "__main__":
    solution = Solution()
    
    # Testing your original matrix
    example_grid0 = [[1,2],[3,4]]
    # example_grid1 = [[26, 24, 3], [2, 22, 17]]
    
    result = solution.minCost(example_grid0)
    print(f"The minimum XOR path cost is: {result}")