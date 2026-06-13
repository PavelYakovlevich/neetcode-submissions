class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s_color = image[sr][sc]

        def dfs(image, r, c, color):
            ROWS, COLS = len(image), len(image[0])

            if (min(r, c) < 0 or 
                r == ROWS or c == COLS or
                image[r][c] != s_color or 
                image[r][c] == color):
                return
            
            image[r][c] = color

            dfs(image, r - 1, c, color)
            dfs(image, r + 1, c, color)
            dfs(image, r, c - 1, color)
            dfs(image, r, c + 1, color)

        dfs(image, sr, sc, color)

        return image
