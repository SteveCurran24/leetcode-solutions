class Solution(object):

    def DFS(self, image, sr, sc, color, start_value):

        image[sr][sc] = color

        up = sr-1
        down = sr+1
        left = sc-1
        right = sc+1

        if color == start_value:
            return

        if up >= 0 and image[up][sc] == start_value:
            self.DFS(image, up, sc, color, start_value)

        if down < len(image) and image[down][sc] == start_value:
            self.DFS(image, down, sc, color, start_value)

        if left >= 0 and image[sr][left] == start_value:
            self.DFS(image, sr, left, color, start_value)

        if right < len(image[sr]) and image[sr][right] == start_value:
            self.DFS(image, sr, right, color, start_value)

        return

            
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        start_value = image[sr][sc]
        self.DFS(image, sr, sc, color, start_value)

        return image


