# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动
# ，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格[35, 37]，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
# 请问该机器人能够到达多少个格子？
class Solution:
    def __init__(self):
        self.res = 0
    def movingCount(self, m: int, n: int, k: int) -> int:
        def judge(x,y,k):
            def sum_x_y(num1):
                sum1 = 0
                while num1:
                    sum1 += num1%10
                    num1//=10
                return sum1
            if sum_x_y(x)+sum_x_y(y)>k:
                return False
            else:
                return True
        path = [[0]*m for _ in range(n)]
        print(path)
        def dsf(x,y):
            if not 0<=x<n or not 0<=y<m or not judge(x,y,k) or path[x][y] ==1:
                return False
            if judge(x,y,k) and path[x][y]==0:
                path[x][y]=1
                self.res+=1
                dsf(x+1,y)
                dsf(x-1,y)
                dsf(x,y+1)
                dsf(x,y-1)
        dsf(0,0)
        return self.res
dp = Solution()
#m = 2, n = 3, k = 1
print(dp.movingCount(1,2,1))