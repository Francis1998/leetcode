class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return  False
        colum = len(matrix[0])-1
        for row in range(len(matrix)):
            if matrix[row][colum]>=target:
                #half
                left = 0
                right = colum
                while left <= right:
                    mid = (left+right)>>1
                    if matrix[row][mid]==target:
                        return True
                    elif matrix[row][mid]>target:
                        right = mid -1
                    else:
                        left = mid +1
        return False