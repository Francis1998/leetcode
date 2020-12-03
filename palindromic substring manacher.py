class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #find the center, and trace to opposite endings   if 
        n = len(s)
        t = "$#"
        for i in range(n):
            t += s[i] + "#"
        n = len(t)
        t += "!"
        iMax, rMax, ans = 0, 0, 0
        f = [0 for _ in range(n)]
        for i in range(1,n):
            if i<=rMax:
                f[i] = min(rMax - i +1,f[2*iMax-i])
            else:
                f[i] = 1
            while(t[i+f[i]] == t[i-f[i]]):
                f[i]+=1
            if i + f[i] -1 >rMax:
                iMax = i
                rMax = i + f[i] -1
            ans += f[i]//2
        return ans
dp = Solution()
print(dp.countSubstrings("abc"))