class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]




        def bfs(r, c):
            visited.add((r, c))
            q = deque()
            q.append((r, c))
            while q:
                ro, co = q.popleft()
                for dr, dc in directions:
                    row, col = ro + dr, co + dc
                    if (row, col) not in visited and row in range(rows) and col in range(cols) and grid[row][col] == "1":
                        visited.add((row, col))
                        q.append((row, col))

                        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    numIslands += 1


        return numIslands

        


        


        