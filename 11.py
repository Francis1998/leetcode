class Solution:
    def integerBreak(self, n):
        if n==2:
            return 1
        if n==3:
            return 2
        mem = [0,1,2,3]+[0]*53
        for i in range(4,n+1):
            for j in range(2,i):
                if mem[i] < mem[j]*mem[i-j]:
                    mem[i] = mem[j]*mem[i-j]
        print(mem[0:10])
        return mem[n]
dp = Solution()
print(dp.integerBreak(10))