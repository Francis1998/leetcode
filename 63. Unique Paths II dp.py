class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        colum = len(obstacleGrid[0])
        if row<=0:
            return 0
        result = [[0]*(colum+1) for _  in range(row+1)]
        result[0][1] = 1
        for index1 in range(1,row+1):
            for index2 in range(1,colum+1):
                if obstacleGrid[index1-1][index2-1] == 0:
                    result[index1][index2] = result[index1][index2-1]+result[index1-1][index2]
        return result[-1][-1]
                    


