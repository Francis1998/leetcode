class Solution(object):
    def __init__(self):
        self.level = 0
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        global row,column,path
        row = len(grid) #row
        column = len(grid[0])#column
        path = [[0 for _ in range(column)] for _ in range(row)]
        def trace(r,c):
            if r<0 or c<0:
                return
            elif r>row-1 or c>column-1:
                return
            elif path[r][c] == 1:
                return
            path[r][c] = 1
            if grid[r][c] == 1:
                grid[r][c] = 2
            trace(r+1,c)
            trace(r-1,c)
            trace(r,c+1)
            trace(r,c-1)
            self.level += 1
            return
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 2:
                    trace(r,c)
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1:
                    self.level=-1
        return self.level
dp = Solution()
print(dp.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))