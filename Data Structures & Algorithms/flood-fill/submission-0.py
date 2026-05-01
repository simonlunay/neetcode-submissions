class Solution:
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image
        rows, cols = len(image), len(image[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r, c, original):
            if r < 0 or c<0 or r >= rows or c >= cols:
                return
            if image[r][c] != original:
                return
            image[r][c] = color

            for dr, dc in directions:
                dfs(r + dr, c + dc, original)




        dfs(sr, sc, image[sr][sc])

        return image




        