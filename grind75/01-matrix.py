class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        dist = []
        queue = []
        for i in range(len(mat)):
            dist.append([-1] * len(mat[0]))

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i,j))
                else:
                    dist[i][j] = -1
        
        while queue:
            #queue.pop(0) is popping the very first position of queue. Alternatively, python has a deque function from the collections library that could be used to reduce time complexity. queue.pop(0) has O(n) complexity. 
            i, j = queue.pop(0)
            #equivalent to:
            # cell_index = queue.pop(0)
            # i = cell_index[0]
            # j = cell_index[1]

            #Check all four directions:
            #if any direction is within bounds and also -1 (the original 1 location) we add the distance of the current value and put it back in queue
            # the only way the loop escapes is if the queue is empty and all values have been accounted for. 
            if i - 1 >= 0 and dist[i-1][j] == -1:
                dist[i-1][j] = dist[i][j]+1
                queue.append((i-1, j))
            if i + 1 < len(mat) and dist[i+1][j] == -1:
                dist[i+1][j] = dist[i][j]+1
                queue.append((i+1, j))
            if j - 1 >= 0 and dist[i][j-1] == -1:
                dist[i][j-1] = dist[i][j]+1
                queue.append((i, j-1))
            if j + 1 < len(mat[i]) and dist[i][j+1] == -1:
                dist[i][j+1] = dist[i][j]+1
                queue.append((i, j+1))

        return dist
            

            
            
