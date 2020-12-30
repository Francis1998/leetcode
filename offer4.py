class Solution:
    def findNumberIn2DArray(self, matrix, target):
        def halffind(matrix,low,high,target):
            while low<= high:
                
                mid = (high+low)>>1
                if matrix[mid] == target:
                    return True
                elif matrix[mid] > target:
                    high = mid -1
                else:
                    low = mid + 1
            return False
        
        row = len(matrix)
        if row == 0:
            return False
        column = len(matrix[0]) -1
        if column == -1:
            return False
        for i in range(row):
            if matrix[i][column]==target:
                return True
            if matrix[i][column]>target and halffind(matrix[i],0,column,target):
                return True
        return False